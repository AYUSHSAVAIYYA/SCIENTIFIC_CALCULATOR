import tkinter
from tkinter import *

me = Tk()
me.geometry("354x460")
me.resizable(0,0)
me.title("scientific calculater")

lbl = Label(
    me ,
    text =" Label " ,
    anchor = SE ,
)
lbl.pack(expand= True , fill = "both", )
btnrow1 = Frame(me)
btnrow1.pack(expand = True , fill = "both" ,)

btnrow2 = Frame(me)
btnrow2.pack(expand= True , fill = "both",)

btnrow3 = Frame (me)
btnrow3.pack(expand = True , fill = "both",)

btnrow4 = Frame (me)
btnrow4.pack(expand = True , fill = "both",)

btn1 = Button(
    btnrow1 ,
    text ="1",
    font =("Verdana" , 22)
)
btn1.pack(side = LEFT, expand = True, fill = "both",)

btn2 = Button(
    btnrow1 ,
    text ="2",
    font =("Verdana" , 22)
)
btn2.pack(side = LEFT, expand = True, fill = "both",)

btn3 = Button(
    btnrow1 ,
    text ="3",
    font =("Verdana" , 22)
)
btn3.pack(side = LEFT, expand = True, fill = "both",)

btn4 = Button(
    btnrow1 ,
    text ="+",
    font =("Verdana" , 22)
)
btn4.pack(side = LEFT, expand = True, fill = "both",)

btn5 = Button(
    btnrow2 ,
    text ="4",
    font =("Verdana" , 22)
)
btn5.pack(side = LEFT, expand = True, fill = "both",)

btn6 = Button(
    btnrow2 ,
    text ="5",
    font =("Verdana" , 22)
)
btn6.pack(side = LEFT, expand = True, fill = "both",)

btn7 = Button(
    btnrow2  ,
    text ="6",
    font =("Verdana" , 22)
)
btn7.pack(side = LEFT, expand = True, fill = "both",)

btn8 = Button(
    btnrow2  ,
    text ="-",
    font =("Verdana" , 22)
)
btn8.pack(side = LEFT, expand = True, fill = "both",)

btn9 = Button(
    btnrow3 ,
    text ="7",
    font =("Verdana" , 22)
)
btn9.pack(side = LEFT, expand = True, fill = "both",)

btn10 = Button(
    btnrow3  ,
    text ="8",
    font =("Verdana" , 22)
)
btn10.pack(side = LEFT, expand = True, fill = "both",)

btn11 = Button(
    btnrow3 ,
    text ="9",
    font =("Verdana" , 22)
)
btn11.pack(side = LEFT, expand = True, fill = "both",)

btn12 = Button(
    btnrow3  ,
    text ="*",
    font =("Verdana" , 22)
)
btn12.pack(side = LEFT, expand = True, fill = "both",)

btn13 = Button(
    btnrow3  ,
    text ="=",
    font =("Verdana" , 22)
)
btn13.pack(side = LEFT, expand = True, fill = "both",)
me.mainloop()