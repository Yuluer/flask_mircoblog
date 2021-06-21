from flask import Flask,render_template#从flask包中导入Flask类

ath = Flask(__name__)
print('等会谁（哪个包或模块）在使用我：',__name__)

from app import routes#从app包中导入模块routes#将Flask类的实例 赋值给名为 app 的变量。这个实例成为app包的成员。

