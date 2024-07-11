import mysql.connector as mc

class Connection:

    def __init__(self):
        self.host = 'localhost'
        self.port = 3306
        self.name = 'webapi'
        self.user = 'root'
        self.password = ''
        # self.host = 'sql.freedb.tech'
        # self.port = 3306
        # self.name = 'freedb_warehouse_management'
        # self.user = 'freedb_muhamad_friza'
        # self.password = '4z!UM%$Y&Dyj9rx'
        self.conn = None
        self.cursor = None
        self.result = None
        self.connected = False
        self.affected = 0
        self.connect()
        
    @property
    def info(self):
        if(self.connected==True):
            return "Server is running on " + self.host + ' using port ' + str(self.port)
        else:
            return "Server is offline."
        
    @property
    def connection_status(self):
        return self.connected
    
    def connect(self):
        try:
            self.conn = mc.connect(host = self.host,
                                    port = self.port,
                                    database = self.name,
                                    user = self.user,
                                    password = self.password)

            self.connected = True
            self.cursor=self.conn.cursor()
        except mc.Error as e:
            self.connected = False
        return self.conn

    def disconnect(self):
        if(self.connected==True):
            self.conn.close
        else:
            self.conn = None

    def findOne(self, sql, val):
        self.connect()
        self.cursor.execute(sql, val)
        self.result = self.cursor.fetchone()
        return self.result

    def findAll(self, sql):
        self.connect()
        self.cursor.execute(sql)
        self.result = self.cursor.fetchall()
        return self.result

    def create(self, sql, val):
        self.connect()  
        self.cursor.execute(sql, val)
        self.conn.commit()
        return self.cursor.lastrowid

    def update(self, sql, val):
        self.connect()  
        self.cursor.execute(sql, val)
        self.conn.commit()

    def deleteOne(self, sql, val):
        self.connect()  
        self.cursor.execute(sql, val)
        self.conn.commit()



