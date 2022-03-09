# update all the doctor using ph no
import sqlite3
folder = sqlite3.connect("hostipal.db")
get_dphno = input(" Enter the doctor phno :")

get_dname = input("Enter the doctor name :")
get_dqualification = input("Enter the doctor qualification :")
get_daddress = input("Enter the doctor address :")
get_pemailid = input("Enter the doctor email id :")


folder.execute("UPDATE HOSPITALDOCTOR SET \
 DOCTORNAME='"+get_dname+"',DOCTORQUALIFICATION='"+get_dqualification+"',DOCTORADDRESS='"+get_daddress+"',DOCTOREMAILID ='"+get_pemailid+"' \
 WHERE DOCTORPHNO = "+get_dphno)
folder.commit()
print("updated sucessfully")
output = folder.execute(" SELECT * FROM HOSPITALDOCTOR ")
for i in output:
    print("doctor name :",i[0])
    print("doctor qualification :",i[1])
    print("doctor address :",i[2])
    print("doctor phno :",i[3])
    print("doctor email id :",i[4])