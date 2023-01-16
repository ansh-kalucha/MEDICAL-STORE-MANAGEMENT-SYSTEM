# source code 
#command used to conneect sql to python

import sys
import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='8888@Sashreek',database='dental_management')

#here we have entered in a program with database dental management
cur=conn.cursor()
if conn.is_connected:
print(' successfully connected')
c1=conn.cursor()
if conn.is_connected:
print()
print("""

.......................................................................................
///////////////////////////////////////////////////////////////////////////////////////
....................WELCOME TO THIS MEDI-SHOP.................................
/////////////////Medicine is a science of uncertainity and///////////////////////////////////
<<<<<<<<<<<<<<<<<<<<<<an art of probability>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>
.......................................................................................

""")
print()
print("1. Login")
print("2. Exit")
print()
option=int(input("Enter your choice : "))

#command to be executed when a person chooses to login
if option==1:
print()
print("Welcome")
print("you have decided to login into our system")
print()
print(" Kindly provide necessary credentials to login")
print()
user=input('User Name : ')
user=user.lower()

#this command is used to check username entered
c1.execute("select * from account_details where User_Name like '" + user + "'")
datas=c1.fetchall()

#this command is used to identify the user
for i in datas:
value_1=i[0]
print("the user in sql table is",value_1)
print("The user entered by you is", user)
print("match found")
value_2=i[1]

#this command is there for the user to enter appropriate password to start surfing
if user==value_1:
password=input('Password : ')
password=password.upper()

#command used to compare the password entered by user with database in sql
if password==value_2:
print()
print(" The password entered is correct")
print('Login succefull')
print("thankyou for logging into our system")


#this choice is for asking who is accessing the database
person=input("Who is using(user/shopkeeper/admin)")
person=person.lower()
print("you have selected")
print(person)
print()

#this loop is for user
if person =='user':
print("welcome user")
print("hope you have a great experience")
print("below is the menu for user")
print()

#this is the menu for user

print("1. Input Patients records")
print("this option helps you to input patient records in the database")
print()
print("5. View patient record")
print("this option helps you to view patient records from the database")
print()
print("7. View doctor details")
print("this option helps you to view doctor details from the database")
print()
print("8. View medicines details")
print("this option helps you to view medicine details from the database")
print()
print("9. Delete patients records")
print("this option helps you to delete patient records from the database")
print()
print("please enter your choice in the input command that follows")
print()

#this loop is for shopkeeper
if person == "shopkeeper":

print("welcome shopkeeper")
print("hope you have a great experience")
print("below is the menu for shopkeeper")

#this is the menu for shopkeeper

print("3. Input doctor details")
print("this option helps you to input doctor details in the database")
print()
print("4. Input Medicines details:")
print("this option helps you to input medicine details in the database")
print()
print("11. Delete doctor details")
print("this option helps you to delete doctor details from the database")
print()
print("12. Delete medicines details")
print("this option helps you to delete medicine details from the database")
print()
print("13. Input supplier details")
print("this option helps you to input supplier details in the database")
print()
print("14. View supplier details:")
print("this option helps you to view supplier details from the database")
print()
print("16. Input sales details:")
print("this option helps you to input sales details in the database")
print()
print("17. view sales details:")
print("this option helps you to view sales details from the database")
print()
print("19. Input promotion details:")
print("this option helps you to input promotion details in the database")
print()
print("20. view promotion details:")
print("this option helps you to view promotion details from the database")
print()

#this loop is for admin
if person == "admin":
print("welcome user")
print("hope you have a great experience")
print("below is the menu for admin")

#this is the menu for admin

