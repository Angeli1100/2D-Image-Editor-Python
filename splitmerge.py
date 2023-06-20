'''
SC32303 DIGITAL IMAGE PROCESSING
ASSIGNMENT 3
FARAH NURUL AIN BINTI MOHD SUFFIAN @ LAURENCE BS19110258
ANGELI ANAK DAVID BS19110452
'''

import cv2
from tkinter import *
import numpy as np

class SplitMerge(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)
        
        self.iconbitmap("images/doodle.ico")
        self.title ("Split and Merge")
        self.geometry ("270x300")
        self.config (bg = "#0C2A33")
        
        self.original_image = self.master.processed_image
        self.processing_image = self.master.processed_image
        self.filtered_image = None
        
        self.labelsplit = LabelFrame (self, text = 'Split Image Color', padx = 30, pady = 10, font = ("Lucida Calligraphy", 10, 'bold'), bg = "#0C2A33", fg = 'white')
        self.labelsplit.pack ()
        
        self.RedButton = Button (self.labelsplit, text = 'Red Image', command = self.redimage)
        self.RedButton.pack ()
        
        self.BlueButton = Button (self.labelsplit, text = 'Blue Image', command = self.blueimage)
        self.BlueButton.pack ()
        
        self.GreenButton = Button (self.labelsplit, text = 'Green Image', command = self.greenimage)
        self.GreenButton.pack ()
        
        self.merge = Button (self, text = 'Merge Image Color', command = self.mergeimage)
        self.merge.pack ()
        
        self.splitImage = LabelFrame (self, text = 'Split Image', padx = 30, pady = 10, font = ("Lucida Calligraphy", 10, 'bold'), bg = "#0C2A33", fg = 'white')
        self.splitImage.pack ()
        
        self.topleft = Button (self.splitImage, text = "Top Left", command = self.topLEFT)
        self.topleft.pack ()
        
        self.topright = Button (self.splitImage, text = "Top Right", command = self.topRIGHT)
        self.topright.pack ()
        
        self.bottomleft = Button (self.splitImage, text = "Bottom Left", command = self.bottomLEFT)
        self.bottomleft.pack ()
        
        self.bottomright = Button (self.splitImage, text = "Bottom Right", command = self.bottomRIGHT)
        self.bottomright.pack ()
        
    def topLEFT (self):
        (self.h, self.w) = self.processing_image.shape[:2]

        centerX, centerY = (self.w // 2), (self.h // 2)

        self.topLeft = self.processing_image[0:centerY, 0:centerX]
        
        self.filtered_image = self.topLeft
        self.master.image_viewer.show_image (img = self.topLeft)
        
    def topRIGHT (self):
        (self.h, self.w) = self.processing_image.shape[:2]

        centerX, centerY = (self.w // 2), (self.h // 2)

        self.topRight = self.processing_image[0:centerY, centerX:self.w]
        
        self.filtered_image = self.topRight
        self.master.image_viewer.show_image (img = self.topRight)
        
    def bottomLEFT (self):
        (self.h, self.w) = self.processing_image.shape[:2]

        centerX, centerY = (self.w // 2), (self.h // 2)

        self.bottomLeft = self.processing_image[centerY:self.h, 0:centerX]
        
        self.filtered_image = self.bottomLeft
        self.master.image_viewer.show_image (img = self.bottomLeft)
        
    def bottomRIGHT (self):
        (self.h, self.w) = self.processing_image.shape[:2]

        centerX, centerY = (self.w // 2), (self.h // 2)

        self.bottomRight = self.processing_image[centerY:self.h, centerX:self.w]
        
        self.filtered_image = self.bottomRight
        self.master.image_viewer.show_image (img = self.bottomRight)
        
    def redimage (self):
        self.r, self.g, self.b = cv2.split (self.processing_image)
        self.filtered_image=self.r
        self.master.image_viewer.show_image (img = self.r)
        
    def greenimage (self):
        self.r, self.g, self.b = cv2.split (self.processing_image)
        self.filtered_image=self.g
        self.master.image_viewer.show_image (img = self.g)
        
    def blueimage (self):
        self.r, self.g, self.b = cv2.split (self.processing_image)
        self.filtered_image=self.b
        self.master.image_viewer.show_image (img = self.b)
        
    def mergeimage (self):
        self.r, self.g, self.b = cv2.split (self.processing_image)
        self.image_merge = cv2.merge ([self.r, self.g, self.b])
        self.filtered_image=self.image_merge
        self.master.image_viewer.show_image (img = self.image_merge)
        
    def show_image(self):
        self.master.image_viewer.show_image(img=self.filtered_image)
        
    def close(self):
        self.destroy()

