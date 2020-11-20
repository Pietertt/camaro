import mysql.connector
import datetime
import serial
import time
import os

class database:
    def __init__(self):
        global db
        global mycursor
        
        db = None
        mycursor = None

    def connect(self):
        db = mysql.connector.connect(
        host="imac-van-pieter",
        user="root",
        password="root",
        database="camaro",
        port="3306"
        )

        self.mycursor = db.cursor()
    
    def insert(self, col_headers, col_values):
        col_headers = col_headers
        col_values = col_values

        sql = "INSERT INTO `" + col_headers[0] + "` (`ID`, `" + col_headers[1] + "`, `" + col_headers[2] + "`, `" + col_headers[3] + "`) VALUES (NULL, %s, %s, %s)"
        val = (col_values[0], col_values[1], col_values[2])
        mycursor.execute(sql, val)
        db.commit()
        print(
            "Inserted into " + col_headers[0] + "\n" +
            col_headers[1] + col_values[0] + "\n" +
            col_headers[2] + col_values[1] + "\n" +
            col_headers[3] + col_values[2]
        )   

    def delete(self, col_headers, col_values):
        col_headers = col_headers
        col_values = col_values

        sql = "DELETE FROM `" + col_headers[0] + "` (`ID`, `" + col_headers[1] + "`, `" + col_headers[2] + "`, `" + col_headers[3] + "`) VALUES (NULL, %s, %s, %s)"
        val = (col_values[0], col_values[1], col_values[2])
        mycursor.execute(sql, val)
        db.commit()

        os.system("sudo rm videos/" + col_values[0])
        print(mycursor.rowcount, "record removed.")	

