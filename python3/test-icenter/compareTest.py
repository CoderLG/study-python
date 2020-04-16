import csv
from locust import HttpLocust, TaskSet, task, between
import random


class lgTasting(TaskSet):

    def placeLikeQuery(self,name,type):
        self.client.get("/placeservice/api/v2/query/placeName="+name,name='placeLikeQuery'+str(type))

    def placeQueryByCoding(self, code):
        self.client.get("/placeservice/api/v2/query/dlbm=" + code, name='placeQueryByGeoCoding')
    # @task
    def queryByCoding(self):
        # 地理编码查询
        with open('csv/place/geocoding.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                self.placeQueryByCoding(row[0])


    @task
    def placeTask(self):
        # 一个字
       # self.placeLikeQuery(chr(random.randint(0x4e00, 0x9fbf)),1)

        # 两个字
       # self.placeLikeQuery(chr(random.randint(0x4e00, 0x9fbf))+chr(random.randint(0x4e00, 0x9fbf)),2)


        #三个字以上
        self.placeLikeQuery(chr(random.randint(0x4e00, 0x9fbf)) + chr(random.randint(0x4e00, 0x9fbf))+chr(random.randint(0x4e00, 0x9fbf)), 3)
        # with open('csv/place/placeName.csv', 'r',encoding= 'utf-8') as f:
        #     reader = csv.reader(f)
        #     for row in reader:
        #         str = row[0]
        #         if(len(str) >= 5 ):
        #             queryName = str[1:len(str)-1]
        #             self.placeLikeQuery(queryName,3)


class UserTaskRunner(HttpLocust):
    task_set = lgTasting
    min_wait = 10
    max_wait = 30

    # wait_time = between(0.0001, 0.0001)





