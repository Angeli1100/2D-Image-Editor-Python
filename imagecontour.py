'''
SC32303 DIGITAL IMAGE PROCESSING
ASSIGNMENT 3
FARAH NURUL AIN BINTI MOHD SUFFIAN @ LAURANCE BS19110258
ANGELI ANAK DAVID BS19110452
'''
import cv2
from tkinter import *
import numpy as np

class ImageContour():
    
    def __init__(self, master=None):
        self.master = master
        self.original_image = self.master.processed_image
        self.processing_image = self.master.processed_image
        
        self.gray_image = cv2.cvtColor (self.original_image, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold (self.gray_image, 150, 255, cv2.THRESH_BINARY)
        
        contours, hierarchy = cv2.findContours (thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        self.image_copy = self.original_image.copy ()
        cv2.drawContours (self.image_copy, contours, -1, (0, 255, 0), 2, cv2.LINE_AA)
        
        self.show_image (self.image_copy)
        
    def show_image (self, img = None):
       self.master.image_viewer.show_image(img=img)
        
    def close(self):
        self.destroy()