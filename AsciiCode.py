#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 13:19:25 2018

@author: sandilya
"""
import os
from PIL import Image
from numpy import *
#Import the image and create image object

# The code is not generic just works for Image Test.png assuming that Test.png is in the same directory of the file.

image=Image.open("Test.png")
image=image.resize((100,100))
#Image format and size
print("The format of the image is ",image.format)
print("The size of image is ",image.size[0],"X",image.size[1])

#import numpy and use its array to convert image to array
matrix=array(image)

# find the no of rows and columns
rows,cols=len(matrix),len(matrix[1])
#brightness of each pixel 
brightness=zeros(shape=(rows,cols),dtype=int)

for row in range(rows):
    for col in range(cols):
        brightness[row][col]=average(matrix[row][col])
print("Constructed Brightness matrix")

mapped="`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
asciiBrightness=empty(shape=(rows,cols),dtype="<U2")

"""approximation
256 numbers to 65 characters
which means 4 numbers to each character"""
for row in range(rows):
    for col in range(cols):
        asciiBrightness[row][col]=mapped[int(round(brightness[row][col]/65))]

for row in range(rows):
    for col in range(cols):
        print(asciiBrightness[row][col],end="")
    print()
 
