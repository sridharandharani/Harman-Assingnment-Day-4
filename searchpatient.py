# search a patient using patient  id
import sqlite3
folder = sqlite3.connect("hostipal.db")
getp_id = input("Enter the patient id :")
output = folder.execute(" SELECT * FROM HOSPITALPATIENT WHERE PATIENTID = "+getp_id)
for i in output:
    print("patient id :",i[0])
    print("patient name :",i[1])
    print("patient address :",i[2])
    print("patient phno :",i[3])
    print("patient email id :",i[4])
    print("patient pincode :",i[5])
