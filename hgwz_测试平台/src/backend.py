from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)  # 路由初始化

# 数据库连接配置，和初始化
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lagou3:lagou3@stuq.ceshiren.com:23306/lagou3'
db = SQLAlchemy(app)


# 数据库结构，表为User表
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # unique是否能相同，True为不能相同
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


# @app.route('/')
# def hello_world():
#     return 'hello world'

# 用户管理
class UserApi(Resource):
    def get(self):
        users = User.query.all()
        return [{'id': u.id, 'username': u.username} for u in users]
        return {'message': 'user'}


# 用例管理
class TestCaseApi(Resource):
    def get(self):
        return {'message': 'TestCase'}


# 任务管理
class TaskApi(Resource):
    def get(self):
        return {'message': 'TestCase'}


# 报告管理
class ReportApi(Resource):
    def get(self):
        return {'message': 'TestCase'}


# 首页管理
class Main(Resource):
    def get(self):
        return {'message': 'TestCase'}


api.add_resource(Main, '/')
api.add_resource(UserApi, '/login')  # 把HelloWorld绑定到 / 路由中；
api.add_resource(TestCaseApi, '/testcase')  # 把HelloWorld绑定到 / 路由中；
api.add_resource(TaskApi, '/task')  # 把HelloWorld绑定到 / 路由中；
api.add_resource(ReportApi, '/report')  # 把HelloWorld绑定到 / 路由中；

if __name__ == '__main__':
    app.run(debug=True)
