# Rename this file to be "filters.py"
# Add commands to import modules here.
from PIL import Image
# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    return Image.open(filename, mode='r')

# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(img):
    img.show()


# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(img, name):
    img.save(name)

# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(img):
    w = img.width
    h = img. height
    new_image = Image.new("RGB", (w,h))
    new_pixels = []
    for i in range(0, h):
        for j in range(0, w):
            pixel_coordinates = (j, i)
            rgb_sum = sum(img.getpixel(pixel_coordinates))
            if rgb_sum < 182:
                new_pixels.append((0, 51, 76))
            elif rgb_sum >= 182 and rgb_sum <= 364:
                new_pixels.append((217, 26, 33))
            elif rgb_sum > 364 and rgb_sum <= 546:
                new_pixels.append((112, 150, 158))
            elif rgb_sum > 546:
                new_pixels.append((252, 227, 166))
        new_image.putdata(new_pixels)
        return new_image
    def corgipy(img):
        w = img.width
        h = img.height
        new_image = Image.new("RBG", (w,h)
         for j in range(0, w):
            pixel_coordinates = (j, i)
            rgb_sum = sum(img.getpixel(pixel_coordinates))
            if rgb_sum < 182:
                new_pixels.append((0, 51, 76))
            elif rgb_sum >= 182 and rgb_sum <= 364:
                new_pixels.append((217, 26, 33))
            elif rgb_sum > 364 and rgb_sum <= 546:
                new_pixels.append((112, 150, 158))
            elif rgb_sum > 546:
                new_pixels.append((252, 227, 166))
                new_image.putdata(new_pixels)
                return new_image
