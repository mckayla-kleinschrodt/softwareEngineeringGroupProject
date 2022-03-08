from tkinter import *
import  secondStep

#set tKinter window
root = Tk()
root.geometry("300x300")

#variabel to import PickleData class from stepTwo.py
PickleData = secondStep.PickleData()

#function to dump the pickle jar
def DumpPickle():
    localData = PickleData.DataPickleRead()
    print("Latest Pickle Data: ", localData)

#functino to add data to the pickle jar
def AddDataToPickle():
    NewData = PickleData.LocalAddEmployee()

#functino to search data that has been pickled
def QueryPickle():
    localData = PickleData.DataPickleRead()

    st = input("Enter Search Term: ")
    for i in localData:
        if st in localData[i]:
            print(i, localData[i])

#button to add employee to pickle jar
addEmployee = Button(text = "Add Employee", command = AddDataToPickle)

#button to load the data that has been dumped 
displayData = Button(text = "Load Data", command = (DumpPickle))

#button to search for employee
searchEmployeeDatabase = Button(text = "Search Employee Database", command = QueryPickle)

#put to tKinter window
addEmployee.pack()
displayData.pack()
searchEmployeeDatabase.pack()

#run program
root.mainloop()
