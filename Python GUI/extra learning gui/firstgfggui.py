import tkinter as t
f=t.Tk()
f.title('Welcome to gui')
f.geometry('800x400')

lbl = t.Label(f,text='are you a geek ?')
lbl.grid()

txt=t.Entry(f,width=10)
txt.grid(column=1,row=0)

def click():
    res="you wrote"+txt.get()
    lbl.configure(text=res)

btn = t.Button(f,text='click me',fg='red',command=click)
btn.grid(column=2,row=1)







f.mainloop()