import tkinter as t
f=t.Tk()
f.geometry('300x500')
f.resizable(width=0,height=0)
f.title('Calculator')

t.Label(f,text='Standard',font=('arial 14 bold')).place(x=20,y=10)

ta = t.Text(f,width=33,height=8)
ta.place(x=15,y=50)

t.Label(f,text='MC',font=('arial 10 bold')).place(x=20,y=190)
t.Label(f,text='MR',font=('arial 10 bold')).place(x=75,y=190)
t.Label(f,text='M+',font=('arial 10 bold')).place(x=135,y=190)
t.Label(f,text='M-',font=('arial 10 bold')).place(x=195,y=190)
t.Label(f,text='MS',font=('arial 10 bold')).place(x=245,y=190)

b1=t.Button(f,text='     %     ')
b1.place(x=15,y=240)

b2=t.Button(f,text='     CE     ')
b2.place(x=80,y=240)

b3=t.Button(f,text='     C     ')
b3.place(x=150,y=240)

b4=t.Button(f,text=' BACK ')
b4.place(x=220,y=240)

b5=t.Button(f,text='    1/x    ')
b5.place(x=15,y=280)

b6=t.Button(f,text='     x2     ')
b6.place(x=80,y=280)

b7=t.Button(f,text='     x     ')
b7.place(x=150,y=280)

b8=t.Button(f,text='     /     ')
b8.place(x=220,y=280)

b9=t.Button(f,text='     7     ')
b9.place(x=15,y=320)

b10=t.Button(f,text='     8     ')
b10.place(x=80,y=320)

b11=t.Button(f,text='     9     ')
b11.place(x=150,y=320)

b12=t.Button(f,text='     X     ')
b12.place(x=220,y=320)

b13=t.Button(f,text='     4     ')
b13.place(x=15,y=360)

b14=t.Button(f,text='     5     ')
b14.place(x=80,y=360)

b15=t.Button(f,text='     6     ')
b15.place(x=150,y=360)

b16=t.Button(f,text='     -     ')
b16.place(x=220,y=360)

b17=t.Button(f,text='     1     ')
b17.place(x=15,y=400)

b18=t.Button(f,text='     2     ')
b18.place(x=80,y=400)

b19=t.Button(f,text='     3     ')
b19.place(x=150,y=400)

b20=t.Button(f,text='     +     ')
b20.place(x=220,y=400)

b21=t.Button(f,text='     +/-     ')
b21.place(x=15,y=440)

b22=t.Button(f,text='     0     ')
b22.place(x=80,y=440)

b23=t.Button(f,text='     .     ')
b23.place(x=150,y=440)

b24=t.Button(f,text='     =     ')
b24.place(x=220,y=440)



f.mainloop()