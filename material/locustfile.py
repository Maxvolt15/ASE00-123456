import time
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):

    @task(1)
    def add(self):
        for a in range(10):
            self.client.get(f"/add?a={a}00&b=999", name = "ritsu", verify = False)
            time.sleep(1)
    @task(1)
    def mod(self):
        for a in range(3,-1,-1):
            self.client.get(f"/mod?a={a}00&b={a}", name = "yui", verify = False)
            time.sleep(1)

    
    @task(1)
    def mul(self):
        for a in range(10):
            self.client.get(f"/mul?a={a}00&b=999", name = "azusa", verify = False)
            time.sleep(1)

    @task(5)
    def div(self):
        for a in range(10):
            time.sleep(1)
            self.client.get(f"/div?a={a}00&b=999", name = "mio", verify = False)
           
 
    @task(1)
    def sub(self):
        for a in range(10):
            self.client.get(f"/sub?a={a}00&b=999", name = "mugi", verify = False)
            time.sleep(1)
    
    #add your test here