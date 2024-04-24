from db import DBConnection as mydb

class Food:

    def __init__(self):
        self.__id=None
        self.__nama=None
        self.__lv_pedas=None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def id(self):
        return self.__id

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def lv_pedas(self):
        return self.__lv_pedas

    @lv_pedas.setter
    def lv_pedas(self, value):
        self.__lv_pedas = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__nama, self.__lv_pedas)
        sql="INSERT INTO warteg (nama, lv_pedas) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__nim, self.__nama, self.__jk, self.__kode_prodi, id)
        sql="UPDATE warteg SET nim = %s, nama = %s, jk=%s, kode_prodi=%s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByNIM(self, nim):
        self.conn = mydb()
        val = (self.__nama, self.__jk, self.__kode_prodi, nim)
        sql="UPDATE warteg SET nama = %s, lv_pedas=%s WHERE nama=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM warteg WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByNIM(self, nama):
        self.conn = mydb()
        sql="DELETE FROM warteg WHERE nim='" + str(nama) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM warteg WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__nim = self.result[1]
        self.__nama = self.result[2]
        self.__jk = self.result[3]
        self.__kode_prodi = self.result[4]
        self.conn.disconnect
        return self.result

    def getByNIM(self, nim):
        a=str(nim)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM warteg WHERE nama='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__nim = self.result[1]
            self.__nama = self.result[2]
            self.__jk = self.result[3]
            self.__kode_prodi = self.result[4]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nim = ''
            self.__nama = ''
            self.__jk = ''
            self.__kode_prodi = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM warteg"
        self.result = self.conn.findAll(sql)
        return self.result

# delete Data
A = Food()
B = A.getAllData()
print(B)