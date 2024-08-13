#import pandas as pd
#import os
#import subprocess, json
#import time
#from pymediainfo import MediaInfo
#import secrets
from Backend import *
from tkinter import *
from Widgets import *
import ctypes
from PIL import Image, ImageTk
from os import startfile

class Window(Tk):
    def __init__(self, vp=r"D:\Videos\Petto", master_csv='porn.csv',
                 icon_filename='icon.png', title='Questionz of Luv', initalll=False):
        print('Doing init.  Please hold')
        u = ctypes.windll.user32
        [self.screenwidth_in_pixels, self.screenheight_in_pixels] = [u.GetSystemMetrics(0), u.GetSystemMetrics(1)]
        self.root = Tk()
        self.backend = BackendFuncs()
        self.root.title(title)
        self.icon = Image.open(icon_filename)
        self.photo = ImageTk.PhotoImage(self.icon)
        self.root.wm_iconphoto(False, self.photo)
        self.backend.write_to_log('init complete')
    
    def set_title(self, title):
        self.title(title)
    
    def scale_image(self):
        pass

    def set_background(self, image):
        self.image_filename = image
        self.image = Image.open(self.image_filename)
        resize_image = self.image.resize((self.window_width, self.window_height))
        img = ImageTk.PhotoImage(resize_image)
        self.image_Lable = Label(self.root, image=img)
        self.image_Lable.image = img
        self.image_Lable.pack()


    def set_window_dimensions(self, width, height):
        self.window_width = int(width)
        self.window_height = int(height)
        self.positionHorizontal = round(self.screenwidth_in_pixels - self.window_width - (.0234375*self.screenwidth_in_pixels))
        self.positionVertical = round(.5*(self.screenheight_in_pixels - height))
        self.backend.write_to_log('screen width is {} height is {}, window width is {} height is {}'.format(
                                                                                        self.screenwidth_in_pixels,
                                                                                        self.screenheight_in_pixels,
                                                                                        width, height))
        self.root.geometry('{}x{}+{}+{}'.format(self.window_width, self.window_height, self.positionHorizontal, self.positionVertical))

    def build_app(self, image=r"Background.png", w=960, h=540):
        self.set_window_dimensions(.95*self.screenwidth_in_pixels, .95*self.screenheight_in_pixels)
        self.set_background(image)

        #Stats Label
        statsLabel = Label_Widget(self.root)
        statsLabelText = 'Stats:\n                 BF                 GF\nScore:            0                 0\nSkips:            1                 1'
        statsLabel.add_widget(statsLabelText)
        good_size = False
        standard_font_size = 1
        while not good_size:
            if statsLabel.width >= (6/32)*self.window_width:
                good_size = True
            elif statsLabel.height >= (16/32)*self.window_width:
                good_size = True
            else:
                standard_font_size = standard_font_size + 1
                statsLabel.change_font_size(standard_font_size)
                if statsLabel.width > (6/32)*self.window_width:
                    statsLabel.change_font_size(standard_font_size-1)
                    standard_font_size = standard_font_size - 1
                    good_size = True
                elif statsLabel.height > (16/32)*self.window_height:
                    statsLabel.change_font_size(standard_font_size-1)
                    standard_font_size = standard_font_size - 1
                    good_size = True
        statsLabel.place_here(1,
                               int(.5*self.screenheight_in_pixels),
                               0, 0)
        
        #skip button
        skipButton = Button_Widget(self.root)
        skipButton.add_widget('Skip', self.backend.skip,
                               multiargument=True, args=[statsLabel])
        skipButton.place_here(int((7/32)*self.window_width), 
                              int((11/18)*self.window_height), 
                              0, 
                              skipButton.height)

        #answer button
        answerButton = Button_Widget(self.root)
        answerButton.add_widget('Answer', self.backend.answer,
                                  multiargument=True,
                                  args=[statsLabel])
        answerButton.place_here(int((21/32)*self.window_width), 
                              int((11/18)*self.window_height), 
                              0, 
                              answerButton.height)

        #buy skip button
        buySkipButton = Button_Widget(self.root)
        buySkipButton.add_widget('Buy Skip', self.backend.buy_skip,
                                  multiargument=True,
                                  args=[statsLabel])
        buySkipButton.place_here(int((14/32)*self.window_width), 
                              int((14/18)*self.window_height), 
                              0, 
                              buySkipButton.height)

        #Names Label
        namesLabel = Label_Widget(self.root)
        namesLabel.add_widget('Names:\nBF:                           \nGF:                           ', 555, 10)
        namesLabel.change_font_size(standard_font_size)
        namesLabel.place_here(1, 1, 0, 0)

        #GF Name Input
        GFInput = Textinput_Widget(self.root)
        GFInput.add_widget(max(len('Evan S. Everett'), len('Laura Parrell')), 1)
        GFInput.place_here(43, 42)

        #GF Name Input
        BFInput = Textinput_Widget(self.root)
        BFInput.add_widget(max(len('Evan S. Everett'), len('Laura Parrell')), 1)
        BFInput.place_here(43, GFInput.y-(GFInput.height/2)-BFInput.height, 0, -1)

        #Rulez Label
        rulesLabel = Label_Widget(self.root)
        rulesLabel.add_widget(self.backend.rulez)
        rulesLabel.change_font_size(standard_font_size)
        rulesLabel.change_width((6/32)*self.window_width)
        rulesLabel.place_here(int((26/32)*self.window_width),
                               int(.5*(self.window_height-rulesLabel.height)),
                               0, -1)

        #Qustion Label
        QustionLable = Label_Widget(self.root)
        QustionLable.add_widget('Please enter your names, hold hands, look into each other eys, and press any buton to begin.')
        QustionLable.change_font_size(standard_font_size)
        QustionLable.place_here(int((1/32)*self.window_width), 
                             int((statsLabel.y+namesLabel.y)/2), 0, 0)

    def display_app(self):
        self.set_window_dimensions(self.window_width, self.window_height)
        self.root.mainloop()

    def destroy_dependant(self, dependant):
        if type(dependant) == type([]):
            for d in dependant:
                try:
                    d.destroy()
                except Exception as err:
                    print('Error: ', err)
        else:
            try:
                dependant.destroy()
            except Exception as error:
                print('Err: ', error)
        self.root.destroy()
