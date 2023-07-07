import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='newparole420', database='my_first_db')

# mycursor = mydb.cursor()
#
# mycursor.execute('SHOW DATABASES')
#
# for i in mycursor:
#     print(i)

# mycursor2 = mydb.cursor()
# mycursor2.execute('SELECT * from countries')
# result2=mycursor2.fetchall()
# for i in result2:
#     print(i)

mycursor=mydb.cursor()

# mycursor.execute('create database my_first_db')
# mycursor.execute('create table student(id INT, name VARCHAR(255))')
# mycursor.execute('create table employee(id INT auto_increment primary key, name VARCHAR(255), salary INT(6))')
#
# mycursor.execute('ALTER TABLE student ADD PRIMARY KEY (id)')

# mycursor.execute('insert into student set name = "John", id=1')
# mydb.commit()
#
# sql2='insert into employee(name, salary) values(%s, %s)'
# val2=[('John', '10000')]
# # #
# mycursor.executemany(sql2, val2)
# mydb.commit()
# print(mycursor.rowcount, 'it was inserted')