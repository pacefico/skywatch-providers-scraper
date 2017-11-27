from pymongo import MongoClient
import json
from search import PHY_CRT, PHY_TYPES

SELECTORS = ['eq', 'gte', 'gt', 'in', 'lte', 'lt', 'ne', 'nin']

"""
$eq	Matches values that are equal to a specified value.
$gt	Matches values that are greater than a specified value.
$gte	Matches values that are greater than or equal to a specified value.
$in	Matches any of the values specified in an array.
$lt	Matches values that are less than a specified value.
$lte	Matches values that are less than or equal to a specified value.
$ne	Matches all values that are not equal to a specified value.
$nin	Matches none of the values specified in an array.

from: https://docs.mongodb.com/manual/reference/operator/query/
"""

def get_db():
    client = MongoClient('localhost', 27017)
    return client.test.spaceObjects


def parse_number(value):
    try:
        return float(value)
    except:
        return value


def get_selector_value(value):
    for sel in SELECTORS:
        if sel in value:
            return sel, value.replace(sel, "")
    return 'eq', value


def convert_selector(value):
    selector, value = get_selector_value(value)
    key = '${}'.format(selector)
    val = parse_number(value)
    return {key: val}


def convert_args_to_mongo_query(args_dict):
    mongo_query = {}
    for k,v in args_dict.items():
        if k == "types":
            type_list = []
            for phy_type in args_dict['types'].split():
                if phy_type in [tuple[1] for tuple in PHY_TYPES]:
                    type_list.append(phy_type)
                else:
                     raise AttributeError("Error: Physical type '{}' is not valid!".format(phy_type))
            mongo_query['types'] = {'$in': type_list}
        else:
            if k in PHY_CRT:
                mongo_query[k] = convert_selector(v)
            else:
                raise AttributeError("Error: Physical criteria '{}' is not valid!".format(k))

    return mongo_query

def query(query):
    response = []
    for item in get_db(query):
        response.append(item)
        print(item)

    return response

