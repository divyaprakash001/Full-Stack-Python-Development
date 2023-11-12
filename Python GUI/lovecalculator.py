import tkinter as t
import random as rand
f=t.Tk()
f.title('Love Calculator')
f.geometry('280x500')
f.resizable(width=0,height=0)


def lovecalculator():
    # n1=len(ta1.get("1.0", 'end-1c'))
    # n2=len(ta2.get("1.0", 'end-1c'))
    lb3.config(text='Your love percent is '+str(rand.randint(60,100)))

# creating Label
lb1 = t.Label(f,text='Boy Name')
lb1.grid(row=0)
lb2 = t.Label(f,text='Girl Name')
lb2.grid(row=2)

# Label for result
lb3 = t.Label(f,text="Your love matching ")
lb3.grid(row=5,column=0)

lb3 = t.Label(f,text="*Disclaimer :-It may vary time to time")
lb3.grid(row=6,column=0)

#create text
ta1 = t.Text(f,width=30,height=1)
ta1.grid(row=1)
ta2 = t.Text(f,width=30,height=1)
ta2.grid(row=3)


# creating button to calculate
btn = t.Button(f,text='calculate',command=lovecalculator)
btn.grid(row=4,column=0)



f.mainloop()