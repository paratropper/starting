# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 21:14:25 2019

@author: HP
"""

from PIL import Image
import os

img = Image.open("aayush.jpg")
print (img.size)
print (img.width)
print (img.height)
print (img.format)
print (img.mode)
#rotaion of image
img_rotate = img.transpose(Image.ROTATE_90)
img_rotate.show()
img_rotate.save("aayush.jpg")
#corp image
img = Image.open("aayush.jpg")
crop_im = img.crop(box=(340, 20, 160, 204))
crop_im.save('crop_aayush.jpg')
crop_im.show()
#creating thumnail
img = Image.open("aayush.jpg")
img.thumbnail((75, 75))
print(img.width, img.height)
img.save('thumb_aayush.jpg')
#gray scale of image
img = Image.open('aayush.jpg').convert('LA')
img.save('aayush1.jpg')
img = Image.open("aayush1.jpg")
img.show()