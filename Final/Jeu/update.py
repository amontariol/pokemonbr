import mysql.connector
import sqlite3

def update():#fonction permettant de mettre a jour dans la base de données hors ligne les données présentes dans la base de données en ligne
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="",
      database="mydb"
    )
    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM joueur")
    person = mycursor.fetchall()

    c.execute("DELETE FROM joueur")

    for i in range (0,len(person)):
        c.execute("INSERT INTO joueur VALUES ('"+str(person[i][0])+"','"+str(person[i][1])+"','"+str(person[i][2])+"','"+str(person[i][3])+"','"+str(person[i][4])+"','"+str(person[i][5])+"','"+str(person[i][6])+"','"+str(person[i][7])+"','"+str(person[i][7])+"')")

    conn.commit()
    conn.close()
    mydb.commit()
    mydb.close()
