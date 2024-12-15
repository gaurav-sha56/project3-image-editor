''' 
This code works like an image editor 
this program can crop, flip, rotate or 
can produce negative of an image i further look 
to add more features in future 

#Keep learning 

'''


import numpy as np
from PIL import Image
import cv2



# Function to flip an image 

def flip(image):

    img = Image.open(image)
    img_array = np.array(img)
    flipped_img = np.fliplr(img_array)
    new=Image.fromarray(flipped_img)
    new.save(image)

    img2=cv2.imread(image)
    flipped_img2 = cv2.flip(img2,1)
    cv2.imshow("flipped", flipped_img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



# Function to rotate an image 
    
def rotate(image):

    img = Image.open(image)
    img_array = np.array(img)
    rotated_img = np.rot90(img_array)
    new_image=Image.fromarray(rotated_img)
    # new_image.save(image)
    new_image.show()

    img2=cv2.imread(image)
    flipped_img2 = cv2.rotate(img2,0)
    cv2.imshow("flipped", flipped_img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Function to convert an image into negative image 
    
def negativeImage(image):

    img = Image.open(image)
    img_array = np.array(img)
    is_grayscale = len(img_array.shape) < 3

    if is_grayscale:
     # For grayscale images
        negative_image = 255 - img_array
    else:
        # For color images (RGB)
        negative_image = 255 - img_array

    new_image=Image.fromarray(negative_image)
    new_image.save(image)
    new_image.show()



# Function to crop an image 

def crop(image):
    # Lists to store the bounding box coordinates
    top_left_corner=[]
    bottom_right_corner=[]
    img2=cv2.imread(image)
    img = Image.open(image)
    img_array=np.array(img)
    def select(action, x, y, flags, *userdata):
        global top_left_corner, bottom_right_corner, cropped_image
        if action == cv2.EVENT_LBUTTONDOWN:
            top_left_corner = [(x,y)]
        elif action == cv2.EVENT_LBUTTONUP:
            bottom_right_corner = [(x,y)]    
            cropped_image=img_array[top_left_corner[0][1]:bottom_right_corner[0][1], top_left_corner[0][0]:bottom_right_corner[0][0]]
            cv2.imshow("Window",cropped_image)
            new_image=Image.fromarray(cropped_image)
            new_image.save(image)
    cv2.namedWindow("Window")
    cv2.setMouseCallback("Window", select)
    cv2.imshow("Window", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__=="__main__":
    print("Welcome to image editor! This program can:\nCROP\nROTATE\nFLIP\nCONVERT TO NEGATIVE")
    image=input("Enter the name/path of the image you want to edit:")
    choice=input("Enter your choice: ")

    condition=True
    while condition:

        if "rotate" in choice.lower():
            rotate(image)

        elif "flip" in choice.lower():
            flip(image)
        
        elif "negative" in choice.lower():
            negativeImage(image)
        
        elif "crop" in choice.lower():
            crop(image)

        choice=input("Tell us what you want to change further if no just enter no: ")

        if "no" in choice.lower():
            condition=False
    
