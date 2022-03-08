# #create a new project hospital patients and doctors data name is hospital.db patient id,name,address,phno,email id, pincode
# search a patient using patient  id
# view all patient
# update patient id
# delete all the patient
import sqlite3
folder = sqlite3.connect("hostipal.db") #create db

# folder.execute('''CREATE TABLE HOSPITALPATIENT(
#                 PATIENTID INTEGER PRIMARY KEY AUTOINCREMENT,
#                 PATIENTNAME TEXT,
#                 PATIENTADDRESS TEXT,
#                 PATIENTPHNO INTEGER,
#                 PATIENTEMAILID TEXT,
#                 PATIENTPINCODE INTEGER
# );''') #Table created
print("Patient Table created")

get_pname = input("Enter the patient name :")
get_paddress = input("Enter the patient address :")
get_pphno = input("Enter the patient ph no :")
get_pemailid = input("Enter the patient email id :")
get_ppincode = input("Enter the patient pincode :")

folder.execute("INSERT INTO HOSPITALPATIENT(PATIENTNAME,PATIENTADDRESS,PATIENTPHNO,PATIENTEMAILID,PATIENTPINCODE)\
VALUES('"+get_pname+"','"+get_paddress+"',"+get_pphno+",'"+get_pemailid+"',"+get_ppincode+")") #inserting values
folder.commit()
folder.close()
print("Inserted sucessfully")

