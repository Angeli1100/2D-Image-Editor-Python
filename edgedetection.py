'''
SC32303 DIGITAL IMAGE PROCESSING
ASSIGNMENT 3
FARAH NURUL AIN BINTI MOHD SUFFIAN @ LAURANCE BS19110258
ANGELI ANAK DAVID BS19110452
'''
import cv2
from tkinter import *
import numpy as np

class EdgeDetection(Toplevel):
    
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)
        
        self.iconbitmap("images/doodle.ico")
        self.title ('Edge Detection')
        self.geometry("250x125")
        self.config (bg = "#0C2A33")
        self.original_image = self.master.processed_image
        self.processing_image = self.master.processed_image
        
        self.cannyEdgeDetection = Button (self, text = "Canny Edge Detection", command = self.cannyED)
        self.cannyEdgeDetection.place (x = 65, y = 5)
        
        self.prewittEdgeDetection = Button (self, text = "Prewitt Edge Detection", command = self.prewittED)
        self.prewittEdgeDetection.place (x = 65, y = 35)
        
        self.sobelEdgeDetection = Button (self, text = "Sobel Edge Detection", command = self.sobelED)
        self.sobelEdgeDetection.place (x = 70, y = 65)
        
        self.robertEdgeDetection = Button (self, text = "Roberts Edge Detection", command = self.robertsED)
        self.robertEdgeDetection.place (x = 65, y = 95)
        
    def cannyED (self):
        self.processing_image = cv2.cvtColor (self.original_image, cv2.COLOR_BGR2GRAY)
        
        self.blurred = cv2.GaussianBlur(self.processing_image, (3, 3), 0)
        
        self.img_canny = cv2.Canny(self.blurred, 100, 200)
        
        self.processing_image = self.img_canny
        self.show_image(self.processing_image)
        self.close()
        
    def prewittED (self):
        self.processing_image = cv2.cvtColor (self.original_image, cv2.COLOR_BGR2GRAY)
        
        self.blurred = cv2.GaussianBlur(self.processing_image, (3, 3), 0)
        
        kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=int)
        kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=int)
        x = cv2.filter2D(self.blurred, cv2.CV_16S, kernelx)
        y = cv2.filter2D(self.blurred, cv2.CV_16S, kernely)
        
        #  Convert to uint8
        absX = cv2.convertScaleAbs(x)
        absY = cv2.convertScaleAbs(y)
        self.prewitt = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
        
        self.processing_image = self.prewitt
        self.show_image(self.processing_image)
        self.close()
        
    def sobelED (self):
        self.processing_image = cv2.cvtColor (self.original_image, cv2.COLOR_BGR2GRAY)
        
        self.blurred = cv2.GaussianBlur(self.processing_image, (3, 3), 0)

        x = cv2.Sobel(self.blurred, cv2.CV_16S, 1, 0)
        y = cv2.Sobel(self.blurred, cv2.CV_16S, 0, 1)
        
        #  Convert to uint8
        absX = cv2.convertScaleAbs(x)
        absY = cv2.convertScaleAbs(y)
        self.sobels = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
        
        self.processing_image = self.sobels
        self.show_image(self.processing_image)
        self.close()
    
    def robertsED (self):
        self.processing_image = cv2.cvtColor (self.original_image, cv2.COLOR_BGR2GRAY)
        
        self.blurred = cv2.GaussianBlur(self.processing_image, (3, 3), 0)
        
        kernelx = np.array([[-1, 0], [0, 1]], dtype=int)
        kernely = np.array([[0, -1], [1, 0]], dtype=int)
        x = cv2.filter2D(self.blurred, cv2.CV_16S, kernelx)
        y = cv2.filter2D(self.blurred, cv2.CV_16S, kernely)
        #  Convert to uint8
        absX = cv2.convertScaleAbs(x)
        absY = cv2.convertScaleAbs(y)
        self.Roberts = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
        
        self.processing_image = self.Roberts
        self.show_image(self.processing_image)
        self.close()
        
    def show_image(self, img = None):
        self.master.image_viewer.show_image(img=img)
        
    def close(self):
        self.destroy()