from PIL import Image
import sys

try:
    img = Image.open("download.jpg")

except IOError:
    print("Unable to load image")
    sys.exit(1)
    
resized_img = img.resize((2500, 2000))
resized_img.save("resized_image.jpg")

grayscale = resized_img.convert('L')
grayscale.show()