from tkinter import *
from tkinter import ttk


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


class addEmployee():

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

class searchEmpID():
    empIDLabel = Label(tab2, text = "Employee ID: ")
    empIDLabel.pack()
    employeeID = Entry(tab2, width= 40)
    employeeID.focus_get()
    employeeID.pack()


newEmployeeButtonSet = Button(tab1, height = 1, width = 20, text = "Enter New Employee", command = lambda: addEmployee())         
newEmployeeButtonSet.pack()

searchEmployeeDBSet = Button(tab2, height = 1, width = 20, text = "Search for Employee", command = lambda: searchEmpID()) 
searchEmployeeDBSet.pack()

root.mainloop()






