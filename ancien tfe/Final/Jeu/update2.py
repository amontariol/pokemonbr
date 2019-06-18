import mysql.connector
import sqlite3

def update2(login,state):#fonction permettant de mettre a jour dans la base de données hors ligne les données présentes dans la base de données en ligne
    pass
    """mydb = mysql.connector.connect(
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
    print(attributes)
    if state=='win':
        for i in range (0,3):
            if attributes[i]==None:
                attributes[i]=0

            newdata = int(attributes[i])+1
            if i == 0:
                mycursor.execute("UPDATE joueur SET nbwins ="+str(newdata)+" WHERE Login='"+str(login)+"'")
                c.execute("UPDATE joueur SET nbwins ="+str(newdata)+" WHERE Login='"+str(login)+"'")
            elif i == 1:
                mycursor.execute("UPDATE joueur SET nbparties ="+str(newdata)+" WHERE Login='"+str(login)+"'")
                c.execute("UPDATE joueur SET nbwins ="+str(newdata)+" WHERE Login='"+str(login)+"'")
            elif i ==2:
                mycursor.execute("UPDATE joueur SET scoremax ="+str(newdata)+" WHERE Login='"+str(login)+"'")
                c.execute("UPDATE joueur SET nbwins ="+str(newdata)+" WHERE Login='"+str(login)+"'")
    else:
        for i in range (0,3):
            if attributes[i]==None:
                attributes[i]=0
            newdata = int(attributes[i])+1
            if i==1:
               newdata = int(attributes[i])

            newdata = int(attributes[i])+1
            if i == 0:
                mycursor.execute("UPDATE joueur SET nbwins ="+str(newdata)+" WHERE Login='"+str(login)+"'")
                c.execute("UPDATE joueur SET nbwins ="+str(newdata)+" WHERE Login='"+str(login)+"'")
            elif i == 1:
                mycursor.execute("UPDATE joueur SET nbparties ="+str(newdata)+" WHERE Login='"+str(login)+"'")
                c.execute("UPDATE joueur SET nbwins ="+str(newdata)+" WHERE Login='"+str(login)+"'")
            elif i ==2:
                mycursor.execute("UPDATE joueur SET scoremax ="+str(newdata)+" WHERE Login='"+str(login)+"'")
                c.execute("UPDATE joueur SET nbwins ="+str(newdata)+" WHERE Login='"+str(login)+"'")
                
    conn.commit()
    conn.close()
    mydb.commit()
    mydb.close()"""
