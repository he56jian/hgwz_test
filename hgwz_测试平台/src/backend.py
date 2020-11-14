from flask import Flask, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)  # 路由初始化(

# 数据库连接配置，和初始化
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lagou3:lagou3@stuq.ceshiren.com:23306/lagou3'
db = SQLAlchemy(app)

# token配置
app.config['JWT_SECRET_KEY'] = 'he56jian'  # token密钥
jwt = JWTManager(app)


# 数据库结构，表为User表
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # unique是否能相同，True为不能相同
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


# 任务表结构定义
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    log = db.Column(db.String(1024), unique=False, nullable=False)
    # 数据库的一对多模型
    # 关联,使用db.ForeignKey('testcase_id')，表示外键指向的是testcase_id(即testcase表的主键
    testcase_id = db.Column(db.Integer, db.ForeignKey('test_case_id'), nullable=False)
    # 反向引用，根据key时获取其内容,即使用test_case_id的时候的结果
    testcase = db.relationship('TestCase', backref=db.backref('task', lazy=True))

    def __repr__(self):
        return '<TestCase %r' % self.name


# 参数用例表类
class TestCase(db.Model):
    # 可以重新定义表的名字
    # __tablename__ = '表名'

    id = db.Column(db.Integer, primary_key=True)
    # unique是否能相同，True为不能相同
    name = db.Column(db.String(80), unique=True, nullable=False)
    # 指向测试数据的标记,步骤
    data = db.Column(db.String(1024), unique=False, nullable=False)

    def __repr__(self):
        return '<TestCase %r' % self.name


# @app.route('/')
# def hello_world():
#     return 'hello world'

# 用户管理接口
class UserApi(Resource):
    # 用户查询
    def get(self):
        users = User.query.all()
        return [{'id': u.id, 'username': u.username, 'password': u.password, 'email': u.email} for u in users]

    # 用户登录
    def post(self):
        # 通过客户端的json中拿到username/password
        username = request.json.get('username')
        password = request.json.get('password')
        email = request.json.get('email')
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            if username:
                # 登录成功后返回用户一个token
                access_token = create_access_token(identity=username)
            elif email:
                access_token = create_access_token(identity=email)
            return {'msg': 'login success', 'token': access_token}
        else:
            return {
                'msg': 'login fail '
            }

    # 用户注册
    def put(self):
        username = request.json.get('username')
        password = request.json.get('password')
        email = request.json.get('email')
        user = User(username=username, password=password, email=email)
        db.session.add(user)
        db.session.commit()
        return {'msg': 'register success'}

    # 用户账号销毁
    def delete(self):
        username = request.json.get('username')
        password = request.json.get('password')
        email = request.json.get('email')
        user = User.query.filter_by(username=username, password=password).first()
        db.session.delete(user)
        db.session.commit()

    # 用户密码修改
    # @jwt_required
    def patch(self):
        username = request.json.get('username')
        password = request.json.get('password')
        newpassword = request.json.get('newpassword')
        # email = request.json.get('email')

        user = User.query.filter_by(username=username, password=password).first()
        user.password = newpassword
        db.session.commit()
        return {
            'msg': 'password modified successfully'
        }


# 用例管理接口
class TestCaseApi(Resource):
    # 该装饰器用于说明，当前需要使用token才能使用，会自动使用token校验；
    # @jwt_required
    def get(self):
        return [{'id': testcase.id, 'name': testcase.name, 'data': testcase.data} for testcase in TestCase.query.all()]

    @jwt_required
    def post(self):
        """
        发起的是/testcase, post ,表示新增
        发起的是/testcase?id=1, post，表示修改
        :return:
        """
        param_id = request.args.get('id')
        if param_id:
            # 是否添加了?格式参数
            testcase = TestCase.query.filter_by(id=param_id).first()
            if request.json.get('name'):
                testcase.name = request.json.get('name')
            if request.json.get('data'):
                testcase.data = request.json.get('data')
            db.session.flush()
            db.session.commit()
        else:

            # request.json获得的是客户端发过来的数据
            testcase = TestCase()
            testcase.name = request.json.get('name')
            testcase.data = request.json.get('data')
            db.session.add(testcase)
            db.session.commit()

    @jwt_required
    def put(self):
        pass

    @jwt_required
    def delete(self):
        pass


# 任务管理接口
class TaskApi(Resource):
    # @jwt_required
    def get(self):
        return [{'id': task.id, 'log': task.log, 'testcase_id': task.testcase_id} for task in Task.query.all()]

    @jwt_required
    def post(self):
        """
        发起的是/testcase, post ,表示新增
        发起的是/testcase?id=1, post，表示修改
        :return:
        """
        # request.json获得的是客户端发过来的数据
        task = Task()
        if request.json.get('log'):
            task.log = request.json.get('log')
        if request.json.get('testcase_id'):
            task.testcase_id = request.json.get('testcase_id')
        db.session.add(task)
        db.session.commit()

    @jwt_required
    def put(self):
        pass

    @jwt_required
    def delete(self):
        pass


# 报告管理接口
class ReportApi(Resource):
    def get(self):
        return {'message': 'TestCase'}


# 首页管理接口
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
