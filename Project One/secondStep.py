import pickle
import re

#validate the email address, ssn, and phone number to correct format
emailFormat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
ssnFormat = r'^\d\d\d-\d\d-\d\d\d\d$'
phoneFormat = r'^\d\d\d-\d\d\d-\d\d\d\d$'

class PickleData:
    #read in data that has been pickled 
    def DataPickleRead(self):
        with open('EmployeeDatabase.pkl', 'rb') as F:
            localData = pickle.load(F)
        return localData

    #take local employee and add it to pickle file
    def LocalAddEmployee(self):
        with open('EmployeeDatabase.pkl', 'rb') as F:
            localData = pickle.load(F)

        empList= []
        name = input("Enter First and Last name: ")
        position = input("Enter position: ")
        address = input("Enter Address: ")

        #validate email address
        email = input("Enter Email Address: ")
        if not (re.fullmatch(emailFormat, email)):
            email = input("Invalid Email! Please input your email again: ")
        #validate ssn number
        ssn = input("Please enter SSN: ")
        if not (re.fullmatch(ssnFormat, ssn)):
            ssn = input("Invalid Social Secutiry Number! Please input SSN: ")
        #validate phone number
        phone = input("Enter phone number: ")
        if not(re.fullmatch(phoneFormat, phone)):
            phone = input("Invalid phone number! Enter phone number: ")


        skills = input("Please input your skills: ")
        EmployeeID = input("Enter employeeID: ")

        empList = [empList.append(i) or i for i in [name, position, address, email, ssn, phone, skills]]
    
        print("Thank you!")

        with open('EmployeeDatabase.pkl', 'wb') as F:
            pickle.dump(localData, F)
