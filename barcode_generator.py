# import barcode
import barcode

# import ImageWriter to generate an image file
from barcode.writer import ImageWriter

# check the complete list of supported formats of barcode
# print(barcode.PROVIDED_BARCODES)

try:
    # Make sure to pass the number as string
    number = '8903454126727'

    # Since we are creating a EAN13 barcode, appropriate barcode format needs to be used
    barcode_format = barcode.get_barcode_class('ean13')

    # let's create an object of EAN13 class and
    # pass the number with the ImageWriter() as the
    # writer
    my_barcode = barcode_format(number, writer=ImageWriter())

    # barcode is ready. Let's save it.
    my_barcode.save("miscellaneous_files/barcode")

    print("Your barcode is generated.")

except Exception as e:
    print(e)
