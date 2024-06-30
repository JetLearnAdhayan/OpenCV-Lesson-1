import cv2

img = cv2.imread("pika.png",0)

#there are 3 parameters to read an image - 
# cv2.imread_colour(1 )=> specify to load the image in colour. excludes transperency
#cv2.imread_GREYSCALE(0) => specify to load the image in greyscale/ black and white 
#cv2.imread_unchanged(-1) => specify to load the image unchanged

#imshow is used to show the loaded image in a new window with a title
cv2.imshow("output image",img)

#to hold the window until the user presses a key on the keyboard 
cv2.waitKey(0)

# delete/close the image window after the key pressed
cv2.destroyAllWindows()