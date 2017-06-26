开始
==========

安装
------------

.. highlight:: bash

:Requirements: **Python 2.6, 2.7**, **Python 3.x >= 3.2** or **PyPy**
* 安装依赖 ：pip install -r requirements.txt
* 运行： python run.py
* gunicorn启动：gunicorn - c gun.conf run:app
* 默认api测试页面： http://localhost:5000/api_test/
* config.py用于常量配置
* gun.conf 用于gunicorn配置
* appmanage.py用于flask.app的运行设置
* controller/api 用于存放接口文件
* docs用于文档维护
* tests存放测试用例
* utils存放工具组件


