import tkinter as t
f=t.Tk()
f.geometry('300x500')
f.resizable(width=0,height=0)
f.title('Calculator')

# function
def cal(a):
    print(a)
    l = len(ta.get())
    print(l)
    if a in ['CE','OFF']:
        ta.config(state='normal')
        ta.delete(0,l+1)
        if a == 'CE':
            ta.insert(0,'0')
        ta.config(state='disabled')
    elif a in ['0','1','2','3','4','5','6','7','8','9']:
        ta.config(state='normal')
        ta.insert(0,a)
        ta.config(state='disabled')


ex = t.Label(f,text='Standard',font=('arial 14 bold')).place(x=20,y=30)

ta = t.Entry(f,width=45,justify='right')
ta.place(x=15,y=100)

t.Label(f,text='MC',font=('arial 10 bold')).place(x=20,y=190)
t.Label(f,text='MR',font=('arial 10 bold')).place(x=75,y=190)
t.Label(f,text='M+',font=('arial 10 bold')).place(x=135,y=190)
t.Label(f,text='M-',font=('arial 10 bold')).place(x=195,y=190)
t.Label(f,text='MS',font=('arial 10 bold')).place(x=245,y=190)

t.Button(f,text='     %     ',command=lambda:cal('%')).place(x=15,y=240)

t.Button(f,text='     CE     ',command=lambda:cal('CE')).place(x=80,y=240)

t.Button(f,text='     OFF     ',command=lambda:cal('OFF')).place(x=150,y=240)

t.Button(f,text=' BACK ',command=lambda:cal('Back')).place(x=220,y=240)

t.Button(f,text='    1/x    ').place(x=15,y=280)

t.Button(f,text='     x2     ').place(x=80,y=280)

t.Button(f,text='     x     ',command=lambda:cal('x')).place(x=150,y=280)

t.Button(f,text='     /     ',command=lambda:cal('/')).place(x=220,y=280)

t.Button(f,text='     7     ',command=lambda:cal('7')).place(x=15,y=320)

t.Button(f,text='     8     ',command=lambda:cal('8')).place(x=80,y=320)

t.Button(f,text='     9     ',command=lambda:cal('9')).place(x=150,y=320)

t.Button(f,text='     X     ',command=lambda:cal('x')).place(x=220,y=320)

t.Button(f,text='     4     ',command=lambda:cal('4')).place(x=15,y=360)

t.Button(f,text='     5     ',command=lambda:cal('5')).place(x=80,y=360)

t.Button(f,text='     6     ',command=lambda:cal('6')).place(x=150,y=360)

t.Button(f,text='     -     ',command=lambda:cal('-')).place(x=220,y=360)

t.Button(f,text='     1     ',command=lambda:cal('1')).place(x=15,y=400)

t.Button(f,text='     2     ',command=lambda:cal('2')).place(x=80,y=400)

t.Button(f,text='     3     ',command=lambda:cal('3')).place(x=150,y=400)

t.Button(f,text='     +     ',command=lambda:cal('+')).place(x=220,y=400)

t.Button(f,text='     +/-     ',command=lambda:cal('+/-')).place(x=15,y=440)

t.Button(f,text='     0     ',command=lambda:cal('0')).place(x=80,y=440)

t.Button(f,text='     .     ',command=lambda:cal('.')).place(x=150,y=440)

t.Button(f,text='     =     ',command=lambda:cal('=')).place(x=220,y=440)



f.mainloop()