print("2. Input Salary records")
print("this option helps you to input salary records in the database")
print()
print("6. View salary records")
print("this option helps you to view salary records from the database")
print()
print("10. Delete salary records")
print("this option helps you to delete salary records from the database")
print()
print("13. Input supplier details")
print("this option helps you to input supplier details in the database")
print()
print("14. View supplier details:")
print("this option helps you to view supplier details from the database")
print()
print("15. Delete supplier details:")
print("this option helps you to delete supplier details from the database")
print()
print("16. Input sales details:")
print("this option helps you to input sales details in the database")
print()
print("17. view sales details:")
print("this option helps you to view sales details from the database")
print()
print("18. delete sales details:")
print("this option helps you to delete sales details from the database")
print()
print("19. Input promotion details:")
print("this option helps you to input promotion details in the database")
print()
print("20. view promotion details:")
print("this option helps you to view promotion details from the database")
print()
print("21. delete promotion details:")
print("this option helps you to delete promotion details from the database")
print()
print("22. Input profit details:")
print("this option helps you to input profit details in the database")
print()
print("23. view profit details:")
print("this option helps you to view profit details from the database")
print()
print("24. delete profit details:")
print("this option helps you to delete profit details from the database")
print()


#this is the main loop of the programme
loop="y"
while loop =='y':

#input command asking the user for the choice
choice=int(input('Enter a option : '))

#this section is for choice 1
#the user can input values into the table patient record
if choice==1:
print("you have successfully selected choice 1")
print(" this choice is for entering patient records")
ans='y'

#this is a loop that will be executed till the time the user enters yes
while ans=='y':
print()
print("please enter the credentials asked below")
s_no=int(input('S.no : '))
name=input('Name : ')
name=name.lower()
age=int(input('Age : '))
doc=input('Doctor Consulted : ')
doc=doc.upper()
add=input('Address : ')
add=add.upper()
phone_no=int(input('Phone Number : '))

prescription=input("do you have doctor's prescription?")
prescription=prescription.lower()
print()

#this command is used to input the record into the table in sql
cur.execute("insert into patient_record values(" + str(s_no) +",'" + name + "'," + str(age) + ",'" + do
c + "','" + add + "'," + str(phone_no) + ",'" + prescription + "')")
conn.commit()
print("Record added")
print()
print("Thankyou for entering a record")
print()
#this command asks the user to input yes or no for the loop to continue
ans=input(' wish to add more records (y/n)')
ans=ans.lower()

#this section is for choice 2
#the user can input values into the table salary record
if choice==2:
print("you have successfully selected choice 2")
print(" this choice is for entering salary records")
answer='y'

#this is a loop that will be executed till the time the user enters yes
while answer=='y':
print()
print("please enter the credentials asked below")
s_no=int(input('S_No : '))
emp_id=int(input("Enter emp ID"))
emp_name=input('Employee_Name : ')
emp_name=emp_name.upper()
designation=input('Designation : ')
designation=designation.lower()
gender=input("Enter your gender")
gender=gender.upper()
salary=int(input('Salary Amount : '))
address=input('Address : ')
address=address.upper()
phone_no=int(input('Phone_Number : '))
print()

#this command is used to input the record into the table in sql
cur.execute("insert into salary_record values(" + str(s_no) + ",'" + emp_name + "','" + designation
+ "'," + str(salary) + ",'" + address + "'," + str(phone_no) + "," + str(emp_id) + ",'" + gender + "')")
conn.commit()
print('Record added')
print()
print("Thankyou for entering a record")
print()

#this command asks the user to input yes or no for the loop to continue
answer=input(' wish to add more records (y/n)')
answer=answer.lower()

#this section is for choice 3
#the user can input values into the table doctor record
if choice==3:
print("you have successfully selected choice 3")
print(" this choice is for entering doctor records")
docans='y'

#this is a loop that will be executed till the time the user enters yes
while docans=='y':
print()
print("please enter the credentials asked below")
doc_name=input('Name : ')
doc_name=doc_name.lower()
doc_age=int(input('Age : '))
doc_phoneno=int(input('Phone Number : '))
doc_degree=input("Enter your degree:")
doc_degree= doc_degree.lower()
doc_patient=int(input("Enter no. of patients treated"))
gender=input("Enter Gender")
gender=gender.upper()
print()

#this command is used to input the record into the table in sql
cur.execute("insert into doctor_records values('" + doc_name + "'," + str(doc_age) + "," + str(doc_p
honeno) + ",'"+ doc_degree +"',"+str(doc_patient)+",'"+ gender +"')")
conn.commit()
print("Record added")
print()
print("Thankyou for entering a record")
print()

