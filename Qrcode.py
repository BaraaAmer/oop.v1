import qrcode

image = qrcode.make(input("Enter your Url --> :"))

image.save(input("Enter path to save and new name --> : "))

print("Done {+}")
