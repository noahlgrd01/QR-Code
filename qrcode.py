import pyqrcode
import png
from pyqrcode import QRCode
from colorama import Fore

i = 0

while True:

    check = input("Generate QRCode ? Y/N ")
    if check == "Y" or check == "y":
        link = input("Enter QR Code content (could be a link, name etc) : ")
        name = input("Enter QR Code name (or leave blank) : ") or "qrcode"

        qr = pyqrcode.create(link)

        qr.png(f"{name or 'qrcode'}_{i+1}.png", scale = 6)

        print("QR Code has been generated ! Find the generated QR Code as .png file\n")
        i +=1

    elif check == "N" or check == "n":
        print(Fore.MAGENTA + "You've generated", i, "QRCode")
        break
