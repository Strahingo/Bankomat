from cProfile import label
from cgitb import text
from email import message
from tkinter import *
from tkinter import messagebox
from tkinter import font
from turtle import Screen, bgcolor, exitonclick, screensize
from PIL import Image,ImageTk
from json import *

currentFunds=10000
newsum2 = 0

def main_window():

    global mainscreen

    mainscreen=Tk()
    mainscreen.geometry("1000x500")
    mainscreen.resizable(False, False)
    mainscreen.title("Bankomat")

    Label(text="Dobrodosli!",font=("Calibri",30,'bold'),anchor="center").pack(pady=40)
    Label(text="Ime: KORISNIK",font=("Calibri",15,'bold'), anchor="center").pack(pady=20)
    Label(text="PIN:",font=("Calibri",15,'bold'), anchor="center").pack(pady=15)

    global entry1
    entry1=Entry(mainscreen,bd=5,show="*")
    entry1.anchor("center")
    entry1.pack(pady=15)
    entry1.focus()
     
    slika=PhotoImage(file="slicica.png")
    Label(mainscreen,image=slika,width=128,height=128).place(x=225,y=150)
    
    Button(mainscreen,text="Login",bg="#7FFF00",command=lambda:login(),height=2,width=10,bd=2, anchor="center",font=("Calibri",12,'bold')).pack(pady=50)
    Button(mainscreen,text="Izlaz",bg="#FF4040",command=mainscreen.destroy,height=1,width=8,bd=2,font=("Calibri",12,'bold')).pack(side=RIGHT)


    mainscreen.mainloop()

def login():
    def closeScreen():
        mainscreen.destroy()
    global currentFunds
    pin=entry1.get()
    if (pin!="1234"):
     messagebox.showerror(title=None, message="Pogresan pin!")
    else:
        messagebox.showinfo( title=None, message="Tacan pin!")
        closeScreen()
        choice()   

def choice():
    window=Tk()
    window.geometry("500x200")
    window.resizable(False, False)
    window.title("")
    Button(window,text="Uplata",bg="#7FFF00",command=lambda:[deposit()],height=1,width=15,bd=2, anchor="center",font=("Calibri",12,'bold')).pack(pady=10)
    Button(window,text="Isplata",bg="#FF4040",command=lambda:[withdraw(),],height=1,width=15,bd=2,font=("Calibri",12,'bold')).pack(pady=5)    


def deposit():
    nw=Tk()
    nw.geometry("1000x720")
    nw.resizable(False, False)
    nw.title("")
               
    nw.columnconfigure(0, weight = 1)
    nw.columnconfigure(1, weight = 1)
    nw.columnconfigure(2, weight = 4)
    nw.columnconfigure(3, weight = 1)
    nw.columnconfigure(4, weight = 1)

    welcomeLabel = Label(nw,text="Uplata novca",font=("Times New Roman",30,'bold'), anchor="center")
    welcomeLabel.grid(column=2, row=0, sticky=N, pady=10)

    button1 = Button(nw,text="",command=lambda:addfunds(100),height=2,width=5,bd=2,bg='#E3CF57')
    button1.grid(column=0, row=1, pady=40)
    sum1 = Label(nw,text="100",font=("Calibri",16,'bold'))
    sum1.grid(column=1, row=1, sticky="EW", pady=40)

    button2 = Button(nw,text="",command=lambda:addfunds(200),height=2,width=5,bd=2,bg='#E3CF57')
    button2.grid(column=0, row=2, pady=40)
    sum2 = Label(nw,text="200",font=("Calibri",16,'bold'))
    sum2.grid(column=1, row=2, sticky="EW", pady=40)

    button3 = Button(nw,text="",command=lambda:addfunds(250),height=2,width=5,bd=2,bg='#E3CF57')
    button3.grid(column=0, row=3, pady=40)
    sum3 = Label(nw,text="250",font=("Calibri",16,'bold'))
    sum3.grid(column=1, row=3, sticky="EW", pady=40)

    button4 = Button(nw,text="",command=lambda:addfunds(500),height=2,width=5,bd=2,bg='#E3CF57')
    button4.grid(column=0, row=4, pady=40)
    sum4 = Label(nw,text="500",font=("Calibri",16,'bold'))
    sum4.grid(column=1, row=4, sticky="EW", pady=40)

    button5 = Button(nw,text="",command=lambda:addfunds(1000),height=2,width=5,bd=2,bg='#E3CF57')
    button5.grid(column=4, row=1, pady=40, padx=30)
    sum5 = Label(nw,text="1000",font=("Calibri",16,'bold'))
    sum5.grid(column=3, row=1, sticky="EW", pady=40, padx=30)

    button6 = Button(nw,text="",command=lambda:addfunds(2000),height=2,width=5,bd=2,bg='#E3CF57')
    button6.grid(column=4, row=2, pady=40, padx=30)
    sum6 = Label(nw,text="2000",font=("Calibri",16,'bold'))
    sum6.grid(column=3, row=2, sticky="EW", pady=40, padx=30)

    button7 = Button(nw,text="",command=lambda:addfunds(5000),height=2,width=5,bd=2,bg='#E3CF57')
    button7.grid(column=4, row=3, pady=40, padx=30)
    sum7 = Label(nw,text="5000",font=("Calibri",16,'bold'))
    sum7.grid(column=3, row=3, sticky="EW", pady=40, padx=30)

    button8 = Button(nw,text="",command=lambda:customsumm(),height=2,width=5,bd=2,bg='#E3CF57')
    button8.grid(column=4, row=4, pady=40, padx=30)
    sum8 = Label(nw,text="Unesite\nSvoju\nSumu",font=("Calibri",16,'bold'))
    sum8.grid(column=3, row=4, sticky="EW", pady=40, padx=30)
           
    global label9
    label9 = Label(nw,text="Trenutno stanje = " + str(currentFunds) ,font=("Calibri",16,'bold'),bg="#FFB90F")
    label9.grid(column=0, row=5, sticky="EW", pady=40, columnspan=2)     

    

