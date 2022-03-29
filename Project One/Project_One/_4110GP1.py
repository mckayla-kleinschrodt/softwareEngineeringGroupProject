from tkinter import *
import pickle
import re
from pathlib import Path


#set tKinter window
root = Tk()
root.geometry("650x350")
root.title('Database Access Window')
root['background'] = '#7B927F'
welcomeTitle = Label(text = "Welcome to the Employee Database Application!\n\n", background='#7B927F', font = 'Helvetica 20 bold')
introReview = Label(text = "To begin, add an employee to the database \nNext you can save the data and see all  the saved employees \nLastly there is an option to search the database for any information that was provided when entered!\n\n", background = '#7B927F', font = 'Helvetica 10')
welcomeTitle.pack()
introReview.pack()

#local employee dictionary 
empDict = {'df8988': ['Ron Brown', 'HR', '123-45-6784', '348 Hard dr', 'yahoo@yahoo.com', '123-456-7892', 'anger managment']}

#validate the email address, ssn, and phone number to correct format
emailFormat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
ssnFormat = r'^\d\d\d-\d\d-\d\d\d\d$'
phoneFormat = r'^\d\d\d-\d\d\d-\d\d\d\d$'


path_to_file = 'EmployeeDatabase.pkl'
path = Path(path_to_file)

if path.is_file():
    with open('EmployeeDatabase.pkl', 'rb') as F:
        empDict = pickle.load(F)
else:
    with open('EmployeeDatabase.pkl', 'wb') as F:
        pickle.dump(empDict, F)


#function to locally add employees
def LocalAddEmployeeData():
    #fileObj = open('EmployeeDatabase.pkl', 'a+')
    localData = pickle.load(open('EmployeeDatabase.pkl', 'rb'))

    #create list of employee attributes
    empList= []

    #gather inputs
    name = input("\n\nEnter First and Last name: ")
    position = input("Enter position: ")
    address = input("Enter Address: ")

    #validate email address
    email = input("Enter Email Address: ")
    notValid = True
    while notValid:
        if not (re.fullmatch(emailFormat, email)):
            email = input("Invalid Email! (exp: name@gmail.com) \nPlease input your email again: ")
        else:
            notValid = False

    #validate ssn number
    ssn = input("Please enter SSN: ")
    notValidSSN = True
    while notValidSSN:
        if not (re.fullmatch(ssnFormat, ssn)):
            ssn = input("Invalid Social Security Number! (exp: xxx-xx-xxxx) \nPlease input SSN: ")
        else:
            notValidSSN = False

    #validate phone number
    phone = input("Enter phone number: ")
    notValidNumber = True
    while notValidNumber:
        if not(re.fullmatch(phoneFormat, phone)):
            phone = input("Invalid phone number! (exp: 000-000-0000) \nEnter phone number: ")
        else:
            notValidNumber = False

    skills = input("Please input skills: ")
    EmployeeID = input("Enter employeeID: ")

    #add attributes to list created on line 13
    empList = [empList.append(i) or i for i in [name, position, address, email, ssn, phone, skills]]

    #save the entry as a dictionary using the ID as the key
    empDict[EmployeeID] = empList

    #with open('EmployeeDatabase.pkl', 'wb') as F:
    pickle.dump(empDict, open('EmployeeDatabase.pkl', 'wb'))

    #end function
    print("\nThank You!\n")
    #fileObj.close()

#display the database
def displayDB():
    localData = pickle.load(open('EmployeeDatabase.pkl', 'rb'))
    
    print("\nDatabase so far: ", localData)

#function to search data that has been pickled
def QueryPickle():
    localData = pickle.load(open('EmployeeDatabase.pkl', 'rb'))
    st = input("Enter Search Term: ")
    for i in localData:
        if st in localData[i]:
            print(i, localData[i])



#button to prompt user to add employee
addEmp = Button(text = "Add Employee", font = 'Helvetica 14 bold', foreground='#7B927F', height = 1, width = 21, borderwidth = 0, command = LocalAddEmployeeData)

#button to show the database
showDB = Button(text = "Show Database", font = 'Helvetica 14 bold', foreground='#7B927F', height = 1, width = 21, borderwidth = 0,  command = displayDB)

#button to search for employee
searchEmployeeDatabase = Button(text = "Search Employee Database",font = 'Helvetica 14 bold', foreground='#7B927F', height = 1, width = 21, borderwidth = 0, command = QueryPickle)

#add buttons to tKinter window
addEmp.pack()
showDB.pack()
searchEmployeeDatabase.pack()

#run the page
root.mainloop()
