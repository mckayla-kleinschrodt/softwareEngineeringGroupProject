from tkinter import *
import pickle
import re

#set tKinter window
root = Tk()
root.geometry("200x200")


open('EmployeeDatabase.pkl', 'w+')


#local employee dictionary 
empDict = {'df8988': ['Ron Brown', 'HR', '123-45-6784', '348 Hard dr', 'yahoo@yahoo.com', '123-456-7892', 'anger managment']}

#validate the email address, ssn, and phone number to correct format
emailFormat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
ssnFormat = r'^\d\d\d-\d\d-\d\d\d\d$'
phoneFormat = r'^\d\d\d-\d\d\d-\d\d\d\d$'

#functino to locally add employees
def LocalAddEmployeeData():
    
    with open('EmployeeDatabase.pkl', 'rb') as F:
        localData = pickle.load(F)

    #create list of employee attributes
    empList= []

    #gather inputs
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

    #add attributes to list created on line 13
    empList = [empList.append(i) or i for i in [name, position, address, email, ssn, phone, skills]]

    #save the entry as a dictionary using the ID as the key
    empDict[EmployeeID] = empList

    with open('EmployeeDatabase.pkl', 'wb') as F:
        pickle.dump(localData, F)

    #end function
    print("Thank You!")


#display the database
def displayDB(empDict):
    print("Database so far: ",empDict)

def DataPickleRead():
    with open('EmployeeDatabase.pkl', 'rb') as F:
        localData = pickle.load(F)
    return localData

def DumpPickle():
    localData = DataPickleRead()
    print("Latest Pickle Data: ", localData)

#function to search data that has been pickled
def QueryPickle():
    localData = DataPickleRead()

    st = input("Enter Search Term: ")
    for i in localData:
        if st in localData[i]:
            print(i, localData[i])

#button to prompt user to add employee
addEmp = Button(text = "Add Employee", command = LocalAddEmployeeData)

#button to show the database
showDB = Button(text = "Show Database",  command = (lambda: displayDB(empDict)))

searchEmployeeDatabase = Button(text = "Search Employee Database", command = QueryPickle)

#add buttons to tKinter window
addEmp.pack()
showDB.pack()
searchEmployeeDatabase.pack()

#close('EmployeeDatabase.pkl')

#run the page
root.mainloop()







                        

