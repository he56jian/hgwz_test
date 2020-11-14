from unittest import TestCase
import requests


class TestUserApi(TestCase):
    def test_post(self):
        r = requests.post('http://127.0.0.1:5000/login', json={
            'username': 'seveniruby',
            'password': 'seveniruby'
        })
        assert r.status_code == 200
        print(r.json())
