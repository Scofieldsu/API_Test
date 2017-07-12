# encoding: utf-8
import sys,os
from flaskapi.api.base_api import *
from flaskapi.utils.api_tools import compose_api_info
from apidata.common import get_all_api_data


# 调用api-data获取接口信息
@api_add
def get_all_api(*args, **kwargs):
    """
    :description 获取接口信息
    :param args:str
    :param kwargs:str
    :return: 所有接口信息
    """
    from apidata.tests import source_path
    project_dir = os.path.abspath('.')
    except_folder = ['.git','.idea','docs','static','templates','tests']
    except_paths = list()
    except_dirs = list()
    except_dirs.append(source_path)
    for x in except_folder:
        except_dirs.append(project_dir+os.sep+x)
    result = get_all_api_data(file_type='py', decor_list=['api_add', 'api_data'], except_dirs=except_dirs,  except_paths=except_paths)
    result.pop("get_all_api_flask")
    result.pop("hello")
    return result


# 调用flask-api获取接口信息
@api_add
def get_all_api_flask(*args, **kwargs):
    _name = sys._getframe().f_code.co_name
    api_dict = api.dispatcher.method_map
    api_name_list = api_dict.keys()
    result = dict()
    for i in api_name_list:
        item = compose_api_info(i, api_dict)
        result[i] = item
    result.pop(_name)
    result.pop("get_all_api")
    return result

# API-DATA协议  返回的数据格式
def get_all_api_temp(*args, **kwargs):
    result = {'login': {'name': 'login', 'description': '登录接口', 'return': '返回信息', 'param_explain': {},  'params': {'login_name': 'str', "password": "str"}},
              'logout': {'name': 'logout', 'description': '退出', 'return': '返回信息',  'param_explain': {}, 'params': {"name": "str", "pwd": "str"}}}
    return result