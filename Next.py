######################
# Next.py
# By Sidhant Soni
# December 02, 2018
######################

""" import statements"""
import tkinter.messagebox
from tkinter import *

import mysql
import os
from mysql.connector import Error

root = Tk()
label0 = Label(root, text='ID:', font=(None, 12), width=20)
entry0 = Entry(root)
label1 = Label(root, text="REF_DATE: ", font=(None, 12), width=20)
entry = Entry(root)
label2 = Label(root, text="GEO: ", font=(None, 12), width=20)
entry1 = Entry(root)
label3 = Label(root, text="DGUID: ", font=(None, 12), width=20)
entry2 = Entry(root)
label4 = Label(root, text="Food_Categories: ", font=(None, 12), width=20)
entry3 = Entry(root)
label5 = Label(root, text="Commodity: ", font=(None, 12), width=20)
entry4 = Entry(root)
label6 = Label(root, text="UOM: ", font=(None, 12), width=20)
entry5 = Entry(root)
label7 = Label(root, text="UOM_ID: ", font=(None, 12), width=20)
entry6 = Entry(root)
label8 = Label(root, text="SCALER_FACTOR: ", font=(None, 12), width=20)
entry7 = Entry(root)
label9 = Label(root, text="SCALER_ID: ", font=(None, 12), width=20)
entry8 = Entry(root)
label10 = Label(root, text="VECTOR: ", font=(None, 12), width=20)
entry9 = Entry(root)
label11 = Label(root, text="COORDINATE: ", font=(None, 12), width=20)
entry10 = Entry(root)
label12 = Label(root, text="VALUE: ", font=(None, 12), width=20)
entry11 = Entry(root)
label13 = Label(root, text="STATUS: ", font=(None, 12), width=20)
entry12 = Entry(root)
label14 = Label(root, text="SYMBOL: ", font=(None, 12), width=20)
entry13 = Entry(root)
label15 = Label(root, text="TERMINATED: ", font=(None, 12), width=20)
entry14 = Entry(root)
label16 = Label(root, text="DECIMALS: ", font=(None, 12), width=20)
entry15 = Entry(root)


def printtext():
    global e, ID, REF_DATE, GEO, DGUID, FOOD_CATEGORIES, COMMODITY, UOM_ID, UOM, SF, SI, VECTOR, CORDINATE
    string = e.get()

    try:
        """Craetes the database connection"""
        mySQLconnection = mysql.connector.connect(host='localhost',
                                                  database='db',
                                                  user='root',
                                                  password='abcd')

        sql_select_Query = "select * from assignment4 where ID = %s"
        id = (string,)
        cursor = mySQLconnection.cursor()
        cursor.execute(sql_select_Query, id)
        records = cursor.fetchone()

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

    label0.place(x=85, y=55)

    entry0.place(x=240, y=55)
    entry0.insert(0, ID)

    label1.place(x=80, y=80)

    entry.place(x=240, y=80)
    entry.insert(0, REF_DATE)

    label2.place(x=68, y=105)

    entry1.place(x=240, y=105)
    entry1.insert(0, GEO)

    label3.place(x=68, y=130)

    entry2.place(x=240, y=130)
    entry2.insert(0, DGUID)

    label4.place(x=68, y=155)

    entry3.place(x=240, y=155)
    entry3.insert(0, FOOD_CATEGORIES)

    label5.place(x=68, y=180)

    entry4.place(x=240, y=180)
    entry4.insert(0, COMMODITY)

    label6.place(x=68, y=205)

    entry5.place(x=240, y=205)
    entry5.insert(0, UOM)

    label7.place(x=68, y=230)

    entry6.place(x=240, y=230)
    entry6.insert(0, UOM_ID)

    label8.place(x=68, y=255)

    entry7.place(x=240, y=255)
    entry7.insert(0, SF)

    label9.place(x=68, y=280)

    entry8.place(x=240, y=280)
    entry8.insert(0, SI)

    label10.place(x=68, y=305)

    entry9.place(x=240, y=305)
    entry9.insert(0, VECTOR)

    label11.place(x=68, y=330)

    entry10.place(x=240, y=330)
    entry10.insert(0, CORDINATE)

    label12.place(x=68, y=355)

    entry11.place(x=240, y=355)
    entry11.insert(0, VALUE)

    label13.place(x=68, y=380)

    entry12.place(x=240, y=380)
    entry12.insert(0, STATUS)

    label14.place(x=68, y=405)

    entry13.place(x=240, y=405)
    entry13.insert(0, SYMBOL)

    label15.place(x=68, y=405)

    entry14.place(x=240, y=405)
    entry14.insert(0, TERMINATED)

    label16.place(x=68, y=405)

    entry15.place(x=240, y=405)
    entry15.insert(0, DECIMALS)


    Update = Button(root, text="Update", command=update)
    Update.place(x=100, y=500)

    Delete = Button(root, text="Delete", command=delete)
    Delete.place(x=170, y=500)

    Next = Button(root, text="Search Row", command=next)
    Next.place(x=230, y=500)

    label.pack()
    root.mainloop()


def next():
    root.destroy()
    root1.destroy()
    os.system('Next.py')


def update():
    ID = entry0.get()
    ref_Date = entry.get()
    GEO = entry1.get()
    DGUID = entry2.get()
    FoodC = entry3.get()
    Commodity = entry4.get()
    UOM = entry5.get()
    UOM_ID = entry6.get()
    SF = entry7.get()
    SI = entry8.get()
    VECTOR = entry9.get()
    COOR = entry10.get()
    VALUE = entry11.get()
    STATUS = entry12.get()
    SYMBOL = entry13.get()
    TERMINATED = entry14.get()
    DECIMALS = entry15.get()
    print(COOR)

    mySQLconnection = mysql.connector.connect(host='localhost',
                                              database='db',
                                              user='root',
                                              password='abcd')

    sql_update_query = """Update assignment4 set REF_DATE = %s, GEO = %s, DGUID = %s, Food_categories = %s,
    Commodity = %s, UOM = %s, UOM_ID = %s, SCALAR_FACTOR = %s, SCALAR_ID = %s, VECTOR = %s,
    COORDINATE = %s, VALUE = %s, STATUS = %s, SYMBOL = %s, TER_MINATED = %s, DECIMALS = %s where id = %s"""
    values = (ref_Date, GEO, DGUID, FoodC, Commodity, UOM, UOM_ID, SF, SI, VECTOR, COOR, VALUE, STATUS, SYMBOL, TERMINATED,
              DECIMALS, ID)
    cursor = mySQLconnection.cursor()
    cursor.execute(sql_update_query, values)
    mySQLconnection.commit()
    tkinter.messagebox.showinfo("Sidhant_Soni_Update", "Updated Successfully")


def delete():
    ID = entry0.get()

    mySQLconnection = mysql.connector.connect(host='localhost',
                                              database='db',
                                              user='root',
                                              password='abcd')

    sql_Delete_query = """Delete from assignment4 where id = %s"""
    values = ID
    cursor = mySQLconnection.cursor()
    cursor.execute(sql_Delete_query, (values,))
    mySQLconnection.commit()
    tkinter.messagebox.showinfo("Sidhant_Soni_Delete", "Deleted Successfully")




root1 = Tk()
root1.title('Sidhant_Soni_Enter the row Number')
root1.geometry('700x500')
label = Label(root1, text='Enter the row number:')
label.place(x=250, y=60)
e = Entry(root1)
e.place(x=400, y=60)
b = Button(root1, text='okay', command=printtext)
b.place(x=350, y=100)
root1.mainloop()
