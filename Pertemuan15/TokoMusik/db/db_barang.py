from .connection import Connection

class Db_Barang():
    def __init__(self):
        self._id = None
        self._nama = None
        self._harga = None
        self._available = None
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value

    @property
    def nama(self):
        return self._nama
    
    @nama.setter
    def nama(self, value):
        self._nama = value

    @property
    def harga(self):
        return self._harga
    
    @harga.setter
    def harga(self, value):
        self._harga = value

    @property
    def available(self):
        return self._available
    
    @available.setter
    def available(self, value):
        self._available = value
    

    def getAll(self):
        src = Connection()
        sql = "SELECT * FROM t_barang"
        return src.findAll(sql)
    
    def getOne(self):
        src = Connection()
        sql = "SELECT * FROM t_barang WHERE id=%s OR nama=%s"
        val = (self.id, self.nama)        
        return src.findOne(sql, val)
    
    def create(self):
        src = Connection()
        sql = "INSERT INTO t_barang (nama, harga, available) VALUES (%s, %s, %s)"
        val = (self._nama, self._harga, self._available) 
        src.create(sql, val)
    
    def update(self):
        src = Connection()
        sql = "UPDATE t_barang SET nama=%s, harga=%s, available=%s, jumlah=%s, keluar=%s, wakel=%s, jumkel=%s WHERE id=%s"
        val = (self._nama, self._harga, self._available, self._jumlah, self._keluar, self._wakel, self._jumkel, self._id,) 
        src.update(sql, val)
        return self.getOne()

    def deleteOne(self):
        src = Connection()
        sql = "DELETE FROM t_barang WHERE id=%s"
        val = (self._id,)
        src.deleteOne(sql,val)
