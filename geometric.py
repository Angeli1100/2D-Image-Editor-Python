'''
SC32303 DIGITAL IMAGE PROCESSING
ASSIGNMENT 3
FARAH NURUL AIN BINTI MOHD SUFFIAN @ LAURANCE BS19110258
ANGELI ANAK DAVID BS19110452
'''
import cv2
from tkinter import *
from tkinter import Toplevel, Button, RIGHT
import numpy as np

class GeometricFrame(Toplevel):
    
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)
        
        self.iconbitmap("images/doodle.ico")
        self.title ("Transformation")
        self.geometry ("250x90")
        self.config (bg = "#0C2A33")
        
        self.original_image = self.master.processed_image
        self.filtered_image = None
        
        self.scaling_button = Button(master=self, text="Scaling")
        self.translation_button = Button(master=self, text="Translation")
        self.rotation_button = Button(master=self, text="Rotation")

        self.scaling_button.bind("<ButtonRelease>", self.scaling_button_released)
        self.translation_button.bind("<ButtonRelease>", self.translation_button_released)
        self.rotation_button.bind("<ButtonRelease>", self.rotation_button_released)

        self.scaling_button.pack()
        self.translation_button.pack()
        self.rotation_button.pack()

    def scaling_button_released(self, null):
        self.scaling(50, 50)
        self.show_image()

    def translation_button_released(self, null):
        self.translation(50, 100)
        self.show_image()
        
    def rotation_button_released(self,rotate):
        self.rotation(90)
        self.show_image()

    def show_image(self):
        self.master.image_viewer.show_image(img=self.filtered_image)

    #resize image
    def scaling(self, width, height):
        self.width=int(self.original_image.shape[1] * width/100)
        self.height=int(self.original_image.shape[0] * height/100)

        dim=(self.width,self.height)
        self.scalling=cv2.resize(self.original_image,dim)
        self.filtered_image = self.scalling
        self.master.image_viewer.show_image(img=self.scalling)
        self.show_image ()
    
    #translate imgage
    def translation(self, tx, ty):
        width,height=self.original_image.shape[:2]
        translationMatrix=np.float32([[1,0,tx],[0,1,ty]])
        self.translateImg=cv2.warpAffine(self.original_image,translationMatrix,(height,width))
        self.filtered_image = self.translateImg
        self.master.image_viewer.show_image(img=self.translateImg)
        self.show_image ()
    
    #image rotate
    def rotation(self,rotate):
        scale=1.0
        centre=(self.original_image.shape[1]/2, self.original_image.shape[0]/2)
        M=cv2.getRotationMatrix2D(centre,rotate,scale)
        self.rotated_images=cv2.warpAffine(self.original_image,M,(self.original_image.shape[0], self.original_image.shape[1]))
        self.filtered_image = self.rotated_images
        self.master.image_viewer.show_image(img=self.rotated_images)
        self.show_image ()

    def close(self):
        self.destroy()
        
        