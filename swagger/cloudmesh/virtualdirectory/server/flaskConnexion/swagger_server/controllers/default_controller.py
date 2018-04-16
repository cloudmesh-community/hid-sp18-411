import connexion
import six
import json


from swagger_server import util
from pymongo import MongoClient

client = MongoClient('localhost',port=27017)
db = client.cloud_hid


def get_records():  # noqa: E501
    """get_records

     # noqa: E501


    :rtype: None
    """
    l = list()
    for each in db.hid_names.find():
        l.append((each['Name'], each['HID']))
    return json.dumps(l)
