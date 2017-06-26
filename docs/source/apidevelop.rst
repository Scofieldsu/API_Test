写一个接口
==========


 在controller/api/base_api.py中使用** @api.dispatcher.add_method **装饰器，依据pycharm补全的方法注释，对参数加上数据类型。
 其中:description是我们自己加上的，为了对接口进行描述。

 .. code-block:: python

    @api.dispatcher.add_method
    def test_api(param_dict, param_int, param_str, param_list):
        """
        :description  测试接口
        :param param_dict: dict
        :param param_int: int
        :param param_str: str
        :param param_list: list
        :return: code or message
        """
        return "success"

这样接口就写好了，可以在接口测试页面 http://localhost:5000/api_test/ 去测试你的接口。


或者你可以在 controller/api/ 中添加自己的接口文件，例如loginout.py,但是在你的接口文件中记得

.. code-block:: python

 from jsonrpc.backend.flask import api

写完以后，需要在controller/common.py中导入你的接口文件：

.. code-block:: python

 from controller.api.loginout import *