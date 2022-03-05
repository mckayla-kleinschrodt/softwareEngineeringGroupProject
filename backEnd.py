import frontEnd.py


empDict = {} #Holds the dictionary for employee information;
#Will have empID as the key and over information as values

#Importing over variables from front end
fullName = frontEnd.fullName
position = frontEnd.position
SSN = frontEnd.ssn
address = frontEnd.address
email = frontEnd.emailAdd
phoneNum = frontEnd.phoneNumber
skills = frontEnd.skills
empID = frontEnd.employeeID
searchVal = frontEnd.searchEmployee


def addEmp():
    empDict[empID] = [fullName, position, SSN, address, email, phoneNum, skills]

def searchEmp():
    if searchVal in empDict.keys():
        print(empDict[searchVal])
    else:
        print(f"{searchVal} is not in the employee database.") 
