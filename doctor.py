# create a doctor name,qualification,address,phno,email id
# search a doctor using name
# search a doctor using phno
# view all doctors
# update all the doctor using ph no
# delete all the doctor using ph no
import sqlite3
folder = sqlite3.connect("hostipal.db") #create db

# folder.execute('''CREATE TABLE HOSPITALDOCTOR(
#                   DOCTORNAME TEXT,
#                   DOCTORQUALIFICATION TEXT,
#                   DOCTORADDRESS TEXT,
#                   DOCTORPHNO INTEGER,
#                   DOCTOREMAILID TEXT);''')
print("Doctor table created")

get_dname = input("Enter the doctor name :")
get_dqualification = input("Enter the qualification :")
get_daddress = input("Enter the doctor address :")
get_dphno = input("Enter the doctor ph no :")
get_demailid = input("Enter the doctor email id :")


folder.execute("INSERT INTO HOSPITALDOCTOR(DOCTORNAME,DOCTORQUALIFICATION,DOCTORADDRESS,DOCTORPHNO,DOCTOREMAILID)\
VALUES('"+get_dname+"','"+get_dqualification+"','"+get_daddress+"',"+get_dphno+",'"+get_demailid+"')") #inserting values
folder.commit()
folder.close()
print("Inserted sucessfully")