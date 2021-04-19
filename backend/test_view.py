import unittest
from unittest import TestCase
# from django.test import TestCase
import xmlrunner

import json
from api.views import fecth_profile, set_profile, stock_detail


def json_convert(input_dict):
    str_json = json.dumps(input_dict, indent=2)
    btye_json = bytes(str_json, encoding="utf-8")
    return btye_json


class Virtual_request:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class UserTestCase(TestCase):

    def setUp(self):

        self.default_profile = {'exist': 0,
                                'user_name': 'zhangsan@tamu.edu',
                                'short_tax_rate': None,
                                'long_tax_rate': None,
                                'stocks': {}}

        self.new_profile = self.change_user_profile(self.default_profile.copy())

    def change_user_profile(self, user_profile):

        user_profile.update({"exist": 1,
                             "user_name": "lisi",
                             "short_tax_rate": 0.4,
                             "long_tax_rate": 0.01,
                             "stocks": {
                                 "AAPL":{
                                    "purchase_price": 100.0,
                                    "purchase_date": "2020-10-21",
                                    "target_price": 200.0
                                 },
                                 "NIO":{
                                     "purchase_price": 27.0,
                                     "purchase_date": "2020-11-19",
                                     "target_price": 40.0
                                 }
                             }})

        return user_profile

    def test_fecth_profile(self):

        # print("Test fecth_profile API ...")
        request = Virtual_request(user={"email": "zhangsan@tamu.edu",})
        user_profile = fecth_profile(request)
        # print(user_profile)
        self.assertEqual(user_profile, self.default_profile)

    def test_set_profile(self):

        request = Virtual_request(user={"email": "zhangsan@tamu.edu",},
                                  method="POST",
                                  body=json_convert(self.new_profile))

        update_profile = set_profile(request)
        self.assertEqual(update_profile, self.new_profile)

        # print(update_profile)

    def test_stock_detail(self):
        request = Virtual_request(user={"email": "zhangsan@tamu.edu", },
                                  method="",
                                  body=json_convert(self.new_profile))
        stock_info = stock_detail(request)
        stock_name = stock_info.keys()
        self.assertEqual(stock_name, self.new_profile["stocks"].keys())

        # print(stock_info)


if __name__ == '__main__':
    # unittest.main()
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(UserTestCase))
    runner = xmlrunner.XMLTestRunner(output='report')
    runner.run(test_suite)


