import tkinter as t
from tkinter import ttk
from DBSender import DBHelper 

'''
# import class from another folder
import sys
sys.path.insert(0,"..")
from Python_MYSQL import DBHelper
# ---------------------------
'''


f=t.Tk()
f.title('Employee Details')
f.geometry('400x500')
f.resizable(width=0,height=0)


v1 = t.StringVar(f,value='Male')
v2=t.IntVar()
v3=t.IntVar()
v4=t.IntVar()
cmb = t.StringVar(value='jharkhand')




def getdata():
    helper = DBHelper()
    ename1 = ename.get()
    if v2.get() == 1:
        post = 'Analyst'
    if v3.get() == 1:
        post = 'Manager'
    if v4.get() == 1:
        post = ' Developer'
    gender =  v1.get()
    state = cmb.get()
    address = adr.get("1.0", 'end-1c')
    print(ename,post,gender,state,address)
    
    helper.insert_data(ename1,post,gender,state,address)



# display all data
def dispData():
    helper = DBHelper()
    print("disp called")
    f=t.Tk()
    f.title('Employee Details')
    f.geometry('400x500')
    f.resizable(width=0,height=0)

    

    swlb = t.Label(f,text='data')
    swlb.place(x=160,y=10)


    helper.fetch_all()
    


    f.mainloop()
    

t.Label(f,text='Employee Details',bg='blue',fg='white',font=('verdana 14 bold')).place(x=90,y=10)
t.Label(f,text='Employee Name',font=('arial 10 bold')).place(x=20,y=50)

ename=t.Entry(f,width=30)
ename.place(x=180,y=50)

t.Label(f,text='Post',font=('arial 10 bold')).place(x=20,y=90)
c1=t.Checkbutton(f,text='Analyst',variable=v2)
c1.place(x=40,y=110)
c2=t.Checkbutton(f,text='Manager',variable=v3)
c2.place(x=140,y=110)
c3=t.Checkbutton(f,text='Developer',variable=v4)
c3.place(x=240,y=110)


t.Label(f,text='Gender',font=('arial 10 bold')).place(x=20,y=150)
r1 = t.Radiobutton(f,text='Male',variable=v1,value='Male')
r1.place(x=40,y=170)
r2 = t.Radiobutton(f,text='Female',variable=v1,value='Female')
r2.place(x=140,y=170)
r3 = t.Radiobutton(f,text='Others',variable=v1,value='Others')
r3.place(x=240,y=170)

t.Label(f,text='State',font=('arial 10 bold')).place(x=20,y=210)
st = ttk.Combobox(f,textvariable=cmb)
st['values']=('Not selected','Bihar','Uttar Pradesh','Madhya Pradesh')
st.place(x=130,y=210)

t.Label(f,text='Address',font=('arial 10 bold')).place(x=20,y=250)
adr = t.Text(f,width=40,height=8)
adr.place(x=40,y=280)

sub = t.Button(f,text='Submit',font=('arial 10 bold'),fg='green', command=getdata)
sub.place(x=90,y=430)

res = t.Button(f,text='Reset',font=('arial 10 bold'),fg='red')
res.place(x=210,y=430)

showbtn = t.Button(f,text='show data',command=dispData)
showbtn.place(x=300,y=430)

f.mainloop()