#this command asks the user to input yes or no for the loop to continue
docans=input(' wish to add more records (y/n)')
docans=docans.lower()

#this section is for choice 4
#the user can input values into the table medicine record
if choice==4:
print("you have successfully selected choice 4")
print(" this choice is for entering medicine records")
medicineans='y'

#this is a loop that will be executed till the time the user enters yes
while medicineans=='y':
print()
medicine_name=input('Name : ')
medicine_name=medicine_name.lower()
medicine_code=int(input('Enter code :(only number) '))
gst=float(input('gst : '))
sgst=float(input("Enter sgst:"))
total_cost=float(input("Enter total cost"))
batch_no=input("Enter batch no(Alphabet and number):")
quantity=int(input("Enter quantity"))
discount=int(input("Enter discount"))
med_type=input("Enter type of medicines(injections/tablets/syrups)")
med_type=med_type.lower()
print()

#this command is used to input the record into the table in sql
cur.execute("insert into medicines_details values('" + medicine_name + "'," + str(medicine_code) +
","+ str(gst) +","+str(sgst)+", "+str(total_cost)+",'"+batch_no+"',"+str(quantity)+","+str(discount)+",'"+med_type+"'
)")
conn.commit()
print("Record added")
print()
print("Thankyou for entering a record")
print()
#this command asks the user to input yes or no for the loop to continue
medicineans=input(' wish to add more records (y/n)')
medicineans=medicineans.lower()

#this section is for choice 5
#the user can view values present in the table patient record
if choice==5:
print("you have successfully selected choice 5")
print(" this choice is for viewing patient records")
patientans='y'

#this is a loop that will be executed till the time the user enters yes
while patientans=='y':
print()
print("Please enter the credentials asked below")
name=input('Name of the patient : ')
name=name.upper()
print("name entered by you is",name)
print()

#this command is used to view records from the table in sql
cur.execute("select * from patient_record where name like '" + str(name) + "'")
data=cur.fetchall()

#this command checks for row in data and then prints
for row in data:
print()
print('s_no : ',row[0])
print('Name : ',row[1])
print('Age : ',row[2])
print('Doctor consulted : ',row[3])
print('Address : ',row[4])
print('Phone Number : ',row[5])
print('prescription :',row[6])
print()
print("Thankyou for viewing a record")
print()

#this command asks the user to input yes or no for the loop to continue
patientans=input("Do you want to view more records (y/n)")
patientans=patientans.lower()
print()

#this section is for choice 6
#the user can view values present in the table salary record
if choice==6:
print("you have successfully selected choice 6")
print(" this choice is for viewing salary records")
salaryans='y'

#this is a loop that will be executed till the time the user enters yes
while salaryans=='y':
print()
print("Please enter the credentials asked below")
emp_name=input('Name of the employee : ')
emp_name=emp_name.upper()
print("the name entered by you is",emp_name)
print()

#this command is used to view records from the table in sql
cur.execute("select * from salary_record where emp_name like '" + str(emp_name) + "'")
data=cur.fetchall()

#this command checks for row in data and then prints
for row in data:
print()
print('S.no : ',row[0])
print('emp_name : ',row[1])
print('proffesion : ',row[2])
print('salary : ',row[3])
print('address : ',row[4])
print("phone_no: ",row[5])
print("emp_id: ",row[6])
print("gender: ",row[7])

print()
print("Thankyou for viewing a record")
print()


#this command asks the user to input yes or no for the loop to continue
salaryans=input("Do you want to view more records (y/n)")
salaryans=salaryans.lower()
print()

#this section is for choice 7
#the user can view values present in the table doctor record
if choice==7:
print("you have successfully selected choice 7")
print(" this choice is for viewing doctor records")
docviewans='y'

#this is a loop that will be executed till the time the user enters yes
while docviewans=='y':
print()
print("Please enter the credentials asked below")
name=input('Name of the doctor : ')
name=name.upper()
print("the name entered by you is",name)


