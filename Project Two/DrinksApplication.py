from tkinter import *
from PIL import Image, ImageTk

#------------------------------set tKinter window-------------------------------
root = Tk()
root.geometry("750x500")
root.title('Database Access Window')
root['background'] = '#6495ED'


#-------------------text labels for sections on tKinter window------------------
welcomeTitle = Label(text = "Welcome to the Bar!\n\n", background='#6495ED', font = 'Helvetica 20 bold')
welcomeTitle.grid(row = 0, column = 6)

instructions = Label(text = "please choose the drink you are serving to update the inventory", background='#6495ED', font = 'Helvetica 18')
instructions.grid(row=1, column = 6)

alcoholicTitle = Label(text = "The popular alcoholic Orders:", background='#6495ED', font = 'Helvetica 18 bold')
alcoholicTitle.grid(row = 5, column = 6)

virginTitle = Label(text = "The popular virgin Orders:", background='#6495ED', font = 'Helvetica 18 bold')
virginTitle.grid(row = 13, column = 6)

#---------class to order drinks, update inventory, and add to order log---------
class Orders:
    def cosmo():
        return
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
cosmoButton = Button(root, text = 'Cosmopolitan', image=cosmo, command= lambda:Orders.cosmo, compound = TOP)
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
