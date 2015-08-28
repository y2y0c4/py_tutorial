import sqlite3
class db_handler:
    def __init__(self):
        self.conn = sqlite3.connect('library2.db')
        self.cursor = self.conn.cursor()
    def __creat__(self):
        try:
            self.cursor.execute('CREATE TABLE library( name VARCHAR(20), auth VARCHAR(20), price int(10))')
            return 'succes'
        except sqlite3.OperationalError:
            return 'error'
    def __dele__(self):
        self.cursor.execute("DROP TABLE IF EXISTS library")
    def __insert__(self, name, auth, price):
        que = "INSERT INTO library VALUES('{0}','{1}',{2})".format(name, auth, price)
        self.cursor.execute(que)
        self.conn.commit()
    def __select__(self, res):
        self.cursor.execute('select * from library')
        res=self.cursor.fetchall()
        return res
    def __close__(self):
        self.conn.close()
    
