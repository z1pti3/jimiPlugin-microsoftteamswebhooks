import requests
import json
from pathlib import Path

class _microsoftteamswebhooks():

    def __init__(self, url, ca=None, requestTimeout=30):
        self.requestTimeout = requestTimeout
        self.url = url
        if ca:
            self.ca = Path(ca)
        else:
            self.ca = None

    def apiCall(self,methord="GET",data=None):
        kwargs={}
        kwargs["timeout"] = self.requestTimeout
        kwargs["headers"] = { "Content-Type" : "application/json" }
        if self.ca:
            kwargs["verify"] = self.ca
        try:
            url = "{0}".format(self.url)
            if methord == "GET":
                response = requests.get(url, **kwargs)
            elif methord == "POST":
                kwargs["data"] = data
                response = requests.post(url, **kwargs)
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
            return "Connection Timeout", 0
        if response.status_code == 200 or response.status_code == 202:
            return json.loads(response.text), response.status_code
        return None, response.status_code

    def postMessage(self,message):
        data = { "text" : message }
        response, statusCode = self.apiCall(methord="POST",data=json.dumps(data))
        return response
