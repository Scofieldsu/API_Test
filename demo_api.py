# encoding: utf-8

import sys,os
from flaskapi.api.base_api import *
from flaskapi.utils.api_tools import compose_api_info
from flaskapi.api import api_add,api_class
from apidata.common import get_all_api_data
from apidata import api_data


@api_add
def login(name, pwd):
    """
    :description 登录接口
    :param name: str
    :param pwd: str
    :return: 登录信息
    """
    result = {"msg": "login success", "code": 200}
    return result


@api_add
def logout(name):
    """
    :description 退出接口
    :param name: str
    :return: 退出信息success or error
    """
    return "logout success"


@api_class
class UserApi(object):

    @api_data
    def login_test(self,name, pwd):
        """
        :description test登录接口
        :param name: str
        :param pwd: str
        :return: test登录信息
        """
        result = {"msg": "login success", "code": 200}
        return result

    @api_data
    def logout_test(self,name):
        """
        :description test退出接口
        :param name: str
        :return: test退出信息success or error
        """
        return "logout success"


# 调用api-data获取接口信息
@api_add
def get_all_api_new(*args, **kwargs):
    _name = sys._getframe().f_code.co_name
    # api_dict = api.dispatcher.method_map
    # api_name_list = api_dict.keys()
    # result = dict()
    # for i in api_name_list:
    #     item = compose_api_info(i, api_dict)
    #     result[i] = item
    # result.pop(_name)
    # result.pop("get_all_api")

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
    result.pop(_name)
    result.pop("hello")
    return result