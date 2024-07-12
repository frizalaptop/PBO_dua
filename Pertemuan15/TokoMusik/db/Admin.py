import requests
import json

class Admin:

    def __init__(self):
        self.__id=None
        self.__username=None
        self.__password=None
        self.__hasLogin=None
        self.__url="http://localhost/webapi/admin_api.php"
               
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value
    
    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def hasLogin(self):
        return self.__hasLogin

    @hasLogin.setter
    def hasLogin(self, value):
        self.__hasLogin = value
        
    def getByUsername(self, username):
        url = self.__url+"?username="+username
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id=item["id"]
            self.__username=item["username"]
            self.__password=item["password"]
            self.__hasLogin=item["hasLogin"]
        return data
               

    def simpan(self):
        payload = {
            "username":self.__username,
            "password":self.__password,
            "hasLogin":self.__hasLogin
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    
    def updateById(self, id):
        url = self.__url+"?id="+id
        payload = {
            "username":self.__username,
            "password":self.__password,
            "hasLogin":self.__hasLogin
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        data = json.loads(response.text)
        return data
    
    def updateHasLogin(self):
        url = self.__url+"?username="+self.username
        payload = {
            "username":self.__username,
            "hasLogin":self.__hasLogin
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    
    def getAllData(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    
    def deleteByUsername(self,username):
        url = self.__url+"?username="+username
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
    