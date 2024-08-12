#import pandas as pd
#import os
#import subprocess, json
#import time
#from pymediainfo import MediaInfo
#import secrets
from Backend import *
from tkinter import *
from tkinter import ttk

class Button_Widget():
    def __init__(self, tk):
        self.root = tk
        self.buttons = []
        self.width = 1
        self.height = 1
        self.x = 1
        self.y = 1
        self.action = ''
        self.actionargs = ''
    
    def add_widget(self, name, action, action_arg='NA', x_pix_loc=1, y_pix_loc=1,
                   ancor='center', rel=False, plaisce=False, multiargument=False, args=[]):
        self.action = action
        self.actionargs = action_arg
        if multiargument:
            if len(args) == 2:
                self.actionargs1 = args[0]
                self.actionargs2 = args[1]
                self.buttons.append(Button(self.root, text=name,
                                        command=lambda: self.action(self.actionargs1, self.actionargs2)))
            elif len(args) == 1:
                self.actionargs1 = args[0]
                self.buttons.append(Button(self.root, text=name,
                                        command=lambda: self.action(self.actionargs1)))
            elif len(args) == 3:
                self.actionargs1 = args[0]
                self.actionargs2 = args[1]
                self.actionargs3 = args[2]
                self.buttons.append(Button(self.root, text=name,
                                        command=lambda: self.action(self.actionargs1, self.actionargs2, self.actionargs3)))
            elif len(args) == 4:
                self.actionargs1 = args[0]
                self.actionargs2 = args[1]
                self.actionargs3 = args[2]
                self.actionargs4 = args[3]
                self.buttons.append(Button(self.root, text=name,
                                        command=lambda: self.action(self.actionargs1,
                                                                    self.actionargs2,
                                                                    self.actionargs3,
                                                                    self.actionargs4)))
            elif len(args) == 5:
                self.actionargs1 = args[0]
                self.actionargs2 = args[1]
                self.actionargs3 = args[2]
                self.actionargs4 = args[3]
                self.actionargs5 = args[4]
                self.buttons.append(Button(self.root, text=name,
                                        command=lambda: self.action(self.actionargs1,
                                                                    self.actionargs2,
                                                                    self.actionargs3,
                                                                    self.actionargs4,
                                                                    self.actionargs5)))
            elif len(args) == 6:
                self.actionargs1 = args[0]
                self.actionargs2 = args[1]
                self.actionargs3 = args[2]
                self.actionargs4 = args[3]
                self.actionargs5 = args[4]
                self.actionargs6 = args[5]
                self.buttons.append(Button(self.root, text=name,
                                        command=lambda: self.action(self.actionargs1,
                                                                    self.actionargs2,
                                                                    self.actionargs3,
                                                                    self.actionargs4,
                                                                    self.actionargs5,
                                                                    self.actionargs6)))
            elif len(args) == 7:
                self.actionargs1 = args[0]
                self.actionargs2 = args[1]
                self.actionargs3 = args[2]
                self.actionargs4 = args[3]
                self.actionargs5 = args[4]
                self.actionargs6 = args[5]
                self.actionargs7 = args[6]
                self.buttons.append(Button(self.root, text=name,
                                        command=lambda: self.action(self.actionargs1,
                                                                    self.actionargs2,
                                                                    self.actionargs3,
                                                                    self.actionargs4,
                                                                    self.actionargs5,
                                                                    self.actionargs6,
                                                                    self.actionargs7)))
            elif len(args) == 8:
                self.actionargs1 = args[0]
                self.actionargs2 = args[1]
                self.actionargs3 = args[2]
                self.actionargs4 = args[3]
                self.actionargs5 = args[4]
                self.actionargs6 = args[5]
                self.actionargs7 = args[6]
                self.actionargs8 = args[7]
                self.buttons.append(Button(self.root, text=name,
                                        command=lambda: self.action(self.actionargs1,
                                                                    self.actionargs2,
                                                                    self.actionargs3,
                                                                    self.actionargs4,
                                                                    self.actionargs5,
                                                                    self.actionargs6,
                                                                    self.actionargs7,
                                                                    self.actionargs8)))
            elif len(args) == 9:
                self.actionargs1 = args[0]
                self.actionargs2 = args[1]
                self.actionargs3 = args[2]
                self.actionargs4 = args[3]
                self.actionargs5 = args[4]
                self.actionargs6 = args[5]
                self.actionargs7 = args[6]
                self.actionargs8 = args[7]
                self.actionargs9 = args[8]
                self.buttons.append(Button(self.root, text=name,
                                        command=lambda: self.action(self.actionargs1,
                                                                    self.actionargs2,
                                                                    self.actionargs3,
                                                                    self.actionargs4,
                                                                    self.actionargs5,
                                                                    self.actionargs6,
                                                                    self.actionargs7,
                                                                    self.actionargs8,
                                                                    self.actionargs9)))
        else:
            self.buttons.append(Button(self.root, text=name, command=lambda: self.action(self.actionargs)))
        if plaisce:
            if rel:
                self.buttons[len(self.buttons)-1].place(relx=x_pix_loc, rely=y_pix_loc, anchor=ancor)
            else:
                self.buttons[len(self.buttons)-1].place(x=x_pix_loc, y=y_pix_loc, anchor=ancor)
        self.width = self.buttons[len(self.buttons)-1].winfo_reqwidth()
        self.height = self.buttons[len(self.buttons)-1].winfo_reqheight()
        self.x = x_pix_loc
        self.y = y_pix_loc

    def place_here(self, xloc, yloc, paddingx, paddingy, ancor='center', rel=False):
        truex = (self.width/2) + paddingx + xloc
        truey = (self.height/2) + paddingy + yloc
        if rel:
            #xcenterpix = 
            self.buttons[len(self.buttons)-1].place(relx=truex, rely=truex, anchor=ancor)
        else:
            self.buttons[len(self.buttons)-1].place(x=truex, y=truey, anchor=ancor)
        self.x = truex
        self.y = truey

    def change_color(self, foreground='', background=''):
        if not foreground == '':
            try:
                self.buttons[0].config(fg=foreground)
            except Exception as err:
                print(err)
        if not background == '':
            try:
                self.buttons[0].config(bg=background)
            except Exception as err:
                print(err)

    def config_width(self, wid_pix=0, ind=0):
        wid = 0
        while self.width < wid_pix:
            self.buttons[ind].config(width=wid)
            self.width = self.buttons[len(self.buttons)-1].winfo_reqwidth()
            wid = wid + 1

    def config_height(self, he_pix=0, ind=0):
        he = 0
        while self.height < he_pix:
            self.buttons[ind].config(height=he)
            self.height = self.buttons[len(self.buttons)-1].winfo_reqheight()
            he = he + 1

    def remove_widget(self, indexes=[]):
        if indexes == []:
            self.buttons = []
        else:
            temp = []
            for index in range(0, len(self.buttons)):
                if index not in indexes:
                    temp.append(self.buttons[index])
            self.buttons = temp
    
    def destroy_widget(self):
        for i in range(0, len(self.buttons)):
            self.buttons[i].destroy()

