from cProfile import label
from cgitb import text
from email import message
from tkinter import *
from tkinter import messagebox
from tkinter import font
from turtle import Screen, bgcolor, exitonclick, screensize
import tkinter as tk




currentFunds=10000

def oduzmi(suma):
    global currentFunds
    currentFunds-=suma
    label9.configure(text = "Trenutno stanje = " + str(currentFunds))
    


currentFunds = 10000
newsum2 = 0

def oduzmi(suma):
    global currentFunds
    currentFunds -=suma
    label9.configure(text = "Trenutno stanje = " + str(currentFunds))
    print(currentFunds)

def login():
    global currentFunds
    pin=entry1.get()
    if (pin!="1234"):
     messagebox.showerror(title=None, message="Pogresan pin!")
    else:
        messagebox.showinfo( title=None, message="Tacan pin!")
        np=Tk()
        np.geometry("1000x720")
        np.resizable(False, False)
        np.title("")
               
        np.columnconfigure(0, weight = 1)
        np.columnconfigure(1, weight = 1)
        np.columnconfigure(2, weight = 4)
        np.columnconfigure(3, weight = 1)
        np.columnconfigure(4, weight = 1)

        welcomeLabel = Label(np,text="Pregled stanja i transakcije",font=("Times New Roman",30,'bold'), anchor="center")
        welcomeLabel.grid(column=2, row=0, sticky=N, pady=10)

        button1 = Button(np,text="",command=lambda:oduzmi(100),height=2,width=5,bd=2,bg='#E3CF57')
        button1.grid(column=0, row=1, pady=40)
        sum1 = Label(np,text="100",font=("Calibri",16,'bold'))
        sum1.grid(column=1, row=1, sticky="EW", pady=40)

        button2 = Button(np,text="",command=lambda:oduzmi(200),height=2,width=5,bd=2,bg='#E3CF57')
        button2.grid(column=0, row=2, pady=40)
        sum2 = Label(np,text="200",font=("Calibri",16,'bold'))
        sum2.grid(column=1, row=2, sticky="EW", pady=40)

        button3 = Button(np,text="",command=lambda:oduzmi(250),height=2,width=5,bd=2,bg='#E3CF57')
        button3.grid(column=0, row=3, pady=40)
        sum3 = Label(np,text="250",font=("Calibri",16,'bold'))
        sum3.grid(column=1, row=3, sticky="EW", pady=40)

        button4 = Button(np,text="",command=lambda:oduzmi(500),height=2,width=5,bd=2,bg='#E3CF57')
        button4.grid(column=0, row=4, pady=40)
        sum4 = Label(np,text="500",font=("Calibri",16,'bold'))
        sum4.grid(column=1, row=4, sticky="EW", pady=40)

        button5 = Button(np,text="",command=lambda:oduzmi(1000),height=2,width=5,bd=2,bg='#E3CF57')
        button5.grid(column=4, row=1, pady=40, padx=30)
        sum5 = Label(np,text="1000",font=("Calibri",16,'bold'))
        sum5.grid(column=3, row=1, sticky="EW", pady=40, padx=30)

        button6 = Button(np,text="",command=lambda:oduzmi(2000),height=2,width=5,bd=2,bg='#E3CF57')
        button6.grid(column=4, row=2, pady=40, padx=30)
        sum6 = Label(np,text="2000",font=("Calibri",16,'bold'))
        sum6.grid(column=3, row=2, sticky="EW", pady=40, padx=30)

        button7 = Button(np,text="",command=lambda:oduzmi(5000),height=2,width=5,bd=2,bg='#E3CF57')
        button7.grid(column=4, row=3, pady=40, padx=30)
        sum7 = Label(np,text="5000",font=("Calibri",16,'bold'))
        sum7.grid(column=3, row=3, sticky="EW", pady=40, padx=30)

        button8 = Button(np,text="",command=lambda:newtab(),height=2,width=5,bd=2,bg='#E3CF57')
        button8.grid(column=4, row=4, pady=40, padx=30)
        sum8 = Label(np,text="Unesite\nSvoju\nSumu",font=("Calibri",16,'bold'))
        sum8.grid(column=3, row=4, sticky="EW", pady=40, padx=30)
           
        global label9

        global label9
        label9 = Label(np,text="Trenutno stanje = " + str(currentFunds) ,font=("Calibri",16,'bold'),bg="#FFB90F")
        label9.grid(column=0, row=5, sticky="EW", pady=40, columnspan=2)
        currentFunds=10000
        

        #np.mainloop()
        
def newtab():
    global newsum2
    screen=Tk()
    screen.geometry("250x250")
    screen.resizable(False, False)
    Label(screen, text="Unesite sumu:",font=("Calibri",20,'bold'),anchor="center").pack(pady=5)
    
    global newsum

    newsum=Entry(screen,bd=5)
    newsum.anchor("center")
    newsum.pack(pady=15)
    newsum.focus


    Button(screen,text="Potvrdi",command =lambda:[oduzmiiiii(newsum2), closeScreen()],height=2,width=10,bd=2, anchor="center",font=("Calibri",16,'bold'),bg="#7FFF00").pack(pady=20)

    def oduzmiiiii(sumaa):
        sumaa = int(newsum.get())
        global currentFunds
        if (sumaa>0):
         currentFunds -=sumaa
        label9.configure(text = "Trenutno stanje = " + str(currentFunds))
        print(currentFunds)

    def stampaj():
        print(newsum2)

    def closeScreen():
        screen.destroy()

def glavni_prozor():

    screen=Tk()
    screen.geometry("1000x500")
    screen.resizable(False, False)
    screen.title("Bankomat")

    Label(text="Dobrodosli!",font=("Calibri",30,'bold'),anchor="center").pack(pady=40)
    Label(text="Ime: KORISNIK",font=("Calibri",15,'bold'), anchor="center").pack(pady=20)
    Label(text="PIN:",font=("Calibri",15,'bold'), anchor="center").pack(pady=15)

    global entry1
    entry1=Entry(screen,bd=5,show="*")
    entry1.anchor("center")
    entry1.pack(pady=15)
    entry1.focus()
     
    
    Button(screen,text="Login",bg="#7FFF00",command=lambda:login(),height=2,width=10,bd=2, anchor="center",font=("Calibri",12,'bold')).pack(pady=50)
    Button(screen,text="Izlaz",bg="#FF4040",command=screen.destroy,height=1,width=8,bd=2,font=("Calibri",12,'bold')).pack(side=RIGHT)
    screen.mainloop()

#otvaranje_svega
glavni_prozor()
 
