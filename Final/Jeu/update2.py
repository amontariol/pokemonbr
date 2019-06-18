import mysql.connector
import sqlite3
import launcherPOO
from random import *

def update(login,state):
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="",
      database="mydb"
    )

    mycursor = mydb.cursor()

    conn = sqlite3.connect('db.db')
    c = conn.cursor()

    c.execute("SELECT * FROM joueur WHERE Login='"+str(login)+"'")

    person = c.fetchall()

    attributes=[person[0][6],person[0][7],person[0][8]]
    if state=='win':
        for i in range (0,3):
            if attributes[i]==None:
                attributes[i]=0

            newdata = int(attributes[i])+1
            if i ==2:
                newdata = randint(200,1000)
                
            if i == 0:
                mycursor.execute("UPDATE joueur SET nbwins ="+str(newdata)+" WHERE Login='"+str(login)+"'")
                c.execute("UPDATE joueur SET nbwins ="+str(newdata)+" WHERE Login='"+str(login)+"'")
            elif i == 1:
                mycursor.execute("UPDATE joueur SET nbparties ="+str(newdata)+" WHERE Login='"+str(login)+"'")
                c.execute("UPDATE joueur SET nbparties ="+str(newdata)+" WHERE Login='"+str(login)+"'")
            elif i ==2:
                mycursor.execute("UPDATE joueur SET scoremax ="+str(newdata)+" WHERE Login='"+str(login)+"'")
                c.execute("UPDATE joueur SET scoremax ="+str(newdata)+" WHERE Login='"+str(login)+"'")
    else:
        for i in range (0,3):
            newdata = int(attributes[i])+1
            if i ==2:
                newdata = randint(200,1000)

            if i == 0:
                pass
            elif i == 1:
                mycursor.execute("UPDATE joueur SET nbparties ="+str(newdata)+" WHERE Login='"+str(login)+"'")
                c.execute("UPDATE joueur SET nbparties ="+str(newdata)+" WHERE Login='"+str(login)+"'")
            elif i ==2:
                mycursor.execute("UPDATE joueur SET scoremax ="+str(newdata)+" WHERE Login='"+str(login)+"'")
                c.execute("UPDATE joueur SET scoremax ="+str(newdata)+" WHERE Login='"+str(login)+"'")

    rand1 = randint(1,151)
    rand2 = randint(0,30)
    mycursor.execute("UPDATE basepokemon SET numberofuses ="+str(rand2)+" WHERE id='"+str(rand1)+"'")
    c.execute("UPDATE basepokemon SET numberofuses ="+str(rand2)+" WHERE id='"+str(rand1)+"'")

    
    conn.commit()
    conn.close()
    mydb.commit()
    mydb.close()
    launcherPOO.launch(login)
    
update(123456,'lose')