class Label_Widget():
    def __init__(self, tk):
        self.root = tk
        self.labels = []
        self.width = 1
        self.height = 1
        self.x = 1
        self.y = 1
        self.txt = ''

    def change_color(self, bg_color='', fg_color=''):
        if not (fg_color == ''):
            self.labels[0].config(fg=fg_color)
        if not (bg_color == ''):
            self.labels[0].config(bg=bg_color)

    def change_text(self, text):
        self.labels[0].config(text=text)
        self.txt = text
    
    def add_widget(self, label, xloc=1, yloc=1, ancor='center', rel=False, plaisce=False, w='', h=''):
        self.labels.append(Label(self.root, text=label))
        if (w == '') and (not (h == '')):
            self.labels[len(self.labels)-1].config(height=h)
        elif (not (w == '')) and (h == ''):
            self.labels[len(self.labels)-1].config(width=w)
        elif (not (w == '')) and (not (h == '')):
            self.labels[len(self.labels)-1].config(width=w, height=h)
        if plaisce:
            if rel:
                self.labels[len(self.labels)-1].place(relx=xloc, rely=yloc, anchor=ancor)
            else:
                self.labels[len(self.labels)-1].place(x=xloc, y=yloc, anchor=ancor)
        self.width = self.labels[len(self.labels)-1].winfo_reqwidth()
        self.height = self.labels[len(self.labels)-1].winfo_reqheight()
        self.x = xloc
        self.y = yloc

    def place_here(self, xloc, yloc, paddingx, paddingy, ancor='center', rel=False):
        truex = (self.width/2) + paddingx + xloc
        truey = (self.height/2) + paddingy + yloc
        if rel:
            #xcenterpix = 
            self.labels[len(self.labels)-1].place(relx=truex, rely=truex, anchor=ancor)
        else:
            self.labels[len(self.labels)-1].place(x=truex, y=truey, anchor=ancor)
        self.x = truex
        self.y = truey

    def change_color(self, foreground='', background=''):
        if not foreground == '':
            try:
                self.labels[0].config(fg=foreground)
            except Exception as err:
                print(err)
        if not background == '':
            try:
                self.labels[0].config(bg=background)
            except Exception as err:
                print(err)
    
    def change_font_size(self, font_size):
        self.labels[0].config(font=("Arial", font_size, "bold"))
        self.width = self.labels[len(self.labels)-1].winfo_reqwidth()
        self.height = self.labels[len(self.labels)-1].winfo_reqheight()

