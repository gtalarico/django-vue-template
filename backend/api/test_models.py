
class Stock:
    def __init__(self, code, name, purchase_price, purchase_date, target_price, expect_return_rate):

        self.code = code
        self.name = name
        self.purchase_price = purchase_price
        self.purchase_date = purchase_date
        self.target_price = target_price
        self.expect_return_rate = expect_return_rate

        # self.code = 0,
        # # self.close_price,
        # self.purchase_price,
        # self.purchase_date.isoformat()[:10] = "01234567890",
        # self.target_price = 0,
        # self.expect_return_rate = 0.

    def stock_info(self):
        return {'code': self.code,
                'name': self.name,
                'purchase_price': self.purchase_price,
                'purchase_date': self.purchase_date,
                'target_price': self.target_price,
                'expect_return_rate': self.expect_return_rate,
        }

    def delete(self):
        pass


class StockDatabase:
    def __init__(self):
        self.stock_buf = []
        self.code2stock = dict()

        pass

    def create(self, code, name, purchase_price, purchase_date, target_price, expect_return_rate):
        new_stock = Stock(code, name, purchase_price, purchase_date, target_price, expect_return_rate)
        self.stock_buf.append(new_stock)
        self.code2stock[name] = new_stock

    def all(self):
        return self.stock_buf

    def stock_profile(self):
        return self.code2stock

    def get(self, code):
        return self.code2stock[code]


class Userinfo:
    def __init__(self, user_id, email_address, user_name, short_tax_rate=0., long_tax_rate=0., invest_horizon=0.):

        self.user_id = user_id
        self.email_address = email_address
        self.user_name = user_name
        self.stocks = StockDatabase()
        self.short_tax_rate = short_tax_rate
        self.long_tax_rate = long_tax_rate
        self.invest_horizon = invest_horizon

    def user_request(self, **kwargs):

        request = dict()
        request['id'] = self.user_id
        for key, value in kwargs.items():
            request[key] = value

        return request

    def user_profile(self):
        return {'user_id': self.user_id,
                'user_name': self.user_name,
                'short_tax_rate': self.short_tax_rate,
                'long_tax_rate': self.long_tax_rate,
                'investment_horizon': self.invest_horizon,
                'stocks': self.stocks.stock_profile(),
        }

    def save(self):
        pass


class UserDatabase:

    def __init__(self):
        self.user_buf = []
        self.id2user = dict()
        self.objects = self
        pass

    def add_new_user(self, new_user):
        # new_user = Userinfo(user_id, email_address, user_name)
        self.user_buf.append(new_user)
        self.id2user[new_user.user_id] = new_user

    def get(self, user_id):
        return self.id2user[user_id]


USER1 = Userinfo(user_id=12345, email_address="zhangsan@tamu.edu", user_name="zhangsan")
USER2 = Userinfo(user_id=23456, email_address="lisi@tamu.edu", user_name="lisi")
STOCK1 = Stock(code=12345, name="AAA", purchase_price=0., purchase_date=0., target_price=0., expect_return_rate=0.)
Userprofile = UserDatabase()
Userprofile.add_new_user(USER1)
Userprofile.add_new_user(USER2)




