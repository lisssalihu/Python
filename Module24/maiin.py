import sqlite3


connection = sqlite3.connect('example.db')


cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS employees(


        id INTEGER primary key autoincrement ,
        name text not null ,
        position text not null ,
        department text not null ,
        salary real
        )
''')

connection.commit()