def addfunds(sum):
    global currentFunds
    ##if currentFunds > 0 and currentFunds>=sum:
    currentFunds+=sum
    label9.configure(text = "Trenutno stanje = " + str(currentFunds))
    quest()

     

def customsumm():
    global newsum2
    screen=Tk()
    screen.geometry("250x250")
    screen.resizable(False, False)
    Label(screen, text="Unesite sumu:",font=("Calibri",20,'bold'),anchor="center").pack(pady=5)
    
    global newsumEntry

    newsumEntry=Entry(screen,bd=5)
    newsumEntry.anchor("center")
    newsumEntry.pack(pady=15)
    newsumEntry.focus


    Button(screen,text="Potvrdi",command =lambda:[subrtactnew(newsum2), closeScreen()],height=2,width=10,bd=2, anchor="center",font=("Calibri",16,'bold'),bg="#7FFF00").pack(pady=20)

    def subrtactnew(sum2):
        sum2 = int(newsumEntry.get())
        global currentFunds
        if currentFunds > 0 and currentFunds>=sum2:
            if sum2%500!=0:
                messagebox.showerror(title=None, message="Suma mora biti deljiva sa 500")
            elif (sum2>=0):
                currentFunds +=sum2
                label9.configure(text = "Trenutno stanje = " + str(currentFunds))
                quest()
    def closeScreen():
        screen.destroy()

