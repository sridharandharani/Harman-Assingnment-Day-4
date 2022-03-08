# search a doctor using phno
import sqlite3
folder = sqlite3.connect("hostipal.db")
get_dphno = input("Enter the doctor phno :")
output = folder.execute(" SELECT * FROM HOSPITALDOCTOR WHERE DOCTORPHNO = "+get_dphno)
for i in output:
    print("doctor name :",i[0])
    print("doctor qualification :",i[1])
    print("doctor address :",i[2])
    print("doctor phno :",i[3])
    print("doctor email id :",i[4])