class Listbox_widget():
    def __init__(self, tk):
        self.root = tk
        self.listboxess = []
        self.width = 2
        self.height = 2
        self.x = 2
        self.y = 2
        self.options = []

    def get_legnth_of_text_plus_one(self, listeORtext):
        if type(listeORtext) == type('Timothy Wing-kin Koppisch touches children'):
            fh = listeORtext.count('\n') + 1
            fw = len(listeORtext) + 1
        elif type(listeORtext) == type(['Nipples', 'Dick']):
            lish = []
            lisw = []
            for word in listeORtext:
                if not (type(word) == type('277353')):
                    text = str(word)
                else:
                    text = word
                lisw.append(len(text))
                lish.append(listeORtext.count('\n') + 1)
            if lish == []:
                fh = 1
            else:
                fh = max(lish) + 1
            if lisw == []:
                fw = 1
            else:
                fw = max(lisw) + 1
        else:
            print('<text> must be a list or string')
            fw = 1
            fh = 1
        return fw, fh
    
    def populate_box(self, box, liste):
        for item in liste:
            if not ((item == '') or (item == ' ') or (item == '\n')):
                box.insert(END, item)
            if not type(self.options) == type([11037, 45510, 277353]):
                self.options = liste
            else:
                if item not in self.options:
                    if not ((item == '') or (item == ' ') or (item == '\n')):
                        self.options.append(item)
        self.options.sort(key=str.lower)

    def remove_everything(self):
        box = self.listboxess[len(self.listboxess)-1]
        box.delete(0, END)
        self.options = []

    def reset_box(self):
        temp = self.options
        self.remove_everything()
        self.populate_box(self.listboxess[0], temp)

    def config_width(self, wid=0, ind=0):
        self.listboxess[ind].config(width=wid)
        self.width = self.listboxess[len(self.listboxess)-1].winfo_reqwidth()

    def config_height(self, he=0, ind=0):
        self.listboxess[ind].config(height=he)
        self.height = self.listboxess[len(self.listboxess)-1].winfo_reqheight()
    
    def add_widget(self, mode, options, xloc=1, yloc=2, window_width=3, window_height=1,
                   ancor='center', rel=False, plaisce=False):
        self.options = options
        self.options.sort(key=str.lower)
        if mode.lower() == 'single':
            self.listboxess.append(Listbox(self.root, selectmode=SINGLE, exportselection=0))
        elif mode.lower() == 'multiple':
            self.listboxess.append(Listbox(self.root, selectmode=MULTIPLE, exportselection=0))
        le, he = self.get_legnth_of_text_plus_one(options)
        self.listboxess[len(self.listboxess)-1].config(width=le, height=int(((20)*window_height)/640))
        while self.width >= window_width:
            le = le - 1
            self.listboxess[len(self.listboxess)-1].config(width=le, height=int(((20)*window_height)/640))
        self.populate_box(self.listboxess[len(self.listboxess)-1], options)
        if plaisce:
            if rel:
                self.listboxess[len(self.listboxess)-1].place(relx=xloc, rely=yloc, anchor=ancor)
            else:
                self.listboxess[len(self.listboxess)-1].place(x=xloc, y=yloc, anchor=ancor)
        self.width = self.listboxess[len(self.listboxess)-1].winfo_reqwidth()
        self.height = self.listboxess[len(self.listboxess)-1].winfo_reqheight()
        self.x = xloc
        self.y = yloc

    def change_color(self, foreground='', background=''):
        if not foreground == '':
            try:
                self.listboxess[0].config(fg=foreground)
            except Exception as err:
                print(err)
        if not background == '':
            try:
                self.listboxess[0].config(bg=background)
            except Exception as err:
                print(err)

    def place_here(self, xloc, yloc, paddingx, paddingy, ancor='center', rel=False):
        truex = (self.width/2) + paddingx + xloc
        truey = (self.height/2) + paddingy + yloc
        if rel:
            #xcenterpix = 
            self.listboxess[len(self.listboxess)-1].place(relx=truex, rely=truex, anchor=ancor)
        else:
            self.listboxess[len(self.listboxess)-1].place(x=truex, y=truey, anchor=ancor)
        self.x = truex
        self.y = truey

