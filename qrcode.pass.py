import qrcode

# Path to your Python file
file_path = "pass.py"  # your file

# Read the Python file content
with open(file_path, "r", encoding="utf-8") as f:
    file_content = f.read()

# Generate QR code
qr = qrcode.QRCode(
    version=None,  # auto-size
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(file_content)
qr.make(fit=True)

# Save QR code as image
img = qr.make_image(fill_color="black", back_color="white")
img.save("pass_qr.png")

print("QR code generated: 'pass_qr.png'")
