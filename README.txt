pythonsite

============================================================================================
2018-02-09
运用蓝图重新构建项目架构
项目结构
pythonsite
|____commonapp 项目公共模块
|	|____forms 表单
|	|____models 模型
|	|____urls 路由
|	|____views 视图
|	|____ __init__.py 新建common蓝图、引入commonapp模块的视图和路由
|
|____migrations
|
|____static 静态文件
|
|____templates 模板
|
|____venv 项目虚拟环境
|
|____.gitignore git忽略文档
|
|____config.py 配置文件
|
|____exts.py 扩展组件
|
|____manage.py 数据库迁移文件
|
|____pythonsite.py 项目程序主入口
|
|____README.txt 项目说明文档


============================================================================================
2018-02-06
本项目旨在开发一套接口自动化测试工具
1、本项目主体框架采用flask web框架，并结合flask-script、flask-migrate、flask-sqlalchemy做数据库迁移
2、ubuntu环境中安装及使用pip来安装依赖库
安装pip3：
sudo apt install python3-pip
安装虚拟环境：
sudo pip3 install virtualenv
创建虚拟环境
virtualenv venv
激活虚拟环境：
source ./venv/bin/activate
在虚拟环境中安装三方库：
pip3 install flask
pip3 install flask-script
pip3 install flask-migrate
pip3 install flask-sqlalchemy
pip3 install flask-bootstrap3
pip3 install flask-wtf
pip3 install flask-login
pip3 install flask-security
pip3 install flask-admin
退出虚拟环境：
deactivate