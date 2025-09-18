# in this we set all the things like background , colour, size etc amny thing

# here we also downlod the pil named module to do editing in our qrcode 
 # pip install pillow
 
import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=20,
                 border=3)    # here QRcode is the functon--- removes overlapping and error 

qr.add_data("pass.py")
qr.make(fit=True)
img=qr.make_image(fill_color="blue",back_color="white")
img.save("advanced_qrcode.png")
