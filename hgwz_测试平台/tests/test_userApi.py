from unittest import TestCase
import requests


class TestUserApi(TestCase):
    # 登录测试
    def test_post(self):
        r = requests.post('http://127.0.0.1:5000/login', json={
            'username': 'test_hjc',
            'password': 'test_hjc'
        })
        assert r.status_code == 200
        print(r.json())

    # 修改密码测试
    def test_modify(self):
        r = requests.patch('http://127.0.0.1:5000/login', json={
            'username': 'test_hjc',
            'password': 'test_hjc',
            'newpassword': 'test_hjc2'
        })
        assert r.status_code == 200
        print(r.json())

    # 删除用户测试
    def test_delete(self):
        r = requests.delete('http://127.0.0.1:5000/login', json={
            'username': 'test_hjc',
            'password': 'test_hjc',
        })

    # 注册用户测试
    def test_put(self):
        r = requests.put('http://127.0.0.1:5000/login', json={
            'username': 'test_hjc',
            'password': 'test_hjc',
            'email': '12345678@qq.com'
        })
        assert r.status_code == 200
