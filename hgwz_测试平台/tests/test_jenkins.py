from jenkinsapi.jenkins import Jenkins


def test_jenkins():
    jenkins = Jenkins('http://localhost:8080', username='username', password='token')
    jenkins['lagou3'].invoke(
        securitytoken='自己创建的token',  # 在初始化的时候已经认证，就不需要添加
        build_params={'testcase_id': 1},
        block=True
    )
