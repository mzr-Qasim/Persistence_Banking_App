from Banking_Pkg.Adding_Records import Add_Records
import random
# Entering New Customer Details

def New_Customer(): 
    global Customer_Name
    Customer_Name=input("Enter Customer Name: ")
    global Customer_Mobile_No
    Customer_Mobile_No=int(input("Enter Customer Mobile Number: "))
    global Customer_New_PIN
    Customer_New_PIN=int(input("Enter Customer New PIN: "))
    global New_Account_No
    New_Account_No = random.randint(100000, 10000000)
    print("Yout new account number is",New_Account_No)
    global Customer_Address
    Customer_Address=input("Enter Customer Address: ")
    

New_Customer()


# Adding Customer Details to Dictionary
global Customer_Dictionary_Content
Customer_Dictionary_Content={
"Name":Customer_Name,
"Mobile_No":Customer_Mobile_No,
"customer_PIN":Customer_New_PIN,
"Account no":New_Account_No,
"customer_Address":Customer_Address
}

Add_Records()