import pyqrcode
import png
from pyqrcode import QRCode

link = input("Enter QR Code content : ")

qr = pyqrcode.create(link)

qr.svg("qrcode.svg", scale = 8)
qr.png("qrcode.png", scale = 6)

print("QR Code has been generated ! Find the generated QR Code in qrcode.png")
