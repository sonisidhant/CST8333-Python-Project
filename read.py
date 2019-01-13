######################
# read.py
# By Sidhant Soni
# December 02, 2018
######################

""" Import statements """
from tkinter import *
from tkinter import Button, Entry
import mysql.connector
import os
from mysql.connector import Error

"""This file creates the connection between the database and the python and then read the data from the mysql database 
and then assign the data in the entry."""

root = Tk()


def main():
    INDEX = 1
    try:
        """Craetes the database connection"""
        mySQLconnection = mysql.connector.connect(host='localhost',
                                                  database='db',
                                                  user='root',
                                                  password='abcd')

        sql_select_Query = "select * from assignment4 where ID = %s"
        id = (INDEX,)
        cursor = mySQLconnection.cursor()
        cursor.execute(sql_select_Query, id)
        records = cursor.fetchone()

        print("Total number of rows in python_developers is - ", cursor.rowcount)
        ID = records[0]
        REF_DATE = records[1]
        GEO = records[2]
        DGUID = records[3]
        FOOD_CATEGORIES = records[4]
        COMMODITY = records[5]
        UOM = records[6]
        UOM_ID = records[7]
        SF = records[8]
        SI = records[9]
        VECTOR = records[10]
        CORDINATE = records[11]
        VALUE = records[12]
        STATUS= records[13]
        SYMBOL = records[14]
        TERMINATED = records[15]
        DECIMALS = records[16]

        cursor.close()

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        # closing database connection.
        if (mySQLconnection.is_connected()):
            mySQLconnection.close()
            print("MySQL connection is closed")

    root.geometry('500x600')
    root.title('Sidhant_Soni')

    label = Label(root, text="Read Data Set", font=(None, 12), bg="black", fg="red",
                  width=20)
    label.place(x=90, y=53)

    label0 = Label(root, text='ID:', font=(None, 12), width=20)
    label0.place(x=85, y=55)
    entry0 = Entry(root)
    entry0.place(x=240, y=55)
    entry0.insert(0, ID)

    label1 = Label(root, text="REF_DATE: ", font=(None, 12), width=20)
    label1.place(x=80, y=80)
    entry = Entry(root)
    entry.place(x=240, y=80)
    entry.insert(0, REF_DATE)

    label2 = Label(root, text="GEO: ", font=(None, 12), width=20)
    label2.place(x=68, y=105)
    entry1 = Entry(root)
    entry1.place(x=240, y=105)
    entry1.insert(0, GEO)

    label3 = Label(root, text="DGUID: ", font=(None, 12), width=20)
    label3.place(x=68, y=130)
    entry2 = Entry(root)
    entry2.place(x=240, y=130)
    entry2.insert(0, DGUID)

    label4 = Label(root, text="Food_Categories: ", font=(None, 12), width=20)
    label4.place(x=68, y=155)
    entry3 = Entry(root)
    entry3.place(x=240, y=155)
    entry3.insert(0, FOOD_CATEGORIES)

    label5 = Label(root, text="Commodity: ", font=(None, 12), width=20)
    label5.place(x=68, y=180)
    entry4 = Entry(root)
    entry4.place(x=240, y=180)
    entry4.insert(0, COMMODITY)

    label6 = Label(root, text="UOM: ", font=(None, 12), width=20)
    label6.place(x=68, y=205)
    entry5 = Entry(root)
    entry5.place(x=240, y=205)
    entry5.insert(0, UOM)

    label7 = Label(root, text="UOM_ID: ", font=(None, 12), width=20)
    label7.place(x=68, y=230)
    entry6 = Entry(root)
    entry6.place(x=240, y=230)
    entry6.insert(0, UOM_ID)

    label8 = Label(root, text="SCALER_FACTOR: ", font=(None, 12), width=20)
    label8.place(x=68, y=255)
    entry7 = Entry(root)
    entry7.place(x=240, y=255)
    entry7.insert(0, SF)

    label9 = Label(root, text="SCALER_ID: ", font=(None, 12), width=20)
    label9.place(x=68, y=280)
    entry8 = Entry(root)
    entry8.place(x=240, y=280)
    entry8.insert(0, SI)

    label10 = Label(root, text="VECTOR: ", font=(None, 12), width=20)
    label10.place(x=68, y=305)
    entry9 = Entry(root)
    entry9.place(x=240, y=305)
    entry9.insert(0, VECTOR)

    label11 = Label(root, text="COORDINATE: ", font=(None, 12), width=20)
    label11.place(x=68, y=330)
    entry10 = Entry(root)
    entry10.place(x=240, y=330)
    entry10.insert(0, CORDINATE)

    label12 = Label(root, text="VALUE: ", font=(None, 12), width=20)
    label12.place(x=68, y=355)
    entry11 = Entry(root)
    entry11.place(x=240, y=355)
    entry11.insert(0, VALUE)

    label13 = Label(root, text="STATUS: ", font=(None, 12), width=20)
    label13.place(x=68, y=380)
    entry12 = Entry(root)
    entry12.place(x=240, y=380)
    entry12.insert(0, STATUS)

    label14 = Label(root, text="SYMBOL: ", font=(None, 12), width=20)
    label14.place(x=68, y=405)
    entry13 = Entry(root)
    entry13.place(x=240, y=405)
    entry13.insert(0, SYMBOL)

    label15 = Label(root, text="TERMINATED: ", font=(None, 12), width=20)
    label15.place(x=68, y=430)
    entry14 = Entry(root)
    entry14.place(x=240, y=430)
    entry14.insert(0, TERMINATED)


    label16 = Label(root, text="DECIMALS: ", font=(None, 12), width=20)
    label16.place(x=68, y=455)
    entry15 = Entry(root)
    entry15.place(x=240, y=455)
    entry15.insert(0, DECIMALS)

    Next = Button(root, text="Search Row", command=next)
    Next.place(x=190, y=500)

    label.pack()
    root.mainloop()


def next():
    root.destroy()
    os.system('Next.py')


main()
