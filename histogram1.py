'''
SC32303 DIGITAL IMAGE PROCESSING
ASSIGNMENT 3
FARAH NURUL AIN BINTI MOHD SUFFIAN @ LAURANCE BS19110258
ANGELI ANAK DAVID BS19110452
'''
import cv2
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

class Histogram(Toplevel):
    
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)
        
        self.title ("Histogram Equalization")
        self.iconbitmap("images/doodle.ico")
        self.geometry  ("300x100")
        self.config (bg = "#0C2A33")
        
        self.original_image = self.master.processed_image
        self.processing_image = self.master.processed_image
        
        blank=np.zeros(self.processing_image.shape[:2], dtype='uint8')
        
        self.mask=cv2.circle(blank, (self.processing_image.shape[1]//2,self.processing_image.shape[0]//2), 100, 255, -1)
        
        self.labelcolor = LabelFrame (self, text = "Histogram of Colors", font = ('Lucida Calligraphy', 10, 'bold'), bg = '#0C2A33', fg = 'white')
        self.labelcolor.pack ()
        
        self.redcolor = Button (self.labelcolor, text = "Red", bg = 'red', command = self.redcolorhistogram)
        self.redcolor.pack ()
        
        self.greencolor = Button (self.labelcolor, text = "Green", bg = 'green', command = self.greencolorhistogram)
        self.greencolor.pack ()
        
        self.bluecolor = Button (self.labelcolor, text = "Blue", bg = 'blue', command = self.bluecolorhistogram)
        self.bluecolor.pack ()
        
    def redcolorhistogram (self):
        plt.figure()
        plt.title('Red Colour Histogram')
        plt.xlabel('Bins')
        plt.ylabel('# of pixels')
        colors = 'r'
        for i,col in enumerate(colors):
            hist = cv2.calcHist([self.processing_image], [i], self.mask, [256], [0,256])
            plt.plot(hist, color=col)
            plt.xlim([0,256])
            plt.show()
            
    def greencolorhistogram (self):
        plt.figure()
        plt.title('Green Colour Histogram')
        plt.xlabel('Bins')
        plt.ylabel('# of pixels')
        colors = 'g'
        for i,col in enumerate(colors):
            hist = cv2.calcHist([self.processing_image], [i], self.mask, [256], [0,256])
            plt.plot(hist, color=col)
            plt.xlim([0,256])
            plt.show()
            
    def bluecolorhistogram (self):
        plt.figure()
        plt.title('Blue Colour Histogram')
        plt.xlabel('Bins')
        plt.ylabel('# of pixels')
        colors = 'b'
        for i,col in enumerate(colors):
            hist = cv2.calcHist([self.processing_image], [i], self.mask, [256], [0,256])
            plt.plot(hist, color=col)
            plt.xlim([0,256])
            plt.show()
        
    def close(self):
        self.destroy()