#this command is used to view records from the table in sql
cur.execute("select * from doctor_records where doc_name like '" + str(name) + "'")
data=cur.fetchall()

#this command checks for row in data and then prints
for row in data:
print()
print('Name : ',row[0])
print('Age : ',row[1])
print('Degree: ',row[2])
print('phone_no : ',row[3])
print('Patient : ',row[4])
print('gender :',row[5])
print()
print("Thankyou for viewing a record")
print()


#this command asks the user to input yes or no for the loop to continue
docviewans=input("Do you want to view more records (y/n)")
docviewans=docviewans.lower()
print()

#this section is for choice 8
#the user can view values present in the table medicine record
if choice==8:
print("you have successfully selected choice 8")
print(" this choice is for viewing medicine records")
medicinesviewans='y'

#this is a loop that will be executed till the time the user enters yes
while medicinesviewans=='y':
print()
name=input('Name of the medicines : ')
name=name.upper()
print("the name entered by you is",name)
print()

#this command is used to view records from the table in sql
cur.execute("select * from medicines_details where medicine_name like '" + str(name) + "'")
data=cur.fetchall()
for row in data:
print()
print('Name : ',row[0])
print('code : ',row[1])
print('GST: ',row[2])
print('SGST : ',row[3])
print('Total cost : ',row[4])
print('Batch No.:',row[5])
print('Quantity:',row[6])
print('discount:',row[7])
print('type.:',row[8])
print()
print("Thank you for viewing a record")
print()

#this command asks the user to input yes or no for the loop to continue
medicinesviewans=input("Do you want to view more records (y/n)")
medicinesviewans=medicinesviewans.lower()
print()

#this section is for choice 9
#the user can delete values present in the table patient record
if choice == 9:
print("you have successfully selected choice 9")
print(" this choice is for deleting patient records")
deletepatientans='y'

#this is a loop that will be executed till the time the user enters yes
while deletepatientans=='y':
print()
name=input('Name of the patient : ')
name=name.upper()
print("the name entered by you is:",name)
print()

#this command is used to delete records from table in sql
cur.execute("delete from patient_record where name like '" + str(name) + "'")
print('Record Deleted Succefully')
print()
print('select choice 1 to reenter/enter new records')
print()

#this command asks the user to input yes or no for the loop to continue
deletepatientans=input("Do you want to delete more records? (y/n)")
deletepatientans=deletepatientans.lower()
print()

#this section is for choice 10
#the user can delete values present in the table salary record
if choice==10:
print("you have successfully selected choice 10")
print(" this choice is for deleting salary records")
deletesalaryans='y'

#this is a loop that will be executed till the time the user enters yes
while deletesalaryans=='y':
print()
name=input('Name of the Employee : ')
name=name.upper()
print("the name entered by you is:",name)
print()

#this command is used to delete records from table in sql
cur.execute("delete from salary_record where emp_name like '" + name + "'")
print('Record Deleted Succefully')
print()
print('select choice 2 to reenter/enter new records')
print()

#this command asks the user to input yes or no for the loop to continue
deletesalaryans=input("Do you want to delete more records? (y/n)")
deletesalaryans=deletesalaryans.lower()
print()

#this section is for choice 11
#the user can delete values present in the table doctor record
if choice==11:
print("you have successfully selected choice 11")
print(" this choice is for deleting doctor records")
deletedocans='y'

#this is a loop that will be executed till the time the user enters yes
while deletedocans=='y':
print()
name=input('Name of the doctor : ')
name=name.upper()
print('the name entered by you is',name)
print()

#this command is used to delete records from table in sql
cur.execute("delete from doctor_records where doc_name like '" + name + "'")
print('Record Deleted Succefully')
print()
print('select choice 3 to reenter/enter new records')
print()


#this command asks the user to input yes or no for the loop to continue
deletedocans=input("Do you want to delete more records? (y/n)")
deletedocans=deletedocans.lower()
print()

