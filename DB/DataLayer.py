import sqlite3

class Database:


    @staticmethod
    def __init__(self, name):
        self._conn = sqlite3.connect("GDB.db")
        self._cursor = self._conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()

    def insertExcel (self , ExcelList:list):
        for item in ExcelList:
            res = self.query(f'SELECT 1 FROM ValidGaranties where Refrence = {item[1]}  ;')
            if res:
                queryStr = f'UPDATE ValidGaranties SET  Desc = \'{item[2]}\' , Start = \'{item[3]}\' , End = \'{item[4]}\' WHERE Refrence = {item[1]} ; '
                self.execute(queryStr)
                self.commit()
            else:
                queryStr = f'INSERT INTO ValidGaranties (Refrence,Desc,Start,End) VALUES ({item[1]},\'{item[2]}\',\'{item[3]}\',\'{item[4]}\');'
                self.execute(queryStr)
                self.commit()