class Textinput_Widget():
    def __init__(self, tk):
        self.root = tk
        self.inputboxes = []
        self.width = 1
        self.height = 1
        self.x = 1
        self.y = 1
    
    def add_widget(self, number_of_characters, number_of_lines, xloc=1, yloc=1, ancor='center', rel=False, plaisce=False):
        self.inputboxes.append(Text(self.root, width=number_of_characters, height=number_of_lines))
        if plaisce:
            if rel:
                self.inputboxes[len(self.inputboxes)-1].place(relx=xloc, rely=yloc, anchor=ancor)
            else:
                self.inputboxes[len(self.inputboxes)-1].place(x=xloc, y=yloc, anchor=ancor)
        self.width = self.inputboxes[len(self.inputboxes)-1].winfo_reqwidth()
        self.height = self.inputboxes[len(self.inputboxes)-1].winfo_reqheight()
        self.x = xloc
        self.y = yloc

    def remove_widget(self, indexes=[]):
        if indexes == []:
            self.inputboxes = []
        else:
            temp = []
            for index in range(0, len(self.inputboxes)):
                if index not in indexes:
                    temp.append(self.inputboxes[index])
            self.inputboxes = temp

    def place_here(self, xloc, yloc, paddingx=1, paddingy=1, ancor='center', rel=False):
        truex = (self.width/2) + paddingx + xloc
        truey = (self.height/2) + paddingy + yloc
        if rel:
            #xcenterpix = 
            self.inputboxes[len(self.inputboxes)-1].place(relx=truex, rely=truex, anchor=ancor)
        else:
            self.inputboxes[len(self.inputboxes)-1].place(x=truex, y=truey, anchor=ancor)
        self.x = truex
        self.y = truey

    def change_color(self, foreground='', background=''):
        if not foreground == '':
            try:
                self.inputboxes[0].config(fg=foreground)
            except Exception as err:
                print(err)
        if not background == '':
            try:
                self.inputboxes[0].config(bg=background)
            except Exception as err:
                print(err)

    def clear(self):
        self.inputboxes[0].delete("1.0",END)

    def get_text_input(self, raw=False):
        if raw:
            return self.inputboxes[0].get(1.0, "end-1c")
        else:
            return str(self.inputboxes[0].get(1.0, "end-1c")).replace('\n', '').strip()
    
    def destroy_widget(self):
        for i in range(0, len(self.inputboxes)):
            self.inputboxes[i].destroy()
        
class Loadingbar_Widget():
    def __init__(self, tk):
        self.root = tk
        self.loadingbar = ''
        self.width = 1
        self.height = 1
        self.x = 1
        self.y = 1
        self.state = 'stopped'
    
    def add_widget(self, orientation='horizontal', mode='indeterminate', width=69,
                   xloc=1, yloc=1, ancor='center', rel=False, plaisce=False):
        self.loadingbar = ttk.Progressbar(self.root, orient=orientation, mode=mode, length=width)
        if plaisce:
            if rel:
                self.loadingbar.place(relx=xloc, rely=yloc, anchor=ancor)
            else:
                self.loadingbar.place(x=xloc, y=yloc, anchor=ancor)
        self.width = self.loadingbar.winfo_reqwidth()
        self.height = self.loadingbar.winfo_reqheight()
        self.x = xloc
        self.y = yloc

    def remove_widget(self, indexes=[]):
        # if indexes == []:
        #     self.inputboxes = []
        # else:
        #     temp = []
        #     for index in range(0, len(self.inputboxes)):
        #         if index not in indexes:
        #             temp.append(self.inputboxes[index])
        #     self.inputboxes = temp
        self.loadingbar = ''

    def place_here(self, xloc, yloc, paddingx=1, paddingy=1, ancor='center', rel=False):
        truex = (self.width/2) + paddingx + xloc
        truey = (self.height/2) + paddingy + yloc
        if rel:
            #xcenterpix = 
            self.loadingbar.place(relx=truex, rely=truex, anchor=ancor)
        else:
            self.loadingbar.place(x=truex, y=truey, anchor=ancor)
        self.x = truex
        self.y = truey

    def start_or_stop(self, option):
        option = str(option).lower()
        if option == 'start':
            self.loadingbar.start()
            self.state = 'started'
        elif option == 'stop':
            self.loadingbar.stop()
            self.state = 'stopped'
        else:
            print('Option {} is not valid.  Will stop the loading bar'.format(option))
            self.loadingbar.stop()
            self.state = 'stopped'

    def change_color(self, foreground='', background=''):
        if not foreground == '':
            try:
                self.loadingbar.config(fg=foreground)
            except Exception as err:
                print(err)
        if not background == '':
            try:
                self.loadingbar.config(bg=background)
            except Exception as err:
                print(err)