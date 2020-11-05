import serial
import time
import mysql.connector

count = 0

ser = serial.Serial('/dev/ttyUSB0', 9600)
time.sleep(2)

active = True

database = mysql.connector.connect(
        host="imac-van-pieter",
        user="root",
        password="root",
        database="camaro",
        port="3306"
)
mycursor = database.cursor()
# Read and record the data
data =[]    # empty list to store the data
while active:
    b = ser.readline()  # read a byte string
    string_n = b.decode()   # decode byte string into Unicode  
    string = string_n.rstrip() # remove \n and \r
    if 's' in string:
        print("distance: ")
        distancevalue = string.replace('s', '')
    else:
        print("ldr: ")
        lightvalue = string.replace('x', '')
    print(string)
    data.append(string) # add to the end of data list
    
    count += 1
    time.sleep(0.1)     # wait (sleep) 0.1 seconds
    print(count)
    if count % 2 == 0 and count != 0:
        sql = "INSERT INTO `sensor_values` (`ID`, `distance`, `ldr`, `userid`) VALUES (NULL, %s, %s, %s)"
        val = (distancevalue, lightvalue, '1')
        mycursor.execute(sql, val)
        database.commit()
        print("Inserted values")

ser.close()