'''
SC32303 DIGITAL IMAGE PROCESSING
ASSIGNMENT 3
FARAH NURUL AIN BINTI MOHD SUFFIAN @ LAURANCE BS19110258
ANGELI ANAK DAVID BS19110452
'''

import cv2
import tkinter as tk
from tkinter import *
from buttonBar import ButtonBar
from imageViewer import ImageViewer

class Main(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        
        self.filename = ""
        self.original_image = None
        self.processed_image = None
        self.is_image_selected = True
        self.is_draw_state = False
        self.is_crop_state = False
        self.filter_frame = None
        self.adjust_frame = None

        self.title("2D Image Manipulation Editor")
        self.iconbitmap("images/doodle.ico")

        self.buttonbar = ButtonBar(master=self)
        self.image_viewer = ImageViewer(master=self)

        self.buttonbar.pack(pady=1)
        self.image_viewer.pack(fill=tk.BOTH, padx=10, pady=5, expand=1)
        
        self.createExit ()
        
    def createExit (self):
        self.exit_btn = PhotoImage (file = 'images/exit.png')
        self.exitbtn = self.exit_btn.subsample (3, 3)
        self.exitlbl = Label (image = self.exitbtn)
        self.exit = Button (self, image = self.exitbtn, bg = '#0C2A33', command = self.destroy)
        self.exit.pack (side = BOTTOM)
        
def main():
    root = Main()
    root.mainloop()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__=="__main__":
    main()