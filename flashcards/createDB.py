import sqlite3

conn = sqlite3.connect("database/fc.db")

conn.execute(''' CREATE TABLE categories (
    id_cat INT PRIMARY KEY NOT NULL, 
    desc TEXT NOT NULL);''')

conn.execute(''' CREATE TABLE cards(
    id_card PRIMARY KEY NOT NULL, 
    id_cat INT NOT NULL, 
    question TEXT NOT NULL, 
    answer TEXT NOT NULL, 
    reviews INT);''')

conn.execute(''' CREATE TABLE images(
    id_image PRIMARY KEY NOT NULL, 
    id_card INT NOT NULL, 
    path TEXT NOT NULL, 
    file_name TEXT NOT NULL, 
    extension CHAR(3) NOT NULL);''')

""" conn.execute(''' DROP TABLE categories ''')
conn.execute(''' DROP TABLE cards ''')
conn.execute(''' DROP TABLE images ''') """

conn.commit()
conn.close()
