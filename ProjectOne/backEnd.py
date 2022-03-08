from tkinter import *
from tkinter import ttk
import pickle
import backEnd


root = Tk()
root.geometry("500x500")


tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tabControl.add(tab1, text ='Add New Employee')
Label(tab1)
tabControl.add(tab2, text ='Search Employee Database')
Label(tab2)
tabControl.pack(expand = 1, fill ="both")


empDict = {'df8988': ['Ron Brown', 'HR', '123-45-6784', '348 Hard dr', 'yahoo@yahoo.com', '123-456-7892', 'anger managment']} #Holds the dictionary for employee information;
#Will have empID as the key and over information as values


def addEmployee():
    empList = []

    fullNameLabel = Label(tab1, text = "Full Name: ")
    fullNameLabel.pack()
    fullName = Entry(tab1, width= 40)
    fullName.focus_get()
    fullName.pack()

    positionLabel = Label(tab1, text = "Position: ")
    positionLabel.pack()
    position = Entry(tab1, width= 40)
    position.focus_get()
    position.pack()
    
    ssnLabel = Label(tab1, text = "SSN: ")
    ssnLabel.pack()
    ssn = Entry(tab1, width= 40)
    ssn.focus_get()
    ssn.pack()

    addressLabel = Label(tab1, text = "Home Address: ")
    addressLabel.pack()
    address = Entry(tab1, width= 40)
    address.focus_get()
    address.pack()

    emailAddLabel = Label(tab1, text = "Email: ")
    emailAddLabel.pack()
    emailAdd = Entry(tab1, width= 40)
    emailAdd.focus_get()
    emailAdd.pack()

    phoneNumberLabel = Label(tab1, text = "Phone Number: ")
    phoneNumberLabel.pack()
    phoneNumber = Entry(tab1, width= 40)
    phoneNumber.focus_get()
    phoneNumber.pack()

    skillsLabel = Label(tab1, text = "Skills: ")
    skillsLabel.pack()
    skills = Entry(tab1, width= 40)
    skills.focus_get()
    skills.pack()

    empIDLabel = Label(tab1, text = "Employee ID: ")
    empIDLabel.pack()
    employeeID = Entry(tab1, width= 40)
    employeeID.focus_get()
    employeeID.pack()

    empList = [empList.append(i) or i for i in [fullName, position, ssn, address, emailAdd, phoneNumber, skills,employeeID]]

    empDict[employeeID] = empList
    print("Added Employee!")


def searchEmpID():
    searchEmpLabel = Label(tab2, text = "Employee ID: ")
    searchEmpLabel.pack()
    searchEmployee = Entry(tab2, width= 40)
    searchEmployee.focus_get()
    searchEmployee.pack()

def displayDB():
    print("Database Entries: \n", empDict)

def DataPickle(empDict):
    with open('EmployeeDatabase.pkl', 'wb') as F:
        pickle.dump(empDict, F)

    with open('EmployeeDatabase.pkl', 'rb') as F:
        E = pickle.load(F)
    
    print("PICKLE DATA: ", E)

startProgramButtonSet = Button(tab1, height = 1, width = 20, text = "Enter New Employee", command = addEmployee())    
startProgramButtonSet.pack()

newEmployeeButtonSet = Button(tab1, height = 1, width = 20, text = "Enter New Employee", command = DataPickle(empDict))    
newEmployeeButtonSet.pack()

searchEmployeeDBSet = Button(tab2, height = 1, width = 20, text = "Search for Employee", command = (lambda: backEnd.QueryPickle))
searchEmployeeDBSet.pack()

printDatabaseButtonSet = Button(tab2, height = 1, width = 20, text = "See All Employees", command = displayDB)     
printDatabaseButtonSet.pack()

root.mainloop()






