from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x500")

class frontEnd():
    fullNameLabel = Label(root, text = "Full Name: ")
    fullNameLabel.pack()
    fullName = Entry(root, width= 40)
    fullName.focus_get()
    fullName.pack()

    positionLabel = Label(root, text = "Position: ")
    positionLabel.pack()
    position = Entry(root, width= 40)
    position.focus_get()
    position.pack()


    
    ssnLabel = Label(root, text = "SSN: ")
    ssnLabel.pack()
    ssn = Entry(root, width= 40)
    ssn.focus_get()
    ssn.pack()

    addressLabel = Label(root, text = "Home Address: ")
    addressLabel.pack()
    address = Entry(root, width= 40)
    address.focus_get()
    address.pack()

    emailAddLabel = Label(root, text = "Email: ")
    emailAddLabel.pack()
    emailAdd = Entry(root, width= 40)
    emailAdd.focus_get()
    emailAdd.pack()

    phoneNumberLabel = Label(root, text = "Phone Number: ")
    phoneNumberLabel.pack()
    phoneNumber = Entry(root, width= 40)
    phoneNumber.focus_get()
    phoneNumber.pack()

    skillsLabel = Label(root, text = "Skills: ")
    skillsLabel.pack()
    skills = Entry(root, width= 40)
    skills.focus_get()
    skills.pack()

    empIDLabel = Label(root, text = "Employee ID: ")
    empIDLabel.pack()
    employeeID = Entry(root, width= 40)
    employeeID.focus_get()
    employeeID.pack()


newEmployeeButtonSet = Button(root, height = 1, width = 20, text = "Enter New Employee", command = lambda: frontEnd())         
newEmployeeButtonSet.pack()

searchEmployeeDBSet = Button(root, height = 1, width = 20, text = "Search for Employee", command = lambda: frontEnd()) 
searchEmployeeDBSet.pack()

root.mainloop()






