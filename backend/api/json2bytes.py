import json


def json_convert(input_dict):
    str_json = json.dumps(input_dict, indent=2)
    btye_json = bytes(str_json, encoding="utf-8")
    return btye_json

a = {
    "haha": 1
}

c = json_convert(a)
d = json.loads(c.decode("utf-8"))

print(d)

'''
get:
{'haha':1}
'''