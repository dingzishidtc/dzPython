#coding: UTF-8
import unittest
import requests
import json
from task import TasksRequest, TasksFilter


#2.3.1	列表（支持筛选）
class Tasks(unittest.TestCase):
    url = "https://10.23.140.75:8083"

    def taskList(self, path, tasksRequest,TasksFilter):

        requestUrl = Tasks.url + "/tasks-server/tasks/"
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.get(url=requestUrl, headers=headers, data=tasksRequest)
        tasksfilter = TasksFilter()
        print(response)


    def test_cancel_task(self, op, path):
        if op is None:
            raise Exception("op为必须参数，请传参！")
        else:
            requestUrl = Tasks.url + path
            headers = {
                'Content-Type': 'application/json'
            }
            res = requests.patch(requestUrl, headers=headers, data=paras)
            data = json.loads(res.text)
            self.assertEqual(data["status"], 200)

    def test_get_taskDetail(self, path):




tasksfilter = TasksFilter(101,"屋顶")
tasksRequest = TasksRequest(0,10,None)
server = '127.0.0.1'
port = 8891

taskList(server,port,tasksRequest,tasksfilter)
