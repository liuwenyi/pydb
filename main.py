from pydb import pydb
from mysql import mysqldb


        
if __name__ == "__main__":

    my=pydb(mysqldb())
    my.printdb()
    my.connection("127.0.0.1","3306","root","root","pytest")

