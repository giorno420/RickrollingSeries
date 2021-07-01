import qrcode

url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
qr.add_data(url)
qr.make(fit=True)

qrimage = qr.make_image(fill='black', back_color='white')
qrimage.save('rickrollimage.png')