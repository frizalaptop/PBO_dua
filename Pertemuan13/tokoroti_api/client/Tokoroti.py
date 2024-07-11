import requests
import json

class Tokoroti:

    def __init__(self):
        self.__id=None
        self.__kd_produk=None
        self.__nama=None
        self.__stok=None
        self.__url="http://localhost/webapi/tokoroti_api.php"
               
    @property
    def id(self):
        return self.__id

    @property
    def kd_produk(self):
        return self.__kd_produk

    @kd_produk.setter
    def kd_produk(self, value):
        self.__kd_produk = value

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, value):
        self.__stok = value

        
    def getByKd_produk(self, kd_produk):
        url = self.__url+"?kd_produk="+kd_produk
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id=item["id"]
            self.__kd_produk=item["kd_produk"]
            self.__nama=item["nama"]
            self.__stok=item["stok"]
        return data
               

    def simpan(self):
        payload = {
            "kd_produk":self.__kd_produk,
            "nama":self.__nama,
            "stok":self.__stok,
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    
    def updateByKd_produk(self, kd_produk):
        url = self.__url+"?kd_produk="+kd_produk
        payload = {
            "kd_produk":self.__kd_produk,
            "nama":self.__nama,
            "stok":self.__stok,
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    
    def getAllData(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    
    def deleteByKd_produk(self,kd_produk):
        url = self.__url+"?kd_produk="+kd_produk
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
    