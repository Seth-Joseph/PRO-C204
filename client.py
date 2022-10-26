import socket
from threading import Thread
from tkinter import *
import random
from PIL import ImageTk, Image

SERVER = None
PORT = None
IP_ADDRESS = None

canvas1 = None
playerName = None
nameEntry = None
nameWindow = None
screen_width = None
screen_height = None

def saveName():
    global SERVER
    global playerName 
    global nameWindow
    global nameEntry

    playerName = nameEntry.get()
    nameEntry.delete(0, END)
    nameWindow.destroy()

    SERVER.send(playerName.encode())

def askPlayerName():
    global playerName
    global nameEntry
    global nameWindow
    global canvas1 
    global screen_width
    global screen_height
    
    nameWindow = Tk()
    nameWindow.title("Tambola Family Game")
    nameWindow.attributes('-fullscreen',True)
    
    screen_width = nameWindow.winfo_screenwidth()
    screen_height = nameWindow.winfo_screenheight()

    bg = ImageTk.PhotoImage(file = "./assets/logo.png")

    canvas1 = Canvas( nameWindow, width = 500,height = 500)
    canvas1.pack(fill = "both", expand = True)
    # Display image
    canvas1.create_image( 0, 0, image = bg, anchor = "nw")
    canvas1.create_text( screen_width/2, screen_height/4 +110, text = "Enter Name", font=("Comic Sans MS",30), fill="white")

    nameEntry = Entry(nameWindow, width=15, justify='center', font=('Comic Sans MS', 25), bd=0, bg='white')
    nameEntry.place(x = screen_width/3+80, y=screen_height/2-20)

    button = Button(nameWindow, text="Save", font=("Comic Sans MS", 25),width=4, height=1,command=saveName, bg="#E38D65", fg='#FFF',bd=0)
    button.place(x = screen_width/2-50, y=screen_height/2 + 50)

    nameWindow.resizable(True, True)
    nameWindow.mainloop()

def recivedMsg():
    pass

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    PORT = 6000
    IP_ADDRESS = '127.0.0.1'

    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS,PORT))

    thread = Thread(target=recivedMsg)
    thread.start()

    askPlayerName()

setup()

 