from tkinter import *
from PIL import Image, ImageTk
import json
from datetime import *

#------------------------------set tKinter window-------------------------------
root = Tk()
root.geometry("750x500")
root.title('BarMaster')
root['background'] = '#6495ED'


#-------------------text labels for sections on tKinter window------------------
welcomeTitle = Label(text = "Welcome to the Bar!\n\n", background='#6495ED', font = 'Helvetica 20 bold')
welcomeTitle.grid(row = 0, column = 6)

instructions = Label(text = "please choose the drink you are serving to update the inventory", background='#6495ED', font = 'Helvetica 18')
instructions.grid(row=1, column = 6)

alcoholicTitle = Label(text = "The Popular Alcoholic Drinks:", background='#6495ED', font = 'Helvetica 18 bold')
alcoholicTitle.grid(row = 5, column = 6)

nonAlcoholicTitle = Label(text = "The Popular Non-Alcoholic Drinks:", background='#6495ED', font = 'Helvetica 18 bold')
nonAlcoholicTitle.grid(row = 13, column = 6)


# we need 2 json files, one for inventory, and one for a log
# below functions will update these files
# need a function that will ask for employee number, and return the beginnning of a log statement, "Emp # orderd ______ at 0:00 PM"
#---------class to order drinks, update inventory, and add to order log---------
def transactionData():
    empID = int(input("Please enter employee ID # from 1 - 10: "))

    if empID == 1:
        employee = 'Employee 1'
    elif empID == 2:
        employee = 'Employee 2'
    elif empID == 3:
        employee = 'Employee 3'
    elif empID == 4: 
        employee = 'Employee 4'
    elif empID == 5: 
        employee = 'Employee 5'
    elif empID == 6: 
        employee = 'Employee 6'
    elif empID == 7: 
        employee = 'Employee 7'
    elif empID == 8:
        employee = 'Employee 8'
    elif empID == 9:
        employee = 'Employee 9'
    elif empID == 10:
        employee = 'Employee 10'
    else:
        print("Invalid Employee ID entered. Please quit and try again!")

    ct = datetime.now()

    log_message = f"At {ct}, {employee} served a "
    return str(log_message)
    


#class to hold drink functions
class Orders:
    def cosmo():
        transactionLog = []
        transaction_data = transactionData()
        transaction_data +="Cosmo"
        print(transaction_data)
        transactionLog.append(transaction_data)

        
        #transactionData()
        print("You placed an order for a Cosmo!")
        

        with open('/Users/kayla/Documents/GitHub/softwareEngineeringGroupProject/Project Two/Inventory.json', 'r') as jsonFile:
            data = json.load(jsonFile)

        data['vodka'] -= 2
        data['triple_sec'] -= 2
        data['juice'] -= 1
        data['fruit'] -= 1
        
        with open('/Users/kayla/Documents/GitHub/softwareEngineeringGroupProject/Project Two/Inventory.json', 'w') as jsonFile:
            json.dump(data,jsonFile)

        Time = datetime.now()

        time_entry = {'time': Time}
        drink_entry = {'drink': 'cosmo'}
        transaction_entry = {'transaction': transaction_data}

        with open('/Users/kayla/Documents/GitHub/softwareEngineeringGroupProject/Project Two/systemLog.json', 'r') as logFile:
            log = json.load(logFile)

        log.append(time_entry)
        log.append(drink_entry)
        log.append(transaction_entry)

        print("System log: ", log)

        with open('/Users/kayla/Documents/GitHub/softwareEngineeringGroupProject/Project Two/systemLog.json', "w") as file:
            json.dump(log,file)
        
    def marg():
       return
    def pina():
        return    
    def daq():
        return
    def white():
        return
    def mule():
        return
    def arnold():
        return
    def shirley():
        return
    def mocktail():
        return


    
#-----------open and size images -- fix paths to not be absolute----------------
cosmoImg = Image.open('/Users/kayla/Documents/GitHub/softwareEngineeringGroupProject/Project Two/Photos/cosmo.png')
cosmoResize = cosmoImg.resize((80, 80))
cosmo = ImageTk.PhotoImage(cosmoResize)

