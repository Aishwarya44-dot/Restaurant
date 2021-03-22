# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 20:14:37 2020

@author: AISHWARYA
"""


import sqlite3
def Address():
    connection=sqlite3.connect("All_Info.db")
    crsr=connection.cursor()
    crsr.execute('drop table if exists Green_Restaurant_Address')
    sql_command="""CREATE TABLE Green_Restaurant_Address (
    NAME VARCHAR(30),
    DoorNo INT,
    Layout VARCHAR(20),
    City VARCHAR(30),
    PinCode INTEGER PRIMARY KEY);"""
    crsr.execute(sql_command)
    sql_command="""INSERT INTO Green_Restaurant_Address VALUES ("Green_Restaurant",185,"Krishnamurthypuram","Mysore",570004);"""
    crsr.execute(sql_command)
    connection.commit()
    connection.close()
    
Address()