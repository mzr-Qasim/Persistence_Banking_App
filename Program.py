# Entering New Customer Details
def New_Customer(): 
    global Customer_Name
    Customer_Name=input("Enter Customer Name: ")
    global Customer_Mobile_No
    Customer_Mobile_No=int(input("Enter Customer Mobile Number: "))
    global Customer_Deposit_Amount
    Customer_Deposit_Amount=int(input("Enter Deposit amount: "))

New_Customer()


# Adding New Customer Details to Json 
def Customer_Dictionary():
    {
        "Name":Customer_Name,
        "Mobile_No":Customer_Mobile_No,
        "deposit_Amount":Customer_Deposit_Amount
        
    }

