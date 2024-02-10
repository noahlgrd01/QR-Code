from tkinter import *
import qrcode

def generate_qr(content):
    link = content.get()
    if len(link) == 0:
        win_L2.config(text="QRCode content couldn't be empty !",fg='red',pady=10,font=('Arial',15,'bold'))
        win.geometry("430x170")
    else:
        win_L2.config(text="QRCode has been generated !",fg='green',pady=10,font=('Arial',15,'bold'))
        win.geometry("430x170")
        img = qrcode.make(link)
        img.save("qrcode.png")

global win
win = Tk()
win.resizable(False,False)
win.geometry("430x150")
win.title("Generate QR Code")
win.config(bg="#34495E")

win_F = Frame(win,bg="#34495E")
win_F.grid(row=0,column=0)
win_L = Label(win_F,bg="#34495E",fg="white",text="Enter QRCode content :")
win_L.grid(row=0,column=0,padx=20,pady=30)
win_E = Entry(win_F)
win_E.grid(row=0,column=1,padx=25,pady=30)
win_B = Button(win_F,text="Confirm",command=lambda:generate_qr(win_E))
win_B.grid(row=3,column=1)
win.bind("<KeyPress-Return>", lambda e: generate_qr(win_E))
global win_L2
win_L2 = Label(win,bg="#34495E",fg="white",text="")
win_L2.grid(row=5,column=0)

win.mainloop() 