写一个文档
==========

* 准备工作，你需要安装sphinx： pip install sphinx

* 在docs/source/目录下添加你的文档，rst文件类型，并在index.rst文件中的toctree添加你的文件名

* windows环境下，在此目录下打开命令行：call make.bat 然后make html生成文档，在docs/build/html下，打开index.html即可

* linux 或者OSX下，依据Makefile生成文档。在docs／ 路径下打开命令行：make html


关于sphinx的使用以及rst的语法规则可去查看相关官网。