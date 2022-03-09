# search a doctor using name
import sqlite3
folder = sqlite3.connect("hostipal.db")
getdname = input("Enter the doctor name :")
output = folder.execute(" SELECT * FROM HOSPITALDOCTOR WHERE DOCTORNAME = '"+getdname+"'")
for i in output:
    print("doctor name :",i[0])
    print("doctor qualification :",i[1])
    print("doctor address :",i[2])
    print("doctor phno :",i[3])
    print("doctor email id :",i[4])
