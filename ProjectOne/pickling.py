import pickle 
import frontEnd

class PickleData: 
    def DataPickleRead(self):
        with open ('EmployeeDatabase.pkl', 'rb') as F:
            localData = pickle.load(F)
            print(localData)
        return localData
        

    def LocalAddEmployeeData(self):
        with open('EmployeeDatabase.pkl', 'rb') as F:
            localData = pickle.load(F)

        empList = []

        fullName = frontEnd.fullName
        position = frontEnd.position
        ssn = frontEnd.ssn
        address = frontEnd.address
        email = frontEnd.emailAdd
        phoneNum = frontEnd.phoneNumber
        skills = frontEnd.skills
        empID = frontEnd.employeeID

        empList = [empList.append(i) or i for i in [fullName, position, ssn, address, email, phoneNum, skills]]

        localData[empID] = empList

        with open('EmployeeDatabase.pkl', 'wb') as F:
            pickle.dump(localData, F)
