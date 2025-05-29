import cv2
image = cv2.imread('cup.jpg')
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
resizedimage=cv2.resize(gray_image,(444,444))
cv2.imshow('Processed Image',resizedimage)
key=cv2.waitKey(0)
if key == ord('s'):
    cv2.imwrite("Grayimage.jpg",resizedimage)
    print("Image Saved as Grayimage.jpg")
else:
    print("Image not saved")
cv2.destroyAllWindows()
print(f'Processed Image Dimensions:{resizedimage.shape}')
