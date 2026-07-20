import cv2
import numpy as np

path1= "data_in/image1.png"
path2= "data_in/image2.png"
img1= cv2.imread(path1)
img2= cv2.imread(path2)

if img1 is None :
    raise FileNotFoundError(f" Image was not found {path1}")
if img2 is None :
    raise FileNotFoundError(f" Image was not found {path2}")
print(img1.shape)
print(img2.shape)

print(img1.ndim)
print(img2.ndim)

print(img1.dtype)
print(img2.dtype)
print(type(img1))
print(type(img2))
# print("First picture loaded ")
# print("First picture shape:", img1.shape)

# print("Second picture loadedы ")
# print("Second picture shape:", img2.shape)
if img1.shape != img2.shape:
    raise ValueError("Images should have the same size ")
difference = cv2.absdiff(img1, img2)
# cv2.imshow("first image",img1)
# cv2.imshow("second image",img2)
# cv2.imshow("Difference", difference)

DifferenceWithColor = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Difference with a gray color ", DifferenceWithColor)


_,ImgThreshold = cv2.threshold(
    DifferenceWithColor,
    30,
    255,
    cv2.THRESH_BINARY
)

saved3 = cv2.imwrite(
    "data_out/threshold_difference.png",
  ImgThreshold
)


saved1 = cv2.imwrite("data_out/difference.png", difference)
saved2 = cv2.imwrite("data_out/gray_difference.png", DifferenceWithColor)

print("difference saved:", saved1)
print("gray difference saved:", saved2)
print("threshold saved:", saved3)

print("difference shape:", difference.shape)
print("gray shape:", ImgThreshold.shape)
print("threshold shape:", ImgThreshold.shape)

print("gray unique values:", np.unique(DifferenceWithColor))
print("threshold unique values:", np.unique(ImgThreshold))
cv2.waitKey(0)
cv2.destroyAllWindows()