from pydb import pydb
from mysql import mysqldb


        
if __name__ == "__main__":

    my=pydb(mysqldb())
    my.printdb()
