from tkinter import *
top=Tk()
top.title("calculator")
top.wm_iconbitmap("calculator.ico")
top.geometry("800x900")
top.maxsize(670,500)
top.minsize(670,500)

def click(event):
    global scvalue
    text=event.widget.cget("text")     #cget() function used to   how to get a text from  a button widget.
    #print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(cal_screen.get())   #eval() function evaluate the integer like --   5*3 gives the 15
        scvalue.set(value)
        cal_screen.update()
    elif text=="c":
        scvalue.set("")
        cal_screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        cal_screen.update()

scvalue=StringVar()
scvalue.set("")
cal_screen=Entry(top,textvar=scvalue,fon="lucida 35 bold",bg="gray")
cal_screen.pack(fill=X,pady=13,padx=15)

f=Frame(top, bg="skyblue")
b=Button(f,text="9",font="lucida 20 bold",padx=20,pady=4)
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="8",font="lucida 20 bold",padx=20,pady=4)
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="7",font="lucida 20 bold",padx=20,pady=4)
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(top, bg="skyblue")
b=Button(f,text="6",font="lucida 20 bold",padx=20,pady=4)
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="5",font="lucida 20 bold",padx=20,pady=4)
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="4",font="lucida 20 bold",padx=20,pady=4)
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(top, bg="skyblue")
b=Button(f,text="3",font="lucida 20 bold",padx=20,pady=4)
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="2",font="lucida 20 bold",padx=20,pady=4)
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="1",font="lucida 20 bold",padx=20,pady=4)
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(top, bg="skyblue")
b=Button(f,text="0",font="lucida 20 bold",padx=20,pady=4)
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="00",font="lucida 20 bold",padx=14.5,pady=4)
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text=".",font="lucida 20 bold",padx=20,pady=4)
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(top, bg="skyblue")
b=Button(f,text="+",font="lucida 20 bold",padx=20,pady=4)
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="-",font="lucida 20 bold",padx=20,pady=4)
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="x",font="lucida 20 bold",padx=20,pady=4)
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
f.pack()


f=Frame(top, bg="skyblue")
b=Button(f,text="c",font="lucida 20 bold",padx=20,pady=4)
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="=",font="lucida 20 bold",padx=20,pady=4)
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="/",font="lucida 20 bold",padx=20,pady=4)
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
f.pack()













top.mainloop()