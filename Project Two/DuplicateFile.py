from tkinter import *
from PIL import ImageTk, Image 
import json
from datetime import *

global entry
#------------------------------set tKinter window-------------------------------
root = Tk()
root.geometry("1500x1500")
root.title('Bar Master')
root['background'] = '#97a258'

#-------------------text labels for sections on tKinter window------------------
welcomeTitle = Label(text = "Welcome to the Bar!\n\n", background='#97a258', font = 'Helvetica 20 bold')
welcomeTitle.grid(row = 0, column = 6)

instructions = Label(text = "Please enter your employee ID #, then press the button for the drink that you are odering!", background='#97a258', font = 'Helvetica 18')
instructions.grid(row=1, column = 6)

alcoholicTitle = Label(text = "The Popular Alcoholic Drinks:", background='#97a258', font = 'Helvetica 18 bold')
alcoholicTitle.grid(row = 5, column = 6)

nonAlcoholicTitle = Label(text = "The Popular Non-Alcoholic Drinks:", background='#97a258', font = 'Helvetica 18 bold')
nonAlcoholicTitle.grid(row = 13, column = 6)

userInputLab = Label(root, text="Please enter employee ID # from 1 - 10: ", font="Helvetica 18", background='#97a258')
userInputLab.grid(row = 2, column = 6)

entry = Entry(root, width = 40)
entry.focus_set()
entry.grid(row = 3, column = 6)

entryButton = Button(root, text="Done!", font="Helvetica 18")
entryButton.grid(row = 4, column = 6)

#-------------------functino to get employee id and time stamp------------------
def transactionData():
    
    empID = int(entry.get())

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

#---------------------function to reset drink inventory-------------------------
def reset():
    with open('Inventory.json', 'r') as jsonFile:
        data = json.load(jsonFile)

    data['vodka'] = 999
    data['gin'] = 999
    data['tequila'] = 999
    data['rum'] = 999
    data['ginger_beer'] = 999
    data['triple_sec'] = 999
    data['cream'] = 999
    data['juice'] = 999
    data['soda_water'] = 999
    data['tea'] = 999
    data['lemonade'] = 999
    data['grenadine'] = 999
    data['fruit'] = 999
    data['ice'] = 999

    with open('Inventory.json', 'w') as jsonFile:
        json.dump(data, jsonFile)
    
    print("Inventory has been refilled!")

