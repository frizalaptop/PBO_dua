from .connection import Connection

class Db_Admin():
    def __init__(self):
        self._id = None
        self._username = None
        self._password = None
        self._hasLogin = None
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value):
        self._password = value

    @property
    def hasLogin(self):
        return self._hasLogin
    
    @hasLogin.setter
    def hasLogin(self, value):
        self._hasLogin = value
    
    def get(self):
        src = Connection()
        sql = "SELECT * FROM t_admin WHERE id=1"        
        return src.findAll(sql)
    
    def getOne(self):
        src = Connection()
        sql = "SELECT * FROM t_admin WHERE username=%s"
        val = (self._username,)        
        return src.findOne(sql, val)
    
    def create(self):
        src = Connection()
        sql = "INSERT INTO t_admin (username, password, hasLogin) VALUES (%s, %s, %s)"
        val = (self._username, self._password, self._hasLogin)
        return src.create(sql, val)
    
    def updateHasLogin(self):
        src = Connection()
        sql = "UPDATE t_admin SET hasLogin=%s WHERE username=%s"
        val = (self._hasLogin, self._username) 
        src.update(sql, val)

    def updateUser(self):
        src = Connection()
        sql = "UPDATE t_admin SET username=%s, password=%s  WHERE id=%s"
        val = (self._username, self._password, self._id) 
        src.update(sql, val)

    def delete(self):
        src = Connection()
        sql = "DELETE FROM `t_admin` WHERE username=%s"
        val = (self._username,) 
        src.deleteOne(sql, val)
