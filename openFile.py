######################
# openFile.py
# By Sidhant Soni
# December 02, 2018
######################

import tkinter.messagebox
import pymysql
import csv
from tkinter.filedialog import askopenfilename


""" The function OpenFile() creates the connection between the database and python and then further creates the table
assignment4. Then it ask to chose the file to save in the database. Then it saves the data in the database."""
def OpenFile():
    conn = pymysql.connect(host='localhost', user='root', password='abcd', db='db')
    a = conn.cursor()
    a.execute("Drop table if exists Assignment4")
    a.execute("""
        CREATE TABLE Assignment4 (
        ID int NOT NULL AUTO_INCREMENT,REF_DATE varchar(255),GEO varchar(255),DGUID varchar(255),
        Food_categories varchar(255),Commodity varchar(255),UOM varchar(255),UOM_ID varchar(255),SCALAR_FACTOR 
        varchar(255),SCALAR_ID varchar(255),VECTOR varchar(255),COORDINATE varchar(255),VALUE varchar(255),
        STATUS varchar(255),SYMBOL varchar(255),TER_MINATED varchar(255),DECIMALS varchar(255),PRIMARY KEY (ID));""")

    """Ask to chose the file"""
    name = askopenfilename(initialdir="E:\\Semester 4\\Research Project\\Project\\",
                           filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
                           title="Choose a file."
                           )
    """Read data from .csv file and then save it into database"""
    with open(name) as csvfile:
        readCSV = csv.reader(csvfile)
        next(readCSV, None)
        for row in readCSV:
            a.execute('INSERT INTO Assignment4(REF_DATE,GEO,DGUID,Food_categories,Commodity,UOM,UOM_ID,SCALAR_FACTOR,'
                      'SCALAR_ID,VECTOR,COORDINATE,VALUE,STATUS,SYMBOL,TER_MINATED,DECIMALS) '
                      'VALUES("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s",'
                      ' "%s", "%s", "%s")',
                      row)
        print(name)
    conn.commit()
    tkinter.messagebox.showinfo("Sidhant_Soni_Insert","Data Insertion Completed")


MsgBox = tkinter.messagebox.askquestion('Exit Application', 'Are you sure you want to insert data',
                                        icon='warning')
if MsgBox == 'yes':
    OpenFile()
else:
    tkinter.messagebox.showinfo('Return', 'You will now return to the application screen')
