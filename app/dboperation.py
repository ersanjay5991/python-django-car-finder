'''
this code use for modify a sqlite3 database need to write a sql query 
'''

import sqlite3
conn = sqlite3.connect('database.db') 
print('Database connection created.') 
conn.execute('''create table Student 
(S_id int primary key, 
S_name text, 
S_roll int, 
S_phone int)''') 
print ('Table created.') 
conn.close()