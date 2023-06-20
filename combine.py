'''
SC32303 DIGITAL IMAGE PROCESSING
ASSIGNMENT 3
FARAH NURUL AIN BINTI MOHD SUFFIAN @ LAURANCE BS19110258
ANGELI ANAK DAVID BS19110452
'''

import cv2
from tkinter import *
import numpy as np
from tkinter import filedialog
from PIL import Image, ImageTk

class Combine(Toplevel):
    
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)
        
        self.iconbitmap("images/doodle.ico")
        self.title ('Combine Images')
        self.original_image = self.master.processed_image
        self.processing_image = self.master.processed_image
        
        self.newimg = Button (self, text = "Add Image", command = self.newimage)
        self.newimg.pack ()
        
        self.canvas = Canvas(self, bg="#0C2A33", width=400, height=400)
        self.canvas.pack ()
        
        self.combinebutton = Button (self, text = "Combine", command = self.combineimage)
        self.combinebutton.pack ()
        
    def newimage (self):
        self.filename = filedialog.askopenfilename(initialdir="/images",title="select a file",
                                             filetypes=(("jpg files","*.jpg"),("png files","*.png"),
                                                        ("bitmap files","*.bmp"),("all files","*.*")))
        self.image = Image.open(self.filename)
        self.height, self.width = self.image.size

        self.shown_image = self.image.resize((400, 400)) 
        self.images = ImageTk.PhotoImage(self.shown_image)
        
        self.imagesprite_open = self.canvas.create_image(200, 200, image = self.images)
        
        self.labelopen = Label(self, image = self.imagesprite_open)
        self.labelopem.image = self.imagesprite_open
        
    def combineimage (self):
        self.height, self.width = self.master.processed_image.size
        print (self.height, self.width)
        
    def close(self):
        self.destroy()