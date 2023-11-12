import tkinter as t
from tkinter import ttk
f=t.Tk()
f.title('Employee Details')
f.geometry('400x500')
f.resizable(width=0,height=0)

t.Label(f,text='Employee Details',bg='blue',fg='white',font=('verdana 14 bold')).place(x=90,y=10)
t.Label(f,text='Employee Name',font=('arial 10 bold')).place(x=20,y=50)

ename=t.Entry(f,width=30).place(x=180,y=50)

t.Label(f,text='Post',font=('arial 10 bold')).place(x=20,y=90)
c1=t.Checkbutton(f,text='Analyst')
c1.place(x=40,y=110)
c2=t.Checkbutton(f,text='Manager')
c2.place(x=140,y=110)
c3=t.Checkbutton(f,text='Developer')
c3.place(x=240,y=110)


t.Label(f,text='Gender',font=('arial 10 bold')).place(x=20,y=150)
r1 = t.Radiobutton(f,text='Male')
r1.place(x=40,y=170)
r2 = t.Radiobutton(f,text='Female')
r2.place(x=140,y=170)
r3 = t.Radiobutton(f,text='Other')
r3.place(x=240,y=170)

t.Label(f,text='State',font=('arial 10 bold')).place(x=20,y=210)
st = ttk.Combobox(f)
st['values']=('Not selected','Bihar','Uttar Pradesh','Madhya Pradesh')
st.place(x=130,y=210)

t.Label(f,text='Address',font=('arial 10 bold')).place(x=20,y=250)
adr = t.Text(f,width=40,height=8)
adr.place(x=40,y=280)

sub = t.Button(f,text='Submit',font=('arial 10 bold'),fg='green')
sub.place(x=90,y=430)

res = t.Button(f,text='Reset',font=('arial 10 bold'),fg='red')
res.place(x=210,y=430)

f.mainloop()