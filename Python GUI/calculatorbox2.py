import tkinter as t
from tkinter import ttk
import math
f= t.Tk()
f.geometry('400x550')
f.resizable(width=0,height=0)
f.command()
t.Label(f,text="Standard",background='yellow',font='Helvetica 15 ' ,foreground="black").place(x=20,y=20)
f.title("Calculator")
def cal(a):
    l=len(ent.get())
    if a in ["CE","OFF"]:
        ent.config(state="normal")
        if a=='CE':
            ent.delete(0,l+1)
            ent.insert(0,"0")
        else:
            ent.insert(0,"")
    elif a in ["0","1","2","3","4","5","6","7","8",'9']:
        ent.config(state="normal")
        ent.insert(0,a)
    ent.config(state="disabled")
ent=t.Entry(f,width=40,foreground='black',background='grey51',font='arial 12 bold',justify="right")
ent.place(x=20,y=50)
t.Button(f,text="%",width=10,height=3, foreground='blue', background='yellow',activebackground='hot pink',command=lambda:cal("%")).place(x=20, y=160)
t.Button(f,text="CE",width=10,height=3, foreground='blue', background='yellow',activebackground='hot pink',command=lambda:cal("CE")).place(x=110, y=160)
t.Button(f,text="OFF",width=10,height=3, foreground='blue', background='yellow',activebackground='hot pink',command=lambda:cal("OFF")).place(x=200, y=160)
t.Button(f,text="⌫",width=10,height=3, foreground='blue', background='yellow',activebackground='hot pink',command=lambda:cal("⌫")).place(x=300, y=160)
t.Button(f,text="1/x",width=10,height=3, foreground='blue', background='yellow',activebackground='hot pink',command=lambda:cal("1/x")).place(x=20, y=220)
t.Button(f,text="x2",width=10,height=3, foreground='blue', background='yellow',activebackground='hot pink',command=lambda:cal("x2")).place(x=110, y=220)
t.Button(f,text="2 root x",width=10,height=3, foreground='blue', background='yellow',activebackground='hot pink',command=lambda:cal("2 root x")).place(x=200, y=220)
t.Button(f,text="/",width=10,height=3, foreground='blue', background='yellow',activebackground='hot pink',command=lambda:cal("/")).place(x=300, y=220)
t.Button(f,text="7",width=10,height=3, foreground='blue', background='cyan',activebackground='yellow',command=lambda:cal("7")).place(x=20, y=280)
t.Button(f,text="8",width=10,height=3, foreground='blue', background='cyan',activebackground='yellow',command=lambda:cal("8")).place(x=110, y=280)
t.Button(f,text="9",width=10,height=3, foreground='blue', background='cyan',activebackground='yellow',command=lambda:cal("9")).place(x=200, y=280)
t.Button(f,text="X",width=10,height=3, foreground='blue', background='yellow',activebackground='hot pink',command=lambda:cal("X")).place(x=300, y=280)
t.Button(f,text="4",width=10,height=3, foreground='blue', background='cyan',activebackground='yellow',command=lambda:cal("4")).place(x=20, y=345)
t.Button(f,text="5",width=10,height=3, foreground='blue', background='cyan',activebackground='yellow',command=lambda:cal("5")).place(x=110, y=345)
t.Button(f,text="6",width=10,height=3, foreground='blue', background='cyan',activebackground='yellow',command=lambda:cal("6")).place(x=200, y=345)
t.Button(f,text="-",width=10,height=3, foreground='blue', background='yellow',activebackground='hot pink',command=lambda:cal("-")).place(x=300, y=345)
t.Button(f,text="1",width=10,height=3, foreground='blue', background='cyan',activebackground='yellow',command=lambda:cal("1")).place(x=20, y=410)
t.Button(f,text="2",width=10,height=3, foreground='blue', background='cyan',activebackground='yellow',command=lambda:cal("2")).place(x=110, y=410)
t.Button(f,text="3",width=10,height=3, foreground='blue', background='cyan',activebackground='yellow',command=lambda:cal("3")).place(x=200, y=410)
t.Button(f,text="+",width=10,height=3, foreground='blue', background='yellow',activebackground='hot pink',command=lambda:cal("+")).place(x=300, y=410)
t.Button(f,text="+/-",width=10,height=3, foreground='blue', background='cyan',activebackground='yellow',command=lambda:cal("+/-")).place(x=20, y=480)
t.Button(f,text="0",width=10,height=3, foreground='blue', background='cyan',activebackground='yellow',command=lambda:cal("0")).place(x=110, y=480)
t.Button(f,text=".",width=10,height=3, foreground='blue',background='cyan',activebackground='yellow',command=lambda:cal(".")).place(x=200, y=480)
t.Button(f,text="=",width=9,height=3,background="pink", font='bold',command=lambda:cal("=")).place(x=295, y=475)
f.mainloop()