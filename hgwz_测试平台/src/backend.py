from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


#
# @app.route('/')
# def hello_world():
#     return 'hello world'

# 用户管理
class UserApi(Resource):
    def get(self):
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
