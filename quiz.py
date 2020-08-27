import time
import datetime
import mysql.connector
from quizpck import test,admin,addu


mydb = mysql.connector.connect(host="localhost",user="root",passwd="*****")#ur db paswd
mycursor = mydb.cursor()


mycursor.execute("use online_test")
#mycursor.execute("select * from user")
#mycursor.execute("select * from questions")
#time.sleep(5)

print('----------------------------------------------------------')
print('-------------Welcome to Appin Tech Test Portal------------')

while True:
    username = input('Enter your user name : ')
    password = input('Enter password : ')
    mycursor.execute("select * from user where name = '{}' ".format(username))
    result = mycursor.fetchone()
    if (result[1] == username and result[2] == password ):
        print('Login successfull.....')
        print('Welcome, {} - {}'.format(result[3],result[1]))
        break
    else:
        print('Wrong login credentials !!!')
print('----------------------------------------------------------')
n = result[1]
uid = result[0]

if result[3] == 'student':
    test(n,uid)
elif result[3] == 'admin':
    print('Welcome to admin panel')
    inp = int(input('Enter \n->1 To add Questions to quiz \n->2 To add users\n'))
    if(inp==1):
        admin()
    elif(inp==2):
        addu()
    
    
