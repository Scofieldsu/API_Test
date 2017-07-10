# encoding: utf-8
# import sys
# if sys.version_info < (2, 7):
#     import unittest2 as unittest
# else:
#     import unittest
#
# # Flask is supported only for python2 and python3.3+
# if sys.version_info < (3, 0) or sys.version_info >= (3, 3):
#     try:
#         from flask import Flask
#     except ImportError:
#         raise unittest.SkipTest('Flask not found for testing')

import os
import sys

import pytest

# myPath = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, myPath + '/../')
from flaskapi.utils.api_tools import trans_str_to_dict, dict_move_key, compose_api_info
from jsonrpc.backend.flask import api

@pytest.fixture
@api.dispatcher.add_method
def show_doc(a=1, b='b'):
    """
    :description test
    :param a:int:int_param
    :param b:str
    :return: test
    """
    return show_doc.__doc__


def test_trans_str_to_dict():
    trans_dict = {
        "description": "test",
        "return": "test",
        "param_explain": {"a":"int_param"},
        "a": "int",
        "b": "str"
    }
    flag = not cmp(trans_str_to_dict(show_doc()), trans_dict)
    assert  flag


def test_dict_move_key():
    b_dict = {
        "b_one": "one",
        "b_two": "two",
    }
    a_dict = {
        "a": "aa",
        "b": b_dict
    }
    c = {
        "a": "aa",
        "b_one": "one",
        "b": {
            "b_two": "two"
        }
    }
    d = dict_move_key(a_dict,b_dict,"b_one")
    flag = not cmp(d, c)
    assert flag



def test_compose_api_info():
    result = compose_api_info("show_doc", api.dispatcher.method_map)
    my_result = {
        "name": "show_doc",
        "description": "test",
        "return": "test",
        "param_explain": {"a": "int_param"},
        "params": {
            "a": "int",
            "b": "str"
        }
    }
    flag = not cmp(result, my_result)
    assert flag



# def main():
#
#     test_trans_str_to_dict(show_doc)
#     test_dict_move_key()
#
# if __name__ == "__main__":
#     main()