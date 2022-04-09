# import os
# from os import listdir
# from os.path import isfile, join
# from pgmagick import Image

# mypath = "/home/jija/Desktop/imagesononepagepdf/images" # path to your Image directory

# for each_file in listdir(mypath):
#     if isfile(join(mypath,each_file)):
#         image_path = os.path.join(mypath,each_file)
#         pdf_path =  os.path.join(mypath,each_file.rsplit('.', 1)[0]+'.pdf')
#         img = Image(image_path)
#         img.write(pdf_path)
import cv2
import numpy as np
 
# Read First Image
img1 = cv2.imread('/home/jija/Desktop/imagesononepagepdf/images/Calibri.png')
 
# Read Second Image
img2 = cv2.imread('/home/jija/Desktop/imagesononepagepdf/images/Calibri.png')
 
 
# concatenate image Horizontally
Hori = np.concatenate((img1, img2), axis=1)

# concatenate image Vertically
Verti = np.concatenate((img1, img2), axis=0)
 
cv2.imshow('HORIZONTAL', Hori)
cv2.imshow('VERTICAL', Verti)
 
cv2.waitKey(0)
cv2.destroyAllWindows()