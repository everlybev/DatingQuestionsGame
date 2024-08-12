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
                 icon_filename='icon.png', title='Evan\'s Porn GUI', initalll=False):
        print('Doing init.  Please hold')
        u = ctypes.windll.user32
        [self.screenwidth_in_pixels, self.screenheight_in_pixels] = [u.GetSystemMetrics(0), u.GetSystemMetrics(1)]
        #self.waiting_window = self.create_initial_window()
        self.root = Tk()
        self.baq = BackendFuncs('', '', do_everything=False,
                                w=self.screenwidth_in_pixels, h=self.screenheight_in_pixels, make_window=True)
        self.baq.write_to_log('\n\n\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        separater = '===================================================================='
        vp = self.baq.get_lines_between_separator(separater)[0]
        separater = '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
        master_csv = self.baq.get_lines_between_separator(separater)[0]
        separater = '--------------------------------------------------------------------'
        icon_filename = self.baq.get_lines_between_separator(separater)[0]
        separater = '````````````````````````````````````````````````````````````````````'
        title = self.baq.get_lines_between_separator(separater)[0]
        #exit()
        self.backend = BackendFuncs(vp, master_csv, do_initial=initalll)
        #print(self.screenwidth_in_pixels, self.screenheight_in_pixels)
        self.root.title(title)
        self.icon = Image.open(icon_filename)
        self.photo = ImageTk.PhotoImage(self.icon)
        self.root.wm_iconphoto(False, self.photo)
        # self.baq.initial_root.lift()
        # self.baq.initial_root.attributes("-topmost", True)
        # self.baq.initial_root.focus_force()
        self.backend.write_to_log('init complete')
    
    def set_title(self, title):
        self.title(title)
    
    def scale_image(self):
        pass

    def set_background(self, image):
        self.image_filename = image
        # self.image_Lable = Label(self.root)
        # self.image_Lable.image = PhotoImage(file=self.image_filename)
        # self.image_Lable['image'] = self.image_Lable.image
        # self.image_Lable.pack()
        self.image = Image.open(self.image_filename)
        resize_image = self.image.resize((self.window_width, self.window_height))
        img = ImageTk.PhotoImage(resize_image)
        self.image_Lable = Label(self.root, image=img)
        self.image_Lable.image = img
        self.image_Lable.pack()


    def set_window_dimensions(self, width, height):
        self.window_width = width
        self.window_height = height
        self.positionHorizontal = round(self.screenwidth_in_pixels - self.window_width - (.0234375*self.screenwidth_in_pixels))
        self.positionVertical = round(.5*(self.screenheight_in_pixels - height))
        self.backend.write_to_log('screen width is {} height is {}, window width is {} height is {}'.format(
                                                                                        self.screenwidth_in_pixels,
                                                                                        self.screenheight_in_pixels,
                                                                                        width, height))
        self.root.geometry('{}x{}+{}+{}'.format(width, height, self.positionHorizontal, self.positionVertical))

    def build_app(self, image=r"Background.png", w=960, h=540):
        self.backend.write_to_log('Building')
        self.set_window_dimensions(w, h)
        separater = '????????????????????????????????????????????????????????????????????'
        image = self.baq.get_lines_between_separator(separater)[0]
        self.set_background(image)
        viewFilters = Button_Widget(self.root)


        Total_Hours_of_Porn = Label_Widget(self.root)
        sortTime = Button_Widget(self.root)
        sortAlpha = Button_Widget(self.root)
        unsortFromCSV = Button_Widget(self.root)


        pornstarList = Listbox_widget(self.root)
        pornstarList.add_widget('Multiple', self.backend.list_of_pornstars, 555, 200,
                     self.screenwidth_in_pixels, 2*self.screenheight_in_pixels/3)
        pornstarList.change_color('#01080f', '#effffe')
        pornstarList.place_here(1, 31, 1, 1)
        pornstarlistx = pornstarList.width
        pornstarlisty = pornstarList.height
        
        pornstarADD = Button_Widget(self.root)
        pornstarADD.add_widget('Add', self.backend.add_pornstars_to_search,
                               multiargument=True, args=[pornstarList.listboxess[0], viewFilters])
        pornstarADD.place_here(pornstarList.width+1, 40, 1, 1)
        pornstarADDx = pornstarADD.x
        pornstarADDy = pornstarADD.y

        pornstarRemove = Button_Widget(self.root)
        pornstarRemove.add_widget('Remove', self.backend.remove_pornstars_from_search,
                                  multiargument=True,
                                  args=[pornstarList.listboxess[0], viewFilters])
        pornstarRemove.place_here(pornstarlistx+1, pornstarADDy+(pornstarRemove.height/2), 2, 3)

        pornstarExclude = Button_Widget(self.root)
        pornstarExclude.add_widget('Exclude', self.backend.set_desire,
                                   multiargument=True,
                                   args=[self.backend.desired_or_undesired_options[1]])
        pornstarExclude.place_here(pornstarlistx+1, pornstarRemove.y+(pornstarExclude.height/2), 3, 4)

        pornstarInclude = Button_Widget(self.root)
        pornstarInclude.add_widget('Include', self.backend.set_desire,
                                   multiargument=True,
                                   args=[self.backend.desired_or_undesired_options[0]])
        pornstarInclude.place_here(pornstarlistx+1,
                                pornstarExclude.y+(pornstarInclude.height/2), 3, 4)

        pornstarLabel = Label_Widget(self.root)
        pornstarLabel.add_widget('Pornstars', 555, 10)
        pornstarLabel.place_here(pornstarList.x/2, 5, 0, 1)


        genreList = Listbox_widget(self.root)
        genreList.add_widget('Multiple', self.backend.list_of_genres, 555, 200,
                     self.screenwidth_in_pixels, int(1.5*self.screenheight_in_pixels/3))
        genreList.change_color('#01080f', '#f0effe')
        longest_buttonx = max(pornstarExclude.x, pornstarRemove.x, pornstarADD.x)
        longest_buttonw = max(pornstarExclude.width, pornstarRemove.width, pornstarADD.width)
        genreListCenterX = longest_buttonx+longest_buttonw+1
        genreList.place_here(genreListCenterX, 31, 1, 1)
        
        genreADD = Button_Widget(self.root)
        genreADD.add_widget('Add', self.backend.add_genres_to_search,
                            multiargument=True,
                            args=[genreList.listboxess[0], viewFilters])
        genreADD.place_here(genreListCenterX+genreList.width+1, 40, 1, 1)

        genreRemove = Button_Widget(self.root)
        genreRemove.add_widget('Remove', self.backend.remove_genres_from_search,
                                multiargument=True,
                                args=[genreList.listboxess[0], viewFilters])
        genreRemove.place_here(genreListCenterX+genreList.width+1, genreADD.y+(genreRemove.height/2), 2, 3)

        genreExclude = Button_Widget(self.root)
        genreExclude.add_widget('Exclude', self.backend.set_desire,
                                multiargument=True,
                                args=[self.backend.desired_or_undesired_options[1], viewFilters])
        genreExclude.place_here(genreListCenterX+genreList.width+1, genreRemove.y+(genreExclude.height/2), 3, 4)

        genreInclude = Button_Widget(self.root)
        genreInclude.add_widget('Include', self.backend.set_desire,
                                multiargument=True,
                                args=[self.backend.desired_or_undesired_options[0], viewFilters])
        genreInclude.place_here(genreListCenterX+genreList.width+1, genreExclude.y+(genreInclude.height/2), 3, 4)

        genreLabel = Label_Widget(self.root)
        genreLabel.add_widget('Genres', 555, 10)
        genreLabel.place_here(genreList.x-(genreLabel.width/2), 5, 0, 1)


        ethnicitiesList = Listbox_widget(self.root)
        ethnicitiesList.add_widget('Multiple', self.backend.list_of_ethnicities, 555, 200,
                     self.screenwidth_in_pixels, (self.screenheight_in_pixels/3))
        ethnicitiesList.change_color('#01080f', '#feefff')
        longest_buttonx = max(genreExclude.x, genreRemove.x, genreADD.x)
        longest_buttonw = max(genreExclude.width, genreRemove.width, genreADD.width)
        ethnicitiesListCenterX = longest_buttonx+longest_buttonw+1
        ethnicitiesList.place_here(ethnicitiesListCenterX, 31, 1, 1)
        
        ethnicitiesADD = Button_Widget(self.root)
        ethnicitiesADD.add_widget('Add', self.backend.add_ethnicities_to_search,
                                  multiargument=True,
                                  args=[ethnicitiesList.listboxess[0], viewFilters])
        ethnicitiesADD.place_here(ethnicitiesListCenterX+ethnicitiesList.width+1, 40, 1, 1)

        ethnicitiesRemove = Button_Widget(self.root)
        ethnicitiesRemove.add_widget('Remove', self.backend.remove_ethnicities_from_search,
                                     multiargument=True,
                                     args=[ethnicitiesList.listboxess[0], viewFilters])
        ethnicitiesRemove.place_here(ethnicitiesListCenterX+ethnicitiesList.width+1,
                                     ethnicitiesADD.y+(ethnicitiesRemove.height/2), 2, 3)

        ethnicitiesExclude = Button_Widget(self.root)
        ethnicitiesExclude.add_widget('Exclude', self.backend.set_desire,
                                    multiargument=True,
                                    args=[self.backend.desired_or_undesired_options[1], viewFilters])
        ethnicitiesExclude.place_here(ethnicitiesListCenterX+ethnicitiesList.width+1,
                                      ethnicitiesRemove.y+(ethnicitiesExclude.height/2), 3, 4)

        ethnicitiesInclude = Button_Widget(self.root)
        ethnicitiesInclude.add_widget('Include', self.backend.set_desire,
                                    multiargument=True,
                                    args=[self.backend.desired_or_undesired_options[0], viewFilters])
        ethnicitiesInclude.place_here(ethnicitiesListCenterX+ethnicitiesList.width+1,
                                ethnicitiesExclude.y+(ethnicitiesInclude.height/2), 3, 4)

        ethnicitiesLabel = Label_Widget(self.root)
        ethnicitiesLabel.add_widget('Ethnicities', 555, 10)
        ethnicitiesLabel.place_here(ethnicitiesList.x-(ethnicitiesLabel.width/2), 5, 0, 1)


        hoursInput = Textinput_Widget(self.root)
        hoursInput.add_widget(2, 1)
        leftWidgetX = max([ethnicitiesInclude.x, ethnicitiesExclude.x, ethnicitiesADD.x, ethnicitiesRemove.x])
        widget_widths = [ethnicitiesInclude.width, ethnicitiesExclude.width,
                         ethnicitiesADD.width, ethnicitiesRemove.width]
        leftWidgetw = max(widget_widths)
        hoursInput.place_here(leftWidgetX+leftWidgetw, ethnicitiesList.y-(ethnicitiesList.height/2))
        
        hoursButton = Button_Widget(self.root)
        hoursButton.add_widget('H', self.backend.update_hours, multiargument=True,
                               args=[hoursInput.inputboxes[len(hoursInput.inputboxes)-1], viewFilters])
        hoursButton.place_here(hoursInput.x+(hoursInput.width/2)+1, hoursInput.y-(hoursInput.height/2), 1, -1)


        minutesInput = Textinput_Widget(self.root)
        minutesInput.add_widget(2, 1)
        minutesInput.place_here(hoursButton.x+(hoursButton.width/2), ethnicitiesList.y-(ethnicitiesList.height/2))
        
        minutesButton = Button_Widget(self.root)
        minutesButton.add_widget('M', self.backend.update_minutes, multiargument=True,
                                 args=[minutesInput.inputboxes[len(minutesInput.inputboxes)-1], viewFilters])
        minutesButton.place_here(minutesInput.x+(minutesInput.width/2)+1,
                                 minutesInput.y-(minutesInput.height/2), 1, -1)


        secondsInput = Textinput_Widget(self.root)
        secondsInput.add_widget(4, 1)
        secondsInput.place_here(minutesButton.x+(minutesButton.width/2), ethnicitiesList.y-(ethnicitiesList.height/2))
        
        secondsButton = Button_Widget(self.root)
        secondsButton.add_widget('S', self.backend.update_seconds, multiargument=True,
                                 args=[secondsInput.inputboxes[len(secondsInput.inputboxes)-1], viewFilters])
        secondsButton.place_here(secondsInput.x+(secondsInput.width/2)+1,
                                 secondsInput.y-(secondsInput.height/2), 1, -1)
        

        EqualsButton = Button_Widget(self.root)
        comparor = '='
        EqualsButton.add_widget(comparor, self.backend.update_comparator, comparor, 222, 123)
        EqualsButton.place_here(hoursInput.x-hoursInput.width/2,
                                 hoursInput.y+(hoursInput.height), 1, -1)
        leftwidgetx = EqualsButton.x
        leftWidgetw = EqualsButton.width
        
        GreaterthanEqualsButton = Button_Widget(self.root)
        comparor = '>='
        GreaterthanEqualsButton.add_widget(comparor, self.backend.update_comparator, comparor, 222, 123)
        GreaterthanEqualsButton.place_here(leftwidgetx+leftWidgetw/2,
                                 hoursInput.y+(hoursInput.height), 1, -1)
        leftwidgetx = GreaterthanEqualsButton.x
        leftWidgetw = GreaterthanEqualsButton.width
        
        LessthanEqualsButton = Button_Widget(self.root)
        comparor = '<='
        LessthanEqualsButton.add_widget(comparor, self.backend.update_comparator, comparor, 222, 123)
        LessthanEqualsButton.place_here(leftwidgetx+leftWidgetw/2,
                                 hoursInput.y+(hoursInput.height), 1, -1)
        leftwidgetx = LessthanEqualsButton.x
        leftWidgetw = LessthanEqualsButton.width
        
        NotEqualsButton = Button_Widget(self.root)
        comparor = '!='
        NotEqualsButton.add_widget(comparor, self.backend.update_comparator, comparor, 222, 123)
        NotEqualsButton.place_here(leftwidgetx+leftWidgetw/2,
                                 hoursInput.y+(hoursInput.height), 1, -1)
        leftwidgetx = NotEqualsButton.x
        leftWidgetw = NotEqualsButton.width
        
        LessButton = Button_Widget(self.root)
        comparor = '<'
        LessButton.add_widget(comparor, self.backend.update_comparator, comparor, 222, 123)
        LessButton.place_here(leftwidgetx+leftWidgetw/2,
                                 hoursInput.y+(hoursInput.height), 1, -1)
        leftwidgetx = LessButton.x
        leftWidgetw = LessButton.width
        
        GreatButton = Button_Widget(self.root)
        comparor = '>'
        GreatButton.add_widget(comparor, self.backend.update_comparator, comparor, 222, 123)
        GreatButton.place_here(leftwidgetx+leftWidgetw/2,
                                 hoursInput.y+(hoursInput.height), 1, -1)
        leftwidgetx = GreatButton.x
        leftWidgetw = GreatButton.width


        FilteredList = Listbox_widget(self.root)
        FilteredList.add_widget('Single', self.backend.list_of_filez_from_dataframe(self.backend.filtereddataframe),
                                'Not using', 'Not using',
                     self.screenwidth_in_pixels, (self.screenheight_in_pixels/1.75))
        FilteredList.change_color('#01080f', '#eeffee')
        FilteredList.place_here(1, pornstarList.x+pornstarList.width*2, 1, 5)


        List_of_Folders = Listbox_widget(self.root)

        
        PlayButton = Button_Widget(self.root)
        # PlayButton.add_widget('Play', self.backend.play_video,
        #                       FilteredList, 222, 123)

        ##add_widget('Filter', self.backend.complete_filter, multiargument=True, args=[FilteredList, viewFilters])
        PlayButton.add_widget('Play', self.backend.play_video, multiargument=True, args=[FilteredList,
                                                                                         Total_Hours_of_Porn,
                                                                                         FilteredList,
                                                                                         List_of_Folders]
                                                                                         )
        PlayButton.place_here(1, FilteredList.y+(FilteredList.height/2), 1, 8)
        
        PlayRandomButton = Button_Widget(self.root)
        # #add_widget('Play', self.backend.play_video, multiargument=True, args=[FilteredList,
        #                                                                                  Total_Hours_of_Porn]
        #                                                                                  )
        # PlayRandomButton.add_widget('Filter Random', self.backend.play_random_video,
        #                       self.backend.filtereddataframe, 222, 123)
        PlayRandomButton.add_widget('Filter Random', self.backend.play_random_video,
                              multiargument=True, args=[self.backend.filtereddataframe, Total_Hours_of_Porn,
                                                                                         FilteredList,
                                                                                         List_of_Folders])
        PlayRandomButton.place_here(PlayButton.x+PlayButton.width, FilteredList.y+(FilteredList.height/2), 2, 8)
        
        TrueRandomButton = Button_Widget(self.root)
        # TrueRandomButton.add_widget('True Random', self.backend.play_random_video_for_real,
        #                       self.backend.filtereddataframe, 222, 123)
        TrueRandomButton.add_widget('True Random', self.backend.play_random_video_for_real, multiargument=True,
                              args=[self.backend.filtereddataframe, Total_Hours_of_Porn,
                                    FilteredList, List_of_Folders])
        TrueRandomButton.place_here(PlayRandomButton.x+PlayRandomButton.width,
                                    FilteredList.y+(FilteredList.height/2), 2, 8)
        
        
        FilterButton = Button_Widget(self.root)
        FilterButton.add_widget('Filter', self.backend.complete_filter, multiargument=True,
                              args=[FilteredList, viewFilters, Total_Hours_of_Porn,
                                    [sortAlpha, sortTime, unsortFromCSV]])
        FilterButton.place_here(secondsButton.x+secondsButton.width, LessButton.y-LessButton.height/4, 0, 0)
        
        ClearButton = Button_Widget(self.root)
        AnimatedLabel = Label_Widget(self.root)
        AnimatedLabel.add_widget(self.backend.animated, 'Not', 'Used', w=len('False'))
        FilenameSearchInput = Textinput_Widget(self.root)
        FilenameChangeInput = Textinput_Widget(self.root)
        ClearButton.add_widget('Clear', self.backend.clear_everything, multiargument=True,
                              args=[FilteredList, AnimatedLabel, viewFilters,
                                    [FilenameSearchInput,
                                    #[FilenameSearchInput, FilenameChangeInput,
                                     hoursInput, minutesInput, secondsInput],
                                     [List_of_Folders],
                                     [sortTime, unsortFromCSV, sortAlpha],
                                     Total_Hours_of_Porn])
        ClearButton.place_here(FilterButton.x+FilterButton.width/2, FilterButton.y-FilterButton.height/2, 0, 0)


        FilenameChangeInput.add_widget(26, 1)
        FilenameChangeInput.place_here(EqualsButton.x-EqualsButton.width/2, EqualsButton.y+(EqualsButton.height/2),
                                       paddingy=10)
        
        renameButton = Button_Widget(self.root)
        renameButton.add_widget('Rename', self.backend.rename_file, 'NA', 'NA', 'NA',
                   multiargument=True, args=[FilenameChangeInput.inputboxes[0], FilteredList])
        renameButtonyPadding = 1
        renameButtonxPadding = 1
        renameButton.place_here(FilenameChangeInput.x+(FilenameChangeInput.width/2)+1,
                                 FilenameChangeInput.y-FilenameChangeInput.height/2,
                                 renameButtonxPadding, renameButtonyPadding)


        pornstarUpdate = Button_Widget(self.root)
        pornstarUpdate.add_widget('Update', self.backend.update_field,
                                   self.backend.desired_or_undesired_options[0], 123,
                                   222,multiargument=True,
                                   args=[pornstarList.listboxess[0], FilteredList, 'Pornstars'])
        pornstarUpdate.place_here(pornstarlistx+1,
                                pornstarInclude.y+(pornstarUpdate.height/2), 3, 4)
        
        pornstardeUpdate = Button_Widget(self.root)
        pornstardeUpdate.add_widget('DeUpdate', self.backend.deupdate_field,
                                   'NA', 'NA', 'NA',multiargument=True,
                                   args=[pornstarList.listboxess[0], FilteredList, 'Pornstars'])
        pornstardeUpdate.place_here(pornstarlistx+1,
                                pornstarUpdate.y+(pornstardeUpdate.height/2), 3, 4)


        genreUpdate = Button_Widget(self.root)
        genreUpdate.add_widget('Update', self.backend.update_field,
                                   self.backend.desired_or_undesired_options[0], 123,
                                   222,multiargument=True,
                                   args=[genreList.listboxess[0], FilteredList, 'Genres'])
        genreUpdate.place_here(genreListCenterX+genreList.width+1,
                                genreInclude.y+(genreUpdate.height/2), 3, 4)
        
        genredeUpdate = Button_Widget(self.root)
        genredeUpdate.add_widget('DeUpdate', self.backend.deupdate_field,
                                   'NA', 'NA', 'NA',multiargument=True,
                                   args=[genreList.listboxess[0], FilteredList, 'Genres'])
        genredeUpdate.place_here(genreListCenterX+genreList.width+1,
                                genreUpdate.y+(genredeUpdate.height/2), 3, 4)


        ethnicityUpdate = Button_Widget(self.root)
        ethnicityUpdate.add_widget('Update', self.backend.update_field,
                                   self.backend.desired_or_undesired_options[0], 123,
                                   222,multiargument=True,
                                   args=[ethnicitiesList.listboxess[0], FilteredList, 'Ethnicities'])
        ethnicityUpdate.place_here(ethnicitiesListCenterX+ethnicitiesList.width+1,
                                      ethnicitiesInclude.y+(ethnicityUpdate.height/2), 3, 4)
        
        ethnicitydeUpdate = Button_Widget(self.root)
        ethnicitydeUpdate.add_widget('DeUpdate', self.backend.deupdate_field,
                                   'NA', 'NA', 'NA',multiargument=True,
                                   args=[ethnicitiesList.listboxess[0], FilteredList, 'Ethnicities'])
        ethnicitydeUpdate.place_here(ethnicitiesListCenterX+ethnicitiesList.width+1,
                                ethnicityUpdate.y+(ethnicitydeUpdate.height/2), 3, 4)


        genreUpdate = Button_Widget(self.root)
        genreUpdate.add_widget('Update', self.backend.update_field,
                                   self.backend.desired_or_undesired_options[0], 123,
                                   222,multiargument=True,
                                   args=[genreList.listboxess[0], FilteredList, 'Genres'])
        genreUpdate.place_here(genreListCenterX+genreList.width+1,
                                genreInclude.y+(genreUpdate.height/2), 3, 4)


        AnimatedLabel.place_here(ClearButton.x+(ClearButton.width/2),
                                 ClearButton.y-ClearButton.height*2, 0, 1)

        AnimatedToggle = Button_Widget(self.root)
        AnimatedToggle.add_widget('Animated', self.backend.set_selection,
                                    multiargument=True,
                                    args=[AnimatedLabel.labels[0], viewFilters])
        difference_in_height = abs(AnimatedToggle.height - AnimatedLabel.height)
        max_number_of_letters = max([len('False'), len('True'), len('')])
        AnimatedToggle.place_here(AnimatedLabel.x-AnimatedLabel.width/2-AnimatedToggle.width,
                                      AnimatedLabel.y-(difference_in_height/2)-(AnimatedToggle.height/2),
                                      -(max_number_of_letters+5), 4)
        

        Loadingbar = Loadingbar_Widget(self.root)
        Loadingbar.add_widget(width=FilteredList.width)
        # Loadingbar.place_here(FilteredList.x-(FilteredList.width/2),
        #                       FilteredList.y-(FilteredList.height/2)-Loadingbar.height, 0, 2)

        RefreshButton = Button_Widget(self.root)
        RefreshButton.add_widget('Refresh', self.backend.refresh,
                                   multiargument=True,
                                   args=[pornstarList, genreList, ethnicitiesList, FilteredList, Loadingbar,
                                         Total_Hours_of_Porn])
        ycenter = int((AnimatedLabel.y+renameButton.y)/2)-RefreshButton.height/2
        RefreshButton.place_here(ClearButton.x+ClearButton.width/2, ycenter, 3, 0)

        
        DeleteButton = Button_Widget(self.root)
        DeleteButton.add_widget('Delete', self.backend.delete_video, multiargument=True, 
                                args=[FilteredList, Total_Hours_of_Porn])
        DeleteButton.place_here(TrueRandomButton.x+TrueRandomButton.width,
                                    FilteredList.y+(FilteredList.height/2), 2, 8)


        i = 27
        FilenameSearchInput.add_widget(i, 1)
        max_legnth = (FilenameChangeInput.width+renameButton.width+renameButtonxPadding)
        while FilenameSearchInput.width < max_legnth:
            i = i + 1
            FilenameSearchInput.remove_widget()
            FilenameSearchInput.add_widget(i, 1)
        FilenameSearchInput.place_here(EqualsButton.x-EqualsButton.width/2, renameButton.y+(renameButton.height/2),
                                       paddingy=10)
        FilenameChangeInput.destroy_widget()
        renamex = renameButton.x
        renameButton.destroy_widget()
        renameButton = Button_Widget(self.root)
        renameButton.add_widget('Rename', self.backend.rename_file, multiargument=True,
                                args=[FilenameSearchInput.inputboxes[0], FilteredList])
        renameButton.place_here(renamex-renameButton.width/2,
                                FilenameSearchInput.y-renameButton.height-(FilenameSearchInput.height/2),
                                0, -1)
        
        SearchButton = Button_Widget(self.root)
        SearchButton.add_widget('Search', self.backend.search_and_filter,
                                   multiargument=True,
                                   args=[FilteredList, FilenameSearchInput, List_of_Folders, viewFilters,
                                         Total_Hours_of_Porn])
        SearchButton.place_here(FilenameSearchInput.x+FilenameSearchInput.width/2,
                                FilenameSearchInput.y-FilenameSearchInput.height/2, 3, -2)
        

        editGitMSG = Button_Widget(self.root)
        editGitMSG.add_widget('Git MSG', self.backend.get_git_msg_from_box, multiargument=True,
                                args=[FilenameSearchInput.inputboxes[0]])
        editGitMSG.place_here(renamex-renameButton.width/2,
                                FilenameSearchInput.y+(editGitMSG.height/2),
                                0, -1)
    
        
        paths = self.backend.get_all_folders_from_root(self.backend.root_path)
        list_height_in_pixels = abs(pornstardeUpdate.y - FilteredList.y) - 1.25*pornstardeUpdate.height
        List_of_Folders.add_widget('single', paths, window_width=FilenameSearchInput.width/3,
                                   window_height=list_height_in_pixels)
        List_of_Folders.change_color('#01080f', '#ffeeff')
        List_of_Folders.place_here(pornstarList.x+pornstarList.width/2,
                                   pornstardeUpdate.y+pornstardeUpdate.height/2,
                                   1, 1)
        
        MoveToButton = Button_Widget(self.root)
        MoveToButton.add_widget('Move', self.backend.move_file, multiargument=True,
                                args=[FilteredList, List_of_Folders])
        MoveToButton.place_here(List_of_Folders.x+(List_of_Folders.width/2),
                                List_of_Folders.y-MoveToButton.height,
                                1, -1)
        
        PathFilterButton = Button_Widget(self.root)
        PathFilterButton.add_widget('Filter w/ Path', self.backend.complete_filter_with_path, multiargument=True,
                                args=[FilteredList, List_of_Folders, viewFilters])
        PathFilterButton.place_here(List_of_Folders.x+(List_of_Folders.width/2),
                                List_of_Folders.y,
                                1, 1)
        
        
        DetailsButton = Button_Widget(self.root)
        DetailsButton.add_widget('View Details', self.backend.view_details, multiargument=True,
                                args=[FilteredList,
                                      max(pornstarList.width, genreList.width, ethnicitiesList.width),
                                      max(pornstarList.height, genreList.height, ethnicitiesList.height)])
        DetailsButton.place_here(DeleteButton.x+(DeleteButton.width),
                                FilteredList.y+(FilteredList.height/2),
                                2, 8)
        
        
        githubButton = Button_Widget(self.root)
        githubButton.add_widget('Update GitHub', self.backend.start_file, multiargument=True,
                                args=['git_update.bat', False, False, 'i', 'j', FilenameSearchInput])
        githubButton.place_here(FilenameSearchInput.x-(githubButton.width/2),
                                int((List_of_Folders.y+FilenameSearchInput.y)/2)-githubButton.height,
                                2, -1)
        
        
        incompleteButton = Button_Widget(self.root)
        incompleteButton.add_widget('Unupdated Filter', self.backend.filter_missing_info, multiargument=True,
                                args=[FilteredList, FilenameSearchInput, List_of_Folders, viewFilters,
                                      [sortAlpha, sortTime, unsortFromCSV],
                                      Total_Hours_of_Porn])
        incompleteButton.place_here(int(.5*(genredeUpdate.x+ethnicitydeUpdate.x))-incompleteButton.width/2,
                                int(genredeUpdate.y-genredeUpdate.height),
                                0, 0)
        
        CompleteButton = Button_Widget(self.root)
        CompleteButton.add_widget('Updated Filter', self.backend.filter_complete_info, multiargument=True,
                                args=[FilteredList, FilenameSearchInput, List_of_Folders, viewFilters,
                                      [sortAlpha, sortTime, unsortFromCSV],
                                      Total_Hours_of_Porn])
        incompbutyTOP = int(incompleteButton.y-incompleteButton.height/2)
        ethlistBOTTOM = int(ethnicitiesList.y+ethnicitiesList.height/2)
        CompleteButton.place_here(incompleteButton.x-CompleteButton.width/2,
                                int((incompbutyTOP+ethlistBOTTOM-CompleteButton.height)/2),
                                0, 0)
        

        viewFilters.add_widget('View Filters', self.backend.view_filters, multiargument=True,
                               args=[List_of_Folders.width,
                                     #int(max(pornstarList.width, genreList.width, ethnicitiesList.width)),
                                      int(1.25*max(pornstarList.height, genreList.height, ethnicitiesList.height))])
        viewFilters.place_here(int(((githubButton.x+ethnicitydeUpdate.x)/2)-(viewFilters.width/2)),
                               githubButton.y-int((viewFilters.height)/2),
                               0,
                               0)
        viewFilters.change_color(background='#f04209')
        

        RangeGreater = Button_Widget(self.root)
        comparor = '>'
        RangeGreater.add_widget(comparor, self.backend.update_lower_comparator, comparor, 222, 123)
        RangeGreater.place_here(hoursInput.x-(RangeGreater.width/2),
                                 2, 0, -1)
        
        RangeGreaterEqual = Button_Widget(self.root)
        comparor = '>='
        RangeGreaterEqual.add_widget(comparor, self.backend.update_lower_comparator, comparor, 222, 123)
        RangeGreaterEqual.place_here(RangeGreater.x+(RangeGreater.width/2),
                                 2, 1, -1)
        
        Rangeless = Button_Widget(self.root)
        comparor = '<'
        Rangeless.add_widget(comparor, self.backend.update_upper_comparator, comparor, 222, 123)
        Rangeless.place_here(secondsButton.x-(Rangeless.width/2),
                                 2, 0, -1)
        
        RangelessEqual = Button_Widget(self.root)
        comparor = '<='
        RangelessEqual.add_widget(comparor, self.backend.update_upper_comparator, comparor, 222, 123)
        RangelessEqual.place_here(Rangeless.x-(RangelessEqual.width)-(Rangeless.width/2),
                                 2, -1, -1)
        

        TimeButton = Button_Widget(self.root)
        inputs = [
            hoursInput,
            minutesInput,
            secondsInput
        ]
        TimeButton.add_widget('Time', self.backend.update_all_time, multiargument=True,
                                args=[inputs, [viewFilters, viewFilters, viewFilters]])
        TimeButton.place_here(int((RangelessEqual.x+RangeGreaterEqual.x-TimeButton.width)/2),
                                RangelessEqual.y-(TimeButton.height/2),
                                0, 0)
        
        
        PornstarListAdder = Button_Widget(self.root)
        PornstarListAdder.add_widget('Update List', self.backend.add_to_txt_list, multiargument=True,
                                     args=[FilenameSearchInput,'pornstar', pornstarList])
        PornstarListAdder.place_here(pornstarADD.x-(pornstarADD.width/2),
                                 pornstarLabel.y-(pornstarLabel.height/2), 0, 1)
        
        PornstarListRemover = Button_Widget(self.root)
        PornstarListRemover.add_widget('D\ne\nu\np\nd\na\nt\ne', 
                                       self.backend.remove_txt_from_list, multiargument=True,
                                     args=[FilenameSearchInput,'pornstar', pornstarList])
        startingX = max([pornstarADD.x+(pornstarADD.width/2),
                         pornstarRemove.x+(pornstarRemove.width/2),
                         pornstarExclude.x+(pornstarExclude.width/2),
                         pornstarInclude.x+(pornstarInclude.width/2),
                         pornstarUpdate.x+(pornstarUpdate.width/2),
                         pornstardeUpdate.x+(pornstardeUpdate.width/2)
                         ])
        PornstarListRemover.place_here(startingX, 40, 0-2, 1)
        
        GenreListAdder = Button_Widget(self.root)
        GenreListAdder.add_widget('Update List', self.backend.add_to_txt_list, multiargument=True,
                                     args=[FilenameSearchInput,'genre', genreList])
        GenreListAdder.place_here(genreADD.x-(genreADD.width/2),
                                 genreLabel.y-(genreLabel.height/2), 0, 1)
        
        GenreListRemover = Button_Widget(self.root)
        GenreListRemover.add_widget('D\ne\nu\np\nd\na\nt\ne', 
                                       self.backend.remove_txt_from_list, multiargument=True,
                                     args=[FilenameSearchInput,'genre', genreList])
        startingX = max([genreADD.x+(pornstarADD.width/2),
                         genreRemove.x+(pornstarRemove.width/2),
                         genreExclude.x+(pornstarExclude.width/2),
                         genreInclude.x+(pornstarInclude.width/2),
                         genreUpdate.x+(pornstarUpdate.width/2),
                         genredeUpdate.x+(pornstardeUpdate.width/2)
                         ])
        GenreListRemover.place_here(startingX, 40, 0-2, 1)
        
        ethnicityListAdder = Button_Widget(self.root)
        ethnicityListAdder.add_widget('Update List', self.backend.add_to_txt_list, multiargument=True,
                                     args=[FilenameSearchInput,'ethnicity', ethnicitiesList])
        ethnicityListAdder.place_here(ethnicitiesADD.x-(ethnicitiesADD.width/2),
                                 ethnicitiesLabel.y-(ethnicitiesLabel.height/2), 0, 1)
        
        ethnicityListRemover = Button_Widget(self.root)
        ethnicityListRemover.add_widget('D\ne\nu\np\nd\na\nt\ne', 
                                       self.backend.remove_txt_from_list, multiargument=True,
                                     args=[FilenameSearchInput,'ethnicity', ethnicitiesList])
        startingX = max([ethnicitiesADD.x+(pornstarADD.width/2),
                         ethnicitiesRemove.x+(pornstarRemove.width/2),
                         ethnicitiesExclude.x+(pornstarExclude.width/2),
                         ethnicitiesInclude.x+(pornstarInclude.width/2),
                         ethnicityUpdate.x+(pornstarUpdate.width/2),
                         ethnicitydeUpdate.x+(pornstardeUpdate.width/2)
                         ])
        ethnicityListRemover.place_here(startingX, 40, -2, 1)

        hoursLabel = Label_Widget(self.root)
        hoursLabel.add_widget('H')
        hoursLabel.place_here(hoursButton.x-hoursLabel.width/2,
                               hoursButton.y-hoursLabel.height/2,
                               0, -1)

        minutesLabel = Label_Widget(self.root)
        minutesLabel.add_widget('M')
        minutesLabel.place_here(minutesButton.x-minutesLabel.width/2,
                               minutesButton.y-minutesLabel.height/2,
                               0, -1)

        secondsLabel = Label_Widget(self.root)
        secondsLabel.add_widget('S')
        secondsLabel.place_here(secondsButton.x-secondsLabel.width/2,
                               secondsButton.y-secondsLabel.height/2,
                               0, -1)
        

        hoursButton.destroy_widget()
        minutesButton.destroy_widget()
        secondsButton.destroy_widget()
        

        sortingDirectionLabel = Label_Widget(self.root)
        sortingDirectionLabel.add_widget('Ascending')
        sortAlpha.add_widget('Sort: abc', self.backend.sort_listbox_widget, multiargument=True,
                                     args=[FilteredList, 'abc', sortingDirectionLabel,
                                           sortAlpha, [sortTime, unsortFromCSV]])
        sortAlpha.place_here(DetailsButton.x+DetailsButton.width,
                                 DetailsButton.y-(DetailsButton.height/2), 0, 0)
        sortAlpha.change_color(background='#09f042')

        sortTime.add_widget('Sort: time', self.backend.sort_listbox_widget, multiargument=True,
                                     args=[FilteredList, 'time', sortingDirectionLabel,
                                           sortTime, [sortAlpha, unsortFromCSV]])
        sortTime.place_here(sortAlpha.x+sortAlpha.width,
                                 sortAlpha.y-(sortAlpha.height/2), 0, 0)
        sortTime.change_color(background='#f04209')

        unsortFromCSV.add_widget('CSV Order', self.backend.sort_listbox_widget, multiargument=True,
                                     args=[FilteredList, 'csv', sortingDirectionLabel,
                                           unsortFromCSV, [sortAlpha, sortTime]])
        unsortFromCSV.place_here(sortTime.x+sortTime.width,
                                 sortTime.y-(sortTime.height/2), 0, 0)
        unsortFromCSV.change_color(background='#f04209')

        sortingDirectionLabel.place_here(unsortFromCSV.x+sortingDirectionLabel.width/2,
                               unsortFromCSV.y-sortingDirectionLabel.height/2,
                               8, 0)
        
        UpdateAll_Button = Button_Widget(self.root) #[pornstarList.listboxess[0], FilteredList, 'Pornstars']
        UpdateAll_Button.add_widget('Update All', self.backend.update_all, multiargument=True,
                                     args=[[pornstarList.listboxess[0], 
                                            genreList.listboxess[0], 
                                            ethnicitiesList.listboxess[0]],
                                           FilteredList,
                                           ['Pornstars', 'Genres', 'Ethnicities']])
        UpdateAll_Button.place_here(EqualsButton.x-(EqualsButton.width/2),
                                 renameButton.y-(renameButton.height/2), 0, 0)
        

        watched_label = 'Total Porn Hours:\n{}\n\nTotal Watched:\n{}\n\nTotal Unwatched:\n{}\n\nFiltered Hours:\n{}\n\nTotal File Size:\n{}GB'.format(
            self.backend.total_porn_hours,
            self.backend.total_watched_porn_hours,
            self.backend.total_unwatched_porn_hours,
            self.backend.filtered_porn_hours,
            self.backend.total_file_size
        )
        Total_Hours_of_Porn.add_widget(watched_label)
        alpha = round((self.window_width - (FilteredList.x+FilteredList.width/2) - Total_Hours_of_Porn.width)/2)
        Total_Hours_of_Porn.place_here(FilteredList.x+FilteredList.width/2,
                               FilteredList.y-Total_Hours_of_Porn.height/2,
                               alpha, 0)
        

        log_Button = Button_Widget(self.root) #[pornstarList.listboxess[0], FilteredList, 'Pornstars']
        log_Button.add_widget('Log', self.backend.start_file, multiargument=True,
                                     args=['log.txt', False, False])
        log_Button.place_here(self.window_width-(log_Button.width),
                                 self.window_height-(log_Button.height), -1, -1)
        

        CSV_Button = Button_Widget(self.root)
        CSV_Button.add_widget('CSV', self.backend.start_file, multiargument=True,
                                     args=['Porn.csv', False, False])
        CSV_Button.place_here(self.window_width-(CSV_Button.width)-(log_Button.width),
                                 self.window_height-(CSV_Button.height), -2, -1)
        

        Config_Button = Button_Widget(self.root)
        Config_Button.add_widget('Config', self.backend.start_file, multiargument=True,
                                     args=['Config.txt', False, False])
        Config_Button.place_here(self.window_width-(Config_Button.width)-(CSV_Button.width)-(log_Button.width),
                                 self.window_height-(Config_Button.height), -2, -1)
        
        
        # Close = Button_Widget(self.root)
        # comparor = 'X'
        # Close.add_widget(comparor, self.destroy_dependant, multiargument=True,
        #                  args=[[self.backend.details_root, self.backend.filters_root]])
        # Close.config_width(Close.width*2)
        # Close.config_height(Close.width)
        # Close.change_color(background='#fe0990')
        # Close.place_here(self.window_width-Close.width,
        #                  0,
        #                  0, 0)
        #self.waiting_window.destroy()
        self.backend.write_to_log('Building complete')

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
