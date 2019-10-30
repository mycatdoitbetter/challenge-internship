# Libraries to build the code
from PIL import Image, ImageFont, ImageDraw
import numpy as np
import cv2 as cv

# setting the colors
black = (0, 0, 0)
white = (255, 255, 255)

# interface start
def menu():
    print("\n" + 60 * "-")
    print("Let's custumise your case?".center(60))
    print(60 * "-" + "\n")
# def to get the image name
def image():
    print("After opening the window, Press Esc to go to the next estage.\n")
    image = input("Please, type the name of your image file (.jpg extension): ")
    return image
# def to get the font name
def font():
    font = input("Please, type the name of your font-type file (.ttf extension): ")
    return font
# def to get the text to print
def name():
    name = input("Please, enter text to print: ")
    return name
# def to get the size of the text
def size():
    size = input("Please, set the size of your text: ")
    return int(size)

# def to set the coordinates for print
def coordinates():
    c_x = input("Now, enter the x coordinate: ")
    c_y = input("To finish, enter the y coordinate: ")
    return int(c_x), int(c_y)

# def to show the the unedited image
def show_image(image):
    image_in = cv.imread(image)
    cv.imshow("Preview", image_in)
    k = cv.waitKey(0)
    if k == 27:
        pass
     

# def to show the font-type
def show_font(font):
    img = np.zeros((300, 400, 3), np.uint8)
    text_preview = "We are GoCase!"
    font_in = ImageFont.truetype(font, 40)
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    draw.text((30, 160), text_preview, font=font_in, fill= white)
    img = np.array(img_pil)
    cv.imshow("Preview of the font-type", img)
    k = cv.waitKey(0)
    if k == 27:
        pass
      

# def to plot the name on the chosen image
def edition(image, font, name, size, c_x, c_y):
    image_in = cv.imread(image)
    pil_img = Image.fromarray(image_in)
    draw = ImageDraw.Draw(pil_img)
    font_out = ImageFont.truetype(font, size)
    draw.text((c_x, c_y), name, font = font_out, fill= black)
    image_out = cv.cvtColor(np.array(pil_img), 1)
    cv.imshow("Final Result", image_out)
    cv.imwrite("Result.jpg",image_out)
    k = cv.waitKey(0)
    if k == 27 :
        pass
       

# loop to organize and get the data for edition of the image
while True:
    menu()
    image = image()
    show_image(image)
    font = font()
    show_font(font)
    name = name()
    size = size()
    c_x, c_y = coordinates()
    edition(image, font, name, size, c_x, c_y)
    cv.destroyAllWindows()
    break
