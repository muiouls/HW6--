import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = False
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error as e:
        print(e)

def create_student(conn, student):
    sql = '''INSERT INTO student (name, mark, hobby, b_date, is_married)
    VALUES (?,?,?,?,?)
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, student)
        conn.commit()
    except Error as e:
        print(e)

def read(conn):
    try:
        sql = 'SELECT * FROM student'
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        for i in rows:
            print(i)
    except Error as e:
        print(e)

def delete_record(conn):
    sql_delete = '''DELETE FROM student WHERE id = 1'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql_delete)
        conn.commit()
    except Error as e:
        print(e)

def update_v(conn, id, name):
    update_values = '''UPDATE student set name = ? WHERE id = ?'''
    nm = (name, id)
    try:
        cursor = conn.cursor()
        cursor.execute(update_values, nm)
        conn.commit()
    except Error as e:
        print(e)


database = r'puge.db'

sql_create_table = '''
CREATE TABLE student(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR (104) NOT NULL,
mark FLOAT NOT NULL DEFAULT 0.0,
hobby TEXT DEFAULT NULL,
b_date DATE NOT NULL ,
is_married BOOLEAN DEFAULT FALSE
);
'''

connection = create_connection(database)
if connection is not None:
    #create_table(connection, sql_create_table)
    #create_student(connection,('Жаннат', 10.0, 'пишу', '2003-05-07', False))
    delete_record(connection)
    update_v(connection, 2, 'Алина')
    read(connection)
    print('Все работает')
