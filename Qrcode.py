import qrcode
from art import *

text = " Qr Code"
font = "smslant"

art = text2art(text, font=font)
print(art)

image = qrcode.make(input(" Enter your Url --> :"))

print("=" * 40)

text = "set path : /sdcard/name.png"

print(text.center(40 , "="))

print("=" * 40)      

image.save(input(" Enter path to save and new name --> : "))

print("Done {+}")
