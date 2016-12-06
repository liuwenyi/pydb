import pydb
import MySQLdb

class mysqldb(pydb.pydb):
    def __init__(self):
        print "This is Mysql init"
    def insert(self,table, item, data):
        db_chk = self.select(table,item[0],"%s=%s"%(item[0],data[0]))
        if db_chk != 0 :
            return -1
        # todo: how to print the items
        return 0
    def update(self):
        pass
    def select(self, table, key , arg=''):
        if arg != '':
            arg = "where %s"%arg
        query_str = "select %s from %s %s"%(key,table,arg)
        cursor=self.__conn.cursor()
        n = cursor.execute(query_str)
        if n != 0:
            return cursor
        cursor.close()
        self.__conn.commit()
        return 0
    def delete(self):
        pass
    def printdb(self):
        print "Hello Mysql"
    def connection(self,ip,port,uname,pwd,db_name):
        try:
            self.__conn=MySQLdb.connect(host=ip,user=uname,passwd=pwd,db=db_name)
            #self.__conn.query("select version()")
            #result = self.__conn.use_result()
            #print "Mysql version: %s " % result.fetch_row()[0]
        except MySQLdb.Error, e:
            print "[pydb Error %d]: %s." % (e.args[0], e.args[1])