'''
SC32303 DIGITAL IMAGE PROCESSING
ASSIGNMENT 3
FARAH NURUL AIN BINTI MOHD SUFFIAN @ LAURANCE BS19110258
ANGELI ANAK DAVID BS19110452
'''

import cv2
from tkinter import Frame, Button, LEFT, RIGHT, filedialog
from convertButton import ConvertButton
from geometric import GeometricFrame
from tkinter import *

from splitmerge import SplitMerge
from histogram1 import Histogram
from filtering import Filtering
from bitslicing import BitSlicing
from combine import Combine

from edgedetection import EdgeDetection
from imagecontour import ImageContour

class ButtonBar(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master=master)
        
        self.open_btn = PhotoImage (file = 'images/open.png')
        self.openbtn = self.open_btn.subsample (3, 3)
        self.openlbl = Label (image = self.openbtn)
        self.open_file_button = Button (self, image = self.openbtn, bg = '#0C2A33')
        
        self.sv_btn = PhotoImage (file = 'images/save.png')
        self.svbtn = self.sv_btn.subsample (3, 3)
        self.svlbl = Label (image = self.svbtn)
        self.save_button = Button (self, image = self.svbtn, bg = '#0C2A33')
        
        self.new_btn = PhotoImage (file = 'images/new.png')
        self.newbtn = self.new_btn.subsample (3, 3)
        self.newlbl = Label (image = self.newbtn)
        self.new_button = Button (self, image = self.newbtn, bg = '#0C2A33')

        self.transformbtn = PhotoImage (file = 'images/transformation.png')
        self.transgeobtn = self.transformbtn.subsample (3, 3)
        self.transformlbl = Label (image = self.transgeobtn)
        self.geometric_button = Button(self, image = self.transgeobtn, bg = '#0C2A33')
        
        self.convert = PhotoImage (file = 'images/convert.png')
        self.convertbtn = self.convert.subsample (3, 3)
        self.convertlbl = Label (image = self.convertbtn)
        self.convert_button = Button(self, image = self.convertbtn, bg = '#0C2A33')
        
        self.draw = PhotoImage (file = 'images/draw.png')
        self.drawbtn = self.draw.subsample (3, 3)
        self.drawlbl = Label (image = self.drawbtn)
        self.draw_button = Button(self, image = self.drawbtn, bg = '#0C2A33')
        
        self.crop = PhotoImage (file = 'images/crop.png')
        self.cropbtn = self.crop.subsample (3, 3)
        self.croplbl = Label (image = self.cropbtn)
        self.crop_button = Button(self, image = self.cropbtn, bg = '#0C2A33')
        
        self.splitmerge = PhotoImage (file = 'images/splitmerge.png')
        self.splitmergebtn = self.splitmerge.subsample (3, 3)
        self.splitmergelbl = Label (image = self.splitmergebtn)
        self.splitmerge_button = Button (self, image = self.splitmergebtn, bg = '#0C2A33')
        
        self.histogram = PhotoImage (file = 'images/histogram.png')
        self.histogrambtn = self.histogram.subsample (3, 3)
        self.histogramlbl = Label (image = self.histogrambtn)
        self.histogram_button = Button (self, image = self.histogrambtn, bg = '#0C2A33')
        
        self.filter = PhotoImage (file = 'images/filter.png')
        self.filterbtn = self.filter.subsample (3, 3)
        self.filterlbl = Label (image = self.filterbtn)
        self.filtering_button = Button (self, image = self.filterbtn, bg = '#0C2A33')
        
        self.bitslice = PhotoImage (file = 'images/bitslice.png')
        self.bitslicebtn = self.bitslice.subsample (3, 3)
        self.bitslicelbl = Label (image = self.bitslicebtn)
        self.bitslicing_button = Button (self, image = self.bitslicebtn, bg = '#0C2A33')
        
        self.combine = PhotoImage (file = 'images/combine.png')
        self.combinebtn = self.combine.subsample (3, 3)
        self.combinelbl = Label (image = self.combinebtn)
        self.combine_button = Button (self, image = self.combinebtn, bg = '#0C2A33')
        
        self.ED = PhotoImage (file = "images/edgedetection.png")
        self.EDbtn = self.ED.subsample (3, 3)
        self.EDlbl = Label (image = self.EDbtn)
        self.edgedetection = Button (self, image = self.EDbtn, bg = '#0C2A33')
        
        self.IC = PhotoImage (file = "images/imagecontour.png")
        self.ICbtn = self.IC.subsample (3, 3)
        self.IClbl = Label (image = self.ICbtn)
        self.imageContour = Button (self, image = self.ICbtn, bg = '#0C2A33')
        
        self.open_file_button.bind("<ButtonRelease>", self.open_file_button_released)        
        self.save_button.bind("<ButtonRelease>", self.save_button_released)
        self.new_button.bind("<ButtonRelease>", self.new_button_released)
        self.draw_button.bind("<ButtonRelease>", self.draw_button_released)
        self.crop_button.bind("<ButtonRelease>", self.crop_button_released)
        self.convert_button.bind("<ButtonRelease>", self.convert_button_released)
        self.geometric_button.bind("<ButtonRelease>", self.geometric_button_released)
        self.splitmerge_button.bind("<ButtonRelease>", self.splitmerge_button_released)
        self.histogram_button.bind("<ButtonRelease>", self.histogram_button_released)
        self.filtering_button.bind("<ButtonRelease>", self.filtering_button_released)
        self.bitslicing_button.bind("<ButtonRelease>", self.bitslicing_button_released)
        self.combine_button.bind("<ButtonRelease>", self.combine_button_released)
        self.edgedetection.bind("<ButtonRelease>", self.edgedetection_button_released)
        self.imageContour.bind("<ButtonRelease>", self.imagecontour_button_released)

        self.open_file_button.pack(side=LEFT)
        self.save_button.pack(side=LEFT)
        self.new_button.pack(side=LEFT)
        self.geometric_button.pack(side=LEFT)
        self.convert_button.pack(side=LEFT)
        self.draw_button.pack(side=LEFT)
        self.crop_button.pack(side=LEFT)
        self.splitmerge_button.pack (side = LEFT)
        self.histogram_button.pack (side = LEFT)
        self.filtering_button.pack (side = LEFT)
        self.bitslicing_button.pack (side = LEFT)
        self.combine_button.pack (side = LEFT)
        self.edgedetection.pack (side = LEFT)
        self.imageContour.pack (side = LEFT)

    def open_file_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.open_file_button:
            if self.master.is_draw_state:
                self.master.image_viewer.deactivate_draw()
            if self.master.is_crop_state:
                self.master.image_viewer.deactivate_crop()

            filename = filedialog.askopenfilename(initialdir="/images",title="select a file",
                                             filetypes=(("jpg files","*.jpg"),("png files","*.png"),
                                                        ("bitmap files","*.bmp"),("all files","*.*")))
            image = cv2.imread(filename)

            if image is not None:
                self.master.filename = filename
                self.master.original_image = image.copy()
                self.master.processed_image = image.copy()
                self.master.image_viewer.show_image()
                self.master.is_image_selected = True
                
    def save_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.save_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                original_file_type = self.master.filename.split('.')[-1]
                filename = filedialog.asksaveasfilename()
                filename = filename + "." + original_file_type

                save_image = self.master.processed_image
                cv2.imwrite(filename, save_image)
                self.master.filename = filename

    def new_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.new_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                    
                filename = filedialog.askopenfilename(initialdir="/images",title="select a file",
                                             filetypes=(("jpg files","*.jpg"),("png files","*.png"),
                                                        ("bitmap files","*.bmp"),("all files","*.*")))
                image = cv2.imread(filename)

                if image is not None:
                    self.master.filename = filename
                    self.master.original_image = image.copy()
                    self.master.processed_image = image.copy()
                    self.master.image_viewer.show_image()
                    self.master.is_image_selected = True
                    
    def draw_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.draw_button:
            if self.master.is_image_selected:
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                else:
                    self.master.image_viewer.activate_draw()

    def crop_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.crop_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                else:
                    self.master.image_viewer.activate_crop()

    def convert_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.convert_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                self.master.filter_frame = ConvertButton(master=self.master)
                self.master.filter_frame.grab_set()
                
    def geometric_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.geometric_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                    
                self.master.others_frame = GeometricFrame(master = self.master)
                self.master.others_frame.grab_set()
                
    def splitmerge_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.splitmerge_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                    
                self.master.others_frame = SplitMerge(master=self.master)
                self.master.others_frame.grab_set()
                
    def histogram_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.histogram_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                    
                self.master.others_frame = Histogram(master=self.master)
                self.master.others_frame.grab_set()
                
    def filtering_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.filtering_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                    
                self.master.others_frame = Filtering(master=self.master)
                self.master.others_frame.grab_set()
    
    def bitslicing_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.bitslicing_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                    
                self.master.others_frame = BitSlicing(master=self.master)
                self.master.others_frame.grab_set()
    
    def combine_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.combine_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                    
                self.master.others_frame = Combine(master=self.master)
                self.master.others_frame.grab_set()
                
    def edgedetection_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.edgedetection:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                    
                self.master.others_frame = EdgeDetection(master=self.master)
                self.master.others_frame.grab_set()
                
    def imagecontour_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.imageContour:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                    
                self.master.others_frame = ImageContour(master=self.master)