#---------class to order drinks, update inventory, and add to order log---------
class Orders:
#------------------------------first row functions------------------------------
    def mule():
        transactionLog = []
        transaction_data = transactionData()
        transaction_data += "Mexican Mule"
        print(transaction_data)
        transactionLog.append(transaction_data)

        #transactionData()
        print("\nYou placed an order for a Mexican Mule!")
        
        with open('Inventory.json', 'r') as jsonFile:
            data = json.load(jsonFile)

        data['tequila'] -= 2
        data['ginger_beer'] -= 2
        data['juice'] -= 1
        data['fruit'] -= 1
        
        with open('Inventory.json', 'w') as jsonFile:
            json.dump(data,jsonFile)

        currentTime = datetime.now()
        formattedTime = currentTime.strftime("%m/%d/%Y, %H:%M:%S")
        time_entry = {'time': formattedTime}
        drink_entry = {'drink': 'mule'}
        transaction_entry = {'transaction': transaction_data}

        with open('systemLog.json', 'r') as otherFile:
            log = json.loads(otherFile.read())


        log.append(time_entry)
        log.append(drink_entry)
        log.append(transaction_entry)

        with open('systemLog.json', "w") as file:
            json.dump(log, file)
        #entry.delete(0, END)
    
    def marg():
        transactionLog = []
        transaction_data = transactionData()
        transaction_data += "Margarita"
        print(transaction_data)
        transactionLog.append(transaction_data)

        print("\nYou placed an order for a Margarita!")
        
        with open('Inventory.json', 'r') as jsonFile:
            data = json.load(jsonFile)

        data['tequila'] -= 2
        data['triple_sec'] -= 2
        data['juice'] -= 1
        data['fruit'] -= 1
        
        with open('Inventory.json', 'w') as jsonFile:
            json.dump(data,jsonFile)

        currentTime = datetime.now()
        formattedTime = currentTime.strftime("%m/%d/%Y, %H:%M:%S")
        time_entry = {'time': formattedTime}
        drink_entry = {'drink': 'marg'}
        transaction_entry = {'transaction': transaction_data}

        with open('systemLog.json', 'r') as otherFile:
            log = json.loads(otherFile.read())


        log.append(time_entry)
        log.append(drink_entry)
        log.append(transaction_entry)

        with open('systemLog.json', "w") as file:
            json.dump(log, file)
        #entry.delete(0, END)
    
    def cosmo():
        transactionLog = []
        transaction_data = transactionData()
        transaction_data +="Cosmo"
        print(transaction_data)
        transactionLog.append(transaction_data)
      
        print("\nYou placed an order for a Cosmo!")
        
        with open('Inventory.json', 'r') as jsonFile:
            data = json.load(jsonFile)

        data['vodka'] -= 2
        data['triple_sec'] -= 2
        data['juice'] -= 1
        data['fruit'] -= 1
        
        with open('Inventory.json', 'w') as jsonFile:
            json.dump(data,jsonFile)

        currentTime = datetime.now()
        formattedTime = currentTime.strftime("%m/%d/%Y, %H:%M:%S")
        time_entry = {'time': formattedTime}
        drink_entry = {'drink': 'cosmo'}
        transaction_entry = {'transaction': transaction_data}

        with open('systemLog.json', 'r') as otherFile:
            log = json.loads(otherFile.read())


        log.append(time_entry)
        log.append(drink_entry)
        log.append(transaction_entry)

        with open('systemLog.json', "w") as file:
            json.dump(log, file)
         
#-----------------------------second row functions------------------------------
    def pina():
        transactionLog = []
        transaction_data = transactionData()
        transaction_data += "Pina Colada"
        print(transaction_data)
        transactionLog.append(transaction_data)

        print("\nYou placed an order for a Piña Colada!")
        
        with open('Inventory.json', 'r') as jsonFile:
            data = json.load(jsonFile)

        data['rum'] -= 2
        data['cream'] -= 2
        data['juice'] -= 1
        data['fruit'] -= 1
        data['ice'] -= 1

        with open('Inventory.json', 'w') as jsonFile:
            json.dump(data,jsonFile)

        currentTime = datetime.now()
        formattedTime = currentTime.strftime("%m/%d/%Y, %H:%M:%S")
        time_entry = {'time': formattedTime}
        drink_entry = {'drink': 'pina'}
        transaction_entry = {'transaction': transaction_data}

        with open('systemLog.json', 'r') as otherFile:
            log = json.loads(otherFile.read())


        log.append(time_entry)
        log.append(drink_entry)
        log.append(transaction_entry)

        with open('systemLog.json', "w") as file:
            json.dump(log, file)
    
    def daq():
        transactionLog = []
        transaction_data = transactionData()
        transaction_data += "Daiquiri"
        print(transaction_data)
        transactionLog.append(transaction_data)

        print("\nYou placed an order for a Strawberry Daiquiri!")
        
        with open('Inventory.json', 'r') as jsonFile:
            data = json.load(jsonFile)

        data['rum'] -= 2
        data['soda_water'] -= 2
        data['juice'] -= 1
        data['fruit'] -= 2
        
        with open('Inventory.json', 'w') as jsonFile:
            json.dump(data,jsonFile)

        currentTime = datetime.now()
        formattedTime = currentTime.strftime("%m/%d/%Y, %H:%M:%S")
        time_entry = {'time': formattedTime}
        drink_entry = {'drink': 'daq'}
        transaction_entry = {'transaction': transaction_data}

        with open('systemLog.json', 'r') as otherFile:
            log = json.loads(otherFile.read())


        log.append(time_entry)
        log.append(drink_entry)
        log.append(transaction_entry)

        with open('systemLog.json', "w") as file:
            json.dump(log, file)
   
    def white():
        transactionLog = []
        transaction_data = transactionData()
        transaction_data += "White Lady"
        print(transaction_data)
        transactionLog.append(transaction_data)

        print("\nYou placed an order for a White Lady!")
        
        with open('Inventory.json', 'r') as jsonFile:
            data = json.load(jsonFile)

        data['gin'] -= 2
        data['triple_sec'] -= 2
        data['juice'] -= 1
        data['egg'] -= 1

        with open('Inventory.json', 'w') as jsonFile:
            json.dump(data,jsonFile)

        currentTime = datetime.now()
        formattedTime = currentTime.strftime("%m/%d/%Y, %H:%M:%S")
        time_entry = {'time': formattedTime}
        drink_entry = {'drink': 'white'}
        transaction_entry = {'transaction': transaction_data}

        with open('systemLog.json', 'r') as otherFile:
            log = json.loads(otherFile.read())


        log.append(time_entry)
        log.append(drink_entry)
        log.append(transaction_entry)

        with open('systemLog.json', "w") as file:
            json.dump(log, file)
 
