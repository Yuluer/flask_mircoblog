from flask import Flask,render_template#从flask包中导入Flask类
from config import Config

from flask_sqlalchemy import SQLAlchemy#从包中导入类
from flask_migrate import Migrate

ath = Flask(__name__)
# print('等会谁（哪个包或模块）在使用我：',__name__)
ath.config.from_object(Config)


db = SQLAlchemy(ath)#数据库对象
migrate = Migrate(ath, db)#迁移引擎对象

from app import routes,models#从app包中导入模块routes#将Flask类的实例 赋值给名为 app 的变量。这个实例成为app包的成员。

