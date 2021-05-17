from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk,Image
import pandas as pd

#Widnow
root_window = Tk() 
root_window.title("Kalkulator ustawien") 
root_window.geometry("500x500")

#Create Frames
topFrame = Frame(root_window).grid()
bottomFrame = Frame(root_window).grid(row = 2)

#Create Label and Entry for lenght
Label(topFrame, text = "L:").grid(row = 0, column = 0)
LenghtEntry = Entry(topFrame)
LenghtEntry.grid(row = 0, column = 1)

#Create Label and Entry for width
Label(topFrame, text = "W:").grid(row = 1, column = 0)
WidthEntry = Entry(topFrame)
WidthEntry.grid(row = 1, column = 1)

#Create Label and Entry for height
Label(topFrame, text = "H:").grid(row = 2, column = 0)
HeightEntry = Entry(topFrame)
HeightEntry.grid(row = 2, column = 1)

#Create combobox
Label(topFrame, text = "Fala:").grid(row = 3, column = 0)
combo = Combobox(topFrame)
combo['values']=('BC', 'B', 'C', 'E', 'BE')
combo.set(combo['values'][0])
combo.grid(row = 3, column = 1)

#create checkbutton
chk_state = IntVar()
chk = Checkbutton(topFrame, text="Górne klapy (FEFCO 201)", variable=chk_state)
chk_state.set(0)
chk.grid(column=2, row=3)

def klapy():
    f = combo['values'].index(combo.get())
    k = str(cena(combo['values'].index(combo.get())))
    Label(bottomFrame, text=k).grid(column=2)

def biga():
    i = combo['values'].index(combo.get())
    if i == 0:
        return 10
    elif i == 3:
        return 3
    else:
        return 5
    
def cena(x):
    if x == 0:
        return 1.63
    elif x == 1:
        return 1.23
    elif x == 2:
        return 1.25
    elif x == 3:
        return 1.12
    else:
        return 1.6
    
def forx():
    fx = 2*(float(LenghtEntry.get()))+2*(float(WidthEntry.get()))+4*biga()+30
    return fx

def fory():
    if chk_state.get()==1:    #warunek dla pudeł z klapami (fefco 201)
        fy = float(HeightEntry.get())+float(WidthEntry.get())+2*biga()
    else:
        fy = float(HeightEntry.get())+0.5*float(WidthEntry.get())+2*biga()
    return fy

def formatka():
    try:
        wycena = forx()*fory()*0.001*cena(combo['values'].index(combo.get()))
        tf = 'Wymiar formatki: '+ str(forx()) +'x' + str(fory()) + '. \nCena za jedno opakowanie: ' + str(wycena)[:4]
    except ValueError:
        tf = 'Podaj wymiary opakowania i grubość fali  ' 
    Label(bottomFrame, text=tf).grid(column=2)
    
def ustmasz():
    n10=forx()-100
    n20='-'
    b10=float(WidthEntry.get())+biga()
    b20=b10+float(LenghtEntry.get())+biga()
    b30=b20+float(WidthEntry.get())+biga()
    b40=b30+float(LenghtEntry.get())+biga()
    n11=0
    n21=0
    b11=0
    b21=0
    b31=0
    b41=0
    d = {'N1': [n10,n11], 'N2': [n20,n21], 'B1':[b10,b11], 'B2':[b20,b21], 'B3':[b30,b31]}
    df = pd.DataFrame(data=d, index=['C1','C2'])
    Label(bottomFrame, text=df).grid(column=2) 
   
#create new window
def open():
    global my_img
    ust=Toplevel()
    ust.title('Podgląd opakowań')
    ust.geometry("500x350")
    if chk_state.get()==1:
        Label(ust, text='Opakowanie z górnymi klapami - FEFCO 201').pack()
        my_img = ImageTk.PhotoImage(Image.open("FEFCO201.jpg"))
    else:
        Label(ust, text='Opakowanie bez górnych klap - FEFCO 200').pack()
        my_img = ImageTk.PhotoImage(Image.open("FEFCO200.jpg"))
    my_label = Label(ust, image=my_img).pack()
    Button(ust, text='Zamknij', command=ust.destroy).pack()
            
#Create Buttons
Button(bottomFrame, text = "Oblicz", command = ustmasz).grid(column=1)

Button(bottomFrame, text = "Format i cena", command = formatka).grid(column=1)

Button(bottomFrame, text = "Podgląd", command = open).grid(column=1)
root_window.mainloop()
