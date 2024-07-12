import requests
import json

class Barang:

    def __init__(self):
        self.__id=None
        self.__nama=None
        self.__harga=None
        self.__available=None
        self.__url="http://localhost/webapi/barang_api.php"
               
    @property
    def id(self):
        return self.__id

    @property
    def kode(self):
        return self.__kode

    @kode.setter
    def kode(self, value):
        self.__kode = value

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, value):
        self.__harga = value
    
    @property
    def available(self):
        return self.__available

    @available.setter
    def available(self, value):
        self.__available = value
        
    def getByNama(self, nama):
        url = self.__url+"?nama="+nama
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id=item["id"]
            self.__nama=item["nama"]
            self.__harga=item["harga"]
            self.__available=item["available"]
        return data
    
    def getById(self, id):
        url = self.__url+"?id="+id
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id=item["id"]
            self.__nama=item["nama"]
            self.__harga=item["harga"]
            self.__available=item["available"]
        return data
               

    def simpan(self):
        payload = {
            "nama":self.__nama,
            "harga":self.__harga,
            "available":self.__available,
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    
    def updateById(self, id):
        url = self.__url+"?id="+id
        payload = {
            "id":self.__id,
            "nama":self.__nama,
            "harga":self.__harga,
            "available":self.__available,
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    
    def getAllData(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    
    def deleteById(self,id):
        url = self.__url+"?id="+id
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
    