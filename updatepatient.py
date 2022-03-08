import sqlite3
folder = sqlite3.connect("hostipal.db")
get_pid = input(" Enter the patient id :")

get_pname = input("Enter the patient name :")
get_paddress = input("Enter the patient address :")
get_pphno = input("Enter the patient ph no :")
get_pemailid = input("Enter the patient email id :")
get_ppincode = input("Enter the patient pincode :")

folder.execute("UPDATE HOSPITALPATIENT SET \
 PATIENTNAME='"+get_pname+"',PATIENTADDRESS='"+get_paddress+"',PATIENTPHNO="+get_pphno+",PATIENTEMAILID ='"+get_pemailid+"',PATIENTPINCODE = "+get_ppincode+" \
 WHERE PATIENTID = "+get_pid)
folder.commit()
print("updated sucessfully")

output = folder.execute(" SELECT * FROM HOSPITALPATIENT ")
for i in output:
    print("patient id :",i[0])
    print("patient name :",i[1])
    print("patient address :",i[2])
    print("patient phno :",i[3])
    print("patient email id :",i[4])
    print("patient pincode :",i[5])