arnoldImg = Image.open('/Users/kayla/Documents/GitHub/softwareEngineeringGroupProject/Project Two/Photos/arnoldPalmer.png')
arnoldResize = arnoldImg.resize((80, 80))
arnold = ImageTk.PhotoImage(arnoldResize)

shirleyImg = Image.open('/Users/kayla/Documents/GitHub/softwareEngineeringGroupProject/Project Two/Photos/shirleyTemple.png')
shirleyResize = shirleyImg.resize((80, 80))
shirley= ImageTk.PhotoImage(shirleyResize)

margImg = Image.open('/Users/kayla/Documents/GitHub/softwareEngineeringGroupProject/Project Two/Photos/marg.png')
margResize = margImg.resize((80, 80))
marg= ImageTk.PhotoImage(margResize)

mocktailImg = Image.open('/Users/kayla/Documents/GitHub/softwareEngineeringGroupProject/Project Two/Photos/mocktail.png')
mocktailResize = mocktailImg.resize((80, 80))
mocktail = ImageTk.PhotoImage(mocktailResize)

muleImg = Image.open('/Users/kayla/Documents/GitHub/softwareEngineeringGroupProject/Project Two/Photos/mule.png')
muleResize = muleImg.resize((80, 80))
mule = ImageTk.PhotoImage(muleResize)

pinaColadaImg = Image.open('/Users/kayla/Documents/GitHub/softwareEngineeringGroupProject/Project Two/Photos/pinaColada.png')
pinaColadaResize = pinaColadaImg.resize((80, 80))
pina = ImageTk.PhotoImage(pinaColadaResize)

strawberryImg = Image.open('/Users/kayla/Documents/GitHub/softwareEngineeringGroupProject/Project Two/Photos/strawDaq.png')
strawberryResize = strawberryImg.resize((80, 80))
strawberry = ImageTk.PhotoImage(strawberryResize)

whiteImg = Image.open('/Users/kayla/Documents/GitHub/softwareEngineeringGroupProject/Project Two/Photos/whiteLady.png')
whiteResize = whiteImg.resize((80, 80))
white = ImageTk.PhotoImage(whiteResize)

#-------------------Drink Buttons with images and labels------------------------
arnoldButton = Button(root, text = 'Arnold Palmer', image=arnold, command= lambda:Orders.arnold(), compound = TOP)
cosmoButton = Button(root, text = 'Cosmopolitan', image=cosmo, command= Orders.cosmo, compound = TOP)
shirleyButton = Button(root, text = 'Shirley Temple', image=shirley, command= lambda:Orders.shirley, compound = TOP)
margButton = Button(root, text = 'Margarita', image=marg, command= lambda:Orders.marg, compound = TOP)
mocktailButton = Button(root, text = 'Island Mocktail', image=mocktail, command= lambda:Orders.mocktail, compound = TOP)
muleButton = Button(root, text = 'Mexican Mule', image=mule, command= lambda:Orders.mule, compound = TOP)
pinaButton = Button(root, text = 'Piña Colada', image=pina, command= lambda:Orders.pina, compound = TOP)
daqButton = Button(root, text = 'Strawberry Daquiri', image=strawberry, command= lambda:Orders.daq, compound = TOP)
whiteButton = Button(root, text = 'White Lady', image=white, command= lambda:Orders.white, compound = TOP)

#----------------Position and post buttons to tkinter window--------------------
muleButton.grid(row=6, column = 4)
margButton.grid(row=6, column = 6)
cosmoButton.grid(row=6, column = 8)

daqButton.grid(row=10, column = 6)
pinaButton.grid(row=10, column = 4)
whiteButton.grid(row=10, column = 8)

shirleyButton.grid(row=14, column = 6)
arnoldButton.grid(row=14, column = 4)
mocktailButton.grid(row=14, column = 8)



#run the page
root.mainloop()
