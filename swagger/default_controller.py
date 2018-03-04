import connexion
import six
import json

from swagger_server.models.no_sq_lentry import NoSQLentry  # noqa: E501
from swagger_server import util
from pymongo import Mongo

client = Mongo(port=27017)
db = client.variables


def get_records():  # noqa: E501
    """get_records

     # noqa: E501


    :rtype: None
    """
    l = list()
    for each in db.Var.find():
        l.append((each['Name'], each['HID']))
    return json.dumps(l)



def getrecordby_id(id):  # noqa: E501
    """getrecordby_id

     # noqa: E501

    :param id: id of entry
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def post_records(record=None):  # noqa: E501
    """post_records

     # noqa: E501

    :param record: entry for the database
    :type record: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        record = NoSQLentry.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def putrecordby_id(id):  # noqa: E501
    """putrecordby_id

    record we want to save # noqa: E501

    :param id: id of entry
    :type id: str

    :rtype: None
    """
    return 'do some magic!'
