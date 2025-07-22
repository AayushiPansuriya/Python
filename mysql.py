#unit-4

#connectivity with SQLite

import sqlite3
con=sqlite3.connect('data.dp')

#creating the table named stud

 # con.execute('CREATE TABLE stud1(ENR integer,NAME varchar)')

#inserting records
# con.execute("""
# 	INSERT INTO stud1 values
# 	(101,'abc'),
# 	(102,'cde')
# 	""")
# con.commit()


#display all the records
# cursor=con.execute('SELECT * FROM STUD1')
# for i in cursor:
# 	print(i)

#display record whose ENR is 102
# cursor=con.execute('SELECT * FROM stud1 WHERE ENR=102')
# for i in cursor:
# 	print(i)

#update the NAME of the student whose ENR is 102
# update='''UPDATE stud1 SET NAME="XYZ" WHERE ENR=102'''
# con.execute(update)
# cursor=con.execute('SELECT * FROM stud1')
# for i in cursor:
# 	print(i)


#delete the student whose Name is xyz

delete='''delete from stud1 where NAME="cde"'''
con.execute(delete)
cursor=con.execute('SELECT * FROM stud1')
for i in cursor:
	print(i)



