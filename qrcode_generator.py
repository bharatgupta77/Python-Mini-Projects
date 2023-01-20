import qrcode

try:
    # Data to be encoded
    data = "This is QR generation code"

    # Creating an instance of QRCode class
    qr_obj = qrcode.QRCode(version=1,
                           box_size=7,
                           border=2)

    # Adding data to the instance 'qr'
    qr_obj.add_data(data)

    # This make method with (fit=True) ensures that the entire dimension of the QR Code is utilized, even if our input data could fit into less number of boxes.
    qr_obj.make(fit=True)

    # to convert qr object into an image , we use this method.
    image = qr_obj.make_image(fill_color='blue',
                              back_color='white')

    # save the image
    image.save("miscellaneous_files/qr_code")

    print("Your QR code is generated.")

except Exception as e:
    print(e)
