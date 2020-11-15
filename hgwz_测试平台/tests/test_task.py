from datetime import datetime

import requests


class Test_TaskApi:
    url = "http://127.0.0.1:5000/task"

    def setup(self):
        r = requests.post('http://127.0.0.1:5000/login', json={
            'username': 'seveniruby',
            'password': 'seveniruby'
        })
        assert r.status_code == 200
        assert r.json()['msg'] == 'login success'

        self.token = r.json()['token']

    def test_task_get(self):
        r = requests.get(
            self.url,
            headers={
                'Authorization': 'Bearer ' + self.token
            }
        )

    def test_task_post(self):
        r = requests.post(
            self.url,
            headers={
                'Authorization': 'Bearer ' + self.token
            },
            json={
                'log': 'log ' + str(datetime.now()),
                'testcase_id': 1
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
