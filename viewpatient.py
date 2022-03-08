# view all patient
import sqlite3
folder = sqlite3.connect("hostipal.db")

output = folder.execute(" SELECT * FROM HOSPITALPATIENT ")
for i in output:
    print("patient id :",i[0])
    print("patient name :",i[1])
    print("patient address :",i[2])
    print("patient phno :",i[3])
    print("patient email id :",i[4])
    print("patient pincode :",i[5])
