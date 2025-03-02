import qrcode
qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
link = str(input("Enter the link: "))
qr.add_data(link)
qr.make()
img = qr.make_image(fill_color = 'black', back_color = 'white')
c=101
while  True :
    if input("Do you want to save the QR code? (y/n): ") == 'y':
        img.save(f'QRCode.png')
    
    break
print("QR code generated successfully.")
if input("Do you want to see the QR code? (y/n): ") == 'y':
    img.show()