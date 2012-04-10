网上商店文档
============

安装依赖包
---------

+   安装python
+   安装setuptools和pip
+   用pip安装依赖包，tornado（服务器），flask，peewee，flask_peewee, Whoosho+   设置settings.py文件

settings.py设置
---------------

+   appname: 商店名称，考虑到一些东西，商店名称放到设置文件中
+   indexdir: 存放索引文件
+   database: 设置数据库，为检查方便，用了sqlite，如果用mysql还要安装mysql的依赖包
+   port: 服务器端口号
+   im_host: 即时通讯的服务地址
+   forum_host: BBS的服务地址

运行
----

+   python syncdb.py (产生数据库，为测试方便，带有生成随即数据)
+   python build_index.py （生成商品索引，真实情况下定时运行）
+   python shop.py （运行服务器）

实现功能
-------

+   实现了所有的基本功能（如果没有记错的话）
+   实现了7个红字标的附加功能（除发送商品信息外）
+   实现了一个额外的附加功能，即时通讯（求加分）
