import qrcode as q
import tkinter as t

f = t.Tk()
f.geometry('500x200')
f.title('qr code genertor')
f.resizable(width=0,height=0)
t.Label(f,text='Enter your url').place(x=30,y=50)
ta = t.Entry(f,width=50)
ta.place(x=140,y=50)

def qr():
    s = ta.get()
    if len(s) == 0:
        l.config(text='Sorry, you have to give url')
    else:
        l.config(text='')
        qr = q.QRCode(
            version=5,
            box_size=10
        )
        qr.add_data(s)
        qr.make(fit = True)
        img = qr.make_image(fill_color='white',back_color='black')
        img.save('myqr.png')
        img.show()

t.Button(text='Generate QR Code',command=qr).place(x=30,y=100)
l = t.Label(f,text='ds')
l.place(x=80, y=145)

f.mainloop()