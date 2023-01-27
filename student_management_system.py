#from dataclasses import dataclass
import mysql.connector as m
import pandas as p
mydatabase=m.connect(host="localhost",user="root",password="mayur",database="mayur")
cursor=mydatabase.cursor()
# query="create table Student(name varchar(100),roll_no int primary key)"
# cursor.execute(query)
def Add_Student():
    query="insert into Student values (%s,%s)"
    name=input("enter name of student: ")
    roll_no=int(input("enter roll number of student: "))
    mylist=[name,roll_no]
    cursor.execute(query,mylist)
    mydatabase.commit()
def Del_Student():
    query="delete from Student where name=%s and roll_no=%s"
    name=input("enter name of student to delete: ")
    roll_no=int(input("enter roll no of student to delete: "))
    cursor.execute(query,[name,roll_no])
    mydatabase.commit()
def Update_Student():
    query="update Student set name=%s where roll_no=%s"
    name=input("enter name")
    roll_no=int(input("enter roll no: "))
    cursor.execute(query,[name,roll_no])
    mydatabase.commit()
def Show_Student():    
    query="select * from Student where name=%s"
    name=input("enter name: ")
    cursor.execute(query,[name])
    result=cursor.fetchall()
    if len(p.DataFrame(result))!=0:
        print(p.DataFrame(result))
    else:
        print("student dose not exist: ")
    mydatabase.commit()
mydatabase.commit()
print("===============MENU===============")
print("1 : Add Student")
print("2 : delete Student")
print("3 : update Student")
print("4 : show Student")
print("5 : Exit")
choice=int(input("Enter your choice: "))
if choice==1:
    Add_Student()
elif choice==2:
    Del_Student()
elif choice==3:
    Update_Student()
elif choice==4:
    Show_Student()
elif choice==5:
    exit()
input()