#-----------------------non-alcoholic drink functions---------------------------
    def arnold():
        transactionLog = []
        transaction_data = transactionData()
        transaction_data += "Arnold Palmer"
        print(transaction_data)
        transactionLog.append(transaction_data)

        #transactionData()
        print("\nYou placed an order for an Arnold Palmer!")
        
        with open('Inventory.json', 'r') as jsonFile:
            data = json.load(jsonFile)

        data['tea'] -= 1
        data['lemonade'] -= 2
        data['fruit'] -= 3
        data['ice'] -= 2

        with open('Inventory.json', 'w') as jsonFile:
            json.dump(data,jsonFile)

        currentTime = datetime.now()
        formattedTime = currentTime.strftime("%m/%d/%Y, %H:%M:%S")
        time_entry = {'time': formattedTime}
        drink_entry = {'drink': 'arnold'}
        transaction_entry = {'transaction': transaction_data}

        with open('systemLog.json', 'r') as otherFile:
            log = json.loads(otherFile.read())


        log.append(time_entry)
        log.append(drink_entry)
        log.append(transaction_entry)

        with open('systemLog.json', "w") as file:
            json.dump(log, file)
    
    def shirley():
        transactionLog = []
        transaction_data = transactionData()
        transaction_data += "Shirley Temple"
        print(transaction_data)
        transactionLog.append(transaction_data)

        print("\nYou placed an order for a Shirley Temple!")
        
        with open('Inventory.json', 'r') as jsonFile:
            data = json.load(jsonFile)

        data['soda_water'] -= 2
        data['grenadine'] -= 1
        data['fruit'] -= 1
        
        with open('Inventory.json', 'w') as jsonFile:
            json.dump(data,jsonFile)

        currentTime = datetime.now()
        formattedTime = currentTime.strftime("%m/%d/%Y, %H:%M:%S")
        time_entry = {'time': formattedTime}
        drink_entry = {'drink': 'shirley'}
        transaction_entry = {'transaction': transaction_data}

        with open('systemLog.json', 'r') as otherFile:
            log = json.loads(otherFile.read())


        log.append(time_entry)
        log.append(drink_entry)
        log.append(transaction_entry)

        with open('systemLog.json', "w") as file:
            json.dump(log, file)
    
    def mocktail():
        transactionLog = []
        transaction_data = transactionData()
        transaction_data += "Island Mocktail"
        print(transaction_data)
        transactionLog.append(transaction_data)

        #transactionData()
        print("\nYou placed an order for an Island Mocktail!")
        
        with open('Inventory.json', 'r') as jsonFile:
            data = json.load(jsonFile)

        data['cream'] -= 1
        data['juice'] -= 2
        data['fruit'] -= 3
        data['ice'] -= 2

        with open('Inventory.json', 'w') as jsonFile:
            json.dump(data,jsonFile)

        currentTime = datetime.now()
        formattedTime = currentTime.strftime("%m/%d/%Y, %H:%M:%S")
        time_entry = {'time': formattedTime}
        drink_entry = {'drink': 'mocktail'}
        transaction_entry = {'transaction': transaction_data}

        with open('systemLog.json', 'r') as otherFile:
            log = json.loads(otherFile.read())

        log.append(time_entry)
        log.append(drink_entry)
        log.append(transaction_entry)

        with open('systemLog.json', "w") as file:
            json.dump(log, file)

    
    
