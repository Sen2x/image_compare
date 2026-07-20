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

# print("Second picture loaded ")
# print("Second picture shape:", img2.shape)

