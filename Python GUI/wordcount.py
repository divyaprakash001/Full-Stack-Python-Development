import tkinter as t

# f variable take the window reference
f=t.Tk()

# for window title
f.title('Welcome to Word Count Application',)

# window size
f.geometry('800x400')

# to make resize inactive
f.resizable(width=0,height=0)

# function to count words
def countword():
     txt = ta.get("1.0", 'end-1c')
     tword=len(txt.strip().split(' '))
     res.config(text="Total Words : "+str(tword))

# function to count sentences
def countsentence():
     res.config(text="Total Sentences : "+str(ta.get("1.0", 'end-1c').count('.')))

# function to count characters
def countcharacter():
     res.config(text="Total Characters : "+str(len(ta.get("1.0", 'end-1c'))))

# text area to input text by end-users
ta = t.Text(f,width=96,height=15)
ta.place(x=12,y=10)

# button to have clicked to get the result
b1=t.Button(f,text='word count',font=('arial 12 bold italic'),bg='navy',foreground='white',command=countword)
b1.place(x=12,y=260)

# button to have clicked to get the result
b2=t.Button(f,text='sentence count',font=('arial 12 bold italic'),bg='navy',foreground='white',command=countsentence)
b2.place(x=300,y=260)

# button to have clicked to get the result
b3=t.Button(f,text='character count',font=('arial 12 bold italic'),bg='navy',foreground='white',command=countcharacter)
b3.place(x=600,y=260)

# Label where when buttons clicked, result shown
res=t.Label(f,text='Total word:',font=('arial 12 bold italic'),fg='red')
res.place(x=30,y=320)






# ta.bind('<KeyPress>', click)
# ta.bind('<KeyRelease>', click)

f.mainloop()
