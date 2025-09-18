"""
first i make download the libraries used in  the qrcode
and module :-
qrcode----- pip install qrcode[pil]----generate qr codes
|
|
segno-----pip install segno----generate high quality qr
|
|
pyqrcode---pip install pyqrcode pypng----generate png/ svg qr codes
|
|
opencv-python---pip install opencv-python----read qr code form images
|
|
zxing---pip install zxing-----decode qr code (java based)

"""
import qrcode as qr
img=qr.make("Hello scan me")#here we give the url of the string named img
img.save("hello_first.png")
# this is the first meathod to make a qr code 

