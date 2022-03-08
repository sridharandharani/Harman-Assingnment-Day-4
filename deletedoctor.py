# delete all the doctor using ph no
import sqlite3
folder = sqlite3.connect("hostipal.db")
del_dphno = input("Enter the doctor phno :")
folder.execute("DELETE FROM HOSPITALDOCTOR WHERE DOCTORPHNO = "+del_dphno)
folder.commit()
print("deleted")

output = folder.execute(" SELECT * FROM HOSPITALDOCTOR ")
for i in output:
    print("doctor name :",i[0])
    print("doctor qualification :",i[1])
    print("doctor address :",i[2])
    print("doctor phno :",i[3])
    print("doctor email id :",i[4])