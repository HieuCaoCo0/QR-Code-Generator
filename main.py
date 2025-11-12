import qrcode

url = input("Enter your URL: ").strip()
file_name = input("Enter the your file name: ")
file_path = "C:\\Users\\admin\\Desktop\\" + file_name + ".png"

qr = qrcode.QRCode()
qr.add_data(url)
img = qr.make_image()
img.save(file_path)

print("QR Code was generated in your Desktop!")