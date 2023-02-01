import pyqrcode
import png
from pyqrcode import QRCode

link = input("Enter QR Code content : ")
name = input("Enter QR Code name : ") or qrcode

qr = pyqrcode.create(link)

qr.png(name + ".png", scale = 6)

print("QR Code has been generated ! Find the generated QR Code in", name, ".png")