def withdraw():
    nw=Tk()
    nw.geometry("1000x720")
    nw.resizable(False, False)
    nw.title("")
               
    nw.columnconfigure(0, weight = 1)
    nw.columnconfigure(1, weight = 1)
    nw.columnconfigure(2, weight = 4)
    nw.columnconfigure(3, weight = 1)
    nw.columnconfigure(4, weight = 1)

    welcomeLabel = Label(nw,text="Podizanje novca",font=("Times New Roman",30,'bold'), anchor="center")
    welcomeLabel.grid(column=2, row=0, sticky=N, pady=10)

    button1 = Button(nw,text="",command=lambda:subrtact(100),height=2,width=5,bd=2,bg='#E3CF57')
    button1.grid(column=0, row=1, pady=40)
    sum1 = Label(nw,text="100",font=("Calibri",16,'bold'))
    sum1.grid(column=1, row=1, sticky="EW", pady=40)

    button2 = Button(nw,text="",command=lambda:subrtact(200),height=2,width=5,bd=2,bg='#E3CF57')
    button2.grid(column=0, row=2, pady=40)
    sum2 = Label(nw,text="200",font=("Calibri",16,'bold'))
    sum2.grid(column=1, row=2, sticky="EW", pady=40)

    button3 = Button(nw,text="",command=lambda:subrtact(250),height=2,width=5,bd=2,bg='#E3CF57')
    button3.grid(column=0, row=3, pady=40)
    sum3 = Label(nw,text="250",font=("Calibri",16,'bold'))
    sum3.grid(column=1, row=3, sticky="EW", pady=40)

    button4 = Button(nw,text="",command=lambda:subrtact(500),height=2,width=5,bd=2,bg='#E3CF57')
    button4.grid(column=0, row=4, pady=40)
    sum4 = Label(nw,text="500",font=("Calibri",16,'bold'))
    sum4.grid(column=1, row=4, sticky="EW", pady=40)

    button5 = Button(nw,text="",command=lambda:subrtact(1000),height=2,width=5,bd=2,bg='#E3CF57')
    button5.grid(column=4, row=1, pady=40, padx=30)
    sum5 = Label(nw,text="1000",font=("Calibri",16,'bold'))
    sum5.grid(column=3, row=1, sticky="EW", pady=40, padx=30)

    button6 = Button(nw,text="",command=lambda:subrtact(2000),height=2,width=5,bd=2,bg='#E3CF57')
    button6.grid(column=4, row=2, pady=40, padx=30)
    sum6 = Label(nw,text="2000",font=("Calibri",16,'bold'))
    sum6.grid(column=3, row=2, sticky="EW", pady=40, padx=30)

    button7 = Button(nw,text="",command=lambda:subrtact(5000),height=2,width=5,bd=2,bg='#E3CF57')
    button7.grid(column=4, row=3, pady=40, padx=30)
    sum7 = Label(nw,text="5000",font=("Calibri",16,'bold'))
    sum7.grid(column=3, row=3, sticky="EW", pady=40, padx=30)

    button8 = Button(nw,text="",command=lambda:customsum(),height=2,width=5,bd=2,bg='#E3CF57')
    button8.grid(column=4, row=4, pady=40, padx=30)
    sum8 = Label(nw,text="Unesite\nSvoju\nSumu",font=("Calibri",16,'bold'))
    sum8.grid(column=3, row=4, sticky="EW", pady=40, padx=30)
           
    global label9
    label9 = Label(nw,text="Trenutno stanje = " + str(currentFunds) ,font=("Calibri",16,'bold'),bg="#FFB90F")
    label9.grid(column=0, row=5, sticky="EW", pady=40, columnspan=2)



def subrtact(sum):
    global currentFunds
    if currentFunds > 0 and currentFunds>=sum:
        currentFunds-=sum
        label9.configure(text = "Trenutno stanje = " + str(currentFunds))
        quest()
    else:
        messagebox.showerror(title=None, message="Nedovoljno sredstava!")

def customsum():
    global newsum2
    screen=Tk()
    screen.geometry("250x250")
    screen.resizable(False, False)
    Label(screen, text="Unesite sumu:",font=("Calibri",20,'bold'),anchor="center").pack(pady=5)
    
    global newsumEntry

    newsumEntry=Entry(screen,bd=5)
    newsumEntry.anchor("center")
    newsumEntry.pack(pady=15)
    newsumEntry.focus


    Button(screen,text="Potvrdi",command =lambda:[subrtactnew(newsum2), closeScreen()],height=2,width=10,bd=2, anchor="center",font=("Calibri",16,'bold'),bg="#7FFF00").pack(pady=20)

    def subrtactnew(sum2):
        sum2 = int(newsumEntry.get())
        global currentFunds
        if currentFunds > 0 and currentFunds>=sum2:
            if sum2%500!=0:
                messagebox.showerror(title=None, message="Suma mora biti deljiva sa 500")
            elif (sum2>=0):
                currentFunds -=sum2
                label9.configure(text = "Trenutno stanje = " + str(currentFunds))
                quest()
        else:
            messagebox.showerror(title=None, message="Nedovoljno sredstava!")

    def closeScreen():
        screen.destroy()


       

def quest():
    global q
    q=Tk()
    q.geometry("500x200")
    q.resizable(False, False)
    q.title("")
    Label(q,text="Da li zelite racun?",font=("Times New Roman",30,'bold'), anchor="center").pack(pady=10)
    Button(q,text="DA",bg="#7FFF00",command=lambda:[receipt(), q.destroy()],height=1,width=10,bd=2, anchor="center",font=("Calibri",12,'bold')).pack(pady=10)
    Button(q,text="NE",bg="#FF4040",command=q.destroy,height=1,width=8,bd=2,font=("Calibri",12,'bold')).pack(pady=5)

def receipt():
    nb=Tk()
    nb.geometry("500x200")
    nb.resizable(False, False)
    nb.title("Novo stanje racuna")
    newBalanceLabel = Label(nb,text="Novo stanje racuna je: " + str(currentFunds),font=("Times New Roman",30,'bold'), anchor="center").pack(pady=20)
    Button(nb,text="Izlaz",bg="#FF4040",command=nb.destroy,height=1,width=8,bd=2,font=("Calibri",12,'bold')).pack(pady=25)





main_window()