'''
SC32303 DIGITAL IMAGE PROCESSING
ASSIGNMENT 3
FARAH NURUL AIN BINTI MOHD SUFFIAN @ LAURANCE BS19110258
ANGELI ANAK DAVID BS19110452
'''

import cv2
from tkinter import Toplevel, Button, RIGHT
import numpy as np
from tkinter import *

class ConvertButton(Toplevel):

    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)
        self.iconbitmap("images/doodle.ico")
        self.title("Color Conversion")
        self.geometry("260x100")
        self.config (bg = "#0C2A33")
        
        self.original_image = self.master.processed_image
        self.filtered_image = None
        
        self.labelconvert = LabelFrame (self, text = "Color Conversion", font = ('Lucida Calligraphy', 10, 'bold'), bg = '#0C2A33', fg = 'white')
        self.labelconvert.pack ()
        
        self.grayscaleBtn = Button (self.labelconvert, text = "Grayscale", command = self.convertgrayscale)
        self.grayscaleBtn.pack ()
        
        self.hsvBtn = Button (self.labelconvert, text = "HSV", command = self.converthsv)
        self.hsvBtn.pack ()
        
        self.bgrabtn = Button (self.labelconvert, text = "BGRA", command = self.convertbgra)
        self.bgrabtn.pack ()
        
    def convertgrayscale (self):  
        self.filtered_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        self.filtered_image = cv2.cvtColor(self.filtered_image, cv2.COLOR_GRAY2BGR)
        self.show_image()
        
    def converthsv (self):
        self.filtered_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2HSV)
        self.filtered_image = cv2.cvtColor(self.original_image, cv2.COLOR_HSV2BGR)
        self.show_image()
        
    def convertbgra (self):
        self.filtered_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2BGRA)
        self.filtered_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGRA2BGR)
        self.show_image()

    def show_image(self):
        self.master.image_viewer.show_image(img=self.filtered_image)

    def close(self):
        self.destroy()