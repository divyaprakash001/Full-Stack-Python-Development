import tkinter as t
from tkinter import ttk

f = t.Tk()
f.title('Employee Details')
f.geometry('350x550')
f.resizable(width=0,height=0)

t.Label(f,text='Employee Details',fg='blue',font=('arial 14 bold')).place(x=90,y=10)

l1 = t.Label(f,text='Employee Name')
l1.place(x=20,y=60)

e1 = t.Entry(f,width=30)
e1.place(x=130,y=60)

l2 = t.Label(f,text='Post')
l2.place(x=20,y=100)
c1=t.Checkbutton(f,text='Analyst')
c1.place(x=40,y=130)
c1=t.Checkbutton(f,text='Manager')
c1.place(x=140,y=130)
c1=t.Checkbutton(f,text='Developer')
c1.place(x=240,y=130)

l3 = t.Label(f,text='Gender')
l3.place(x=20,y=170)

r1 = t.Radiobutton(f,text='Male')
r1.place(x=40,y=200)
r1 = t.Radiobutton(f,text='Female')
r1.place(x=140,y=200)
r1 = t.Radiobutton(f,text='Other')
r1.place(x=240,y=200)

l4 = t.Label(f,text='State')
l4.place(x=20,y=240)

d1 = ttk.Combobox(f)
d1['value']=('Bihar','Jharkhand','Uttar Pradesh','West Bengal')
d1.place(x=130,y=240)

l5 = t.Label(f,text='Address')
l5.place(x=20,y=280)

adr = t.Text(f,width=35,height=8)
adr.place(x=40,y=310)

sub = t.Button(f,text='Submit',fg='green')
sub.place(x=110,y=470)
res = t.Button(f,text='Reset',fg='red')
res.place(x=190,y=470)

f.mainloop()