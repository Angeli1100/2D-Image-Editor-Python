'''
SC32303 DIGITAL IMAGE PROCESSING
ASSIGNMENT 3
FARAH NURUL AIN BINTI MOHD SUFFIAN @ LAURANCE BS19110258
ANGELI ANAK DAVID BS19110452
'''

import cv2
from tkinter import *
import numpy as np

class BitSlicing(Toplevel):
    
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)
        
        self.iconbitmap("images/doodle.ico")
        self.original_image = self.master.processed_image
        self.processing_image = self.master.processed_image
        self.geometry("220x260")
        self.config (bg = "#0C2A33")
        self.title ("Bit Slicing")
        
        self.labelslicing = LabelFrame (self, text='Bit Plane Slicing Option', pady = 15, font =  ("Lucida Calligraphy", 10, 'bold'), bg = "#0C2A33", fg = 'white')
        self.slicing1_button = Button(self.labelslicing, text="Bit Plane Slicing 0")
        self.slicing2_button = Button(self.labelslicing, text="Bit Plane Slicing 1")
        self.slicing3_button = Button(self.labelslicing, text="Bit Plane Slicing 2")
        self.slicing4_button = Button(self.labelslicing, text="Bit Plane Slicing 3")
        self.slicing5_button = Button(self.labelslicing, text="Bit Plane Slicing 4")
        self.slicing6_button = Button(self.labelslicing, text="Bit Plane Slicing 5")
        self.slicing7_button = Button(self.labelslicing, text="Bit Plane Slicing 6")
        self.slicing8_button = Button(self.labelslicing, text="Bit Plane Slicing 7")

        self.slicing1_button.bind("<ButtonRelease>", self.slicing1_button_released)
        self.slicing2_button.bind("<ButtonRelease>", self.slicing2_button_released)
        self.slicing3_button.bind("<ButtonRelease>", self.slicing3_button_released)
        self.slicing4_button.bind("<ButtonRelease>", self.slicing4_button_released)
        self.slicing5_button.bind("<ButtonRelease>", self.slicing5_button_released)
        self.slicing6_button.bind("<ButtonRelease>", self.slicing6_button_released)
        self.slicing7_button.bind("<ButtonRelease>", self.slicing7_button_released)
        self.slicing8_button.bind("<ButtonRelease>", self.slicing8_button_released)
        
        self.labelslicing.place(x=0,y=0)
        self.slicing1_button.pack()
        self.slicing2_button.pack()
        self.slicing3_button.pack()
        self.slicing4_button.pack()
        self.slicing5_button.pack()
        self.slicing6_button.pack()
        self.slicing7_button.pack()
        self.slicing8_button.pack()
    
    def slicing1_button_released(self, event):
        self.processing_image=cv2.cvtColor (self.original_image, cv2.COLOR_BGR2GRAY)
        r, c = self.processing_image.shape
        x = np.zeros((r, c), dtype=np.uint8)
        x[:, :] = 2**0
        r = np.zeros((r, c), dtype=np.uint8)
        r[:, :] = cv2.bitwise_and(self.processing_image, x[:, :])
        mask = r[:, :] > 0
        r[mask] = 255
        
        self.processing_image = r[:, :]
        self.show_image (self.processing_image)
        
    def slicing2_button_released(self, event):
        self.processing_image=cv2.cvtColor (self.original_image, cv2.COLOR_BGR2GRAY)
        r, c = self.processing_image.shape
        x = np.zeros((r, c), dtype=np.uint8)
        x[:, :] = 2**1
        r = np.zeros((r, c), dtype=np.uint8)
        r[:, :] = cv2.bitwise_and(self.processing_image, x[:, :])
        mask = r[:, :] > 0
        r[mask] = 255
        
        self.processing_image = r[:, :]
        self.show_image (self.processing_image)
        
    def slicing3_button_released(self, event):
        self.processing_image=cv2.cvtColor (self.original_image, cv2.COLOR_BGR2GRAY)
        r, c = self.processing_image.shape
        x = np.zeros((r, c), dtype=np.uint8)
        x[:, :] = 2**2
        r = np.zeros((r, c), dtype=np.uint8)
        r[:, :] = cv2.bitwise_and(self.processing_image, x[:, :])
        mask = r[:, :] > 0
        r[mask] = 255
        
        self.processing_image = r[:, :]
        self.show_image (self.processing_image)
        
    def slicing4_button_released(self, event):
        self.processing_image=cv2.cvtColor (self.original_image, cv2.COLOR_BGR2GRAY)
        r, c = self.processing_image.shape
        x = np.zeros((r, c), dtype=np.uint8)
        x[:, :] = 2**3
        r = np.zeros((r, c), dtype=np.uint8)
        r[:, :] = cv2.bitwise_and(self.processing_image, x[:, :])
        mask = r[:, :] > 0
        r[mask] = 255
        
        self.processing_image = r[:, :]
        self.show_image (self.processing_image)
        
    def slicing5_button_released(self, event):
        self.processing_image=cv2.cvtColor (self.original_image, cv2.COLOR_BGR2GRAY)
        r, c = self.processing_image.shape
        x = np.zeros((r, c), dtype=np.uint8)
        x[:, :] = 2**4
        r = np.zeros((r, c), dtype=np.uint8)
        r[:, :] = cv2.bitwise_and(self.processing_image, x[:, :])
        mask = r[:, :] > 0
        r[mask] = 255
        
        self.processing_image = r[:, :]
        self.show_image (self.processing_image)
        
    def slicing6_button_released(self, event):
        self.processing_image=cv2.cvtColor (self.original_image, cv2.COLOR_BGR2GRAY)
        r, c = self.processing_image.shape
        x = np.zeros((r, c), dtype=np.uint8)
        x[:, :] = 2**5
        r = np.zeros((r, c), dtype=np.uint8)
        r[:, :] = cv2.bitwise_and(self.processing_image, x[:, :])
        mask = r[:, :] > 0
        r[mask] = 255
        
        self.processing_image = r[:, :]
        self.show_image (self.processing_image)
        
    def slicing7_button_released(self, event):
        self.processing_image=cv2.cvtColor (self.original_image, cv2.COLOR_BGR2GRAY)
        r, c = self.processing_image.shape
        x = np.zeros((r, c), dtype=np.uint8)
        x[:, :] = 2**6
        r = np.zeros((r, c), dtype=np.uint8)
        r[:, :] = cv2.bitwise_and(self.processing_image, x[:, :])
        mask = r[:, :] > 0
        r[mask] = 255
        
        self.processing_image = r[:, :]
        self.show_image (self.processing_image)
        
    def slicing8_button_released(self, event):
        self.processing_image=cv2.cvtColor (self.original_image, cv2.COLOR_BGR2GRAY)
        r, c = self.processing_image.shape
        x = np.zeros((r, c), dtype=np.uint8)
        x[:, :] = 2**7 
        r = np.zeros((r, c), dtype=np.uint8)
        r[:, :] = cv2.bitwise_and(self.processing_image, x[:, :])
        mask = r[:, :] > 0
        r[mask] = 255
        
        self.processing_image = r[:, :]
        self.show_image (self.processing_image)
        
    def show_image(self, img = None):
        self.master.image_viewer.show_image(img=img)
        
    def close(self):
        self.destroy()


