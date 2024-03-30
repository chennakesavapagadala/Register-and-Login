#------------------------------------------------------------------------------------------
#  Registration And Log in System with (database) BackEnd
#-----------------------------------------------------------------------------------------
# import modules
import pymysql as pl
import re
import string

# connection to mysql server
connection = pl.connect(user="root", password="834000", host="localhost", port=6666, db="register_db")
c = connection.cursor()

# creating a table to store user data
'''
c.execute("""create table user(first_name varchar(100),last_name varchar(100),user_name varchar(200),
email varchar(200), password1 varchar(200), password2 varchar(200)  )""")
'''
'''
# Register Starts
fname = input("Enter First Name: ")
lname = input("Enter Last  Name: ")
while True:
    uname = input("Enter User Name:_")
    c.execute("select * from user") # ((------),(-----),(------)) in tuple formate
    data = c.fetchall()
    existing_users = []
    for i in data:
        existing_users.append(i[2])
    if uname in existing_users:
        print("{} User Name is Already Existed".format(uname))
        continue
    else:
        while True:
            email = input("Enter Email Id: ")
            c.execute("select * from user") # ((------),(-----),(------)) in tuple formate
            data = c.fetchall()
            existing_emails = []
            for i in data:
                existing_emails.append(i[3])
            if email in existing_emails:
                print("{} email is already existed...".format(email))
                continue
            else:
                while True:
                    password1 = input("Enter New Password: ")
                    password2 = input("Enter Confirm Password: ")
                    if password1 != password2:
                        print("Passwords does not Match...")
                        continue
                    elif len(password1) < 8:
                        print("Password must contain minumum 8 charactors")
                        continue
                    elif len([i for i in password1 if i in string.ascii_lowercase]) == 0:
                        print("password must contains atleast 1 lowercase value")
                        continue
                    elif len([i for i in password1 if i in string.ascii_uppercase]) == 0:
                        print("password must contains atleast 1 uppercase value")
                        continue
                    elif len([i for i in password1 if i in string.digits]) == 0:
                        print("password must contains atleast 1 digit ")
                        continue
                    elif len([i for i in password1 if i in string.punctuation]) == 0:
                        print("password must contains atleast 1 special charactor ")
                        print("""Special Characters are = !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ """)
                        continue
                    else:
                        print("Successfully Registered...")
                        c.execute("insert into user values(%s,%s,%s,%s,%s,%s)",
                                (fname,lname,uname,email,password1,password2))
                        connection.commit()
                        connection.close()
                        break
                break
        break
                
'''
# To Print/Show All The Data From Database
'''
c.execute("select * from user") # ((------),(-----),(------)) in tuple formate
data = c.fetchall() 
print(data)
'''

#------------ User Login --------------

# fetch Only User name and Password From Database    
c.execute("select user_name,password1 from user") # ((--),(--),(--)) in tuple formate
data = c.fetchall()
dic = {}
for i in data:
    dic[i[0]]=i[1]
print(dic) #Conver into KeyValue Pair dict form.

while True:
    user_name = input('Enter User Name ')
    if user_name in dic:
        while True:
            password = input('Enter Your Password ')
            if dic[user_name]== password:
                print('Login SuccessFull')
                break
            else:
                print('Invalid password')
                
        break
    else:
        print(" Invalid User Name....! ")


#---------------------------------- END -----------------------------------------------

