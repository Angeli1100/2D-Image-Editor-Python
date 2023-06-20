'''
SC32303 DIGITAL IMAGE PROCESSING
ASSIGNMENT 3
FARAH NURUL AIN BINTI MOHD SUFFIAN @ LAURANCE BS19110258
ANGELI ANAK DAVID BS19110452
'''
import cv2
from tkinter import *
import numpy as np

class Filtering(Toplevel):
    
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)
        
        self.title("Average & Median Blur")
        self.iconbitmap("images/doodle.ico")
        self.geometry("300x150")
        self.config (bg = "#0C2A33")
        
        self.original_image = self.master.processed_image
        self.processing_image = self.master.processed_image
        self.filtering_image = None

        self.labelAverage = LabelFrame (self, text='Average Filter', pady = 15, font = ("Lucida Calligraphy", 10, 'bold'), bg = "#0C2A33", fg = 'white')
        self.average_three_button = Button (self.labelAverage, text='Average: 3 x 3')
        self.average_five_button = Button (self.labelAverage, text='Average: 5 x 5')
        self.average_seven_button = Button (self.labelAverage, text='Average: 7 x 7')
        self.labelMedian = LabelFrame (self, text='Median Filter', pady = 15, font = ("Lucida Calligraphy", 10, 'bold'), bg = "#0C2A33", fg = 'white')
        self.median_three_button = Button (self.labelMedian, text='Median: 3 x 3')
        self.median_five_button = Button (self.labelMedian, text='Median: 5 x 5')
        self.median_seven_button = Button (self.labelMedian, text='Median: 7 x 7')
        
        self.average_three_button.bind("<ButtonRelease>", self.average_three_button_released)
        self.average_five_button.bind("<ButtonRelease>", self.average_five_button_released)
        self.average_seven_button.bind("<ButtonRelease>", self.average_seven_button_released)
        self.median_three_button.bind("<ButtonRelease>", self.median_three_button_released)
        self.median_five_button.bind("<ButtonRelease>", self.median_five_button_released)
        self.median_seven_button.bind("<ButtonRelease>", self.median_seven_button_released)
        
        self.labelAverage.place(x=15,y=0)
        self.average_three_button.pack()
        self.average_five_button.pack()
        self.average_seven_button.pack()
        self.labelMedian.place(x=160,y=0)
        self.median_three_button.pack()
        self.median_five_button.pack()
        self.median_seven_button.pack()
    
    def average_three_button_released(self, event):
        self.filtered_image = cv2.blur(self.original_image, (3,3))
        self.filtered_image = cv2.blur(self.filtered_image, (3,3))
        self.show_image()
        
    def average_five_button_released(self, event):
        self.filtered_image = cv2.blur(self.original_image, (5,5))
        self.filtered_image = cv2.blur(self.filtered_image, (5,5))
        self.show_image()
        
    def average_seven_button_released(self, event):
        self.filtered_image = cv2.blur(self.original_image, (7,7))
        self.filtered_image = cv2.blur(self.filtered_image, (7,7))
        self.show_image()
        
    def median_three_button_released(self, event):
        self.filtered_image = cv2.medianBlur(self.original_image, (3))
        self.filtered_image = cv2.medianBlur(self.filtered_image, (3))
        self.show_image()
        
    def median_five_button_released(self, event):
        self.filtered_image = cv2.medianBlur(self.original_image, (5))
        self.filtered_image = cv2.medianBlur(self.filtered_image, (5))
        self.show_image()
        
    def median_seven_button_released(self, event):
        self.filtered_image = cv2.medianBlur(self.original_image, (7))
        self.filtered_image = cv2.medianBlur(self.filtered_image, (7))
        self.show_image()
        
    def show_image(self):
        self.master.image_viewer.show_image(img=self.filtered_image)
        
    def close(self):
        self.destroy()

