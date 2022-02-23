import sqlite3
#database connect
con=sqlite3.connect("movieinformation")
print("connected")
# create table
con.execute("create table movies(moviename text, actor text, actress text,year of release text, directorName text)")
print("created")
# data inserted
con.execute("insert into movies values ('Genius', 'Urvish Sharma', 'Urvashi Patel','2014','Rohit Patel')")
con.execute("insert into movies values ('Education', 'Riyan Sharma', 'Neha Patel','2022','Akash Patel')")
con.execute("insert into movies values ('Success', 'Ginesh Patel', 'Rudra Mehta','2018','Sakshi Soni')")
con.execute("insert into movies values ('Dangal', 'Amir Khan', 'Suhani Bhatnagar','2016','Pritam Chakraborty')")
print("inserted")
con.commit()

#display data
show=con.execute("select * from movies")

for i in show:
    print(i)

con.commit()