import cv2
import numpy as np

def get_pixelart_dimensions():
    height = int(input("Height of pixel art: "))
    width = int(input("Width of pixel art: "))
    return height, width

def get_output_dimensions(pixel_height, pixel_width):
    height = int(input("Output height: "))
    width = int(input("Output width: "))

    if height % pixel_height != 0:
        remainder = height % pixel_height
        height += pixel_height - remainder

    if width % pixel_width != 0:
        remainder = width % pixel_width
        width += pixel_width - remainder
        
    return height, width

img_name = input("Image name: ")
image = cv2.imread(img_name)
image_height, image_width, channels = image.shape

pixelart_height, pixelart_width = get_pixelart_dimensions()
output_height, output_width = get_output_dimensions(pixelart_height, pixelart_width)

scale_value_height = int(output_height / pixelart_height)
scale_value_width = int(output_width / pixelart_width)

resized = cv2.resize(image, (pixelart_height, pixelart_width), interpolation=cv2.INTER_AREA)
pixel_art_list = []

output_pixel_row = []
pixel_height_in_img = 0
for row in resized:
    for j in range(scale_value_height):
        for pixel in row:
            for i in range(scale_value_width):
                output_pixel_row.append(pixel)
        pixel_art_list.append(output_pixel_row)
        output_pixel_row = []

output = np.array(pixel_art_list)
cv2.imshow("Pixel Art", output)
cv2.waitKey(0)
cv2.destroyAllWindows


#That's it for today