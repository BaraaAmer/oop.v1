import qrcode
from art import *

text = "Qr Code"
font = "slant"

art = text2art(text, font=font)
print(art)

image = qrcode.make(input("Enter your Url --> :"))

image.save(input("Enter path to save and new name --> : "))

print("Done {+}")
