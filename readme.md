- 使用docker-compose启动： docker-compose up -d

- 使用gunicorn启动：gunicorn -c gun.conf  run:app

-  调试运行：python run.py

 - - -

 - 运行后，localhost:5000/api_test/ 为api测试页面

 - 其中flaskapi包也可以从内网pypi镜像站安装

 - 在appmanage.py中:

   ```python
   app.register_blueprint(api.as_blueprint())
   CORS(app, supports_credentials=True)
   ```

 - 例如在demo_api.py中需要写接口

  > from flaskapi.api import api_add

 - 然后在appmanage.py中导入即可：

  > from demo_api import *

 - 接口注释根据pycharm的自动补全，在参数后面填写数据类型即可；其中:description为接口描述（可选项）

 - 接口模型：


 ```python
@api.dispatcher.add_method
def my_method(param_dict, param_int, param_str, param_list):
    """
    :description  测试接口
    :param param_dict: dict:字典参数
    :param param_int: int:整型参数
    :param param_str: str:字符串参数
    :param param_list: list:列表参数
    :return: code or message
    """
    return result
 ```

---

### 效果图

- 此项目中使用了flask-api或api-data两种方法分别实现获取接口信息。

  - 使用flask-api包时，在flaskapi/common.py中已经实现了get_all_api接口。

  - 使用api-data包时，在demo_api.py中实现了get_all_api_new接口，调用api-data中的方法进行返回数据。

  - 默认调用get_all_api接口（使用flask-api包），当更改更改为get_all_api_new时，则使用了api-data。

![api-test](picture/show.gif)
