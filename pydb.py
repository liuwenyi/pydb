       
class pydb(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(pydb, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

    def __init__(self,db):
        self.db=db
    def connection(self,ip,port,uname,pwd,db_name):
        return self.db.connection(ip,port,uname,pwd,db_name)
    def insert(self):
        return self.db.insert()
    def update(self):
        return self.db.update()
    def select(self):
        return self.db.select()
    def delete(self):
        return self.db.delete()
    def printdb(self):
        return self.db.printdb()


