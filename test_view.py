import unittest
from unittest import TestCase
# from django.test import TestCase
# import xmlrunner

import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings.dev')
django.setup()

import json

from backend.api.views import import_test_models
from backend.api.views import get_profile, set_profile, delete_stock, set_stock
from backend.api.views import add_new_stock, google_login, google_logout
from backend.api.test_models import USER1, USER2, STOCK1
from backend.api.test_models import Userprofile, Stock


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

        pass

    def test_get_profile(self):

        request = Virtual_request(id=USER1.user_id,
                                  body=json_convert(USER1.user_request()))

        # request = Virtual_request(user={"email": "zhangsan@tamu.edu", })
        user_profile = get_profile(request)
        user_profile_json = json.loads(user_profile.content)

        self.assertEqual(user_profile_json, USER1.user_profile())

    def test_set_profile(self):

        request = Virtual_request(id=USER1.user_id,
                                  method="POST",
                                  body=json_convert(USER1.user_request()))

        user_profile = set_profile(request)
        user_profile_json = json.loads(user_profile.content)
        user_profile_json.pop("state")
        # print("user_profile", user_profile)
        self.assertEqual(user_profile_json, USER1.user_profile())

    def test_delete_stock(self):

        request = Virtual_request(id=USER1.user_id,
                                  method="POST",
                                  body=json_convert(USER1.user_request(deleted_stocks=12345)))

        delete_stock(request)

    def test_set_stock(self):

        request = Virtual_request(id=USER1.user_id,
                                  method="POST",
                                  body=json_convert(USER1.user_request(s_code=12345)))

        set_stock(request)


    # def test_add_new_stock(self): # do not test due to its high time consumption
    #
    #     request = Virtual_request(id=USER1.user_id,
    #                               method="POST",
    #                               body=json_convert(USER1.user_request(added_stocks=STOCK1.stock_info())))
    #     add_new_stock(request)



if __name__ == '__main__':
    import_test_models()
    unittest.main()
    # test_suite = unittest.TestSuite()
    # test_suite.addTest(unittest.makeSuite(UserTestCase))
    # runner = xmlrunner.XMLTestRunner(output='report')
    # runner.run(test_suite)