#this section is for choice 12
#the user can delete values present in the table medicine record
if choice==12:
print("you have successfully selected choice 12")
print(" this choice is for deleting medicine records")
deletemedicineans='y'

#this is a loop that will be executed till the time the user enters yes
while deletemedicineans=='y':
print()
name=input('Name of the medicine : ')
name=name.upper()
name=name.upper()
print('the name entered by you is',name)
print()

#this command is used to delete records from table in sql
cur.execute("delete from medicines_details where medicine_name like '" + name + "'")
print('Record Deleted Succefully')
print()
print('select choice 4 to reenter/enter new records')
print()
#this command asks the user to input yes or no for the loop to continue
deletemedicineans=input("Do you want to delete more records? (y/n)")
deletemedicineans=deletemedicineans.lower()
print()

#this section is for choice 13
#the user can input values into the table supplier
if choice ==13:
print("you have successfully selected choice 13")
print(" this choice is for entering suppliers records")
supplierans='y'

#this is a loop that will be executed till the time the user enters yes
while supplierans=='y':
print()
print("please enter the credentials asked below")
name=input('Name : ')
name=name.lower()
discount=int(input('Discount : '))
pay_mode=input('payment mode(cash/credit) : ')
pay_mode=pay_mode.upper()
delivery_time=int(input('time (only digits) : '))
co_name=input('Enter Company Name ')
co_name=co_name.upper()
print()


#this command is used to input the record into the table in sql
cur.execute("insert into supplier values('" + name + "'," + str(discount) + ",'" + pay_mode + "'," + st
r(delivery_time) + ",'" + co_name + "')")
conn.commit()
print("Record added")
print()
print("Thankyou for entering a record")
print()
#this command asks the user to input yes or no for the loop to continue
supplierans=input(' wish to add more records (y/n)')
supplierans=supplierans.lower()

#this section is for choice 14
#the user can view values present in the table supplier
if choice==14:
print("you have successfully selected choice 14")
print(" this choice is for viewing supplier records")
suppviewans='y'

#this is a loop that will be executed till the time the user enters yes
while suppviewans=='y':
print()
print("Please enter the credentials asked below")
suppname=input('Name of the supplier : ')
suppname=suppname.upper()
print("the name entered by you is",suppname)


#this command is used to view records from the table in sql
cur.execute("select * from supplier where name like '" + str(suppname) + "'")
data=cur.fetchall()

#this command checks for row in data and then prints
for row in data:
print()
print('Name : ',row[0])
print('Discount: ',row[1])
print('Pay_mode: ',row[2])
print('delivery_time: ',row[3])
print('co_name : ',row[4])
print()
print("Thankyou for viewing a record")
print()


#this command asks the user to input yes or no for the loop to continue
suppviewans=input("Do you want to view more records (y/n)")
suppviewans=suppviewans.lower()
print()

#this section is for choice 15
#the user can delete values present in the table patient record
if choice == 15:
print("you have successfully selected choice 15")
print(" this choice is for deleting supplier records")
deletesuppans='y'

#this is a loop that will be executed till the time the user enters yes
while deletesuppans=='y':
print()
suppname=input('Name of the supplier : ')
suppname=suppname.upper()
print("the name entered by you is:",suppname)
print()

#this command is used to delete records from table in sql
cur.execute("delete from supplier where name like '" + suppname + "'")
print('Record Deleted Succefully')
print()
print('select choice 13 to reenter/enter new records')
print()

#this command asks the user to input yes or no for the loop to continue
deletesuppans=input("Do you want to delete more records? (y/n)")
deletesuppans=deletesuppans.lower()
print()

#this section is for choice 16
#the user can input values into the table sales
if choice==16:
print("you have successfully selected choice 16")
print(" this choice is for entering sales records")
salans='y'

#this is a loop that will be executed till the time the user enters yes
while salans=='y':
print()
print("please enter the credentials asked below")
s_no=int(input('S.no : '))
amt_of_purchase=int(input('Amt of Purchase : '))
item=input('Enter Item : ')
item=item.upper()
discarded=int(input('No. of discarded items : '))

print()

