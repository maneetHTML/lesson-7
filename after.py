import cv2
import random


image = cv2.imread('cup.jpg')


if image is None:
    print("Error: Could not read image 'cup.jpg'")
    exit()

random_width = random.randint(111, 700) 
random_height = random.randint(333, 500) 


resizedimage = cv2.resize(image, (random_width, random_height))

cv2.imshow('Processed Image', resizedimage)

key = cv2.waitKey(0)


if key == ord('s'):
    cv2.imwrite("RandomResizedImage.jpg", resizedimage)
    print("Image Saved as RandomResizedImage.jpg")
else:
    print("Image not saved")

cv2.destroyAllWindows()

print(f'Processed Image Dimensions: {resizedimage.shape}')
