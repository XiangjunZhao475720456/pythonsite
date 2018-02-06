pythonsite

2018-02-06
本项目旨在开发一套接口自动化测试工具
1、本项目主体框架采用flask web框架，并结合flask-script、flask-migrate、flask-sqlalchemy做数据库迁移
2、ubuntu环境中安装及使用pip来安装依赖库
安装pip3：
sudo apt install python3-pip
安装虚拟环境：
sudo pip3 install virtualenv
激活虚拟环境：
source ./activate
在虚拟环境中安装三方库：
pip3 install flask
pip3 install flask-script
pip3 install flask-migrate
pip3 install flak-sqlalchemy
退出虚拟环境：
deactivate