#this command is used to input the record into the table in sql
cur.execute("insert into sales values(" + str(s_no) +"," + str(amt_of_purchase) + ",'" + item + "'," +
str(discarded) + ")")
conn.commit()
print("Record added")
print()
print("Thankyou for entering a record")
print()
#this command asks the user to input yes or no for the loop to continue
salans=input(' wish to add more records (y/n)')
salans=salans.lower()

if choice==17:
print("you have successfully selected choice 17")
print(" this choice is for viewing sales records")
salviewans='y'

#this is a loop that will be executed till the time the user enters yes
while salviewans=='y':
print()
print("Please enter the credentials asked below")
s_no=int(input('Enter S_no. : '))

print("the s_no entered by you is",s_no)


#this command is used to view records from the table in sql
cur.execute("select * from sales where s_no like '" + str(s_no) + "'")
data=cur.fetchall()

#this command checks for row in data and then prints
for row in data:
print()
print('s_no : ',row[0])
print('amt_of_purchase: ',row[1])
print('item : ',row[2])
print('discarded : ',row[3])
print()
print("Thankyou for viewing a record")
print()


#this command asks the user to input yes or no for the loop to continue
salviewans=input("Do you want to view more records (y/n)")
Salviewans=salviewans.lower()
print()

#this section is for choice 18
#the user can delete values present in the table sales
if choice==18:
print("you have successfully selected choice 18")
print(" this choice is for deleting sales")
deletesalans='y'

#this is a loop that will be executed till the time the user enters yes
while deletesalans=='y':
print()
s_no=int(input('Enter S_no. you want to delete : '))
print("the s_no entered by you is:",s_no)
print()

#this command is used to delete records from table in sql
cur.execute("delete from sales where s_no like " + str(s_no) + "")
print('Record Deleted Succefully')
print()
print('select choice 16 to reenter/enter new records')
print()

#this command asks the user to input yes or no for the loop to continue
deletesalans=input("Do you want to delete more records? (y/n)")
deletesalans=deletesalans.lower()
print()


#this section is for choice 19
#the user can input values into the table promotion
if choice==19:
print("you have successfully selected choice 19")
print(" this choice is for entering promotion records")
proans='y'

#this is a loop that will be executed till the time the user enters yes
while proans=='y':
print()
print("please enter the credentials asked below")
money_marketing=int(input('Enter total amt spent on marketing'))
money_newspaper=int(input('Enter total amt spent on newspaper marketing '))

money_socialmedia=int(input('Enter total amt spent on social media marketing '))
money_discount=int(input('Enter the amt of discount given : '))
print()

#this command is used to input the record into the table in sql
cur.execute("insert into promotion values(" + str(money_marketing) +", " +str(money_newspaper)
+ "," + str(money_socialmedia) + "," + str(money_discount) + ")")
conn.commit()
print("Record added")
print()
print("Thankyou for entering a record")
print()
#this command asks the user to input yes or no for the loop to continue
proans=input(' wish to add more records (y/n)')
proans=proans.lower()



#this section is for choice 20
#the user can view values present in the table promotions
if choice==20:
print("you have successfully selected choice 20")
print(" this choice is for viewing promotion records")
proviewans='y'

#this is a loop that will be executed till the time the user enters yes
while proviewans=='y':
print()
print("Please enter the credentials asked below")
money_marketing=int(input('Enter total amt spent on marketing'))

print("the amt entered by you is",money_marketing)


