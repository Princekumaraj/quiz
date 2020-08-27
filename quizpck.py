import time
import datetime
import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="888929")
mycursor = mydb.cursor()


def test(n,uid):
    
    #myc = mydb.cursor()
    #mycursor = mydb.cursor()
    mycursor.execute('use online_test')
    marks = 0
    '''
    print('Select the test technology :')
    print('1.: C\t2.: Python')
    '''
    #print(n,i)
    print('Type the technology to have the questions(case Sensitive) :')
    mycursor.execute('select * from technology')
    r = mycursor.fetchall()
    for i in r:
            print(" {}. : {}".format(i[0],i[1]))
    
        
    inp = input()
    if(inp == 'c'):
        mycursor.execute("select * from questions where tech_id = 'c';")
    
    elif(inp == 'python'):
        mycursor.execute("select * from questions where tech_id = 'python';")
    
    #result1 = mycursor1.fetchone()
    resultall = mycursor.fetchall()
    
    print('----------------------------------------------------------')
    print("Your {} test will begin in 5 seconds...".format(inp))
    time.sleep(1)
    print('----------------------------------------------------------')
    for i in resultall:
        print("{}.: \n {} \n\n A : {} \t B : {} \n C : {} \t D : {} \n Your Answer :-".format(i[0],i[1],i[2],i[3],i[4],i[5]))
        ans = input()
        print()
        if ( ans == str(i[6])):
            marks = marks + 1
    #totm = (marks//(10*mycursor1.rowcount))*100
    print()
    print("{} your Result is {} out of {}".format(n,marks,mycursor.rowcount))
    
    per = (marks/mycursor.rowcount)*100
    #mycursor1.execute('commit')
    ts = time.time()
    d = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    #myc.execute('select * from marks')
    #print(uid,n,per,d,inp)
    mycursor.execute("""insert into marks values({},'{}',{},'{}','{}')""".format(uid,n,per,d,inp))
    mycursor.execute('commit')


def admin():

    #mycursor = mydb.cursor()
    time.sleep(2)
    print('Add Questions to the test')
    
    while True:
        print('Type the technology to add questions(case Sensitive) :')
        mycursor.execute('use online_test')
        mycursor.execute('select * from technology')
        resultall = mycursor2.fetchall()
        for i in resultall:
            print(" {}. : {}".format(i[0],i[1]))
    
        inp = input()
        print('Keep the questions ready related to ',inp)
        time.sleep(2)
        
        #mycursor2.execute('select * from questions')
        mycursor.execute('select q_id from questions order by q_id desc limit 1')
        r = mycursor.fetchone()
        qn = int(r[0])+1
        
        q = input('Enter question : ')
        optiona = input('Enter option A : ')
        optionb = input('Enter option B : ')
        optionc = input('Enter option C : ')
        optiond = input('Enter option D : ')
        answ = input('Enter the correct option : ')
        mycursor.execute("""insert into questions values({},'{}','{}','{}','{}','{}','{}','{}')""".format(qn,q,optiona,optionb,optionc,optiond,answ,inp))
        mycursor.execute("commit")
        print("{}th added to the database ".format(qn))
        print('----------------------------------------------------------')
        if(input('do want to add another queston [y/n]') == 'n'):
            break
    print('----------------------------------------------------------')

def addu():
    #mycursor = mydb.cursor()
    mycursor.execute('use online_test')
    time.sleep(2)
    while True:
        print('----------------------------------------------------------')
        print('Add Students for this quiz panel')
        n = input('Enter student name : ')
        p = input('Enter student pswd : ')
        role = 'student'
        mycursor.execute('select id from user order by id desc limit 1')
        res = mycursor.fetchone()
        i = (int(res[0])+1)
        mycursor.execute("""insert into user values({},'{}','{}','{}')""".format(i,n,p,role))
        mycursor.execute("""commit""")
        a = input("Do u want to add another user : [y/n] ")
        if(a == 'n'):
            break
    
