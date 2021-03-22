# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 20:24:54 2020

@author: AISHWARYA
"""


import sqlite3
def Show_All_Restaurant_Address():
    connection=sqlite3.connect("All_Info.db")
    crsr=connection.cursor()
    crsr.execute("SELECT * FROM Green_Restaurant_Address")
    Address=crsr.fetchone()
    for each in Address:
        print(each)
        
    connection.commit()
    connection.close()
    
 