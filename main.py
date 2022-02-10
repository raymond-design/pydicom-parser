import pydicom
import numpy
from PIL import Image

#path of dicom file
path = ''

image = pydicom.dcmread(path)

#extract pixel data from file
image = image.pixel_array.astype(float)

rescale = (numpy.maximum(image, 0)/image.max())*255
final = numpy.uint8(rescale)

final = Image.fromarray(final)

final.show()
image_name = 'new.png'
final.save(image_name)