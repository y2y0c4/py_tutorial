import sqlite3
class db_handler:
    def __init__(self):
        self.conn = sqlite3.connect('nameage.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("DROP TABLE IF EXISTS nameage")
        self.cursor.execute('CREATE TABLE nameage( name VARCHAR(20), age int(10))')
    def __insert__(self, name, age):
        que = "INSERT INTO nameage VALUES('{0}',{1})".format(name, age)
        self.cursor.execute(que)
        self.conn.commit()
    def __select__(self):
        self.cursor.execute('select * from nameage')
        print(self.cursor.fetchall())
    def __close__(self):
        self.conn.close()
    
