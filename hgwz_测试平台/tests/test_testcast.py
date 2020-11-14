from datetime import datetime

import requests


class Test_UserApi:
    url = "http://127.0.0.1:5000/testcase"

    def setup(self):
        r = requests.post('http://127.0.0.1:5000/login', json={
            'username': 'seveniruby',
            'password': 'seveniruby'
        })
        assert r.status_code == 200
        assert r.json()['msg'] == 'login success'

        self.token = r.json()['token']

    def test_teatcase_get(self):
        r = requests.get(
            self.url,
            headers={
                'Authorization': 'Bearer ' + self.token
            }
        )
        assert r.status_code == 200
        assert r.json()['message'] == 'TestCase'

    def test_teatcase_post(self):
        r = requests.post(
            self.url,
            headers={
                'Authorization': 'Bearer ' + self.token
            },
            json={
                'name': 'hjc testname' + str(datetime.now()),
                'data': 'click a;click b'
            }
        )
        assert r.status_code == 200

        r = requests.get(
            self.url,
            headers={
                'Authorization': 'Bearer ' + self.token
            }
        )
        assert r.status_code == 200

    def test_testcast_put(self):
        r = requests.post(
            self.url,
            headers={
                'Authorization': 'Bearer ' + self.token
            },
            params={
                'id': 7
            },
            json={
                'data': 'click a2;click b2'
            }
        )
        assert r.status_code == 200

        r = requests.get(
            self.url,
            headers={
                'Authorization': 'Bearer ' + self.token
            }
        )
        assert r.status_code == 200
        # 在服务端可以写成testcase.data，但是在客户端，只能使用testcase['data']
        data = [testcase['data'] for testcase in r.json() if testcase['id'] == 7][0]
        assert 'b2' in data
