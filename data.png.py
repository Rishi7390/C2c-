import qrcode

download_link = "http://192.168.1.84:8000/data.py"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(download_link)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("data.png")

print("QR code generated: 'data.png'")
