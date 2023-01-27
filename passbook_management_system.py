import mysql.connector as m 
import pandas as p 
import numpy as np
database=m.connect(host="LOCAL",user="USER",password="PASS",database="DATA")
cursor=database.cursor()
def Create_Ac():
    print("==========================================Enter Details===========================================")
    try:
        q="insert into Account(name,Ac_balance,password) values(%s,%s,%s)"
        name=input("Enter Full Name: ")
        Ac_balance=float(input("Opening Acount With Balance : "))
        password=input("Enter a password : ")
        cursor.execute(q,[name,Ac_balance,password])    
        database.commit()
        print("=======Account is Created With :=========","\n","Name : ",name,"\n","Balance : ",Ac_balance,"\n")
        print("==========Enter Your Choice===========","\n","1.Go To MENU","\n","2.Exit")
        a=int(input("Enter Your Choise : "))
        if a==1:
           choice()  
        elif a==2:
            exit()
    except Exception as e:
        print("==========Enter Valid Details Or Exit===========","\n","1.Enter Again","\n","2.Go To MENU","\n","3.Exit")
        a=int(input("Enter Your Choise : "))
        if a==1:
            Create_Ac() 
        elif a==2:
            choice()
        elif a==3:
            exit()
             
def Check_bal():
    print("==========================================Enter Details===========================================")
    try:
        q="select Ac_balance from Account where password=%s and Ac_no=%s"
        Ac_no=input("Enter your Account number : ")
        password=input("Enter Password : ")
        cursor.execute(q,[password,Ac_no])
        result=cursor.fetchall()
        print("==========Account Balance is : ==========",result[0][0])
        database.commit()
        print("==========Enter Your Choice===========","\n","1.Go To MENU","\n","2.Exit")
        a=int(input("Enter Your Choise : "))
        if a==1:
           choice()  
        elif a==2:
            exit()
    except Exception as e: 
        print("==========Enter Valid Details Or Exit===========","\n","1.Enter Again","\n","2.Go To MENU","\n","3.Exit")
        a=int(input("Enter Your Choise : "))
        if a==1:
            Check_bal()
        elif a==2:
            choice()
        elif a==3:
            exit()
def Dip_amount():
    print("==========================================Enter Details===========================================")
    try:
        q="update Account set Ac_balance=(Ac_balance+%s) where Ac_no=%s and name=%s"
        name=input("Enter your Name : ")
        Ac_no=input("Enter your Account number : ")
        dip_amt=float(input("Enter The Amount To Deposit : "))
        cursor.execute(q,[dip_amt,Ac_no,name])
        database.commit()
        print("=======Account is Credit with :=========","\n","Amount : ",dip_amt)
        print("==========Enter Your Choice===========","\n","1.Go To MENU","\n","2.Exit")
        a=int(input("Enter Your Choise : "))
        if a==1:
           choice()  
        elif a==2:
            exit()

    except Exception as e:
        print("==========Enter Valid Details Or Exit===========","\n","1.Enter Again","\n","2.Go To MENU","\n","3.Exit")
        a=int(input("Enter Your Choise : "))
        if a==1:
           Dip_amount()
        elif a==2:
            choice()
        elif a==3:
            exit()
def Withdraw_amt():
    print("==========================================Enter Details===========================================")
    try:
        q1="select Ac_balance,name from Account where Ac_no=%s"
        Ac_no=input("Enter your Account number : ")
        cursor.execute(q1,[Ac_no])
        result=cursor.fetchall()
        bal=result[0][0]
        name=result[0][1]
        print("Name :",name)
        q="update Account set Ac_balance=(Ac_balance-%s) where Ac_no=%s and name=%s and password=%s"
        password=input("Enter Password : ")
        while True:
            amt=float(input("Enter ammout you want to withdrow : "))
            if amt>bal:
                print("insufficient balance Enter ammount again")
            elif bal>=amt:
                cursor.execute(q,[amt,Ac_no,name,password])
                break
        database.commit()
        print("==========Enter Your Choice===========","\n","1.Go To MENU","\n","2.Exit")
        a=int(input("Enter Your Choise : "))
        if a==1:
           choice()  
        elif a==2:
            exit()
    except Exception as e:
        print("==========Enter Valid Details Or Exit===========","\n","1.Enter Again","\n","2.Go To MENU","\n","3.Exit")
        a=int(input("Enter Your Choise : "))
        if a==1:
            Withdraw_amt() 
        elif a==2:
            choice()
        elif a==3:
            exit()
    
def choice():
    print("============================================MENU=============================================")
    print("1. Create Account : ")
    print("2. Check Balance : ")
    print("3. Deposit an Amount: ")
    print("4. WithDraw Amount: ")
    print("5. Exit: ")
    choice=int(input("Enter your Choice (1-5): "))  
    if choice==1:
        Create_Ac()
    elif choice==2:
        Check_bal()
    elif choice==3:
        Dip_amount()
    elif choice==4:
        Withdraw_amt()
    elif choice==5:
        exit()
    else:
        print("Enter a valid choice")
choice()

        

        
