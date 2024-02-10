from tkinter import *
import qrcode

def generate_qr(content):
    link = content.get()
    img = qrcode.make(link)
    img.save("qrcode.png")

win = Tk()
win.resizable(False,False)
win.geometry("400x200")
win.title("Generate QR Code")
win.config(bg="#34495E")

win_F = Frame(win,bg="#34495E")
win_F.grid(row=0,column=0)
win_L = Label(win_F,bg="#34495E",fg="white",text="Enter QRCode content :")
win_L.grid(row=0,column=0,padx=30,pady=30)
win_E = Entry(win_F)
win_E.grid(row=0,column=1,padx=25,pady=30)
win_B = Button(win_F, text="Valider", command= lambda:generate_qr(win_E))
win_B.grid(row=3,column=1)
global win_L2
win_L2 = Label(win,bg="#34495E",fg="white",text="")
win_L2.grid(row=5,column=1)

win.mainloop()