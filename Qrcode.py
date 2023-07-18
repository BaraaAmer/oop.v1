import qrcode
import pyfiglet
import termcolor

print(pyfiglet.figlet_format(" Qr Code"))

image = qrcode.make(input("Enter your Url --> :"))

image.save(input("Enter path to save and new name --> : "))

print("Done {+}")