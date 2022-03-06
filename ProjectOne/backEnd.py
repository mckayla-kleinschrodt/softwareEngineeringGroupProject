import pickling
from tkinter import *

root = Tk()
root.geometry("500x500")

#empDict = {} #Holds the dictionary for employee information;
#Will have empID as the key and over information as values

#do we need a list and then to push each dictionary entry to that? 
 
#pData = pickling.PickleData()

#Importing over variables from front end

# i think we need a function that gives all employees in DB

#dump data to desktop
def DumpPickle():
    localData = pickling.PickleData.DataPickleRead()
    print("Latest pickle data: ", localData)

def QueryPickle():
    localData = pickling.PickleData.DataPickleRead()

    st = input("Enter search term: ")
    for i in localData:
        if st in localData[i]:
            print(i, localData[i])

#add new data to desktop   
def AddDataToPickle():
   pickling.PickleData.LocalAddEmployeeData()


AddEmployee =  Button(root, height = 1, width = 20, text = "Enter New Employee", command = AddDataToPickle)    
AddEmployee.pack()

displayButton = Button(root, height = 1, width = 20, text = "Display Employee", command = DumpPickle)    
displayButton.pack()

root.mainloop()