# -*- coding: utf-8 -*-
import time 
import sqlite3
from config import database# import database name from config.py

def add_new_record_in_table(step, err):#step - крок на котрому виявлено помиилку(ім'я викликаючої функції), err - опис помилки
    """Записуємо дані  про помилку до бази  данних
       data це кортеж данних. функція написана трохи костильно тому що нова таблиця створюється в результаті
       виявлення помилки
       We write down data on an error to a database
       data is a tuple of data"""
    try:
        connection = sqlite3.connect(database)# Connect to ...
        cursor = connection.cursor()# ... database
        print("Succesfully Connected to DataBase")
        tablename = "errors" + time.strftime("%d_%m_%Y", time.localtime())#TABLE NAME IS CURENT DATE
    except Exception as e:
        print ("No Connect to DataBase\ne==", e)
    try:
        time_ = str(time.strftime("%H.%M.%S", time.localtime()))#ERROR RECORDING TIME
        cursor.execute(f"""INSERT INTO {tablename} (times, step, err)  VALUES (?,?,?)""",(time_,step,err))#add information to table
        connection.commit()
        print(f"error recorded to table {tablename}")
        connection.close()
        print("The sqlite connection is closed")

    except Exception as e:
        if e.args[0].startswith('no such table'):
            cursor.execute(f"""CREATE TABLE IF NOT EXISTS {tablename} (id INTEGER PRIMARY KEY AUTOINCREMENT , times TEXT NOT NULL, step TEXT NOT NULL, err TEXT NOT NULL)""")#create new table
            connection.commit()
            print(f"Created new table in database {database}\n new table name is {tablename}")
            cursor.execute(f"""INSERT INTO {tablename} (times, step, err) VALUES (?,?,?)""",(time_,step,err))#add information to table
            connection.commit()
            print(f"error recorded to table {tablename}")
            connection.close()
            print("The sqlite connection is closed")
        else:
            print('Error DataBase\n e ==', e)


 