#this command is used to view records from the table in sql
cur.execute("select * from promotion where money_marketing like '" + str(money_marketing) + "'
")
data=cur.fetchall()

#this command checks for row in data and then prints
for row in data:
print()
print('total money spend on marketing : ',row[0])
print('total money spend on newspaper marketing : ',row[1])
print('total money spend on social media marketing ',row[2])
print('total money spend on discount ',row[3])
print()
print("Thankyou for viewing a record")
print()

#this command asks the user to input yes or no for the loop to continue
proviewans=input("Do you want to view more records (y/n)")
proviewans=proviewans.lower()
print()

#this section is for choice 21
#the user can delete values present in the table promotion
if choice == 21:
print("you have successfully selected choice 21")
print(" this choice is for deleting promotion records")
deleteproans='y'

#this is a loop that will be executed till the time the user enters yes
while deleteproans=='y':
print()
money_marketing=int(input('total money spend on marketing '))

print("the name entered by you is:",money_marketing)
print()

#this command is used to delete records from table in sql
cur.execute("delete from promotion where money_marketing like " + str(money_marketing) + "")
print('Record Deleted Succefully')
print()
print('select choice 19 to reenter/enter new records')
print()

#this command asks the user to input yes or no for the loop to continue
deleteproans=input("Do you want to delete more records? (y/n)")
deleteproans=deleteproans.lower()
print()

#this section is for choice 22
#the user can input values into the table profits
if choice==22:
print("you have successfully selected choice 22")
print(" this choice is for entering profits records")
profans='y'

#this is a loop that will be executed till the time the user enters yes
while profans=='y':
print()
print("please enter the credentials asked below")
money_mach=int(input('Enter total amt spent on machinery'))
money_sal=int(input('Enter total amt spent on salary '))

money_tax=int(input('Enter total amt spent on tax '))
gross_profit=int(input('Enter the amt of total profit : '))
net_profit=int(input('Enter the amt of Net profit'))
print()

#this command is used to input the record into the table in sql
cur.execute("insert into profit values(" + str(money_mach) +", " +str(money_sal) + "," + str(money
_tax) + "," + str(gross_profit) + ","+ str(net_profit)+")")
conn.commit()
print("Record added")
print()
print("Thankyou for entering a record")
print()
#this command asks the user to input yes or no for the loop to continue
profans=input(' wish to add more records (y/n)')
profans=profans.lower()
print()

#this section is for choice 23
#the user can view values present in the table profits
if choice==23:
print("you have successfully selected choice 23")
print(" this choice is for viewing profits records")
profviewans='y'

#this is a loop that will be executed till the time the user enters yes
while profviewans=='y':
print()
print("Please enter the credentials asked below")
gross_profit=int(input('Enter total amt of profit'))

print("the amt entered by you is",gross_profit)


#this command is used to view records from the table in sql
cur.execute("select * from profit where gross_profit like '" + str(gross_profit) + "'")
data=cur.fetchall()

#this command checks for row in data and then prints
for row in data:
print()
print('total money spend on machinry : ',row[0])
print('total money spend on salary : ',row[1])
print('total money spend on tax ',row[2])
print('total amt of profit ',row[3])
print('total amt of net profit ',row[4])
print()
print("Thankyou for viewing a record")
print()

#this command asks the user to input yes or no for the loop to continue
profviewans=input("Do you want to view more records (y/n)")
profviewans=profviewans.lower()
print()

#this section is for choice 24
#the user can delete values present in the table profits
if choice == 24:
print("you have successfully selected choice 24")
print(" this choice is for deleting profits records")
deleteprofans='y'

#this is a loop that will be executed till the time the user enters yes
while deleteprofans=='y':
print()
gross_profit=int(input('total amt of profit '))

print("the amt entered by you is:",gross_profit)
print()

#this command is used to delete records from table in sql
cur.execute("delete from profit where gross_profit like " + str(gross_profit) + "")
print('Record Deleted Succefully')
print()
print('select choice 22 to reenter/enter new records')
print()

#this command asks the user to input yes or no for the loop to continue
deleteprofans=input("Do you want to delete more records? (y/n)")
deleteprofans=deleteprofans.lower()
print()
loop =input("Do you wish to continue?")
loop=loop.lower()





#this else command is the else for password entered correct/incorrect
#this will be choosen if user enters incorrect password
#this will prevent unknown users to access the database
else:
print()
print('Invalid Password')
print('Tryagain')
print()

#this command is for login/exit
#this will be executed if the person chooses option 2-Exit
elif option==2:
print("you have decided to exit from our system")
print("thank you so much for visiting")
print("have a great day!")
print("hope to see you again soon")
print()
sys.exit()

conn.commit()
input()
 
