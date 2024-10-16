import customtkinter
import random
import time
from PIL import Image

# var

# fenetre

app = customtkinter.CTk()
app.title("Guess it")
app.geometry("685x300")
app._set_appearance_mode("dark") # par defaut

# Dictionnaire (ne pas toucher)

Data = {
    
}


# fonctions

def newGame():
    number = random.randint(1, Data["Difficulté"])
    number = int(number)
    Data["nombre"] = number
    Data["Lifes"] = 3
    coeur1.configure(fg_color="transparent")
    coeur2.configure(fg_color="transparent")
    coeur3.configure(fg_color="transparent")
    print(Data["nombre"])

def entry():
    number = Data["nombre"]
    userInput = int(entrée.get())
    if number > userInput:
        anwser.configure(text="too small")
        Data["Lifes"] = max(0, Data["Lifes"] - 1)
    elif number < userInput:
        anwser.configure(text="too big")
        Data["Lifes"] = max(0, Data["Lifes"] - 1)
    elif number == userInput:
        anwser.configure(text="you win")
    if Data["Lifes"] == 0:
        anwser.configure(text="you loose, the number was " + str(Data["nombre"]))
    UpdateLifes()
    print(Data["Lifes"])

def Theme():
    SwitchValue = switch.get()
    if SwitchValue == True:
        app._set_appearance_mode("dark")
    elif SwitchValue == False:
        app._set_appearance_mode("light")

def Easy():
    Data["Difficulté"] = 10

def Hard():
    Data["Difficulté"]= 50

def Medium():
    Data["Difficulté"]= 25

def UpdateLifes():
    if Data["Lifes"] == 2:
        coeur3.configure(fg_color="grey")
    elif Data["Lifes"] == 1:
        coeur2.configure(fg_color="grey")
    elif Data["Lifes"] == 0:
        coeur1.configure(fg_color="grey")

# boucles

    

# Boutton 1 (new game)

boutton = customtkinter.CTkButton(app, corner_radius=0, text="new game", command=newGame, width=120, height=40)
boutton.place(x=15, y=10)

# Bouton 2 (number pick)

entrée = customtkinter.CTkEntry(app, placeholder_text="number ?", corner_radius=0)
entrée.place(x=225, y=75)

send = customtkinter.CTkButton(app, text="send", command=entry, width=60, height=20, corner_radius=0)
send.place(x=265, y=105)

# anwser 

anwser = customtkinter.CTkLabel(app, corner_radius=0, text="Choose a number")
anwser.place(x=265, y=145)

# Switch

switch = customtkinter.CTkSwitch(app, text="night", command=Theme)
switch.place(x=500, y=170)

# boutton difficulté 1
easy = customtkinter.CTkButton(app, width=30, height=30, corner_radius=0, text="Easy   ", command=Easy)
easy.place(x=10, y=170)

# boutton difficulté 2

hard = customtkinter.CTkButton(app, width=30, height=30, corner_radius=0, text="Hard   ", command=Hard)
hard.place(x=130, y=170)

# boutton difficulté 3

medium = customtkinter.CTkButton(app, width=30, height=30, corner_radius=0, text="Medium   ", command=Medium)
medium.place(x=60, y=170)

# coeur 1
coeur1pic = customtkinter.CTkImage(light_image=Image.open("Heart.png"), size=(50, 50))
coeur1 = customtkinter.CTkLabel(app, image=coeur1pic, text="")
coeur1.place(x=540, y=20)

# coeur 2
coeur2pic = customtkinter.CTkImage(light_image=Image.open("Heart.png"), size=(50, 50))
coeur2 = customtkinter.CTkLabel(app, image=coeur1pic, text="")
coeur2.place(x=480, y=20)

# coeur 3
coeur3pic = customtkinter.CTkImage(light_image=Image.open("Heart.png"), size=(50, 50))
coeur3 = customtkinter.CTkLabel(app, image=coeur1pic, text="")
coeur3.place(x=420, y=20)

# instructions

rules = customtkinter.CTkLabel(app, text="Instuctions: You need first to choose a difficulty and after create a new game, enjoy my first game made with python.")
rules.place(x=20, y=250)

app.mainloop()