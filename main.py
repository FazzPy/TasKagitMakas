import random
import time
from tkinter import *

root = Tk()
root.geometry("500x500+450+100")
root.title("Taş Kağıt Makas v0.1")
color="#C500FF"
background = Label(width=500, height=500, bg=color)
background.place(x=0, y=0)
root.iconbitmap("logo.ico")
root.resizable(width=False, height=False)

list1 = ["taş", "kağıt","makas"]

skorsiz = 0

skorrakip = 0

def Rock():
    global skorrakip
    global skorsiz
    v = random.choice(list1)
    if v == "taş":
        label3["text"] = v
        label4["text"] = "Kazanan : Berabere"
    elif v == "kağıt":
        label3["text"] = v
        label4["text"] = "Kazanan : Rakip"
        skorrakip = skorrakip+1
        label6["text"] = "Rakip : {0}".format(skorrakip)
    elif v == "makas":
        label3["text"] = v
        label4["text"] = "Kazanan : Siz"
        skorsiz = skorsiz+1
        label5["text"]="Siz : {0}".format(skorsiz)

def Paper():
    global skorrakip
    global skorsiz
    v = random.choice(list1)
    if v == "kağıt":
        label3["text"] = v
        label4["text"] = "Kazanan : Berabere"
    elif v == "makas":
        label3["text"] = v
        label4["text"] = "Kazanan : Rakip"
        skorrakip = skorrakip+1
        label6["text"] = "Rakip : {0}".format(skorrakip)
    elif v == "taş":
        label3["text"] = v
        label4["text"] = "Kazanan : Siz"
        skorsiz = skorsiz+1
        label5["text"]="Siz : {0}".format(skorsiz)

def Scissors():
    global skorrakip
    global skorsiz
    v = random.choice(list1)
    if v == "makas":
        label3["text"] = v
        label4["text"] = "Kazanan : Berabere"
    elif v == "taş":
        label3["text"] = v
        label4["text"] = "Kazanan : Rakip"
        skorrakip = skorrakip+1
        label6["text"] = "Rakip : {0}".format(skorrakip)
    elif v == "kağıt":
        label3["text"] = v
        label4["text"] = "Kazanan : Siz"
        skorsiz = skorsiz+1
        label5["text"]="Siz : {0}".format(skorsiz)


def Again():
    global skorrakip
    global skorsiz
    skorrakip = 0
    skorsiz = 0
    label3["text"] = "Seçiyor..."
    label4["text"] = "Kazanan : "
    label5["text"] = "Siz : 0"
    label6["text"] = "Rakip : 0"





label1 = Label(text="Taş Kağıt Makas", bg=color, font="Arial 24")
label1.place(x=130, y=10)

label2 = Label(bg="Black", width=1000, height=1)
label2.place(x=0, y=225)

label3 = Label(text="Rakip", bg=color, font="Arial 24", fg="Yellow")
label3.place(x=200, y=60)

label3 = Label(text="Seçiyor...", bg=color, font="Arial 24", fg="#00FFE0")
label3.place(x=200, y=110)

label4 = Label(text="Kazanan : ", bg=color, font="Arial 24", fg="#36FF00")
label4.place(x=175, y=214)

label5 = Label(text="Siz : 0", bg=color, font="Arial 12", fg="blue")
label5.place(x=10, y=460)

label6 = Label(text="Rakip : 0", bg=color, font="Arial 12", fg="blue")
label6.place(x=420, y=460)

buton0 = Button(text="Tekar Başla", bg="white", fg="black", font="Arial 18", command=Again)
buton0.place(x=175, y=265)

buton1 = Button(text="Taş", bg="yellow", fg="black", font="Arial 32", command=Rock)
buton1.place(x=30, y=330)

buton2 = Button(text="Kağıt", bg="yellow", fg="black", font="Arial 32", command=Paper)
buton2.place(x=150, y=330)

buton3 = Button(text="Makas", bg="yellow", fg="black", font="Arial 32", command=Scissors)
buton3.place(x=300, y=330)



root.mainloop()
