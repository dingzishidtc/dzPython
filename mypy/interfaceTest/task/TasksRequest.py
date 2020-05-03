#coding:utf8
from . import TasksFilter

class TasksRequests(object):
    offset = 0
    limit = 0
    filter = TasksFilter()
    def __init__(self,offset,limit,filter):
        self.offset = offset
        self.limit = limit
        self.filter = filter

    # def getOffect(self):
    #     return self.offset
    #
    # def setOffect(self,offect):
    #     self.offset = offect
    #
    # def getLimit(self):
    #     return self.limit
    #
    # def setLimit(self, limit):
    #     self.limit = limit
    #
    # def getFilter(self):
    #     return self.filter
    #
    # def setFilter(self, filter):
    #     self.offset = filter

class CancelTasksRequest(object):
    op = ""

    def __init__(self, op):
        self.op = op