#-----------open and size images -- fix paths to not be absolute----------------
cosmoImg = Image.open('Photos/cosmo.png')
cosmoResize = cosmoImg.resize((150, 100))
cosmo = ImageTk.PhotoImage(cosmoResize)

arnoldImg = Image.open('Photos/arnoldPalmer.png')
arnoldResize = arnoldImg.resize((150, 100))
arnold = ImageTk.PhotoImage(arnoldResize)

shirleyImg = Image.open('Photos/shirleyTemple.png')
shirleyResize = shirleyImg.resize((150, 100))
shirley= ImageTk.PhotoImage(shirleyResize)

margImg = Image.open('Photos/marg.png')
margResize = margImg.resize((150, 100))
marg= ImageTk.PhotoImage(margResize)

mocktailImg = Image.open('Photos/mocktail.png')
mocktailResize = mocktailImg.resize((150, 100))
mocktail = ImageTk.PhotoImage(mocktailResize)

muleImg = Image.open('Photos/mule.png')
muleResize = muleImg.resize((150, 100))
mule = ImageTk.PhotoImage(muleResize)

pinaColadaImg = Image.open('Photos/pinaColada.png')
pinaColadaResize = pinaColadaImg.resize((150, 100))
pina = ImageTk.PhotoImage(pinaColadaResize)

strawberryImg = Image.open('Photos/strawDaq.png')
strawberryResize = strawberryImg.resize((150, 100))
strawberry = ImageTk.PhotoImage(strawberryResize)

whiteImg = Image.open('Photos/whiteLady.png')
whiteResize = whiteImg.resize((150, 100))
white = ImageTk.PhotoImage(whiteResize)

#-------------------Drink Buttons with images and labels------------------------
arnoldButton = Button(root, text = 'Arnold Palmer', image=arnold, command=Orders.arnold, compound = TOP)
cosmoButton = Button(root, text = 'Cosmopolitan', image=cosmo, command=Orders.cosmo, compound = TOP)
shirleyButton = Button(root, text = 'Shirley Temple', image=shirley, command=Orders.shirley, compound = TOP)
margButton = Button(root, text = 'Margarita', image=marg, command= Orders.marg, compound = TOP)
mocktailButton = Button(root, text = 'Island Mocktail', image=mocktail, command=Orders.mocktail, compound = TOP)
muleButton = Button(root, text = 'Mexican Mule', image=mule, command= Orders.mule, compound = TOP)
pinaButton = Button(root, text = 'Piña Colada', image=pina, command= Orders.pina, compound = TOP)
daqButton = Button(root, text = 'Strawberry Daquiri', image=strawberry, command=Orders.daq, compound = TOP)
whiteButton = Button(root, text = 'White Lady', image=white, command= Orders.white, compound = TOP)


resetButton = Button(root, text= 'Reset the Inventory', command = reset, background='#97a258')
emptySpace = Label(root, background='#97a258')
#----------------Position and post buttons to tkinter window--------------------
emptySpace.grid(row = 16, column = 6)
resetButton.grid(row=20, column=6)


muleButton.grid(row=6, column = 4)
margButton.grid(row=6, column = 6)
cosmoButton.grid(row=6, column = 8)

pinaButton.grid(row=10, column = 4)
daqButton.grid(row=10, column = 6)
whiteButton.grid(row=10, column = 8)

arnoldButton.grid(row=14, column = 4)
shirleyButton.grid(row=14, column = 6)
mocktailButton.grid(row=14, column = 8)



#run the page
root.mainloop()
