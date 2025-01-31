import mysql.connector
import datetime
import serial
import time
import os

class database:
    mycursor = None
    db = None
    active = False
    def __init__(self):
        pass

    def connect(self):
        self.db = mysql.connector.connect(
        host="imac-van-pieter",
        user="root",
        password="root",
        database="camaro",
        port="3306"
        )
        
        self.mycursor = self.db.cursor()
    
    def insert(self, col_headers, col_values):
        sql = "INSERT INTO `" + col_headers[0] + "` (`ID`, `" + col_headers[1] + "`, `" + col_headers[2] + "`, `" + col_headers[3] + "`) VALUES (NULL, %s, %s, %s)"
        val = (col_values[0], col_values[1], col_values[2])
        self.mycursor.execute(sql, val)
        self.db.commit()
        print(
            "Inserted into " + col_headers[0] + "\n" +
            col_headers[1] + col_values[0] + "\n" +
            col_headers[2] + col_values[1] + "\n" +
            col_headers[3] + col_values[2]
        )   

    def delete(self, col_headers, col_values):
        sql = "DELETE FROM `" + col_headers[0] + "` (`ID`, `" + col_headers[1] + "`, `" + col_headers[2] + "`, `" + col_headers[3] + "`) VALUES (NULL, %s, %s, %s)"
        val = (col_values[0], col_values[1], col_values[2])
        self.mycursor.execute(sql, val)
        self.db.commit()

        print(self.mycursor.rowcount, "record removed.")

    

