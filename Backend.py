#import pandas as pd
from datetime import datetime
import os
#import json
import time
from pymediainfo import MediaInfo
import subprocess
import secrets
import psutil
from tkinter import Label
from tkinter import Tk
from Widgets import Label_Widget
from Widgets import Listbox_widget
import shutil
from PIL import Image, ImageTk
from cv2 import imwrite
from cv2 import CAP_PROP_FPS
from cv2 import CAP_PROP_POS_FRAMES
import ctypes

class BackendFuncs:
    def __init__(self):
        self.player_index = self.generate_random_integer(1, 4) % 2
        if self.player_index == 1:
            self.other_player_index = 0
        if self.player_index == 0:
            self.other_player_index = 1
        self.players = [[],[]]
        self.questions = [
            'What is one thing you have always wanted to try in the bedroom but have not told me?',
            'If money was no object would you want a grand wedding or something small?  Explain.',
            'How long should you date a person at minimum before getting married?'
            'What do you think is my favorite thing about you?'
            'Where is the most adventurous place you wouldd like to make love?',
            'What is a secret fantasy you have never shared with anyone?',
            'How do you feel about role play, and what scenario intrigues you?',
            'What is the naughtiest thought you have had about us?',
            'Is there a type of clothing you would love to see me wear?',
            'What is one thing that I do that drives you wild without fail?',
            'Have you ever fantasized about us while you were alone?',
            'What is your favorite memory of us that turns you on just thinking about it?',
            'How do you feel about public displays of affection?',
            'What is something new you would like to explore together?',
            'How important is experimentation in our intimate life to you?',
            'What is the most sensitive part of your body?',
            'How do you feel about dirty talk, and could we incorporate more of it?',
            'What is a movie or book scene that you find incredibly erotic?',
            'Have you ever had a dream about us that you have not shared?',
            'What kind of touch do you crave the most?',
            'Is there a song that makes you think about being intimate with me?',
            'How old were you when you started masturbating?',
            'How do you feel about taking our intimacy outside the bedroom?',
            'What is the most daring thing you have ever wanted to do with me?',
            'What is something you find incredibly attractive about me that I would never guess?',
            'How do you feel about making out in public?',
            'What is one thing I do that makes your heart skip a beat?',
            'If we could teleport anywhere right now, just for a kiss, where would we go?',
            'What kind of outfit would you love to see me in?',
            'What is a romantic fantasy you have always had?',
            'When did you first realize you were attracted to me?',
            'What is your favorite pet name',
            'How do you feel about cuddling on the couch vs. cuddling in bed?',
            'What is the most romantic date you can imagine?',
            'If you could describe our chemistry in one word, what would it be?',
            'What is something flirty you have wanted to say to me but have not yet?',
            'How would you react if I whispered something naughty in your ear in public?',
            'What is one thing I do that unexpectedly turns you on?',
            'If we had a whole day to ourselves, no interruptions, what would we do?',
            'Describe the most passionate kiss you have ever imagined us having.',
            'What is a small act of affection you find incredibly sexy?',
            'How do you feel about holding hands in public?',
            'What is one thing you wish we would done sooner in our relationship?',
            'If you could have any superpower when with me, what would it be?',
            'What is the most embarrassing thing you have done around me, hoping I did not notice?',
            'If we were animals, what would we be and why?',
            'What is the silliest reason you have ever gotten into a laugh with me?',
            'If you could prank me without repercussions, what would you do?',
            'What movie title best describes our relationship?',
            'What is the funniest thing you have ever seen me do?', 
            'If we could have a theme song, what would it be?',
            'What is the weirdest dream you have had about us?',
            'If we were in a food fight, what would be your weapon of choice?',
            'What is a goofy habit of mine that you secretly love?',
            'If we could switch lives for a day, what is the first thing you would do?',
            'What is something you do better than me, and vice versa?',
            'If we were stranded on a deserted island, what role would each of us play?',
            'What is the most bizarre gift you have ever thought about giving me?',
            'If we made a sitcom about our lives, what would it be called?',
            'What is a hobby you would love us to try together but think I would never go for?',
            'If we were superheroes, what powers would complement each other the best?',
            'If you could invent a holiday for us, what would it celebrate?',
            'What experience has shaped you most in life, and why?',
            'What was your most profound moment of vulnerability, and what did it teach you?',
            'How do you define love, and do you believe it evolves?',
            'What is a fear you have overcome, and how did you do it?',
            'What do you dream about achieving the most, and why?',
            'What was a turning point in your life, and how did it change you?',
            'What is something you have always wanted to tell me but have not found the right moment?',
            'What does trust mean to you in a relationship?',
            'How do you see our future together, and what are your aspirations for us?',
            'What is a lesson from a past relationship that you have brought into ours?',
            'What are your thoughts on forgiveness and second chances in love?',
            'How do you maintain your sense of self while being deeply connected to someone else?',
            'What is something you have learned about yourself from being with me?',
            'How do you express love, and in what ways do you prefer to receive it?',
            'What is a dream you have yet to achieve, and how can I support you in it?',
            'If you could change one aspect of our relationship, what would it be and why?',
            'How do you envision our life together in 10 years?',
            'How do you define happiness, and do you think it is achievable?',
            'How do you reconcile the existence of good and evil in the world?',
            'What role does love play in the universe?',
            'How do you balance the need for individual freedom with the importance of community?',
            'How do you define success, and is it subjective or universal?',
            'What does it mean to live a good life?',
            'How important is it to leave a legacy, and what kind do you want to leave?',
            'Do you believe in the concept of a parallel universe or alternate realities?',
            'What is the role of art and creativity in society?',
            'Is there such a thing as absolute truth, or is everything relative?',
            'If you could travel to any point back in time, what year would you choose and why?',
            'What are a few things at the top of your bucket list?',
            'What decision do you look back on and say, "What was I thinking?"',
            'If you could give your 16-year-old self one piece of advice, what would it be? Would you have listened?',
            'Who is/was the most influential person in your life?',
            'What is the first thing you would do if you won the mega millions lottery?', 
            'What is the weirdest dream you have ever had?',
            'What is the most embarrassing thing you have done in public?',
            'Would you consider yourself adventurous, or do you play it on the safe side?',
            'What would you title this chapter of your life?',
            'If you could re-live any part of your life so far, which part would you choose and why?',
            'What is the biggest lesson you learned from your teens/twenties?',
            'Who would you want to sit next to on a ten-hour flight across the world (aside from self.signifigant_other), and why?',
            'If you could be any kind of dog, what breed would you be? ',
            'Do you think the convenience of the internet is worth the loss of privacy that comes with it?',
            'If you found out that your current life has been only a dream, would you choose to wake up or stay in it?', 
            'What are three non-negotiable traits you want in a partner?',
            'What have you always dreamed someone would do for you?',
            'What is your idea of the perfect relationship?',
            'Do you believe opposites attract? ',
            'What is a common relationship belief that you do not agree with?',
            'Aside from common pet names such as babe, sweethert, hun, etc. what is a pet name you would like to exclusively call me?',
            'What quirky habit do you have that no one knows about?',
            'How would you want to spend a one-week vacation with your lover?',
            'What brings you the most joy in life?',
            'What part of yourself have you learned to accept?',
            'Imagine you are dating the most attractive person in the world, but your family does not like them. Would you stay with them? Why or why not?',
            'How important is humor for you in a relationship?',
            'What is your definition of a healthy relationship?',
            'What was your first impression of me?',
            'When looking at someone you are attracted to, where do your eyes go first?',
            'How old were you when you had your first kiss?',
            'What is the most spontaneous thing you have ever done?',
            'What is your biggest regret?',
            'If you could live someone else is life for a day, who would you choose?',
            'What do you consider the most romantic travel destination in the world?',
            'What is your biggest fear when it comes to relationships?',
            'Romantic lunch picnic in the park or a high-class dinner and cocktails?',
            'What is your biggest turn-on?',
            'Do you prefer cuddling or kissing?',
            'Have you ever had a crush on a teacher or someone much older (5+ years) than you?',
            'Love or money?',
            'What is the shortest and longest relationship you have ever had?',
            'What is the craziest thing you have ever seen someone do for love?',
            'What is a relationship deal breaker?',
            'What is your favorite thing about me?',
            'What sets you apart from other people?',
            'What do you think sets me apart from other people?',
            'What is your favorite childhood memory?',
            'Have you ever skinny dipped with a group?',
            'Do you think you are a good kisser?',
            'Where do you like being touched the most?',
            'Is there anywhere you would like to be kissed more often aside from the lips',
            'How old were you when you lost your virginity?',
            'Where is the strangest place you have ever had sex?',
            'Where would you love to have sex?',
            'What turns you on almost instantly?',
            'How do you feel about bringing toys into the bedroom?',
            'Have you ever bragged to your friends about me?',
            'Have you ever been to a strip club?',
            'What kind of talk do you like, if any, in bed?',
            'Have you ever had a dream about me?', 
            'Have you ever kissed me in public just to make someone jealous?',
            'Hickies: major yes or no way?',
            'What is a fantasy you have never shared with anyone?',
            'Outside of relationship fears what are your biggest fears?',
            'Premarital (safe) sex: Yes or No?'
        ]
        self.bf_total_questions = 0
        self.gf_total_questions = 0
        self.bf_answered_questions = 0
        self.gf_answered_questions = 0
        self.BF_score = 0
        self.GF_score = 0
        self.BF_skips = 1
        self.GF_skips = 1
        self.BF_number_of_bought_skips = 0
        self.GF_number_of_bought_skips = 0
        u = ctypes.windll.user32
        [self.screenwidth_in_pixels, self.screenheight_in_pixels] = [u.GetSystemMetrics(0), u.GetSystemMetrics(1)]
        self.bf_name = ''
        self.gf_name = ' '
        self.rulez = 'Rules:\n1. Players must alternate\nturns.  The first player will\nbe determined at random.\n\n'
        self.rulez = self.rulez + '2. This is meant to build\nyour relationship.  As such\nall answers MUST be made\nwhileholding hands '
        self.rulez = self.rulez + 'and\nmaking full eye contact.\n\n'
        self.rulez = self.rulez + '3. Players can use their\nskips whenever they choose\nas long as they have skips.\n\n'
        self.rulez = self.rulez + '4. Players can accrue skips\nat a rate of 1 skip per 5\nanswered questions.\n\n'
        self.rulez = self.rulez + '5. Skips can be bought by\ngiving your partner a\npassionate kiss if it is your\nturn.\n\n'
        self.rulez = self.rulez + '6. Skips can be bought after\nanswering 3 questions.\n\n'
        self.rulez = self.rulez + '7. A player may only hold 3\nskips at once.'
        self.game_started = False
        self.bf_turns_of_accural = 0
        self.gf_turns_of_accural = 0
        self.bf_turns_of_purchase = 0
        self.gf_turns_of_purchase = 0

    def start_game(self, bf_text_widget, gf_text_widget, questions_label_widget):
        if self.game_started != False:
            pass
        else:
            self.bf_name = bf_text_widget.get_text_input()
            self.gf_name = gf_text_widget.get_text_input()
            if (self.bf_name.strip() == '') or (self.gf_name.strip() == ''):
                pass
            else:
                self.game_started = True
                self.players = [
                    [self.gf_name, self.GF_score, self.GF_skips, self.gf_answered_questions, self.gf_total_questions,
                    'female', self.GF_number_of_bought_skips, self.gf_turns_of_accural, self.gf_turns_of_purchase],
                    [self.bf_name, self.BF_score, self.BF_skips, self.bf_answered_questions, self.bf_total_questions,
                    'male', self.BF_number_of_bought_skips, self.bf_turns_of_accural, self.bf_turns_of_purchase]
                ]
                self.active_player_info = self.players[self.player_index]
                question_index = self.generate_random_integer(0, len(self.questions)-1)
                question = self.questions[question_index]
                print(question)
                question = question.replace(' me ', ' '+self.players[self.other_player_index][0]+' ')
                question = question.replace(' me.', ' '+self.players[self.other_player_index][0]+'.')
                question = question.replace(' me?', ' '+self.players[self.other_player_index][0]+'?')
                question = question.replace(' me!', ' '+self.players[self.other_player_index][0]+'!')
                question = question.replace(' my ', ' '+self.players[self.other_player_index][0]+"'s ")
                question = question.replace(' my.', ' '+self.players[self.other_player_index][0]+"'s.")
                question = question.replace(' me?', ' '+self.players[self.other_player_index][0]+"'s?'")
                question = question.replace(' me!', ' '+self.players[self.other_player_index][0]+"'s!")
                print(question)
                self.questions.pop(question_index)
                questions_label_widget.change_text(question)
                if self.active_player_info[5] == 'male':
                    questions_label_widget.labels[0].config(fg='#0999ff')#fg_color='0999ff'
                elif self.active_player_info[5] == 'female':
                    questions_label_widget.labels[0].config(fg='#ff8080')#fg_color='ff8080'
                self.current_turn = 0
        #exit()

    def move_to_next_round(self, questions_label_widget):
        self.toggle_player_index()
        self.active_player_info = self.players[self.player_index]
        question_index = self.generate_random_integer(0, len(self.questions)-1)
        question = self.questions[question_index]
        question = question.replace(' me ', ' '+self.players[self.other_player_index][0]+' ')
        question = question.replace(' me.', ' '+self.players[self.other_player_index][0]+'.')
        question = question.replace(' me?', ' '+self.players[self.other_player_index][0]+'?')
        question = question.replace(' me!', ' '+self.players[self.other_player_index][0]+'!')
        question = question.replace(' my ', ' '+self.players[self.other_player_index][0]+"'s ")
        question = question.replace(' my.', ' '+self.players[self.other_player_index][0]+"'s.")
        question = question.replace(' me?', ' '+self.players[self.other_player_index][0]+"'s?'")
        question = question.replace(' me!', ' '+self.players[self.other_player_index][0]+"'s!")
        self.questions.pop(question_index)
        questions_label_widget.change_text(question)
        if self.active_player_info[5] == 'male':
            questions_label_widget.labels[0].config(fg='#0999ff')#fg_color='0999ff'
        elif self.active_player_info[5] == 'female':
            questions_label_widget.labels[0].config(fg='#ff8080')#fg_color='ff8080'
    
    def toggle_player_index(self):
        if self.player_index == 1:
            self.player_index = 0
            self.other_player_index = 1
        elif self.player_index == 0:
            self.player_index = 1
            self.other_player_index = 0
        elif self.player_index % 2 == 1:
            self.player_index = 0
            self.other_player_index = 1
        else:
            self.player_index = 1
            self.other_player_index = 0

    def update_stats(self, stats_label_widget):
        stats = 'Stats:\n                 BF                 GF\nScore:            {}                 {}\nSkips:            {}                 {}'.format(
            round(self.BF_score, 1), round(self.GF_score, 1), self.BF_skips, self.GF_skips
        )
        stats_label_widget.change_text(stats)
        stats_label_widget.place_here(1,
                               int(.5*self.screenheight_in_pixels),
                               0, 0)

    def update_player_info(self):
        self.GF_score = self.players[0][1]
        self.GF_skips = self.players[0][2]
        self.gf_answered_questions = self.players[0][3]
        self.gf_total_questions = self.players[0][4]
        self.GF_number_of_bought_skips = self.players[0][6]
        self.gf_turns_of_accural = self.players[0][7]
        self.gf_turns_of_purchase = self.players[0][8]
        self.BF_score = self.players[1][1]
        self.BF_skips = self.players[1][2]
        self.bf_answered_questions = self.players[1][3]
        self.bf_total_questions = self.players[1][4]
        self.BF_number_of_bought_skips = self.players[1][6]
        self.bf_turns_of_accural = self.players[1][7]
        self.bf_turns_of_purchase = self.players[1][8]
        self.players = [
                [self.gf_name, self.GF_score, self.GF_skips, self.gf_answered_questions, self.gf_total_questions,
                 'female', self.GF_number_of_bought_skips, self.gf_turns_of_accural, self.gf_turns_of_purchase],
                [self.bf_name, self.BF_score, self.BF_skips, self.bf_answered_questions, self.bf_total_questions,
                 'male', self.BF_number_of_bought_skips, self.bf_turns_of_accural, self.bf_turns_of_purchase]
            ]
    
    def skip(self, stats_label_widget, bf_text_widget, gf_text_widget, questions_label_widget):
        if self.game_started == False:
            self.start_game(bf_text_widget, gf_text_widget, questions_label_widget)
        else:
            #[self.gf_name, self.GF_score, self.GF_skips, self.gf_answered_questions, self.gf_total_questions, 'female', bought_skips]
            print('skipping')
            if self.players[self.player_index][2] > 0:
                print(self.players[self.player_index][2])
                self.players[self.player_index][2] =  self.players[self.player_index][2] - 1
                self.players[self.player_index][4] =  self.players[self.player_index][4] + 1
                self.players[self.player_index][1] =  self.calculate_score(self.players[self.player_index][1],
                                                                           self.players[self.player_index][3],
                                                                           self.players[self.player_index][4],
                                                                           self.players[self.player_index][6])
                print(self.players[self.player_index][2])
                self.update_player_info()
                self.update_stats(stats_label_widget)
                self.move_to_next_round(questions_label_widget)
            else:
                print('{} does not have enough.  Must buy')

    def answer(self, stats_label_widget, bf_text_widget, gf_text_widget, questions_label_widget):
        # [self.bf_name, self.BF_score, self.BF_skips, self.bf_answered_questions, self.bf_total_questions,
        #          'male', self.BF_number_of_bought_skips, self.bf_turns_of_accural, self.bf_turns_of_purchase]
        if self.game_started == False:
            self.start_game(bf_text_widget, gf_text_widget, questions_label_widget)
        else:
            self.players[self.player_index][4] =  self.players[self.player_index][4] + 1
            self.players[self.player_index][3] =  self.players[self.player_index][3] + 1
            self.players[self.player_index][1] =  self.calculate_score(self.players[self.player_index][1],
                                                                           self.players[self.player_index][3],
                                                                           self.players[self.player_index][4],
                                                                           self.players[self.player_index][6])
            self.accrue_skip()
            self.update_stats(stats_label_widget)
            self.move_to_next_round(questions_label_widget)
            
    def accrue_skip(self):
        if (self.players[self.player_index][2] < 3) and (self.players[self.player_index][7] >= 5):
            self.players[self.player_index][2] = self.players[self.player_index][2] + 1
            self.players[self.player_index][7] = 0
        elif (self.players[self.player_index][2] >= 3) and (self.players[self.player_index][7] >= 5):
            self.players[self.player_index][2] = 3
            self.players[self.player_index][7] = 0
        else:
            self.players[self.player_index][7] = self.players[self.player_index][7] + 1
        if self.players[self.player_index][8] < 3:
            self.players[self.player_index][8] = self.players[self.player_index][8] + 1
        else:
            self.players[self.player_index][8] = 3
        self.update_player_info()

    def buy_skip(self, stats_label_widget, bf_text_widget, gf_text_widget, questions_label_widget):
        if self.game_started == False:
            self.start_game(bf_text_widget, gf_text_widget, questions_label_widget)
        else:
            if (self.players[self.player_index][8] >= 3) and (self.players[self.player_index][2] < 3):
                self.players[self.player_index][2] = self.players[self.player_index][2] + 1
                self.players[self.player_index][6] = self.players[self.player_index][6] + 1
                self.players[self.player_index][8] = 0
                self.update_player_info()
                self.players[self.player_index][1] =  self.calculate_score(self.players[self.player_index][1],
                                                                           self.players[self.player_index][3],
                                                                           self.players[self.player_index][4],
                                                                           self.players[self.player_index][6])
                self.update_stats(stats_label_widget)
            elif (self.players[self.player_index][8] >= 3) and (self.players[self.player_index][2] >= 3):
                pass
            else:
                pass


    def calculate_score(self, current_score, answered_questions, total_questions, skips_bought):
        if total_questions == 0:
            return 0
        else:
            return max(current_score, (answered_questions*5)+((answered_questions/total_questions)*3)+(2*skips_bought))
    
    # def alphabatize_txt_list(self, text_doc_name, new_text_doc_name=False):
    #     contents = self.get_list_of_contents(text_doc_name)
    #     _contents = self.get_list_of_contents(text_doc_name)
    #     contents.sort(key=str.lower)
    #     if contents != _contents:
    #         if new_text_doc_name == False:
    #             file_name = open(text_doc_name, 'w')
    #         else:
    #             file_name = open(new_text_doc_name, 'w')
    #         for i in contents:
    #             file_name.write(i+'\n')
    #         file_name.close()

    # def get_folder_size(self, aFUCKINGfolder):
    #     size = 0
    #     for path, dirs, files in os.walk(aFUCKINGfolder):
    #         for f in files:
    #             fp = os.path.join(path, f)
    #             size += os.stat(fp).st_size
    #     return size

    # def get_batch_file_message(self):
    #     batch_file = open('git_update.bat', 'r')
    #     msg = batch_file.read()
    #     batch_file.close()
    #     msg = msg.split('git commit -m "')[1].strip()
    #     msg = msg.split('"')[0].strip()
    #     self.write_to_log('original '+msg)
    #     return msg
    
    # def update_batch_file_message(self, new_msg='update'):
    #     old_msg = self.get_batch_file_message()
    #     batch_file = open('git_update.bat', 'r')
    #     msg = batch_file.read()
    #     batch_file.close()
    #     self.write_to_log(msg)
    #     if old_msg == '':
    #         old_msg = '""'
    #         msg = msg.replace(old_msg, '"'+new_msg+'"')
    #     else:
    #         msg = msg.replace(old_msg, new_msg)
    #     batch_file = open('git_update.bat', 'w')
    #     batch_file.write(msg)
    #     batch_file.close()
    #     self.write_to_log(msg)

    # def get_git_msg_from_box(self, textbox):
    #     try:
    #         new_name = str(textbox.get(1.0, "end-1c")).replace('\n', '').strip()
    #     except:
    #         new_name = 'update'
    #     self.update_batch_file_message(new_name)
    
    # def get_unwatched_porn_hours(self):
    #     animated = ''
    #     filename = ''
    #     comparator = '>='
    #     desired_ethnicities = []
    #     desired_genres = []
    #     desired_pornstars = ''
    #     duration = ''
    #     path_in_filter = self.root_path
    #     undesired_ethnicities = []
    #     undesired_genres = []
    #     undesired_pornstars = []
    #     for genre in self.get_list_of_contents(self.genretxt):
    #         if genre.strip() not in self.allowed:
    #             undesired_genres.append(genre)
    #     filename = ''
    #     path_in_filter = self.root_path
    #     filtereddataframe = self.filter_dataframe(self.dataframe, animated, desired_pornstars, 
    #                                 filename, duration,
    #                                 comparator, 's', desired_genres, '', desired_ethnicities,
    #                                 path_in_filter, undesired_pornstars, undesired_genres,
    #                                 undesired_ethnicities, set_global_filter=False)
    #     return filtereddataframe['Duration'].sum()
    
    # def update_porn_hours(self, hourLable):
    #     self.total_porn_hours = round((self.dataframe['Duration'].sum()) / 3600, 2)
    #     self.filtered_porn_hours = round((self.filtereddataframe['Duration'].sum()) / 3600, 2)
    #     self.total_unwatched_porn_hours = round((self.get_unwatched_porn_hours()) / 3600, 2)
    #     self.total_watched_porn_hours = round(self.total_porn_hours - self.total_unwatched_porn_hours, 2)
    #     self.total_file_size = round(self.get_folder_size(self.root_path)/1073741824, 2)
    #     self.write_to_log('{}, {}, {}'.format(self.total_porn_hours, self.total_watched_porn_hours, self.total_unwatched_porn_hours))
    #     watched_label = 'Total Porn Hours:\n{}\n\nTotal Watched:\n{}\n\nTotal Unwatched:\n{}\n\nFiltered Hours:\n{}\n\nTotal File Size:\n{}GB'.format(
    #         self.total_porn_hours,
    #         self.total_watched_porn_hours,
    #         self.total_unwatched_porn_hours,
    #         self.filtered_porn_hours,
    #         self.total_file_size
    #     )
    #     Total_Hours_of_Porn = Label_Widget(Tk)
    #     if type(hourLable) == type(Total_Hours_of_Porn):
    #         hourLable.change_text(watched_label)

    # def replace_text_in_textfile(self, filename, oldstring='\n\n', newstring='\n', justAddingToEnd=False):
    #     file_name = open(filename, 'r')
    #     text = file_name.read()
    #     file_name.close()
    #     if text.__contains__(oldstring):
    #         self.write_to_log('{} contains {} and will be replaced with {}'.format(filename, oldstring, newstring))
    #         text = text.replace(oldstring, newstring)
    #         file_name = open(filename, 'w')
    #         file_name.write(text)
    #         file_name.close()
    #     else:
    #         self.write_to_log('{} does not contain {} and so it will not be replaced with {}'.format(filename, oldstring, newstring))
    #         if justAddingToEnd:
    #             text = text.strip()+'\n'+newstring
    #             file_name = open(filename, 'w')
    #             file_name.write(text)
    #             file_name.close()

    # def initial_update(self):
    #     master_done = False
    #     iterations = 0
    #     while (not master_done) and iterations <= 3:
    #         iterations = iterations + 1
    #         list_of_known_paths = self.list_from_dataframe(self.dataframe, 'Path')
    #         list_of_known_videos = self.list_from_dataframe(self.dataframe, 'Filename')
    #         list_of_known_files = []
    #         if len(list_of_known_paths) == len(list_of_known_videos):
    #             for i in range(0, len(list_of_known_videos)):
    #                 pathe = list_of_known_paths[i]
    #                 vid = list_of_known_videos[i]
    #                 list_of_known_files.append(os.path.join(pathe, vid))
    #             list_of_known_files = list(set(list_of_known_files))
    #         else:
    #             self.write_to_log('The number of filenames does not match the number of paths')
    #         list_of_all_videos = self.get_all_videos_from_root(self.root_path)
    #         paths_to_check = []
    #         list_of_all_videos.sort(key=str.lower)
    #         list_of_known_files.sort(key=str.lower)
    #         if list_of_all_videos == list_of_known_files:
    #             self.write_to_log('All videos are accounted for')
    #             skip = True
    #         elif len(list_of_all_videos) > len(list_of_known_files):
    #             skip = False
    #             self.write_to_log('There are more videos in root than known')
    #             self.write_to_log('All {}; Known {}'.format(len(list_of_all_videos), len(list_of_known_files)))
    #             for file in list_of_all_videos:
    #                 if file not in list_of_known_files:
    #                     path, name = os.path.split(file)
    #                     if path not in paths_to_check:
    #                         paths_to_check.append(path)
    #         elif len(list_of_all_videos) < len(list_of_known_files):
    #             skip = False
    #             self.write_to_log('There are more videos in known than root')
    #             self.write_to_log('All {}; Known {}'.format(len(list_of_all_videos), len(list_of_known_files)))
    #             for file in list_of_known_files:
    #                 if file not in list_of_all_videos: #then we know it does not exist
    #                     path, name = os.path.split(file)
    #                     if path not in paths_to_check:
    #                         paths_to_check.append(path)
    #                     filteredframe = self.filter_dataframe(self.dataframe, Filename=name)
    #                     if len(filteredframe) == 0:
    #                         self.dataframe = self.remove_row_from_dataframe(self.dataframe, name, path)
    #                     elif len(filteredframe) == 1:
    #                         rowI = self.get_row_index(filteredframe, name, path)
    #                         p = self.get_value_at_cell(rowI, 'Path', filteredframe)
    #                         n = self.get_value_at_cell(rowI, 'Filename', filteredframe)
    #                         self.dataframe = self.remove_row_from_dataframe(self.dataframe, n, p)
    #                     elif (name.lower().__contains__('psi')) and (len(filteredframe) != 0):
    #                         self.write_to_log('!')
    #                         self.write_to_log(filteredframe)
    #             self.dataframe.replace(float('nan'), '')
    #             self.dataframe.replace(',nan,', '')
    #             self.dataframe.to_csv(self.the_csv, index=False)
    #             list_of_known_paths = self.list_from_dataframe(self.dataframe, 'Path')
    #             list_of_known_videos = self.list_from_dataframe(self.dataframe, 'Filename')
    #             list_of_known_files = []
    #             for i in range(0, len(list_of_known_videos)):
    #                 pathe = list_of_known_paths[i]
    #                 vid = list_of_known_videos[i]
    #                 list_of_known_files.append(os.path.join(pathe, vid))
    #             list_of_known_files = list(set(list_of_known_files))
    #             list_of_known_files.sort(key=str.lower)
    #             if list_of_known_files == list_of_all_videos:
    #                 self.write_to_log('they match now')
    #                 skip = True
    #         elif len(list_of_all_videos) == len(list_of_known_files):
    #             self.write_to_log('The number of videos is the same but these lists are not equivalent')
    #             if iterations > 1:
    #                 list_of_known_filesL = [element.lower() for element in list_of_known_files]
    #                 list_of_all_videosL = [element.lower() for element in list_of_all_videos]
    #                 if list_of_all_videosL == list_of_known_filesL:
    #                     self.write_to_log('For whatever reason there is a case difference but all of the file names are there')
    #                     for index in range(0, len(list_of_all_videos)):
    #                         shin_name = list_of_all_videos[index]
    #                         faux_name = list_of_known_files[index]
    #                         if not (shin_name == faux_name):
    #                             self.write_to_log('A case difference was found:\nReal name: {}\nCSV name: {}'.format(shin_name,
    #                                                                                                     faux_name))
    #                             shin_path, shin_name = os.path.split(shin_name)
    #                             shin_extension = shin_name.split('.')[1]
    #                             faux_path, faux_name = os.path.split(faux_name)
    #                             faux_extension = faux_name.split('.')[1]
    #                             if shin_path == faux_path:
    #                                 self.write_to_log('The paths are good.  They both are:\n{}'.format(shin_path))
    #                             else:
    #                                 self.dataframe = self.edit_dataframe(self.dataframe, faux_name, faux_path,
    #                                                                     'Path', shin_path)
    #                                 self.write_to_log('The path was updated from:\n{}\nto\n{}'.format(faux_path, shin_path))
    #                             if shin_name == faux_name:
    #                                 self.write_to_log('The names are good.  They both are:\n{}'.format(shin_name))
    #                             else:
    #                                 try:
    #                                     self.dataframe = self.edit_dataframe(self.dataframe, faux_name, shin_path,
    #                                                                         'Filename', shin_name)
    #                                 except:
    #                                     self.write_to_log('{}, {}, {}, {}'.format(faux_name, shin_path, 'Filename', shin_name))
    #                                     exit()
    #                             if shin_extension == faux_extension:
    #                                 self.write_to_log('The extensions are good.  They both are:\n{}'.format(shin_extension))
    #                             else:
    #                                 self.dataframe = self.edit_dataframe(self.dataframe, shin_name, shin_path,
    #                                                                     'Filetype', shin_extension)
    #                                 self.write_to_log('The extension was updated from:\n{}\nto\n{}'.format(faux_extension,
    #                                                                                            shin_extension))
    #                     self.dataframe.to_csv(self.the_csv, index=False)
    #             else:
    #                 skip = False
    #                 nonexistent_files = []
    #                 for full_file in list_of_known_files:
    #                     if full_file not in list_of_all_videos:
    #                         nonexistent_files.append(full_file)
    #                 for full_file in nonexistent_files:
    #                     pathe, name = os.path.split(full_file)
    #                     for path in self.get_all_folders_from_root(self.root_path):
    #                         if os.path.exists(os.path.join(path, name)):
    #                             self.dataframe = self.edit_dataframe(self.dataframe, name, pathe, 'Path', path)
    #                 list_of_known_paths = self.list_from_dataframe(self.dataframe, 'Path')
    #                 list_of_known_videos = self.list_from_dataframe(self.dataframe, 'Filename')
    #                 if len(list_of_known_paths) == len(list_of_known_videos):
    #                     if len(list_of_all_videos) == len(list_of_known_files):
    #                         self.write_to_log('lengths still match')
    #                     list_of_known_files = []
    #                     for i in range(0, len(list_of_known_videos)):
    #                         pathe = list_of_known_paths[i]
    #                         vid = list_of_known_videos[i]
    #                         list_of_known_files.append(os.path.join(pathe, vid))
    #                     list_of_known_files = list(set(list_of_known_files))
    #                     list_of_known_files.sort(key=str.lower)
    #                 if not (list_of_all_videos == list_of_known_files):
    #                     self.write_to_log('There is still a mismatch')
    #                     for file in list_of_known_files:
    #                         if file not in list_of_all_videos:
    #                             self.write_to_log(file)
    #                 else:
    #                     skip = True
    #                     self.write_to_log('skip = True')
    #                     self.dataframe.to_csv(self.the_csv, index=False)
    #         else:
    #             self.write_to_log('This should never happen')
    #             skip = True
    #         if not skip:
    #             done = False
    #             while not done:
    #                 self.write_to_log('Must check:')
    #                 self.write_to_log(paths_to_check)
    #                 upper_paths = []
    #                 for path in paths_to_check:
    #                     if not os.path.exists(path):
    #                         self.write_to_log('{} not longer exists'.format(path))
    #                         up_path = os.path.abspath(os.path.join(path, os.pardir))
    #                         if up_path not in upper_paths:
    #                             upper_paths.append(up_path)
    #                     elif len(os.listdir(path)) < 1:
    #                         self.write_to_log('{} has {} files'.format(os.listdir(path), len(os.listdir(path))))
    #                         up_path = os.path.abspath(os.path.join(path, os.pardir))
    #                         if up_path not in upper_paths:
    #                             upper_paths.append(up_path)
    #                     else:
    #                         self.update_csv(self.get_all_videos_from_root(path), self.the_csv)
    #                         self.check_existence_of_videos_from_directory(path)
    #                         self.dataframe.replace(',nan,', '')
    #                         self.dataframe.replace(float('nan'), '')
    #                         self.dataframe.to_csv(self.the_csv, index=False)
    #                         self.start_file('git_update.bat', False)
    #                         self.dataframe = pd.read_csv(self.the_csv, delimiter=',', header=0,
    #                                             skip_blank_lines=True, na_values='') 
    #                 if upper_paths == []:
    #                     done = True
    #                 elif self.root_path in upper_paths:
    #                     done = True
    #                 else:
    #                     paths_to_check = []
    #                     for item in upper_paths:
    #                         paths_to_check.append(item)
    #         else:
    #             master_done = True

    # def check_existence_of_videos_from_directory(self, directory):
    #     sus_dataframe = self.filter_dataframe(self.dataframe, Path=directory)
    #     for file in self.list_of_filez_from_dataframe(sus_dataframe):
    #         if not os.path.exists(file):
    #             self.write_to_log('{} seems to no longer exist'.format(file))
    #             path, name = os.path.split(file)
    #             self.dataframe = self.remove_row_from_dataframe(self.dataframe, name, path)

    # def ave_num_char(self, heading):
    #     names = []
    #     for index in range(0, len(self.dataframe)):
    #         names.append(len(self.get_value_at_cell(index, heading, self.dataframe)))
    #     self.write_to_log('{}, {}, {}'.format(max(names), min(names), int((max(names)+min(names))/2)))

    # def add_pornstars_to_search(self, listbox, filterButtonWidget):
    #     if self.desired_or_undesired == self.desired_or_undesired_options[0]:
    #         self.get_multiple_selection(listbox, self.desired_pornstars)
    #         self.write_to_log(self.desired_pornstars)
    #     elif self.desired_or_undesired == self.desired_or_undesired_options[1]:
    #         self.get_multiple_selection(listbox, self.undesired_pornstars)
    #         self.write_to_log(self.undesired_pornstars)
    #     else:
    #         self.write_to_log('Was {} which is not valid.  It is now set to {}'.format(self.desired_or_undesired_options[0]))
    #         self.get_multiple_selection(listbox, self.desired_pornstars)
    #         self.write_to_log(self.desired_pornstars)
    #     listbox.selection_clear(0, 'end')
    #     filterButtonWidget.change_color(background='#09f042')

    # def add_genres_to_search(self, listbox, filterButtonWidget):
    #     if self.desired_or_undesired == self.desired_or_undesired_options[0]:
    #         self.get_multiple_selection(listbox, self.desired_genres)
    #         self.write_to_log(self.desired_genres)
    #     elif self.desired_or_undesired == self.desired_or_undesired_options[1]:
    #         self.get_multiple_selection(listbox, self.undesired_genres)
    #         self.write_to_log(self.undesired_genres)
    #     else:
    #         self.write_to_log('Was {} which is not valid.  It is now set to {}'.format(self.desired_or_undesired_options[0]))
    #         self.get_multiple_selection(listbox, self.desired_genres)
    #         self.write_to_log(self.desired_genres)
    #     listbox.selection_clear(0, 'end')
    #     filterButtonWidget.change_color(background='#09f042')

    # def add_ethnicities_to_search(self, listbox, filterButtonWidget):
    #     if self.desired_or_undesired == self.desired_or_undesired_options[0]:
    #         self.get_multiple_selection(listbox, self.desired_ethnicities)
    #         self.write_to_log(self.desired_ethnicities)
    #     elif self.desired_or_undesired == self.desired_or_undesired_options[1]:
    #         self.get_multiple_selection(listbox, self.undesired_ethnicities)
    #         self.write_to_log(self.undesired_ethnicities)
    #     else:
    #         self.write_to_log('Was {} which is not valid.  It is now set to {}'.format(self.desired_or_undesired_options[0]))
    #         self.get_multiple_selection(listbox, self.desired_ethnicities)
    #         self.write_to_log(self.desired_ethnicities)
    #     listbox.selection_clear(0, 'end')
    #     filterButtonWidget.change_color(background='#09f042')

    # def remove_pornstars_from_search(self, listbox, buttonWiget):
    #     if self.desired_or_undesired == self.desired_or_undesired_options[0]:
    #         self.get_multiple_selections_removed(listbox, self.desired_pornstars)
    #         self.write_to_log(self.desired_pornstars)
    #     elif self.desired_or_undesired == self.desired_or_undesired_options[1]:
    #         self.get_multiple_selections_removed(listbox, self.undesired_pornstars)
    #         self.write_to_log(self.undesired_pornstars)
    #     else:
    #         self.write_to_log('Was {} which is not valid.  It is now set to {}'.format(self.desired_or_undesired_options[0]))
    #         self.get_multiple_selections_removed(listbox, self.desired_pornstars)
    #         self.write_to_log(self.desired_pornstars)
    #     listbox.selection_clear(0, 'end')
    #     if self.there_are_filters():
    #         buttonWiget.change_color(background='#f04209')
    #     else:
    #         buttonWiget.change_color(background='#09f042')

    # def remove_genres_from_search(self, listbox, buttonWiget):
    #     if self.desired_or_undesired == self.desired_or_undesired_options[0]:
    #         self.get_multiple_selections_removed(listbox, self.desired_genres)
    #         self.write_to_log(self.desired_genres)
    #     elif self.desired_or_undesired == self.desired_or_undesired_options[1]:
    #         self.get_multiple_selections_removed(listbox, self.undesired_genres)
    #         self.write_to_log(self.undesired_genres)
    #     else:
    #         self.write_to_log('Was {} which is not valid.  It is now set to {}'.format(self.desired_or_undesired_options[0]))
    #         self.get_multiple_selections_removed(listbox, self.desired_genres)
    #         self.write_to_log(self.desired_genres)
    #     listbox.selection_clear(0, 'end')
    #     if self.there_are_filters():
    #         buttonWiget.change_color(background='#f04209')
    #     else:
    #         buttonWiget.change_color(background='#09f042')

    # def remove_ethnicities_from_search(self, listbox, buttonWiget):
    #     if self.desired_or_undesired == self.desired_or_undesired_options[0]:
    #         self.get_multiple_selections_removed(listbox, self.desired_ethnicities)
    #         self.write_to_log(self.desired_ethnicities)
    #     elif self.desired_or_undesired == self.desired_or_undesired_options[1]:
    #         self.get_multiple_selections_removed(listbox, self.undesired_ethnicities)
    #         self.write_to_log(self.undesired_ethnicities)
    #     else:
    #         self.write_to_log('Was {} which is not valid.  It is now set to {}'.format(self.desired_or_undesired_options[0]))
    #         self.get_multiple_selections_removed(listbox, self.desired_ethnicities)
    #         self.write_to_log(self.desired_ethnicities)
    #     listbox.selection_clear(0, 'end')
    #     if self.there_are_filters():
    #         buttonWiget.change_color(background='#f04209')
    #     else:
    #         buttonWiget.change_color(background='#09f042')
    
    # def there_are_filters(self):
    #     val = False
    #     if self.desired_ethnicities == []:
    #         if self.undesired_ethnicities == []:
    #             if (self.desired_genres == []) and (self.undesired_genres == []):
    #                 if (self.undesired_pornstars == []) and (self.desired_pornstars == []):
    #                     if (self.animated == '') and (self.filename == ''):
    #                         if (self.path_in_filter == self.root_path) or (self.path_in_filter == ''):
    #                             if (self.range_selected == False) and (self.duration < 1):
    #                                 val = True
    #                             elif (self.range_selected == True):
    #                                 if (self.upper_duration > 5*60*60) and (self.lower_duration < 2):
    #                                     val = True
    #                             if (val):
    #                                 if not (len(self.dataframe) == len(self.filtereddataframe)):
    #                                     val = False
    #                                 if val:
    #                                     self.video_completeness = 'incomplete/complete'
    #     return val
    
    # def get_multiple_selection(self, listbox, liste):
    #     for selection in listbox.curselection():
    #         if listbox.get(selection) not in liste:
    #             liste.append(listbox.get(selection))
    #     return liste
    
    # def get_multiple_selections_removed(self, listbox, liste):
    #     for selection in listbox.curselection():
    #         if listbox.get(selection) in liste:
    #             liste.remove(listbox.get(selection))
    #     return liste

    # def get_list_of_contents(self, filename):
    #     file = open(filename, 'r')
    #     contents = file.readlines()
    #     file.close()
    #     real_list = []
    #     for content in contents:
    #         real_list.append(content.replace('\n', '').strip())
    #     return real_list
    
    # def set_selection(self, selection, buttonWiget):
    #     if selection in self.selections:
    #         self.selection = selection
    #         self.write_to_log('{} is selected'.format(selection))
    #     elif type(selection) == type(Label()):
    #         if self.animated == '':
    #             self.animated = 'True'
    #         elif self.animated == 'True':
    #             self.animated = 'False'
    #         elif self.animated == 'False':
    #             self.animated = ''
    #         self.selection = selection
    #         self.write_to_log('{} is selected'.format(selection))
    #         selection.config(text=self.animated)
    #     else:
    #         self.write_to_log('{} is not allowed'.format(selection))
    #         self.selection = self.selections[0]
    #     if self.there_are_filters():
    #         buttonWiget.change_color(background='#f04209')
    #     else:
    #         buttonWiget.change_color(background='#09f042')
    
    # def reset_animated_label(self, label, defalttext=''):
    #     self.animated = defalttext
    #     label.labels[0].config(text=self.animated)

    # def update_hours(self, inputbod, buttonWiget):
    #     inp = inputbod.get(1.0, "end-1c")
    #     self.write_to_log(inp)
    #     try:
    #         inp = int(inp)
    #     except:
    #         self.write_to_log('{} is not a number'.format(inp))
    #         inp = 0
    #     self.hours = inp
    #     self.update_duration(buttonWiget)

    # def update_minutes(self, inputbod, buttonWiget):
    #     inp = inputbod.get(1.0, "end-1c")
    #     self.hours_overflowm = 0
    #     self.write_to_log(inp)
    #     try:
    #         inp = int(inp)
    #     except:
    #         self.write_to_log('{} is not a number'.format(inp))
    #         inp = 0
    #     # if inp >= 60:
    #     #     self.hours_overflowm = int(inp/60)
    #     #     self.minutes = inp - (60*self.hours_overflowm)
    #     # else:
    #     self.minutes = inp
    #     self.hours_overflowm = 0
    #     self.update_duration(buttonWiget)

    # def update_seconds(self, inputbod, buttonWiget):
    #     inp = inputbod.get(1.0, "end-1c")
    #     self.write_to_log(inp)
    #     try:
    #         inp = int(inp)
    #     except:
    #         self.write_to_log('{} is not a number'.format(inp))
    #         inp = 0
    #     self.seconds = inp
    #     self.update_duration(buttonWiget)

    # def update_all_time(self, inputbod, buttonWiget):
    #     if (len(inputbod)==len(buttonWiget))and(type(inputbod)==type(buttonWiget))and(type(inputbod)==type([])):
    #         for i in range(0, len(inputbod)):
    #             inbo = inputbod[i].inputboxes[len(inputbod[i].inputboxes)-1]
    #             widget = inputbod[i]
    #             buwi = buttonWiget[i]
    #             if i == 0:
    #                 self.update_hours(inbo, buwi)
    #             elif i == 1:
    #                 self.update_minutes(inbo, buwi)
    #             elif i == 2:
    #                 self.update_seconds(inbo, buwi)
    #             else:
    #                 self.write_to_log(str(i) + 'This aint right')
    #             widget.clear()
    #     else:
    #         self.write_to_log('Check again!')
    #         exit(0)

    # def update_duration(self, buttonWiget):
    #     self.duration = ((self.hours) * 60 * 60)
    #     self.duration = self.duration + ((self.minutes) * 60)
    #     self.duration = self.duration + self.seconds
    #     if self.there_are_filters():
    #         buttonWiget.change_color(background='#f04209')
    #     else:
    #         buttonWiget.change_color(background='#09f042')

    # def update_comparator(self, comparator):
    #     self.write_to_log(comparator)
    #     self.comparator = comparator
    #     self.range_selected = False

    # def update_upper_comparator(self, comparator):
    #     self.write_to_log(comparator)
    #     self.comparator = '>='
    #     self.upper_duration = self.duration
    #     self.upper_comparator = comparator
    #     self.range_selected = True

    # def update_lower_comparator(self, comparator):
    #     self.write_to_log(comparator)
    #     self.comparator = '>='
    #     self.lower_duration = self.duration
    #     self.lower_comparator = comparator
    #     self.range_selected = True

    # def get_single_selection(self, box):
    #     try:
    #         try:
    #             listbox = box.listboxess[len(box.listboxess)-1]
    #             try:
    #                 video = listbox.get(listbox.curselection())
    #             except Exception as error:
    #                 self.write_to_log(str(error)+ ' therefor I am returning \'\'')
    #                 video = ''
    #         except Exception as err:
    #             self.write_to_log('here'+ str(err))
    #             video = ''
    #     except Exception as error:
    #         self.write_to_log('Error:' + str(error))
    #         index = self.generate_random_integer(0, len(self.dataframe))
    #         path = self.get_value_at_cell(index, 'Path', self.dataframe)
    #         name = self.get_value_at_cell(index, 'Filename', self.dataframe)
    #         video = os.path.join(path, name)
    #         self.write_to_log(video)
    #     return video
    
    # def move_file(self, filtered_listbox_widget, list_of_folders_widget):
    #     video = self.get_single_selection(filtered_listbox_widget)
    #     new_path = self.get_single_selection(list_of_folders_widget)
    #     old_path, filename = os.path.split(video)
    #     new_video = os.path.join(new_path, filename)
        # shutil.move(video, new_video)
        # self.dataframe = self.edit_dataframe(self.dataframe, filename, old_path, 'Path', new_path)
        # self.filtereddataframe = self.edit_dataframe(self.filtereddataframe, filename,
        #                                              old_path, 'Path', new_path)
        # self.dataframe.replace(float('nan'), '')
        # self.dataframe.replace(',nan,', '')
        # self.dataframe.to_csv(self.the_csv, index=False)
        # optionz = list_of_folders_widget.options
        # list_of_folders_widget.remove_everything()
        # list_of_folders_widget.populate_box(list_of_folders_widget.listboxess[0], optionz)
        # optionz = filtered_listbox_widget.options
        # optionz.remove(video)
        # optionz.append(new_video)
        # optionz.sort(key=str.lower)
        # filtered_listbox_widget.remove_everything()
        # filtered_listbox_widget.populate_box(filtered_listbox_widget.listboxess[0], optionz)

    def get_value_at_cell_without_row(self, frame, filename, pathe, heading):
        rowI = self.get_row_index(frame, filename, pathe)
        val = self.get_value_at_cell(rowI, heading, frame)
        return val
    
    def start_file(self, file, is_video=True, hours_lable=False,
                   filtered_listbox_widget='i', list_of_folders_widget='j',
                   FilenameSearchInput='k'):
        if is_video:
            # subprocess.Popen('Taskkill /f /im Video.UI.exe',
            #                  stdout=subprocess.PIPE,
            #                  stderr=subprocess.STDOUT,
            #                  shell=True)
            duration = self.get_duration(file)
            path, name = os.path.split(file)
            current_duration = self.get_value_at_cell_without_row(self.dataframe, name, path, 'Duration')
            self.write_to_log('got_duration')
            if not abs(duration - current_duration) <= 1:
                self.write_to_log('Will play {} but the duration is not correct'.format(file))
                self.write_to_log('Old duration is {}secs.  Updated duration is {}secs'.format(current_duration, duration))
                self.dataframe = self.edit_dataframe(self.dataframe, name, path, 'Duration', duration)
                self.dataframe.to_csv(self.the_csv, index=False)
                self.filtereddataframe = self.edit_dataframe(self.filtereddataframe, name,
                                                             path, 'Duration', duration)
            if not hours_lable==False:
                self.write_to_log('"not hours_lable==False" is True')
                self.total_porn_hours = round((self.dataframe['Duration'].sum()) / 3600, 2)
                self.filtered_porn_hours = round((self.filtereddataframe['Duration'].sum()) / 3600, 2)
                self.total_unwatched_porn_hours = round((self.get_unwatched_porn_hours()) / 3600, 2)
                self.total_watched_porn_hours = round(self.total_porn_hours - self.total_unwatched_porn_hours, 2)
                self.write_to_log('{}, {}, {}'.format(self.total_porn_hours, self.total_watched_porn_hours,
                                   self.total_unwatched_porn_hours))
                self.total_file_size = round(self.get_folder_size(self.root_path)/1073741824, 2)
                watched_label = 'Total Porn Hours:\n{}\n\nTotal Watched:\n{}\n\nTotal Unwatched:\n{}\n\nFiltered Hours:\n{}\n\nTotal File Size:\n{}GB'.format(
                    self.total_porn_hours,
                    self.total_watched_porn_hours,
                    self.total_unwatched_porn_hours,
                    self.filtered_porn_hours,
                    self.total_file_size
                    )
                hours_lable.change_text(watched_label)
            else:
                self.write_to_log(type(hours_lable))
        else:
            path = ''
            if file == 'git_update.bat':
                message = self.get_batch_file_message()
                if (message == '') or (message == '""'):
                    self.write_to_log('the message is blank for github.  Will set it to update')
                    self.update_batch_file_message()
        os.startfile(file)
        if path.__contains__('to\\H\\new'):
            self.move_seen_video(name, path, duration, filtered_listbox_widget=filtered_listbox_widget,
                                 list_of_folders_widget=list_of_folders_widget)
        if not FilenameSearchInput == 'k':
            FilenameSearchInput.clear()
        if file.__contains__('.bat'):
            time.sleep(1)

    def move_seen_video(self, file, path, duration, filtered_listbox_widget='i', list_of_folders_widget='j'):
        application = 'Video.UI.exe'
        video_still_open = self.check_if_application_is_open(application)
        if video_still_open:
            the_new_hentai_folder = path
            the_old_hentai_folder = path.replace('\\new', '\\old')
            if self.was_the_video_watched(file, the_new_hentai_folder, duration):
                self.move_the_file(file, the_old_hentai_folder, new_folder=the_new_hentai_folder,
                                   filtered_listbox_widget=filtered_listbox_widget,
                                   list_of_folders_widget=list_of_folders_widget)

    def was_the_video_watched(self, file, path, duration_of_video_in_seconds):
        a_watched_video = os.path.join(path, file)
        application = 'Video.UI.exe'
        self.write_to_log('was_the_video_watched start for {}'.format(file))
        video_access_time = 1677555334.6660264
        try:
            video_access_time = os.path.getatime(a_watched_video)
            self.write_to_log('video access time: {}'.format(video_access_time))
        except Exception as something:
            self.write_to_log('Could not get video access time')
            self.write_to_log(something)
        try:
            error = os.path.getatime(a_watched_video) - video_access_time
        except:
            try:
                error = os.path.getatime(a_watched_video) - video_access_time
            except Exception as idfk:
                self.write_to_log('Accounting for error in acces time ERROR with video {}'.format(a_watched_video))
                self.write_to_log(idfk)
                error = 1
        alpha = 3*.01
        sleep_durration = alpha*duration_of_video_in_seconds
        for_loop_delay = .731676
        if sleep_durration <= for_loop_delay:
            sleep_durration = ((1 + int(for_loop_delay *100)) / 100)
        else:
            sleep_durration = sleep_durration - .731676
        self.write_to_log('for_loop_delay is {}; sleep_durration is {}'.format(for_loop_delay, sleep_durration))
        for i in range(1, 1+1):
            time.sleep(sleep_durration/1)
            if not self.check_if_application_is_open('Video.UI.exe'):
                return False
        bad = 0
        for i in range(0+1, 20+1): #Check if 75ish% was watched
            try:
                video_still_open = self.check_if_application_is_open('Video.UI.exe')
            except Exception as something_else:
                self.write_to_log('video_still_open = check_if_application_is_open(application) threw an error')
                self.write_to_log(something_else)
                return False
            if not video_still_open:
                self.write_to_log(str(a_watched_video) + ' video is not still open at i = ' + str(i))
                return False
            alpha_i = 3*i*.01
            new_video_access_time = os.path.getatime(a_watched_video)
            if (i==1) or (i==21) or (i%3==0):
                self.write_to_log('i in the was_the_video_watched for loop is {}'.format(i))
            self.write_to_log('new time ' + str(new_video_access_time))
            self.write_to_log('time delta ' + str(new_video_access_time - video_access_time))
            self.write_to_log('total duration ' + str(((alpha)*duration_of_video_in_seconds)))
            self.write_to_log(abs((new_video_access_time - video_access_time) - ((alpha)*duration_of_video_in_seconds)))
            absolute_diff = abs((new_video_access_time - video_access_time) - ((alpha)*duration_of_video_in_seconds))
            if absolute_diff < 20: #should not differ by more than 20 seconds
                self.write_to_log('probably being watched')
                bad = 0
                video_access_time = new_video_access_time
                for i in range(1, 1+1):
                    time.sleep(sleep_durration/1)
                    if not self.check_if_application_is_open('Video.UI.exe'):
                        return False
            else:
                self.write_to_log('probably was accessed but bug might have happened')
                bad = 1 + bad
                video_access_time = new_video_access_time
                for i in range(1, 1+1):
                    time.sleep(sleep_durration/1)
                    if not self.check_if_application_is_open('Video.UI.exe'):
                        return False
                if (bad > 1) and i > 2: #Odd to watch that much of video then stop
                    self.write_to_log('probably was accessed but not being watched')
                    return False
                else:
                    bad = bad - .001
        self.write_to_log('plenty was watched')
        if bad == 0:
            self.write_to_log('shall let it finish before continuing')
            ready_to_return = False
            i = 0
            sleep_durration = .01*duration_of_video_in_seconds
            while_not_loop_delay = .76113
            if sleep_durration <= while_not_loop_delay:
                sleep_durration = ((1 + int(while_not_loop_delay *100)) / 100)
            else:
                sleep_durration = sleep_durration - while_not_loop_delay
            video_access_time = os.path.getatime(a_watched_video)
            self.write_to_log('while not ready_to_return: initial video access time = {}'.format(video_access_time))
            while not ready_to_return:
                video_still_open = self.check_if_application_is_open(application)
                self.write_to_log('video still open-->' + str(video_still_open))
                if (i >= 17) and (not video_still_open):
                    self.write_to_log('returning True:\n(i >= 17) and (not video_still_open) == True')
                    ready_to_return = True#>85ish or so% of hentai was watched
                elif (i < 1) and (not video_still_open):
                    self.write_to_log('returning False:\n(i < 1) and (not video_still_open); i = ' + str(i))
                    return False #<85% of hentai was watched
                else:
                    time.sleep(sleep_durration/5)
                    i = i + 1/5
                    if i >= 35:
                        self.write_to_log('returning True:\ni is >= 35 so I think we are done here')
                        ready_to_return = True#95ish% of hentai was watched
            self.write_to_log('exited the while not ready_to_return i = ' + str(i))
            if i % 3 < 1:
                new_video_access_time = os.path.getatime(a_watched_video)
                self.write_to_log('new video access time: {}\nvideo access time: {}'.format(new_video_access_time, video_access_time))
                self.write_to_log('video access time difference: {}'.format(abs(new_video_access_time-video_access_time)))
            if new_video_access_time - video_access_time < 2:
                ready_to_return = True
            else:
                video_access_time == new_video_access_time
            return True
        else:
            self.write_to_log('this should not be printed')
            return False

    def check_if_application_is_open(self, app):
        processName = app
        '''
        Check if there is any running process that
        contains the givenname processName.
        '''
        #Iterate over the all the running process
        for proc in psutil.process_iter():
            #print(proc.name())
            try:
                # Check if process name contains the given name string.
                if processName.lower() in proc.name().lower():
                    self.write_to_log('Application is open')
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        #write2file('Application is closed')
        self.write_to_log('application is open return boolean = False')
        return False
    
    def move_the_file(self, the_file_to_be_moved, old_folder, new_folder='unused',
                      list_of_folders_widget='i', filtered_listbox_widget='j'):
        seen_it_folder = str(os.path.join(old_folder, the_file_to_be_moved))
        have_yet_to_see_it_folder = str(os.path.join(old_folder.replace('\\old', '\\new'), the_file_to_be_moved))
        self.write_to_log('not seen: ' + have_yet_to_see_it_folder)
        self.write_to_log('seen: ' + seen_it_folder)
        tries = 0
        video = seen_it_folder
        old_path, filename = os.path.split(seen_it_folder)
        new_path = old_path.replace('\\old', '\\new')
        new_video = os.path.join(new_path, filename)
        while (not os.path.exists(seen_it_folder)) and tries < 3:
            shutil.move(have_yet_to_see_it_folder, seen_it_folder)
        if os.path.exists(seen_it_folder):
            self.write_to_log('{} was successfully moved to {}'.format(seen_it_folder, old_folder))
            #need to make kosher with the csv and gui
            self.write_to_log('move_the_file\n{}, from {}, to {}'.format(filename, new_path, old_path))
            self.dataframe = self.edit_dataframe(self.dataframe, filename, new_path, 'Path', old_path)
            self.write_to_log('move_the_file dataframe was edited')
            self.filtereddataframe = self.edit_dataframe(self.filtereddataframe, filename,
                                                     new_path, 'Path', old_path)
            self.write_to_log('move_the_file filtered dataframe was edited')
            self.dataframe.replace(float('nan'), '')
            self.dataframe.replace(',nan,', '')
            self.dataframe.to_csv(self.the_csv, index=False)
            err = ''
            try:
                optionz = list_of_folders_widget.options
            except Exception as err:
                self.write_to_log('optionz = list_of_folders_widget.options {}'.format(err))
            try:
                list_of_folders_widget.remove_everything()
            except Exception as err:
                self.write_to_log('list_of_folders_widget.remove_everything() failed {}'.format(err))
            try:
                list_of_folders_widget.populate_box(list_of_folders_widget.listboxess[0], optionz)
            except Exception as err:
                self.write_to_log('list_of_folders_widget.populate_box(list_of_folders_widget.listboxess[0], optionz) {}'.format(err))
            try:
                optionz = filtered_listbox_widget.options
                self.write_to_log('move_the_file video variable is {}'.format(video))
                new_video = video.replace('\\old', '\\new')
                self.write_to_log('move_the_file new_video variable is {}'.format(new_video))
                try:
                    if new_video.__contains__('\\old\\'):
                        new_video = new_video.replace('\\old\\', '\\new\\')
                    if video.__contains__('\\new\\'):
                        video = video.replace('\\new\\', '\\old\\')
                    optionz.remove(new_video)
                except Exception as err:
                    message = 'optionz block failed.  error is:\n{}\ndebug info is:\n'.format(err)
                    message = message + 'Type of optionz is {}\n'.format(type(optionz))
                    message = message + 'Type of video is {}\n'.format(type(video))
                    message = message + 'Video is {}\n'.format(video)
                    message = message + 'optionz is/are {}\n'.format(optionz)
                    self.write_to_log(message)
                optionz.append(video)
                self.write_to_log('{} was removed from optionz and {} was added to optionz'.format(new_video, video))
                optionz.sort(key=str.lower)
                filtered_listbox_widget.remove_everything()
                filtered_listbox_widget.populate_box(filtered_listbox_widget.listboxess[0], optionz)
            except Exception as err:
                self.write_to_log('optionz block failed {}'.format(err))
            message = self.get_batch_file_message()
            if (message == '') or (message == '""'):
                self.write_to_log('the message is blank for github.  Will set it to update')
                self.update_batch_file_message()
            subprocess.Popen('git_update.bat',
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT,
                             shell=True)
        else:
            self.write_to_log('{} was unsuccessfully moved to {}'.format(seen_it_folder, old_folder))

    def play_video(self, listbox, hourLable=False, filtered_listbox_widget='i', list_of_folders_widget='j'):
        video = self.get_single_selection(listbox)
        pathe, file = os.path.split(video)
        dur = self.get_value_at_cell_without_row(self.filtereddataframe, file, pathe, 'Duration')
        self.write_to_log('play_video dur done')
        #videos must be a file "C:\path\name.extension"
        if os.path.exists(video) and (dur > 0):
            self.write_to_log('Playing {}'.format(video))
            self.start_file(video, hours_lable=hourLable, filtered_listbox_widget=filtered_listbox_widget,
                            list_of_folders_widget=list_of_folders_widget)
        elif os.path.exists(video) and not (dur > 0):
            self.write_to_log('{} is probably corrupted'.format(video))
            self.dataframe = self.remove_row_from_dataframe(self.dataframe, file, pathe)
            self.filtereddataframe = self.remove_row_from_dataframe(self.filtereddataframe, file, pathe)
            self.play_random_video(self.dataframe, filtered_listbox_widget=filtered_listbox_widget,
                                   list_of_folders_widget=list_of_folders_widget)
        else:
            self.write_to_log('{} does not exist'.format(video))
            self.dataframe = self.remove_row_from_dataframe(self.dataframe, file, pathe)
            self.dataframe.to_csv(self.the_csv, index=False)
            self.filtereddataframe = self.remove_row_from_dataframe(self.filtereddataframe, file, pathe)
            self.play_random_video(self.dataframe, filtered_listbox_widget=filtered_listbox_widget,
                                   list_of_folders_widget=list_of_folders_widget)

    def generate_random_integer(self, minimum, maximum):
        secretsGenerator = secrets.SystemRandom()
        return secretsGenerator.randint(minimum, maximum)
    
    def clear_everything(self, box, labels, buttonWiget, textboxes=[], other_list_boxes=[], sort_buttons=[],
                         hours_lable=1):
        self.desired_genres = []
        self.desired_pornstars = []
        self.undesired_genres = []
        self.undesired_pornstars = []
        self.desired_ethnicities = []
        self.undesired_ethnicities = []
        self.viewing_unupdated = False
        self.video_completeness = 'incomplete/complete'
        self.animated = ''
        self.filename = ''
        self.path_in_filter = ''
        self.hours = 0
        self.minutes = 0
        self.seconds = 0 #seconds
        self.duration = (self.hours * 60 *60) + (self.minutes * 60) + self.seconds
        self.comparator = '>='
        self.lower_comparator = '>='
        self.upper_comparator = '<='
        self.lower_duration = 1
        self.upper_duration = 45510
        self.range_selected = False
        self.path_in_filter = self.root_path
        self.filter_dataframe(self.dataframe,self.animated,
                                                       self.desired_pornstars, '', self.duration,
                                                       self.comparator, 's', self.desired_genres,
                                                       '', self.desired_ethnicities, '',
                                                       self.undesired_pornstars, self.undesired_genres,
                                                       self.undesired_ethnicities)
        self.update_videos_listbox(box)
        self.reset_animated_label(labels)
        for list_box in other_list_boxes:
            list_box.reset_box()
        for list_box in other_list_boxes:
            list_box.reset_box()
        for txtinput in textboxes:
            txtinput.clear()
        if sort_buttons == []:
            pass
        elif len(sort_buttons) < 3:
            pass
        elif len(sort_buttons) > 3:
            pass
        else:
            sort_buttons[0].change_color(background='#f04209')
            sort_buttons[1].change_color(background='#f04209')
            sort_buttons[2].change_color(background='#09f042')
        if self.there_are_filters():
            buttonWiget.change_color(background='#f04209')
        else:
            buttonWiget.change_color(background='#09f042')
        self.filtered_porn_hours = round((self.filtereddataframe['Duration'].sum()) / 3600, 2)
        self.total_unwatched_porn_hours = round((self.get_unwatched_porn_hours()) / 3600, 2)
        self.total_watched_porn_hours = round(self.total_porn_hours - self.total_unwatched_porn_hours, 2)
        watched_label = 'Total Porn Hours:\n{}\n\nTotal Watched:\n{}\n\nTotal Unwatched:\n{}\n\nFiltered Hours:\n{}\n\nTotal File Size:\n{}GB'.format(
                    self.total_porn_hours,
                    self.total_watched_porn_hours,
                    self.total_unwatched_porn_hours,
                    self.filtered_porn_hours,
                    self.total_file_size
                    )
        hours_lable.change_text(watched_label)

    def update_field(self, listbox, videos_listbox, heading, run_git_update=True):
        porno = self.get_single_selection(videos_listbox)
        absolute_path, file = os.path.split(porno)
        for dataframe in [self.dataframe, self.filtereddataframe]:
            index = self.get_row_index(dataframe, file, absolute_path)
            known_things = self.get_value_at_cell(index, heading, dataframe)
            stuff = []
            for index in listbox.curselection():
                new_thing = listbox.get(index)
                self.write_to_log('New Pornstar/Genre/Erhinicity is {}'.format(new_thing))
                stuff.append(new_thing)
                if not known_things.__contains__(new_thing):
                    if (known_things == '') or (known_things.lower() == 'nan'):
                        known_things = new_thing
                    else:
                        known_things = known_things + '; ' + new_thing
            known_things = known_things.replace('nan; ', '')
            known_things = known_things.replace('; nan', '')
            self.write_to_log('All known things are:\n{}'.format(known_things))
            dataframe = self.edit_dataframe(dataframe, file, absolute_path, heading, known_things)
            #check for 2 ethnicities
            if heading == 'Ethnicities':
                index = self.get_row_index(self.dataframe, file, absolute_path)
                known_eths = self.get_value_at_cell(index, heading, self.dataframe)
                known_gens = self.get_value_at_cell(index, 'Genres', self.dataframe)
                if known_eths.__contains__(';') and not (known_gens.__contains__('Interracial')):
                    for fra in [self.dataframe, self.filtereddataframe]:
                        if (known_gens == '') or (known_gens.lower() == 'nan'):
                            known_gens = 'Interracial'
                        else:
                            known_gens = known_gens + '; ' + 'Interracial'
                        dataframe = self.edit_dataframe(fra, file, absolute_path, 'Genres', known_gens)
            if heading == 'Genres' and (('Christmas' in stuff) or ("Valentine's Day" in stuff)):
                index = self.get_row_index(self.dataframe, file, absolute_path)
                known_gens = self.get_value_at_cell(index, 'Genres', self.dataframe)
                if (('Christmas' in stuff) or ("Valentine's Day" in stuff)) and not (known_gens.__contains__('Holiday Theme')):
                    for fra in [self.dataframe, self.filtereddataframe]:
                        if (known_gens == '') or (known_gens.lower() == 'nan'):
                            known_gens = 'Holiday Theme'
                        else:
                            known_gens = known_gens + '; ' + 'Holiday Theme'
                        dataframe = self.edit_dataframe(fra, file, absolute_path, 'Genres', known_gens)
                        dataframe = self.edit_dataframe(fra, file, absolute_path, 'Genres', known_gens)
            if heading == 'Genres' and (('Easter' in stuff) or ("St. Patrick's Day" in stuff)):
                index = self.get_row_index(self.dataframe, file, absolute_path)
                known_gens = self.get_value_at_cell(index, 'Genres', self.dataframe)
                if (('Easter' in stuff) or ("St. Patrick's Day" in stuff)) and not (known_gens.__contains__('Holiday Theme')):
                    for fra in [self.dataframe, self.filtereddataframe]:
                        if (known_gens == '') or (known_gens.lower() == 'nan'):
                            known_gens = 'Holiday Theme'
                        else:
                            known_gens = known_gens + '; ' + 'Holiday Theme'
                        dataframe = self.edit_dataframe(fra, file, absolute_path, 'Genres', known_gens)
                        dataframe = self.edit_dataframe(fra, file, absolute_path, 'Genres', known_gens)
            if heading == 'Genres' and (('Memorial Day' in stuff) or ("4th of July" in stuff)):
                index = self.get_row_index(self.dataframe, file, absolute_path)
                known_gens = self.get_value_at_cell(index, 'Genres', self.dataframe)
                if (('Memorial Day' in stuff) or ("4th of July" in stuff)) and not (known_gens.__contains__('Holiday Theme')):
                    for fra in [self.dataframe, self.filtereddataframe]:
                        if (known_gens == '') or (known_gens.lower() == 'nan'):
                            known_gens = 'Holiday Theme'
                        else:
                            known_gens = known_gens + '; ' + 'Holiday Theme'
                        dataframe = self.edit_dataframe(fra, file, absolute_path, 'Genres', known_gens)
                        dataframe = self.edit_dataframe(fra, file, absolute_path, 'Genres', known_gens)
            if heading == 'Genres' and (('Halloween' in stuff) or ("Thanksgiving" in stuff)):
                index = self.get_row_index(self.dataframe, file, absolute_path)
                known_gens = self.get_value_at_cell(index, 'Genres', self.dataframe)
                if (('Halloween' in stuff) or ("Thanksgiving" in stuff)) and not (known_gens.__contains__('Holiday Theme')):
                    for fra in [self.dataframe, self.filtereddataframe]:
                        if (known_gens == '') or (known_gens.lower() == 'nan'):
                            known_gens = 'Holiday Theme'
                        else:
                            known_gens = known_gens + '; ' + 'Holiday Theme'
                        dataframe = self.edit_dataframe(fra, file, absolute_path, 'Genres', known_gens)
                        dataframe = self.edit_dataframe(fra, file, absolute_path, 'Genres', known_gens)
            if heading == 'Genres' and (('New Years' in stuff) or ("Fuck this shit I'm Out" in stuff)):
                index = self.get_row_index(self.dataframe, file, absolute_path)
                known_gens = self.get_value_at_cell(index, 'Genres', self.dataframe)
                if (('New Years' in stuff) or ("Fuck this shit" in stuff)) and not (known_gens.__contains__('Holiday Theme')):
                    for fra in [self.dataframe, self.filtereddataframe]:
                        if (known_gens == '') or (known_gens.lower() == 'nan'):
                            known_gens = 'Holiday Theme'
                        else:
                            known_gens = known_gens + '; ' + 'Holiday Theme'
                        dataframe = self.edit_dataframe(fra, file, absolute_path, 'Genres', known_gens)
                        dataframe = self.edit_dataframe(fra, file, absolute_path, 'Genres', known_gens)
            if heading == 'Genres' and (('FFM' in stuff) or ('FMM' in stuff)):
                index = self.get_row_index(self.dataframe, file, absolute_path)
                known_gens = self.get_value_at_cell(index, 'Genres', self.dataframe)
                if (('FFM' in stuff) or ('FMM' in stuff)) and not (known_gens.__contains__('Threesome')):
                    for fra in [self.dataframe, self.filtereddataframe]:
                        if (known_gens == '') or (known_gens.lower() == 'nan'):
                            known_gens = 'Threesome'
                        else:
                            known_gens = known_gens + '; ' + 'Threesome'
                        dataframe = self.edit_dataframe(fra, file, absolute_path, 'Genres', known_gens)
            if heading == 'Genres' and (('TTM' in stuff) or ('TMM' in stuff)):
                index = self.get_row_index(self.dataframe, file, absolute_path)
                known_gens = self.get_value_at_cell(index, 'Genres', self.dataframe)
                if (('TTM' in stuff) or ('TMM' in stuff)) and not (known_gens.__contains__('Threesome')):
                    for fra in [self.dataframe, self.filtereddataframe]:
                        if (known_gens == '') or (known_gens.lower() == 'nan'):
                            known_gens = 'Threesome'
                        else:
                            known_gens = known_gens + '; ' + 'Threesome'
                        dataframe = self.edit_dataframe(fra, file, absolute_path, 'Genres', known_gens)
            if heading == 'Genres' and (('Bukakke' in stuff)):
                index = self.get_row_index(self.dataframe, file, absolute_path)
                known_gens = self.get_value_at_cell(index, 'Genres', self.dataframe)
                if (('Bukakke' in stuff)) and not (known_gens.__contains__('Facial')):
                    for fra in [self.dataframe, self.filtereddataframe]:
                        if (known_gens == '') or (known_gens.lower() == 'nan'):
                            known_gens = 'Facial'
                        else:
                            known_gens = known_gens + '; ' + 'Facial'
                        dataframe = self.edit_dataframe(fra, file, absolute_path, 'Genres', known_gens)
            if heading == 'Genres' and (('TTF' in stuff) or ('TFF' in stuff)):
                index = self.get_row_index(self.dataframe, file, absolute_path)
                known_gens = self.get_value_at_cell(index, 'Genres', self.dataframe)
                if (('TTF' in stuff) or ('TFF' in stuff)) and not (known_gens.__contains__('Threesome')):
                    for fra in [self.dataframe, self.filtereddataframe]:
                        if (known_gens == '') or (known_gens.lower() == 'nan'):
                            known_gens = 'Threesome; Lesbian'
                        else:
                            known_gens = known_gens + '; ' + 'Threesome'
                            if not known_gens.__contains__('Lesbian'):
                                known_gens = known_gens + '; ' + 'Lesbian'
                        dataframe = self.edit_dataframe(fra, file, absolute_path, 'Genres', known_gens)
                        dataframe = self.edit_dataframe(fra, file, absolute_path, 'Genres', known_gens)
            if heading == 'Genres' and (('Switch' in stuff) and ('Trans With Girl' in stuff)):
                index = self.get_row_index(self.dataframe, file, absolute_path)
                known_gens = self.get_value_at_cell(index, 'Genres', self.dataframe)
                if (('Trans With Girl' in stuff) and ('Switch' in stuff)) and not (known_gens.__contains__('Female Tops Trans')):
                    for fra in [self.dataframe, self.filtereddataframe]:
                        if (known_gens == '') or (known_gens.lower() == 'nan'):
                            known_gens = 'Female Tops Trans'
                        else:
                            known_gens = known_gens + '; ' + 'Female Tops Trans'
                        if not known_gens.__contains__('Toys -Strap On-'):
                            known_gens = known_gens + '; ' + 'Toys -Strap On-'
                        if not known_gens.__contains__('Anal'):
                            known_gens = known_gens + '; ' + 'Anal'
                        if not known_gens.__contains__('Lesbian'):
                            known_gens = known_gens + '; ' + 'Lesbian'
                        dataframe = self.edit_dataframe(fra, file, absolute_path, 'Genres', known_gens)
            if heading == 'Genres' and (('Toys -Strap On-' in stuff) and ('Trans With Girl' in stuff)):
                index = self.get_row_index(self.dataframe, file, absolute_path)
                known_gens = self.get_value_at_cell(index, 'Genres', self.dataframe)
                if (('Trans With Girl' in stuff) and ('Toys -Strap On-' in stuff)) and not (known_gens.__contains__('Female Tops Trans')):
                    for fra in [self.dataframe, self.filtereddataframe]:
                        if (known_gens == '') or (known_gens.lower() == 'nan'):
                            known_gens = 'Female Tops Trans'
                        else:
                            known_gens = known_gens + '; ' + 'Female Tops Trans'
                if (('Trans With Girl' in stuff) and ('Toys -Strap On-' in stuff)) and not (known_gens.__contains__('Anal')):
                    for fra in [self.dataframe, self.filtereddataframe]:
                        if (known_gens == '') or (known_gens.lower() == 'nan'):
                            known_gens = 'Anal'
                        else:
                            known_gens = known_gens + '; ' + 'Anal'
                        dataframe = self.edit_dataframe(fra, file, absolute_path, 'Genres', known_gens)
            if heading == 'Genres' and (('Female Tops Trans' in stuff)):
                index = self.get_row_index(self.dataframe, file, absolute_path)
                known_gens = self.get_value_at_cell(index, 'Genres', self.dataframe)
                if (('Female Tops Trans' in stuff)) and not ((known_gens.__contains__('Toys -Strap On-')) or (known_gens.__contains__('Anal'))):
                    for fra in [self.dataframe, self.filtereddataframe]:
                        if (known_gens == '') or (known_gens.lower() == 'nan'):
                            known_gens = 'Anal; Toys -Strap On-'
                        else:
                            if not known_gens.__contains__('Anal'):
                                known_gens = known_gens + '; ' + 'Anal'
                            if not known_gens.__contains__('Toys -Strap On-'):
                                known_gens = known_gens + '; ' + 'Toys -Strap On-'
                        dataframe = self.edit_dataframe(fra, file, absolute_path, 'Genres', known_gens)
            if heading == 'Genres' and (('Male Virgin' in stuff)):
                index = self.get_row_index(self.dataframe, file, absolute_path)
                known_gens = self.get_value_at_cell(index, 'Genres', self.dataframe)
                if (('Male Virgin' in stuff)) and not (known_gens.__contains__('Male Present')):
                    for fra in [self.dataframe, self.filtereddataframe]:
                        if (known_gens == '') or (known_gens.lower() == 'nan'):
                            known_gens = 'Male Present' + '; ' + 'Virgin'
                        else:
                            known_gens = known_gens + '; ' + 'Male Present'
                            if known_gens.startswith('Virgin'):
                                pass
                            elif not known_gens.__contains__('; Virgin'):
                                known_gens = known_gens + '; ' + 'Virgin'
                        dataframe = self.edit_dataframe(fra, file, absolute_path, 'Genres', known_gens)
            if heading == 'Genres' and (('Male Virgin' in stuff) or ('Female Virgin' in stuff)):
                self.write_to_log("heading == 'Genres' and (('Male Virgin' in stuff) or ('Female Virgin' in stuff))")
                index = self.get_row_index(self.dataframe, file, absolute_path)
                known_gens = self.get_value_at_cell(index, 'Genres', self.dataframe)
                self.write_to_log("known_gens:\n{}".format(known_gens))
                if (('Male Virgin' in stuff) or ('Female Virgin' in stuff)) and not ((known_gens.__contains__('; Virgin')) or (str(known_gens).startswith('Virgin'))):
                    for fra in [self.dataframe, self.filtereddataframe]:
                        if (known_gens == '') or (known_gens.lower() == 'nan'):
                            known_gens = 'Virgin'
                        else:
                            known_gens = known_gens + '; ' + 'Virgin'
                        dataframe = self.edit_dataframe(fra, file, absolute_path, 'Genres', known_gens)
            if heading == 'Genres' and (('Face Fuck' in stuff)):
                index = self.get_row_index(self.dataframe, file, absolute_path)
                known_gens = self.get_value_at_cell(index, 'Genres', self.dataframe)
                if (('Face Fuck' in stuff)) and not (known_gens.__contains__('Blow Job')):
                    for fra in [self.dataframe, self.filtereddataframe]:
                        if (known_gens == '') or (known_gens.lower() == 'nan'):
                            known_gens = 'Blow Job'
                        else:
                            known_gens = known_gens + '; ' + 'Blow Job'
                        dataframe = self.edit_dataframe(fra, file, absolute_path, 'Genres', known_gens)
            if heading == 'Genres' and (('Teacher' in stuff) and (('Teen' in stuff) or ('School Girl' in stuff))):
                index = self.get_row_index(self.dataframe, file, absolute_path)
                known_gens = self.get_value_at_cell(index, 'Genres', self.dataframe)
                if not (known_gens.__contains__('Age Gap')):
                    for fra in [self.dataframe, self.filtereddataframe]:
                        if (known_gens == '') or (known_gens.lower() == 'nan'):
                            known_gens = 'Age Gap'
                        else:
                            known_gens = known_gens + '; ' + 'Age Gap'
                        dataframe = self.edit_dataframe(fra, file, absolute_path, 'Genres', known_gens)
            if (heading == 'Genres') and (('TMF' in stuff) or ('TFF' in stuff)):
                index = self.get_row_index(self.dataframe, file, absolute_path)
                known_gens = self.get_value_at_cell(index, 'Genres', self.dataframe)
                if (('TMF' in stuff) or ('TFF' in stuff)) and not (known_gens.__contains__('Threesome')):
                    for fra in [self.dataframe, self.filtereddataframe]:
                        if (known_gens == '') or (known_gens.lower() == 'nan'):
                            known_gens = 'Threesome'
                        else:
                            known_gens = known_gens + '; ' + 'Threesome'
                        dataframe = self.edit_dataframe(fra, file, absolute_path, 'Genres', known_gens)
            if heading == 'Genres' and (('Teacher -Male-' in stuff) or ('TTM' in stuff)):
                rel_gen = 'Male Present'
                index = self.get_row_index(self.dataframe, file, absolute_path)
                known_gens = self.get_value_at_cell(index, 'Genres', self.dataframe)
                if (('Teacher -Male-' in stuff) or ('TTM' in stuff)) and not (known_gens.__contains__(rel_gen)):
                    for fra in [self.dataframe, self.filtereddataframe]:
                        if (known_gens == '') or (known_gens.lower() == 'nan'):
                            known_gens = rel_gen
                        else:
                            known_gens = known_gens + '; ' + rel_gen
                        dataframe = self.edit_dataframe(fra, file, absolute_path, 'Genres', known_gens)
            if heading == 'Genres' and (('TMM' in stuff) or ('TFM' in stuff)):
                rel_gen = 'Male Present'
                index = self.get_row_index(self.dataframe, file, absolute_path)
                known_gens = self.get_value_at_cell(index, 'Genres', self.dataframe)
                if (('TMM' in stuff) or ('TFM' in stuff)) and not (known_gens.__contains__(rel_gen)):
                    for fra in [self.dataframe, self.filtereddataframe]:
                        if (known_gens == '') or (known_gens.lower() == 'nan'):
                            known_gens = rel_gen
                        else:
                            known_gens = known_gens + '; ' + rel_gen
                        dataframe = self.edit_dataframe(fra, file, absolute_path, 'Genres', known_gens)
            if heading == 'Genres' and (('Trans With Male' in stuff) or ('FMM' in stuff)):
                rel_gen = 'Male Present'
                index = self.get_row_index(self.dataframe, file, absolute_path)
                known_gens = self.get_value_at_cell(index, 'Genres', self.dataframe)
                if (('Trans With Male' in stuff) or ('FMM' in stuff)) and not (known_gens.__contains__(rel_gen)):
                    for fra in [self.dataframe, self.filtereddataframe]:
                        if (known_gens == '') or (known_gens.lower() == 'nan'):
                            known_gens = rel_gen
                        else:
                            known_gens = known_gens + '; ' + rel_gen
                        dataframe = self.edit_dataframe(fra, file, absolute_path, 'Genres', known_gens)
            if heading == 'Genres' and (('Ugly Bastard' in stuff) or ('FFM' in stuff)):
                rel_gen = 'Male Present'
                index = self.get_row_index(self.dataframe, file, absolute_path)
                known_gens = self.get_value_at_cell(index, 'Genres', self.dataframe)
                if (('Ugly Bastard' in stuff) or ('FFM' in stuff)) and not (known_gens.__contains__(rel_gen)):
                    for fra in [self.dataframe, self.filtereddataframe]:
                        if (known_gens == '') or (known_gens.lower() == 'nan'):
                            known_gens = rel_gen
                        else:
                            known_gens = known_gens + '; ' + rel_gen
                        dataframe = self.edit_dataframe(fra, file, absolute_path, 'Genres', known_gens)
            if heading == 'Genres' and (('Trans With Trans' in stuff) or ('Trans With Girl' in stuff)):
                rel_gen = 'Lesbian'
                index = self.get_row_index(self.dataframe, file, absolute_path)
                known_gens = self.get_value_at_cell(index, 'Genres', self.dataframe)
                if (('Trans With Trans' in stuff) or ('Trans With Girl' in stuff)) and not (known_gens.__contains__(rel_gen)):
                    for fra in [self.dataframe, self.filtereddataframe]:
                        if (known_gens == '') or (known_gens.lower() == 'nan'):
                            known_gens = rel_gen
                        else:
                            known_gens = known_gens + '; ' + rel_gen
                        dataframe = self.edit_dataframe(fra, file, absolute_path, 'Genres', known_gens)
            if heading == 'Genres' and (('TTF' in stuff) or ('TFF' in stuff)):
                rel_gen = 'Lesbian'
                index = self.get_row_index(self.dataframe, file, absolute_path)
                known_gens = self.get_value_at_cell(index, 'Genres', self.dataframe)
                if (('TTF' in stuff) or ('TFF' in stuff)) and not (known_gens.__contains__(rel_gen)):
                    for fra in [self.dataframe, self.filtereddataframe]:
                        if (known_gens == '') or (known_gens.lower() == 'nan'):
                            known_gens = rel_gen
                        else:
                            known_gens = known_gens + '; ' + rel_gen
                        dataframe = self.edit_dataframe(fra, file, absolute_path, 'Genres', known_gens)
            if dataframe is self.dataframe:
                self.dataframe = dataframe
            else:
                self.filtereddataframe = dataframe
        self.dataframe.replace(float('nan'), '')
        self.dataframe.replace('nan', '')
        self.dataframe.to_csv(self.the_csv, index=False)
        if run_git_update:
            #to change git msg
            porno = str(self.get_single_selection(videos_listbox))
            msg = '{} had the {} category updated with the following:  {}'.format(porno, heading, stuff)
            self.update_batch_file_message(msg)
            self.start_file('git_update.bat', False)
            self.update_batch_file_message('update')
        listbox.selection_clear(0, 'end')
    
    def update_all(self, listboxes=[], filteredlist=5, heads=[]):
        if len(listboxes) == len(heads):
            for i in range(0, len(heads)):
                self.update_field(listboxes[i], filteredlist, heads[i], False)
            #to change git msg
            porno = str(self.get_single_selection(filteredlist))
            msg = '{} had the following categories updated:  {}'.format(porno, heads)
            self.update_batch_file_message(msg)
            self.start_file('git_update.bat', False)
            self.update_batch_file_message('update')
        else:
            self.write_to_log('update_all ERROR:\nlen of listboxes = {} but len of heads = {}'.format(
                len(listboxes),
                len(heads)))

    def deupdate_field(self, listbox, videos_listbox, heading):
        porno = self.get_single_selection(videos_listbox)
        absolute_path, file = os.path.split(porno)
        for dataframe in [self.dataframe, self.filtereddataframe]:
            index = self.get_row_index(dataframe, file, absolute_path)
            known_things = self.get_value_at_cell(index, heading, dataframe)
            for index in listbox.curselection():
                thing_to_be_removed = listbox.get(index)
                if known_things.__contains__('; '+thing_to_be_removed):
                    known_things = known_things.replace('; '+thing_to_be_removed, '')
                elif known_things.__contains__(thing_to_be_removed+'; '):
                    known_things = known_things.replace(thing_to_be_removed+'; ', '')
                elif known_things.__contains__(thing_to_be_removed):
                    known_things = known_things.replace(thing_to_be_removed, '')
            known_things = known_things.replace('NAN', '')
            known_things = known_things.replace('NaN', '')
            known_things = known_things.replace('; ;', ';')
            known_things = known_things.replace(';;', ';')
            self.edit_dataframe(dataframe, file, absolute_path, heading, known_things)
        self.dataframe.replace(',nan,', '')
        self.dataframe.to_csv(self.the_csv, index=False)
        self.start_file('git_update.bat', False)
        listbox.selection_clear(0, 'end')
    
    def get_value_at_cell(self, rowindex, heading, frame):
        return frame.at[rowindex, heading]
    
    def play_random_video(self, frame, hoursLable=False, filtered_listbox_widget='i', list_of_folders_widget='j'):
        done = False
        while not done:
            #videos must be a file "C:\path\name.extension"
            if len(self.filtereddataframe) == 0:
                self.write_to_log('There is no video to play in this list')
                done = True
            else:
                self.write_to_log('There are videos to play.  The list has {} items in it'.format(
                            len(self.filtereddataframe)
                        )
                    )
                videopicked = False
                i = 0
                master_i = 0
                while (not videopicked) or (i > len(self.filtereddataframe)/5) or (master_i > len(self.filtereddataframe)/2):
                    index = self.generate_random_integer(0, len(self.filtereddataframe))
                # self.write2ANYfile(self.filtereddataframe)
                    self.write_to_log('play_random_video index is '+str(index))
                    path = 'path'
                    name = 'name'
                    master_i = master_i + 1
                    self.write_to_log('i: {}; master i: {}'.format(i, master_i))
                    try:
                        path = self.get_value_at_cell(index, 'Path', self.filtereddataframe)
                        name = self.get_value_at_cell(index, 'Filename', self.filtereddataframe)
                        self.write_to_log('self.path_in_filter: {}\npath: {}'.format(self.path_in_filter, path))
                        if master_i >= (len(self.filtereddataframe)/2)-1:
                            self.write_to_log('Aight screw it.  Im just putting on whatever but first I will avoid new hentai')
                            tries = 0
                            index = len(self.filtereddataframe) - 1
                            while (((path.__contains__('H'))) and ((path.__contains__('new')))) or tries > (len(self.filtereddataframe)/2)-2:
                                path = self.get_value_at_cell(index, 'Path', self.filtereddataframe)
                                name = self.get_value_at_cell(index, 'Filename', self.filtereddataframe)
                                index = index - 1
                                if index <= 0:
                                    index = 0
                            self.write_to_log('Aight this shit was finally picked and double checked')
                            videopicked = True
                            done = True
                        #D:\Videos\Petto\H\new
                        if self.path_in_filter.__contains__('\\H\\') and self.path_in_filter.__contains__('\\new'):
                            self.write_to_log('We want a new random hentai')
                            videopicked = True
                        elif self.path_in_filter.__contains__('/H/') and self.path_in_filter.__contains__('/new'):
                            self.write_to_log('We want a new random hentai')
                            videopicked = True
                        elif path.__contains__('\\H\\') and path.__contains__('\\new'):
                            hentai = os.path.join(path, name)
                            self.write_to_log('We dont want want a new random hentai but {} was picked'.format(
                                hentai
                            ))
                            i = i - 1
                        elif path.__contains__('/H/') and path.__contains__('/new'):
                            hentai = os.path.join(path, name)
                            self.write_to_log('We dont want want a new random hentai but {} was picked'.format(
                                hentai
                            ))
                            i = i - 1
                        elif ('Hentai' in self.desired_genres) or (self.path_in_filter.__contains__('\\H\\') and self.path_in_filter.__contains__('\\old')):
                            self.write_to_log('We want an old random hentai')
                            videopicked = True
                        elif ('Hentai' in self.desired_genres) or self.path_in_filter.__contains__('/H/') and self.path_in_filter.__contains__('/old'):
                            self.write_to_log('We want an old random hentai')
                            videopicked = True
                        elif path.__contains__('\\H\\') and path.__contains__('\\old'):
                            hentai = os.path.join(path, name)
                            self.write_to_log('We dont want want an old random hentai but {} was picked'.format(
                                hentai
                            ))
                            i = i - 1
                        elif path.__contains__('/H/') and path.__contains__('/old'):
                            hentai = os.path.join(path, name)
                            self.write_to_log('We dont want want an old random hentai but {} was picked'.format(
                                hentai
                            ))
                            i = i - 1
                        elif ('JAV' in self.desired_genres) or (self.path_in_filter.__contains__('\\ASylum FA Nihon SM Bois\\') and self.path_in_filter.__contains__('\\Nihon')):
                            self.write_to_log('We want a new random JAV')
                            videopicked = True
                        elif ('JAV' in self.desired_genres) or self.path_in_filter.__contains__('/ASylum FA Nihon SM Bois/') and self.path_in_filter.__contains__('/Nihon'):
                            self.write_to_log('We want a new random JAV')
                            videopicked = True
                        elif path.__contains__('\\ASylum FA Nihon SM Bois\\') and path.__contains__('\\Nihon'):
                            hentai = os.path.join(path, name)
                            self.write_to_log('We dont want want a new random JAV but {} was picked'.format(
                                hentai
                            ))
                            i = i - 1
                        elif path.__contains__('/ASylum FA Nihon SM Bois/') and path.__contains__('/Nihon'):
                            hentai = os.path.join(path, name)
                            self.write_to_log('We dont want want a new random JAV but {} was picked'.format(
                                hentai
                            ))
                            i = i - 1
                        else:
                            if (name == 'name') or (path == 'path'):
                                i = i + 1
                            else:
                                videopicked = True
                    except Exception as error:
                        self.write_to_log('play_random_video index error:\n'+str(error))
                        i = i + 1
                if str(path).lower().__contains__('\\h\\new'):
                    name = self.get_lowest_episode_of_new_hentai(path, name)
                video = os.path.join(path, name)
                self.write_to_log('play_random_video video is '+str(video))
                if os.path.exists(video):
                    self.start_file(video, hours_lable=hoursLable,
                                    filtered_listbox_widget=filtered_listbox_widget,
                                   list_of_folders_widget=list_of_folders_widget)
                    done = True
                else:
                    self.write_to_log('That video does not exist.  Will play a different random video')
                    existence = os.path.exists(video)
                    self.dataframe = self.remove_row_from_dataframe(self.dataframe, name, path)
                    self.dataframe.to_csv(self.the_csv, index=False)
                    self.filtereddataframe = self.remove_row_from_dataframe(self.filtereddataframe, name, path)
                    while not existence:
                        list_of_vidz = self.get_all_videos_from_root(self.root_path)
                        index = self.generate_random_integer(0, len(list_of_vidz))
                        video = list_of_vidz[index]
                        existence = os.path.exists(video)
                    self.start_file(video, hours_lable=hoursLable,
                                    filtered_listbox_widget=filtered_listbox_widget,
                                    list_of_folders_widget=list_of_folders_widget)
                    done = True

    def get_lowest_episode_of_new_hentai(self, path, name):
        self.write_to_log(name)
        potential_hentai_minus_crap = self.remove_crap(name)
        self.write_to_log(potential_hentai_minus_crap)
        episode_number = int(potential_hentai_minus_crap[len(potential_hentai_minus_crap)-1])
        list_of_hentai = os.listdir(path)
        earlier_index = list_of_hentai.index(name)
        i = 1
        found = 0
        potential_hentai = name
        while found < 1:
            potential_earlier_episode_number = episode_number - 1
            earlier_index = earlier_index - 1
            lower_index_filename = list_of_hentai[earlier_index]
            self.write_to_log('lower index --> ' + str(lower_index_filename))
            lower_index_filename_minus_crap = self.remove_crap(lower_index_filename)
            if self.remove_crap(self.remove_numbers(self.remove_crap(lower_index_filename))) == self.remove_crap(self.remove_numbers(self.remove_crap(potential_hentai))):
                episode_number = episode_number - 1
                potential_hentai = list_of_hentai[earlier_index]
                i = i + 1
            else: #they are different series and therefor this is the episode to watch
                found = 2
        self.write_to_log('{}, {}'.format(name, potential_hentai))
        return potential_hentai

    def remove_crap(self, name_of_file):
        name_of_file = name_of_file.replace('-1080p-v1x', '')
        name_of_file = name_of_file.replace('-1080p-v2x', '')
        name_of_file = name_of_file.replace('-720p-v1x', '')
        name_of_file = name_of_file.replace('-720p-v2x', '')
        name_of_file = name_of_file.replace('1080p-v1x', '')
        name_of_file = name_of_file.replace('1080p-v2x', '')
        name_of_file = name_of_file.replace('720p-v1x', '')
        name_of_file = name_of_file.replace('720p-v2x', '')
        name_of_file = name_of_file.replace('-v1x', '')
        name_of_file = name_of_file.replace('-v2x', '')
        name_of_file = name_of_file.replace('v1x', '')
        name_of_file = name_of_file.replace('v2x', '')
        name_of_file = name_of_file.replace('-1080p', '')
        name_of_file = name_of_file.replace('1080p', '')
        name_of_file = name_of_file.replace('-720p', '')
        name_of_file = name_of_file.replace('720p', '')
        name_of_file = name_of_file.replace('-1080', '')
        name_of_file = name_of_file.replace('1080', '')
        name_of_file = name_of_file.replace('-720', '')
        name_of_file = name_of_file.replace('720', '')
        name_of_file = name_of_file.replace('.mp4', '')
        name_of_file = name_of_file.replace('.MP4', '')
        name_of_file = name_of_file.replace('.MPEG', '')
        name_of_file = name_of_file.replace('.mpeg', '')
        name_of_file = name_of_file.replace('.AVI', '')
        name_of_file = name_of_file.replace('.avi', '')
        name_of_file = name_of_file.replace('vx', '')
        name_of_file = name_of_file.replace('-v3x', '')
        name_of_file = name_of_file.replace('-h1x', '')
        return name_of_file

    def remove_numbers(self, name_of_the_file):
        name_of_the_file = name_of_the_file.replace('0', '')
        name_of_the_file = name_of_the_file.replace('1', '')
        name_of_the_file = name_of_the_file.replace('2', '')
        name_of_the_file = name_of_the_file.replace('3', '')
        name_of_the_file = name_of_the_file.replace('4', '')
        name_of_the_file = name_of_the_file.replace('6', '')
        name_of_the_file = name_of_the_file.replace('5', '')
        name_of_the_file = name_of_the_file.replace('7', '')
        name_of_the_file = name_of_the_file.replace('8', '')
        name_of_the_file = name_of_the_file.replace('9', '')
        return name_of_the_file
    
    def play_random_video_for_real(self, frame, hoursLable=False,
                                   filtered_listbox_widget='i', list_of_folders_widget='j'):
        #videos must be a file "C:\path\name.extension"
        index = self.generate_random_integer(0, len(self.dataframe))
        self.write_to_log(self.dataframe)
        path = self.get_value_at_cell(index, 'Path', self.dataframe)
        name = self.get_value_at_cell(index, 'Filename', self.dataframe)
        if str(path).lower().__contains__('\\h\\new'):
            name = self.get_lowest_episode_of_new_hentai(path, name)
        video = os.path.join(path, name)
        self.write_to_log(video)
        if os.path.exists(video):
            self.start_file(video, hours_lable=hoursLable, filtered_listbox_widget=filtered_listbox_widget,
                                   list_of_folders_widget=list_of_folders_widget)
        else:
            self.write_to_log('That video does not exist.  Will play a different random video')
            list_of_vidz = self.get_all_videos_from_root(self.root_path)
            index = self.generate_random_integer(0, len(list_of_vidz))
            path = self.get_value_at_cell(index, 'Path', self.filtereddataframe)
            name = self.get_value_at_cell(index, 'Filename', self.filtereddataframe)
            video = os.path.join(path, name)
            self.start_file(video, hours_lable=hoursLable,
                            filtered_listbox_widget=filtered_listbox_widget,
                            list_of_folders_widget=list_of_folders_widget)
    
    def set_desire(self, selection, buttonwidghet='unused'):
        if selection in self.desired_or_undesired_options:
            self.desired_or_undesired = selection
            self.write_to_log('You are set to {}'.format(selection))
        else:
            self.write_to_log('{} is not allowed'.format(selection))
            self.desired_or_undesired = self.desired_or_undesired_options[0]

    def write2ANYfile(self, string, filename, option):
        string = str(string)
        logger = open(filename, option)
        try:
            logger.write(string)
        except:
            stri = str(string)
            try:
                logger.write(stri)
            except Exception as error:
                logger.write('Sorry but I can not write the string to the file.  The error message is '.format(stri))
        logger.close()

    def add_to_list(self, a_list, list_file, addition):
        if addition not in a_list:
            self.write_to_log('{} is not in the list from {}'.format(addition, list_file))
            a_list.append(addition)
            self.write_to_log('\n'+addition+ ' '+str(list_file))
            a_list.sort(key=str.lower)
            #self.replace_text_in_textfile(list_file)
            self.replace_text_in_textfile(list_file, newstring=addition+'\n', justAddingToEnd=True)
        return a_list

    def get_item_type(self, item):
        item = str(item)
        item = item.lower()
        if item.__contains__('temp'):
            return 'exit'
        elif item.endswith('.avi'):
            return 'video'
        elif item.endswith('.mp4'):
            return 'video'
        elif item.endswith('.mpeg'):
            return 'video'
        elif item.endswith('.mov'):
            return 'video'
        elif item.endswith('.wmv'):
            return 'video'
        elif item.endswith('.mpg'):
            return 'video'
        elif item.endswith('.zip'):
            return 'exit'
        elif item.endswith('.rar'):
            return 'exit'
        elif item.endswith('.ini'):
            return 'exit'
        elif item.endswith('.txt'):
            return 'exit'
        elif item.__contains__('.'):
            return 'exit'
        else:
            return 'folder'

    def get_all_videos_from_root(self, root_path):
        filez = []
        for path, subdirs, files in os.walk(root_path):
            for name in files:
                if self.get_item_type(name) == 'video':
                    #print(os.path.join(path, name))
                    filez.append(os.path.join(path, name))
                else:
                    pass#rint(os.path.join(path, name))
        return filez

    def get_all_folders_from_root(self, root_path):
        filez = []
        for path, subdirs, files in os.walk(root_path):
            #for name in files:
            if self.get_item_type(path) == 'folder':
                #print(os.path.join(path, name))
                filez.append(os.path.join(path))
            else:
                pass#rint(os.path.join(path, name))
        return filez

    def write2file(self, string):
        string = str(string)
        filename = 'PornGUI.txt'
        if(os.path.exists(filename)):
            pass
        else:
            logger = open(filename, 'w')
            logger.write('Debug Log\n')
            logger.close()
        logger = open(filename, 'a')
        print(string)
        logger.write(string + '\n')
        logger.close()

    def get_duration(self, a_video):
        try:
            clip_info = MediaInfo.parse(a_video)
            duration = (clip_info.tracks[0].duration) / 1000
            return duration
        except Exception as Error:
            self.write2file('get_duration:\n'+str(a_video)+' is unplayable\n'+str(Error))
            #exit(0)
            return 0
        
    def add_general_genres(self, genres, path_and_file):
        genres = str(genres)
        path_and_file = str(path_and_file)
        path_and_file_test = path_and_file.replace('-', ' ')
        path_and_file = path_and_file.replace('-', ' ')
        for genre in self.list_of_genres:
            if genre.__contains__('\n'):
                self.write_to_log('l')
            if path_and_file_test.lower().__contains__(' '+genre+' '.lower()):
                if not genres.lower().__contains__(genre.lower()):
                    if genres == '':
                        genres = genre
                    else:
                        genres = genres + '; ' + genre
            elif path_and_file_test.lower().startswith(genre+' '.lower()):
                if not genres.lower().__contains__(genre.lower()):
                    if genres == '':
                        genres = genre
                    else:
                        genres = genres + '; ' + genre
            elif path_and_file_test.lower().__contains__(' '+genre+'.'.lower()):
                if not genres.lower().__contains__(genre.lower()):
                    if genres == '':
                        genres = genre
                    else:
                        genres = genres + '; ' + genre
            elif path_and_file_test.lower().startswith(genre+'.'.lower()):
                if not genres.lower().__contains__(genre.lower()):
                    if genres == '':
                        genres = genre
                    else:
                        genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('rim'.lower()):
            genre = 'Rimming'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('rimjob'.lower()):
            genre = 'Rimming'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('rim job'.lower()):
            genre = 'Rimming'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('ass eat'.lower()):
            genre = 'Rimming'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('toss'.lower()) and path_and_file_test.lower().__contains__('salad'.lower()):
            genre = 'Rimming'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('ass lick'.lower()):
            genre = 'Rimming'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('\\GOW\\'.lower()):
            genre = 'Aussie'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('Australia'.lower()):
            genre = 'Aussie'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('Angela White'.lower()):
            genre = 'Aussie'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('Max Hardcore'.lower()):
            genre = 'Ugly Bastard'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('3some'.lower()):
            genre = 'Threesome'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        elif path_and_file_test.lower().__contains__('3 some'.lower()):
            genre = 'Threesome'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        elif path_and_file_test.lower().__contains__('3 sum'.lower()):
            genre = 'Threesome'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        elif path_and_file_test.lower().__contains__('3sum'.lower()):
            genre = 'Threesome'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('Marissa Minx'.lower()):
            genre = 'Aussie'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('pussy eat'.lower()):
            genre = 'Pussy Eating'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('\\H\\'.lower()):
            genre = 'Hentai'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('rosebud'.lower()):
            genre = 'Prolapse'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('rose bud'.lower()):
            genre = 'Prolapse'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('ass'.lower()):
            genre = 'Anal'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('futabu'.lower()):
            genre = 'Futanari'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('blowjob'.lower()):
            genre = 'Blow Job'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('bj'.lower()):
            genre = 'Blow Job'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('Fellatio'.lower()):
            genre = 'Blow Job'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('Mimia Cute'.lower()):
            genre = '3d CGI'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('\\l\\'.lower()):
            genre = 'Lesbian'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('paizuri'.lower()):
            genre = 'Boob Job'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('paizzuri'.lower()):
            genre = 'Boob Job'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('titty fuck'.lower()):
            genre = 'Boob Job'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('costume'.lower()):
            genre = 'Cosplay'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('nakadashi'.lower()):
            genre = 'Creampie'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('cream pie'.lower()):
            genre = 'Creampie'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('internal cum'.lower()):
            genre = 'Creampie'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('laura teen'.lower()):
            genre = 'Creampie'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('cum shot'.lower()):
            genre = 'Facial'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('cumshot'.lower()):
            genre = 'Facial'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('megane'.lower()):
            genre = 'Glasses'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('Lacta'.lower()):
            genre = 'Lactation'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('shoujo'.lower()) and path_and_file_test.lower().__contains__('ramune'.lower()):
            genre = 'Loli'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('futabu'.lower()):
            genre = 'Loli'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('mom'.lower()):
            genre = 'MILF'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('mother'.lower()):
            genre = 'MILF'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('cat ear'.lower()):
            genre = 'Kenomimi'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('dog ear'.lower()):
            genre = 'Kenomimi'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('nurse'.lower()):
            genre = 'Nurses'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('preg'.lower()):
            genre = 'Pregnant'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('Max Hardcore'.lower()):
            genre = 'Male Present'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('Male'.lower()):
            genre = 'Male Present'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('\\FA'.lower()):
            genre = 'Male Present'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('\\ASylum'.lower()):
            genre = 'Male Present'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('\\SM'.lower()):
            genre = 'Male Present'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if (path_and_file_test.lower().__contains__('shit'.lower())):
            _path_and_file = path_and_file_test.lower()
            _path_and_file = _path_and_file.replace('-', ' ')
            _path_and_file = _path_and_file.replace('_', ' ')
            if (_path_and_file.lower().__contains__(' shit'.lower())):
                check = True
            elif (_path_and_file.lower().__contains__('shit '.lower())):
                check = True
            elif (_path_and_file.lower().__contains__(' shit.'.lower())):
                check = True
            else:
                check = False
            if check:
                genre = 'Scat'
                if not genres.lower().__contains__(genre.lower()):
                    if genres == '':
                        genres = genre
                    else:
                        genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('Seifuku'.lower()):
            genre = 'School Girl'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('school'.lower()):
            genre = 'School Girl'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('sailor suit'.lower()):
            genre = 'School Girl'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('strap on'.lower()):
            genre = 'Toys -Strap On-'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file_test.lower().__contains__('strapon'.lower()):
            genre = 'Toys -Strap On-'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('strap-on'.lower()):
            genre = 'Toys -Strap On-'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('strplzz'.lower()):
            genre = 'Toys -Strap On-'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('Dildo'.lower()):
            genre = 'Toys -Dildo-'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('Piss'.lower()):
            genre = 'Watersports'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('pee'.lower()):
            genre = 'Watersports'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('urin'.lower()):
            genre = 'Watersports'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('squirt'.lower()):
            genre = 'Watersports'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('gokkun'.lower()):
            genre = 'Bukakke'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
                if not genres.__contains__('Facial'):
                    genres = genres + '; ' + 'Facial'
        if path_and_file.lower().__contains__('dp'.lower()):
            genre = 'Double Penetration'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if (genres.__contains__('FMM')) and (not (genres.__contains__('Double Penetration'))):
            genres = genres + '; ' + 'Double Penetration'
        if path_and_file.lower().__contains__('d p'.lower()):
            genre = 'Double Penetration'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('Magical Girl'.lower()):
            genre = 'Mahou Shoujo'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('Magical-Girl'.lower()):
            genre = 'Mahou Shoujo'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('Magical_Girl'.lower()):
            genre = 'Mahou Shoujo'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('MagicalGirl'.lower()):
            genre = 'Mahou Shoujo'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('Nun'.lower()):
            genre = 'Nuns'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('Office'.lower()):
            genre = 'Office Lady'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('Cop'.lower()):
            genre = 'Police'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('Hime'.lower()):
            genre = 'Princess'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('slave'.lower()):
            genre = 'Sex Slave'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('dorei'.lower()):
            genre = 'Sex Slave'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if (genres.__contains__('Sex Slave')) and (not (genres.__contains__('BDSM or Bondage'))):
            genres = genres + '; ' + 'BDSM or Bondage'
        if path_and_file.lower().__contains__('tortured'.lower()):
            genre = 'Torture'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if (genres.__contains__('Torture')) and (not (genres.__contains__('BDSM or Bondage'))):
            genres = genres + '; ' + 'BDSM or Bondage'
        if (genres.__contains__('Elf;')) and (not (genres.__contains__('Fantasy'))):
            genres = genres + '; ' + 'Fantasy'
        if path_and_file.lower().__contains__('Vamp'.lower()):
            genre = 'Vampire'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('Vamp'.lower()):
            genre = 'Vampire'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('\\GOW\\'.lower()):
            genre = 'Amateur'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('\\Laura Teen\\'.lower()):
            genre = 'Amateur'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('\\Midwest Freaks\\'.lower()):
            genre = 'Amateur'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('\\Private Society\\'.lower()):
            genre = 'Amateur'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('\\Mimia Cute\\'.lower()):
            genre = 'Amateur'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('h\\dl\\'.lower()):
            genre = 'Amateur'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('fat'.lower()):
            genre = 'BBW'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('plus size'.lower()):
            genre = 'BBW'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('phat'.lower()):
            genre = 'BBW'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('fist'.lower()):
            genre = 'Fisting'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('Japanese AV'.lower()):
            genre = 'JAV'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('JHDV'.lower()):
            genre = 'JAV'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('Newhalf'.lower()):
            genre = 'JAV'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
            genre = 'Tranny'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('Reso '.lower()):
            genre = 'JAV'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
            genre = 'Lesbian'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('Res '.lower()):
            genre = 'JAV'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
            genre = 'Lesbian'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('Rez'.lower()):
            genre = 'JAV'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
            genre = 'Lesbian'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('\\GP\\'.lower()):
            genre = 'Tranny'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if (path_and_file.lower().__contains__('young'.lower())) and (path_and_file.lower().__contains__('old'.lower())):
            genre = 'Age Gap'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if (genres.__contains__('Teacher (Male)')) and (genres.__contains__('School')) and (not (genres.__contains__('Age Gap'))):
            genres = genres + '; ' + 'Age Gap'
        if (genres.__contains__('MILF')) and (genres.__contains__('Teen')) and (not (genres.__contains__('Age Gap'))):
            genres = genres + '; ' + 'Age Gap'
        if path_and_file.lower().__contains__('puke'.lower()):
            genre = 'Vomit'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('pukikg'.lower()):
            genre = 'Vomit'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('throw up'.lower()):
            genre = 'Vomit'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('deep throat'.lower()):
            genre = 'Blow Job'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('\\ASylum FA Nihon SM Bois\FA\\'.lower()):
            genre = 'Face Fuck'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
            genre = 'Blow Job'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('Peg'.lower()):
            genre = 'Pegging'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('Aneki My Sweet Elder Sister ep 2'.lower()):
            genre = 'Pegging'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
            genre = 'FFM'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
            genre = 'Swimsuit (Other)'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('Discipline Zero ep 2'.lower()):
            genre = 'Pegging'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
            genre = 'FFM'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('BDSM'.lower()):
            genre = 'BDSM or Bondage'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('Bondage'.lower()):
            genre = 'BDSM or Bondage'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('monsta musume'.lower()):
            genre = 'Monster Girl'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('mon musu'.lower()):
            genre = 'Monster Girl'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('monmusu'.lower()):
            genre = 'Monster Girl'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if path_and_file.lower().__contains__('furyou-ni-hamerarete-jusei-suru-kyonyuu-okaa-san-2-720p-v1x'.lower()):
            genre = 'Pegging'
            if not genres.lower().__contains__(genre.lower()):
                if genres == '':
                    genres = genre
                else:
                    genres = genres + '; ' + genre
        if (genres.__contains__('Pegging')) and (not (genres.__contains__('Toys -Strap On-'))):
            genres = genres + '; ' + 'Toys -Strap On-'
        if (genres.__contains__('Ugly Bastard')) and (not (genres.__contains__('Male Present'))):
            genres = genres + '; ' + 'Male Present'
        if (genres.__contains__('Pegging')) and (not (genres.__contains__('Anal'))):
            genres = genres + '; ' + 'Anal'
        return genres

    # def update_dataframe(self, old_frame, the_path, filename, extension, dur):
    #     if (the_path.__contains__('\\H')) and ((the_path.__contains__('\\old')) or (the_path.__contains__('\\new')) or (the_path.__contains__('\\dl')) or (the_path.__contains__('\\Mimia Cute'))):
    #         animation = 'True'
    #     else:
    #         animation = 'False'
    #     if (the_path.__contains__('\\H')) and ((the_path.__contains__('\\old')) or (the_path.__contains__('\\new')) or (the_path.__contains__('\\dl')) or (the_path.__contains__('\\Mimia Cute'))):
    #         genre = 'Hentai'
    #     else:
    #         genre = ''
    #     genre = self.add_general_genres(genre, os.path.join(the_path, filename))
    #     pornstars = '11037'
    #     filename = os.path.join(the_path, filename)
    #     if filename.lower().__contains__('Office Ms Conduct'.lower()):
    #         conduct_pornstars = self.get_list_of_contents('OfficeMsConduct.txt')
    #         conduct_pornstars.sort(key=str.lower)
    #         pornstars = '11037'
    #         for line in conduct_pornstars:
    #             star = line.replace('\n', '')
    #             if pornstars == '11037':
    #                 pornstars = pornstars + star
    #             else:
    #                 pornstars = pornstars + '; ' + star
    #     elif filename.lower().__contains__('Trans Lesbians'.lower()):
    #         conduct_pornstars = self.get_list_of_contents('Trans Lesbians.txt')
    #         conduct_pornstars.sort(key=str.lower)
    #         pornstars = '11037'
    #         for line in conduct_pornstars:
    #             star = line.replace('\n', '')
    #             if pornstars == '11037':
    #                 pornstars = pornstars + star
    #             else:
    #                 pornstars = pornstars + '; ' + star
    #     elif filename.lower().__contains__('The Gift.'.lower()):
    #         self.write_to_log('filename to update is The Gift')
    #         conduct_pornstars = self.get_list_of_contents('The Gift.txt')
    #         conduct_pornstars.sort(key=str.lower)
    #         pornstars = '11037'
    #         self.write_to_log('pornstars are {}'.format(conduct_pornstars))
    #         for line in conduct_pornstars:
    #             star = line.replace('\n', '')
    #             if pornstars == '11037':
    #                 pornstars = pornstars + star
    #             else:
    #                 pornstars = pornstars + '; ' + star
    #     elif filename.lower().__contains__('The Oral Experiment'.lower()):
    #         conduct_pornstars = self.get_list_of_contents('Oral Experiment.txt')
    #         conduct_pornstars.sort(key=str.lower)
    #         pornstars = '11037'
    #         for line in conduct_pornstars:
    #             star = line.replace('\n', '')
    #             if pornstars == '11037':
    #                 pornstars = pornstars + star
    #             else:
    #                 pornstars = pornstars + '; ' + star
    #     elif filename.lower().__contains__('Too Hot For Teacher'.lower()):
    #         conduct_pornstars = self.get_list_of_contents('Hot for Teach.txt')
    #         conduct_pornstars.sort(key=str.lower)
    #         pornstars = '11037'
    #         for line in conduct_pornstars:
    #             star = line.replace('\n', '')
    #             if pornstars == '11037':
    #                 pornstars = pornstars + star
    #             else:
    #                 pornstars = pornstars + '; ' + star
    #     else:
    #         for star in self.list_of_pornstars:
    #             star = star.replace('\n', '')
    #             pornstar = star.lower().strip()
    #             if filename.lower().__contains__(pornstar):
    #                 if pornstars == '11037':
    #                     pornstars = pornstars + star
    #                 else:
    #                     if star.__contains__(' '):
    #                         first_name = star.split(' ')[0]
    #                     else:
    #                         first_name = star
    #                     if not (pornstars.__contains__(first_name)):
    #                         pornstars = pornstars + '; ' + star
    #                     else:
    #                         #some pornstar first names are repeated
    #                         if pornstars.__contains__('11037' + first_name + '; '): #first name in list of pornstars
    #                             pornstars = pornstars.replace(first_name + '; ', star + '; ')
    #                         elif (pornstars.__contains__('11037' + first_name)) and not (pornstars.__contains__(' ')): #Only name in list of pornstars
    #                             pornstars = pornstars.replace(first_name, star)
    #                         elif pornstars.__contains__('; ' + first_name + ';'): #middle in list of pornstars
    #                             pornstars = pornstars.replace('; ' + first_name, '; ' + star)
    #                         elif pornstars.__contains__('; ' + first_name): #Last name in list of pornstars
    #                             pornstars = pornstars.replace('; ' + first_name, '; ' + star)
    #                         else:
    #                             pornstars = pornstars + '; ' + star
    #     pornstars = pornstars.replace('11037', '')
    #     the_path, filename = os.path.split(filename)
    #     update_dic = {
    #                     'Path': [the_path],
    #                     'Filename': [filename],
    #                     'Filetype': [extension],
    #                     'Animated': [animation],
    #                     'Pornstars': [pornstars],
    #                     'Ethnicities': [''],
    #                     'Genres': [genre],
    #                     'Duration': [dur]
    #                     }
    #     new_df = pd.DataFrame(update_dic)
    #     dataframe = pd.concat([old_frame, new_df], ignore_index = True)
    #     dataframe.replace(float('nan'), '')
    #     dataframe.replace(',nan,', '')
    #     self.write_to_log(os.path.join(the_path, filename))
    #     return dataframe
    
    def generic_update(self):
        for frame in [self.dataframe, self.filtereddataframe]:
            for rowindex in range(0, len(frame)):
                for head in ['Pornstars', 'Ethnicities', 'Genres', 'Ethnicities', 'Genres']:
                    filename = self.get_value_at_cell(rowindex, 'Filename', frame)
                    path = self.get_value_at_cell(rowindex, 'Path', frame)
                    full_file_name = os.path.join(path, filename)
                    thing = self.get_value_at_cell(rowindex, head, frame)
                    if head == 'Pornstars':
                        liste = self.list_of_pornstars
                    elif head == 'Ethnicities':
                        liste = self.list_of_ethnicities
                    elif head == 'Genres':
                        liste = self.list_of_genres
                    for element in liste:
                        if full_file_name.__contains__(element) and (not (thing.__contains__(element))):
                            if thing == '':
                                thing = element
                            else:
                                thing = thing + element
                        if (head == 'Ethnicities') or (head == 'Genres'):
                            linked_field = self.get_value_at_cell(rowindex, ['Genres'], frame)
                            updated_field = self.add_linked_stuff(thing, linked_field, element)
                            self.write_to_log('g'+str(linked_field)+ str(updated_field))
                            linked_field = self.get_value_at_cell(rowindex, ['Pornstars'], frame)
                            updated_field = self.add_linked_stuff(updated_field, linked_field, element)
                            self.write_to_log('p'+ str(linked_field)+ str(updated_field))
                            linked_field = self.get_value_at_cell(rowindex, ['Ethnicities'], frame)
                            updated_field = self.add_linked_stuff(updated_field, linked_field, element)
                            self.write_to_log('e'+str(linked_field)+str(updated_field))
                            self.edit_dataframe(frame, filename, path, head, updated_field)
                        # elif head == 'Genres':
                        #     linked_field = self.get_value_at_cell(rowindex, ['Genres'], frame)
                        else:
                            linked_field = 'Timothy Wing-kin Koppisch'
                        pass

    def add_linked_stuff(self, known_things, linked_things, element):
        if element == 'Double Penetration':
            if (not known_things.__contains__(element)) and linked_things.__contains__('Gangbang'):
                if known_things == '':
                    known_things = element
                else:
                    known_things = known_things + '; ' + element
        if element == 'Interracial':
            if (not known_things.__contains__(element)) and len(linked_things.split(';'))>1:
                if known_things == '':
                    known_things = element
                else:
                    known_things = known_things + '; ' + element
        if element == 'Anal':
            if (not known_things.__contains__(element)) and linked_things.__contains__('Prolapse'):
                if known_things == '':
                    known_things = element
                else:
                    known_things = known_things + '; ' + element
        if element == 'Anal':
            if (not known_things.__contains__(element)) and linked_things.__contains__('Trans '):
                if known_things == '':
                    known_things = element
                else:
                    known_things = known_things + '; ' + element
        if element == 'Anal':
            if (not known_things.__contains__(element)) and linked_things.__contains__('Tranny'):
                if known_things == '':
                    known_things = element
                else:
                    known_things = known_things + '; ' + element
        if element == 'Anal':
            if (not known_things.__contains__(element)) and linked_things.__contains__('Rimming'):
                if known_things == '':
                    known_things = element
                else:
                    known_things = known_things + '; ' + element
        if element == 'Tranny':
            if (not known_things.__contains__(element)) and linked_things.__contains__('Trans '):
                if known_things == '':
                    known_things = element
                else:
                    known_things = known_things + '; ' + element
        if element == 'Prolapse':
            if (not known_things.__contains__(element)) and linked_things.__contains__('Anal'):
                if known_things == '':
                    known_things = element
                else:
                    known_things = known_things + '; ' + element
        if element == 'Blow Job':
            if (not known_things.__contains__(element)) and linked_things.__contains__('Gangbang'):
                if not (known_things.__contains__('Lesbian') or known_things.__contains__('Yuri')):
                    if known_things == '':
                        known_things = element
                    else:
                        known_things = known_things + '; ' + element
        if element == 'Lesbian':
            if (not known_things.__contains__(element)) and linked_things.__contains__('Trans With Girl'):
                if known_things == '':
                    known_things = element
                else:
                    known_things = known_things + '; ' + element
        if element == 'Lesbian':
            if (not known_things.__contains__(element)) and linked_things.__contains__('Trans With Trans'):
                if known_things == '':
                    known_things = element
                else:
                    known_things = known_things + '; ' + element
        if element == 'Blow Job':
            if (not known_things.__contains__(element)) and linked_things.__contains__('Face Fuck'):
                if known_things == '':
                    known_things = element
                else:
                    known_things = known_things + '; ' + element
        if element == 'Face Fuck':
            if (not known_things.__contains__(element)) and linked_things.__contains__('Blow Job'):
                if known_things == '':
                    known_things = element
                else:
                    known_things = known_things + '; ' + element
        if element == 'Cosplay':
            if (not known_things.__contains__(element)) and linked_things.__contains__('Maid'):
                if known_things == '':
                    known_things = element
                else:
                    known_things = known_things + '; ' + element
        if element == 'Cosplay':
            if (not known_things.__contains__(element)) and linked_things.__contains__('Nurses'):
                if known_things == '':
                    known_things = element
                else:
                    known_things = known_things + '; ' + element
        if element == 'Rape':
            if (not known_things.__contains__(element)) and linked_things.__contains__('Reverse Rape'):
                if known_things == '':
                    known_things = element
                else:
                    known_things = known_things + '; ' + element
        if element == 'Teen':
            if (not known_things.__contains__(element)) and linked_things.__contains__('School Girl'):
                if known_things == '':
                    known_things = element
                else:
                    known_things = known_things + '; ' + element
        if element == 'Gangbang':
            if (not known_things.__contains__(element)) and linked_things.__contains__('Bukkake'):
                if known_things == '':
                    known_things = element
                else:
                    known_things = known_things + '; ' + element
        if element == 'Cosplay':
            if (not known_things.__contains__(element)) and linked_things.__contains__('Mahou Shoujo'):
                if known_things == '':
                    known_things = element
                else:
                    known_things = known_things + '; ' + element
        if element == 'Cosplay':
            if (not known_things.__contains__(element)) and linked_things.__contains__('Nuns'):
                if known_things == '':
                    known_things = element
                else:
                    known_things = known_things + '; ' + element
        if element == 'Cosplay':
            if (not known_things.__contains__(element)) and linked_things.__contains__('Office Lady'):
                if known_things == '':
                    known_things = element
                else:
                    known_things = known_things + '; ' + element
        if element == 'Cosplay':
            if (not known_things.__contains__(element)) and linked_things.__contains__('Police'):
                if known_things == '':
                    known_things = element
                else:
                    known_things = known_things + '; ' + element
        if element == 'Teen':
            if (not known_things.__contains__(element)) and linked_things.__contains__('Age Gap'):
                if known_things == '':
                    known_things = element
                else:
                    known_things = known_things + '; ' + element
        if element == 'Anal':
            if (not known_things.__contains__(element)) and linked_things.__contains__('Pegging'):
                if known_things == '':
                    known_things = element
                else:
                    known_things = known_things + '; ' + element
        if element == 'To-Strap On-':
            if (not known_things.__contains__(element)) and linked_things.__contains__('Pegging'):
                if known_things == '':
                    known_things = element
                else:
                    known_things = known_things + '; ' + element
        if element == 'Tranny':
            if (not known_things.__contains__(element)) and linked_things.__contains__('Alexa Scout'):
                if known_things == '':
                    known_things = element
                else:
                    known_things = known_things + '; ' + element
        if element == 'Male Present':
            if (not known_things.__contains__(element)) and linked_things.__contains__('TTM'):
                if known_things == '':
                    known_things = element
                else:
                    known_things = known_things + '; ' + element
        if element == 'Male Present':
            if (not known_things.__contains__(element)) and linked_things.__contains__('TMM'):
                if known_things == '':
                    known_things = element
                else:
                    known_things = known_things + '; ' + element
        if element == 'Male Present':
            if (not known_things.__contains__(element)) and linked_things.__contains__('TFM'):
                if known_things == '':
                    known_things = element
                else:
                    known_things = known_things + '; ' + element
        if element == 'Male Present':
            if (not known_things.__contains__(element)) and linked_things.__contains__('Trans With Male'):
                if known_things == '':
                    known_things = element
                else:
                    known_things = known_things + '; ' + element
        if element == 'Male Present':
            if (not known_things.__contains__(element)) and linked_things.__contains__('Teacher -Male-'):
                if known_things == '':
                    known_things = element
                else:
                    known_things = known_things + '; ' + element
        if element == 'Male Present':
            if (not known_things.__contains__(element)) and linked_things.__contains__('FMM'):
                if known_things == '':
                    known_things = element
                else:
                    known_things = known_things + '; ' + element
        if element == 'Male Present':
            if (not known_things.__contains__(element)) and linked_things.__contains__('FFM'):
                if known_things == '':
                    known_things = element
                else:
                    known_things = known_things + '; ' + element
        if element == 'Male Present':
            if (not known_things.__contains__(element)) and linked_things.__contains__('Ugly Bastard'):
                if known_things == '':
                    known_things = element
                else:
                    known_things = known_things + '; ' + element
        return known_things
    
    def get_row_index(self, frame, filename, abs_path):
        self.write_to_log(filename+ ' file')
        self.write_to_log(abs_path+ ' path')
        try:
            row_index = frame[(frame['Filename'] == filename) & (frame['Path'] == abs_path)].index[0]
        except Exception as get_row_index_ERROR:
            if ((filename == '') and (abs_path == '')) or ((filename == ' ') and (abs_path == ' ')):
                row_index = self.generate_random_integer(1, len(self.filtereddataframe))
            elif ((filename == ' ') and (abs_path == '')) or ((filename == '') and (abs_path == ' ')):
                row_index = self.generate_random_integer(1, len(self.filtereddataframe))
            else:
                self.write_to_log('Something aint right in get_row_index!  Error meassage:\n{}'.format(
                    get_row_index_ERROR
                ))
                row_index = 1
        return row_index

    def edit_dataframe(self, dataframe_to_be_updated, filename, abs_path, heading, cell_value):
        self.write_to_log('edit_dataframe inputs:\n{}, {}, {}, {}'.format(filename, abs_path, heading, cell_value))
        row_index = dataframe_to_be_updated[(dataframe_to_be_updated['Filename'] == filename) & (dataframe_to_be_updated['Path'] == abs_path)].index[0]
        self.write_to_log('edit_dataframe row_index={}'.format(row_index))
        dataframe_to_be_updated.at[row_index, heading] = cell_value
        dataframe_to_be_updated.replace(float('nan'), '')
        dataframe_to_be_updated.replace(',nan,', '')
        dataframe_to_be_updated.replace('NaN', '')
        dataframe_to_be_updated.replace('NAN', '')
        dataframe_to_be_updated.replace('; nan ;', '')
        dataframe_to_be_updated.replace(',nan ;', '')
        dataframe_to_be_updated.replace('; nan,', '')
        #self.dataframe = dataframe_to_be_updated
        return dataframe_to_be_updated
    
    def rename_file(self, textbox, listbox):
        new_name = str(textbox.get(1.0, "end-1c")).replace('\n', '').strip()
        video = self.get_single_selection(listbox)
        absolute_path, file = os.path.split(video)
        if not new_name.__contains__('.'):
            extension = file.split('.')[1]
            new_name = new_name + '.' + extension
        try:
            os.rename(video, os.path.join(absolute_path, new_name))
            self.edit_dataframe(self.dataframe, file, absolute_path, 'Filename', new_name)
            self.edit_dataframe(self.filtereddataframe, file, absolute_path, 'Filename', new_name)
            self.update_videos_listbox(listbox)
            self.dataframe.replace(float('nan'), '')
            self.dataframe.replace(',nan,', '')
            self.dataframe.to_csv(self.the_csv, index=False)
        except:
            self.write_to_log('Can not rename file {}'.format(os.rename(video,
                                                                         os.path.join(absolute_path,
                                                                                      new_name))))

    # def refresh(self, pornstar_widget, genres_widget, ethnicity_widget, filtered_widget, main_root, hourLable):
    #     self.list_of_pornstars = self.get_list_of_contents(self.porntxt)
    #     self.list_of_pornstars.sort(key=str.lower)
    #     self.list_of_genres = self.get_list_of_contents(self.genretxt)
    #     self.list_of_genres.sort(key=str.lower)
    #     self.list_of_ethnicities = self.get_list_of_contents(self.ethnicitytxt)
    #     self.list_of_ethnicities.sort(key=str.lower)
    #     self.viewing_unupdated = False
    #     self.initial_update()
    #     #self.update_csv(self.get_all_videos_from_root(self.root_path), self.the_csv)
    #     self.dataframe = pd.read_csv(self.the_csv, delimiter=',', header=0,
    #                                  skip_blank_lines=True, na_values='')
    #     self.dataframe.replace(',nan,', '')
    #     self.dataframe.replace('NaN', '')
    #     self.dataframe.replace('NAN', '')
    #     self.dataframe.replace('; nan ;', '')
    #     self.dataframe.replace(',nan ;', '')
    #     self.dataframe.replace('; nan,', '')
    #     self.dataframe.to_csv(self.the_csv, index=False)
    #     self.filtereddataframe = pd.read_csv(self.the_csv, delimiter=',', header=0,
    #                                          skip_blank_lines=True, na_values='')
    #     self.filtereddataframe.replace(',nan,', '')
    #     self.dataframe['Ethnicities'] = self.dataframe['Ethnicities'].astype(str)
    #     self.filtereddataframe['Ethnicities'] = self.filtereddataframe['Ethnicities'].astype(str)
    #     self.dataframe['Genres'] = self.dataframe['Genres'].astype(str)
    #     self.filtereddataframe['Genres'] = self.filtereddataframe['Genres'].astype(str)
    #     self.dataframe['Pornstars'] = self.dataframe['Pornstars'].astype(str)
    #     self.filtereddataframe['Pornstars'] = self.filtereddataframe['Pornstars'].astype(str)
    #     self.dataframe['Animated'] = self.dataframe['Animated'].astype(str)
    #     self.filtereddataframe['Animated'] = self.filtereddataframe['Animated'].astype(str)
    #     self.dataframe['Duration'] = self.dataframe['Duration'].astype(float)
    #     self.filtereddataframe['Duration'] = self.filtereddataframe['Duration'].astype(float)
    #     self.desired_genres = []
    #     self.desired_pornstars = []
    #     self.undesired_genres = []
    #     self.undesired_pornstars = []
    #     self.desired_ethnicities = []
    #     self.undesired_ethnicities = []
    #     self.selections = ['Pornstar', 'Ethnicity', 'Genre']
    #     self.animatedselections = ['Pornstar', 'Ethnicity', 'Genre']
    #     self.selection = self.selections[self.generate_random_integer(0, len(self.selections)-1)]#'Pornstar'
    #     self.desired_or_undesired_options = ['Desired', 'Undesired']
    #     self.desired_or_undesired = self.desired_or_undesired_options[self.generate_random_integer(0,
    #                                                                                                len(self.desired_or_undesired_options)-1)
    #                                                                                                ]#'Desired'
    #     self.hours = 0
    #     self.minutes = 0
    #     self.seconds = 0 #seconds
    #     self.duration = (self.hours * 60 *60) + (self.minutes * 60) + self.seconds
    #     self.comparator = '>='
    #     self.animated = ''
    #     self.filename = ''
    #     self.update_generic_listbox(pornstar_widget, self.list_of_pornstars)
    #     self.update_generic_listbox(genres_widget, self.list_of_genres)
    #     self.update_generic_listbox(ethnicity_widget, self.list_of_ethnicities)
    #     self.update_videos_listbox(filtered_widget)
    #     self.update_porn_hours(hourLable)

    # def delete_video(self, listbox_widget, hourLable=False):
    #     vid = self.get_single_selection(listbox_widget)
    #     if os.path.exists(vid):
    #         self.write_to_log(vid)
    #         os.remove(vid)
    #     else:
    #         self.write_to_log('{} DNE'.format(vid))
    #     absolute_path, file = os.path.split(vid)
    #     self.write_to_log(absolute_path+' , '+file)
    #     self.dataframe = self.remove_row_from_dataframe(self.dataframe, file, absolute_path)
    #     self.filtereddataframe = self.remove_row_from_dataframe(self.filtereddataframe, file, absolute_path)
    #     self.update_videos_listbox(listbox_widget)
    #     self.dataframe.replace(float('nan'), '')
    #     self.dataframe.replace(',nan,', '')
    #     self.dataframe.to_csv(self.the_csv, index=False)
    #     self.update_batch_file_message(vid+' removed')
    #     self.start_file('git_update.bat', False)
    #     if hourLable != False:
    #         self.update_porn_hours(hourLable) 

    # def update_csv(self, list_of_files, csv_file):
    #     #list_of_files must have full abolute path
    #     dataframe = pd.read_csv(csv_file, delimiter=',', header=0,
    #                                  skip_blank_lines=True, na_values='')
    #     dataframe = dataframe.drop_duplicates()
    #     list_of_files_in_dataframe = self.list_from_dataframe(dataframe, 'Filename')
    #     self.write_to_log('Updating...')
    #     for file_with_absolute_path in list_of_files:
    #         absolute_path, file = os.path.split(file_with_absolute_path)
    #         if os.path.exists(file_with_absolute_path):#checking if it exits
    #             #check if file is already in the dataframe
    #             self.write_to_log('check if file is already in the dataframe')
    #             if not (file in list_of_files_in_dataframe):
    #                 #Add to dataframe
    #                 self.write_to_log('Add to dataframe')
    #                 duration = self.get_duration(file_with_absolute_path) #in seconds
    #                 file_type = file_with_absolute_path.split('.')[1]
    #                 if duration > 0:
    #                     dataframe = self.update_dataframe(dataframe, absolute_path, file, file_type, duration)
    #             else:
    #                 #Check if path is the same
    #                 filtered_df = self.filter_dataframe(dataframe, Filename=file, Path=absolute_path)
    #                 path_filtered_list = self.list_from_dataframe(filtered_df, 'Path')
    #                 if len(path_filtered_list) == 0:
    #                     self.write_to_log('len(path_filtered_list) == 0')
    #                     less_filtered_df = self.filter_dataframe(dataframe, Filename=file)
    #                     path_filtered_list = self.list_from_dataframe(less_filtered_df, 'Path')
    #                     if len(path_filtered_list) == 1:
    #                         self.write_to_log('Here!'+ file_with_absolute_path+ '\n'+ less_filtered_df)
    #                         og_abs_path = self.get_value_at_cell(less_filtered_df.head().index[0],
    #                                                              'Path', less_filtered_df)
    #                         self.dataframe = self.edit_dataframe(self.dataframe, file, og_abs_path,
    #                                                              'Path', absolute_path)
    #                         try:
    #                             self.filtereddataframe = self.edit_dataframe(self.filtereddataframe, file,
    #                                                                          og_abs_path,
    #                                                                         'Path', absolute_path)
    #                         except:
    #                             self.filtereddataframe = self.dataframe
    #                         dataframe = self.dataframe
    #                     else:
    #                         duration = self.get_duration(file_with_absolute_path) #in seconds
    #                         file_type = file_with_absolute_path.split('.')[1]
    #                         dataframe = self.update_dataframe(dataframe, absolute_path, file, file_type, duration)
    #                         updated_filtered_df = self.filter_dataframe(dataframe, Filename=file)
    #                         for index in updated_filtered_df.head().index:
    #                             name_of_file = self.get_value_at_cell(index, 'Filename', updated_filtered_df)
    #                             path_of_file = self.get_value_at_cell(index, 'Path', updated_filtered_df)
    #                             full_file = os.path.join(path_of_file, name_of_file)
    #                             if not os.path.exists(full_file):
    #                                 #remove from dataframe
    #                                 self.write_to_log('remove from dataframe')
    #                                 self.dataframe = self.remove_row_from_dataframe(self.dataframe,
    #                                                                                 name_of_file,
    #                                                                                 path_of_file)
    #                                 self.filtereddataframe = self.remove_row_from_dataframe(self.filtereddataframe,
    #                                                                                 name_of_file,
    #                                                                                 path_of_file)
    #                 elif len(path_filtered_list) == 1:
    #                     #Check if duration is the same
    #                     self.write_to_log('Check if duration is the same')
    #                     duration = self.get_duration(file_with_absolute_path) #in seconds
    #                     duration_filtered_list = self.list_from_dataframe(filtered_df, 'Duration')
    #                     if abs(duration - duration_filtered_list[0]) < 1:
    #                         self.write_to_log('abs(duration - duration_filtered_list[0]) < 1')
    #                     else:
    #                         dataframe = self.edit_dataframe(dataframe, file, absolute_path, 'Duration', duration)
    #                 else:
    #                     #There are multiple files in the dataframe with the same name and path
    #                     #Windows does not allow that so there must be a duplicate
    #                     #Might be better to just start from scratch on this one
    #                     self.write_to_log('Might be better to just start from scratch on this one')
    #                     dataframe = self.remove_row_from_dataframe(dataframe, file, absolute_path)
    #                     duration = self.get_duration(file_with_absolute_path) #in seconds
    #                     if duration > 0:
    #                         file_type = file_with_absolute_path.split('.')[1]
    #                         dataframe = self.update_dataframe(dataframe, absolute_path, file, file_type, duration)
    #         else:
    #             self.write_to_log('os.path.exists(file_with_absolute_path) iz false')
    #             dataframe = self.remove_row_from_dataframe(dataframe, file, absolute_path)
    #     self.dataframe = dataframe
    #     self.dataframe = self.dataframe.drop_duplicates(subset=['Path', 'Filename',
    #                                                                             #'Pornstars', 'Ethnicities',
    #                                                                             'Genres', 'Duration'])
    #     self.dataframe.replace(',nan,', '')
    #     self.dataframe.replace(float('nan'), '')
    #     self.dataframe.to_csv(csv_file, index=False)
    #     self.write_to_log('Update complete')

    def remove_row_from_dataframe(self, dataframe_to_be_updated, filename, abs_path):
        row_indexes = dataframe_to_be_updated[(dataframe_to_be_updated['Filename'] == filename) & (dataframe_to_be_updated['Path'] == abs_path)].index.tolist()
        for row in row_indexes:
            dataframe_to_be_updated = dataframe_to_be_updated.drop(row)
        #self.dataframe = dataframe_to_be_updated
        return dataframe_to_be_updated

    def remove_nonexistent_files(self, frame, csv_file=''):
        paths = []
        files = []
        for row in range(0, len(frame)):
            filename = frame.at[row, 'Filename']
            file_path = frame.at[row, 'Path']
            full_name = os.path.join(file_path, filename)
            if not os.path.exists(full_name):
                paths.append(file_path)
                files.append(filename)
                self.write_to_log(full_name)
        for i in range(0, len(paths)):
            frame = self.remove_row_from_dataframe(frame, files[i], paths[i])
            self.dataframe = frame
        if not csv_file == '':
            frame.replace(float('nan'), '')
            frame.replace(',nan,', '')
            frame.to_csv(csv_file, index=False)
        self.dataframe = frame

    def update_videos_listbox(self, box, liste='default'):
        originalx = box.x
        originaly = box.y
        #Empty listbox
        box.remove_everything()
        #Update listbox
        if liste == 'default':
            box.populate_box(box.listboxess[len(box.listboxess)-1], 
                            self.list_of_filez_from_dataframe(self.filtereddataframe))
        else:
            box.populate_box(box.listboxess[len(box.listboxess)-1], 
                            liste)
        box.listboxess[len(box.listboxess)-1].place(
            x = originalx,
            anchor = 'center',
            y = originaly
        )
                
    def sort_listbox_widget(self, listbox_widget, option, labelWiget='',
                            clickedWiget='', otherButton='', toggle_sort=False):
        if not toggle_sort:
            self.sorting_revese = not self.sorting_revese
        if option == 'abc':
            self.update_videos_listbox(listbox_widget)
        elif option == 'time':
                new_list = self.list_of_filez_from_dataframe(self.filtereddataframe.sort_values(
                    'Duration', ascending=self.sorting_revese),
                    False)
                self.update_videos_listbox(listbox_widget, new_list)
        elif option == 'csv':
                new_list = self.list_of_filez_from_dataframe(
                    self.filtereddataframe.sort_index(ascending=self.sorting_revese),
                    False)
                self.update_videos_listbox(listbox_widget, new_list)
        else:
            self.write_to_log('{} is not a valid <option>'.format(str(option)))
            self.update_videos_listbox(listbox_widget)
        if not labelWiget == '':
            if self.sorting_revese:
                direction = 'Ascending'
            else:
                direction = 'Descending'
            labelWiget.change_text(direction)
        if not clickedWiget == '':
            if type(clickedWiget) == type([1, 2]):
                for cw in clickedWiget:
                    cw.change_color(background='#09f042')
            else:
                clickedWiget.change_color(background='#09f042')
        if not otherButton == '':
            if type(otherButton) == type([1, 2]):
                for ob in otherButton:
                    ob.change_color(background='#f04209')
            else:
                otherButton.change_color(background='#f04209')

    def update_generic_listbox(self, box_widget, liste):
        box = box_widget
        originalx = box.x
        originaly = box.y
        #Empty listbox
        box.remove_everything()
        #Update listbox
        box.populate_box(box.listboxess[len(box.listboxess)-1], liste)
        box.listboxess[len(box.listboxess)-1].place(
            x = originalx,
            anchor = 'center',
            y = originaly
        )

    def complete_filter(self, box, buttonWiget, hours_lable, alphachronocsv):
        #filter dataframe
        if not self.range_selected:
            if not self.viewing_unupdated:
                self.filter_dataframe(self.dataframe, self.animated, self.desired_pornstars, 
                                        self.filename, self.duration,
                                    self.comparator, 's', self.desired_genres, '', self.desired_ethnicities,
                                    self.path_in_filter, self.undesired_pornstars, self.undesired_genres,
                                    self.undesired_ethnicities)
            else:
                self.filter_dataframe(self.filtereddataframe, self.animated, self.desired_pornstars, 
                                        self.filename, self.duration,
                                    self.comparator, 's', self.desired_genres, '', self.desired_ethnicities,
                                    self.path_in_filter, self.undesired_pornstars, self.undesired_genres,
                                    self.undesired_ethnicities)
        else:
            if not self.viewing_unupdated:
                self.filter_dataframe(self.dataframe, self.animated, self.desired_pornstars, 
                                        self.filename, self.lower_duration,
                                    self.lower_comparator, 's', self.desired_genres, '', self.desired_ethnicities,
                                    self.path_in_filter, self.undesired_pornstars, self.undesired_genres,
                                    self.undesired_ethnicities)
                self.filter_dataframe(self.filtereddataframe, self.animated, self.desired_pornstars, 
                                        self.filename, self.upper_duration,
                                    self.upper_comparator, 's', self.desired_genres, '', self.desired_ethnicities,
                                    self.path_in_filter, self.undesired_pornstars, self.undesired_genres,
                                    self.undesired_ethnicities)
            else:
                self.filter_dataframe(self.filtereddataframe, self.animated, self.desired_pornstars, 
                                        self.filename, self.lower_duration,
                                    self.lower_comparator, 's', self.desired_genres, '', self.desired_ethnicities,
                                    self.path_in_filter, self.undesired_pornstars, self.undesired_genres,
                                    self.undesired_ethnicities)
                self.filter_dataframe(self.filtereddataframe, self.animated, self.desired_pornstars, 
                                        self.filename, self.upper_duration,
                                    self.upper_comparator, 's', self.desired_genres, '', self.desired_ethnicities,
                                    self.path_in_filter, self.undesired_pornstars, self.undesired_genres,
                                    self.undesired_ethnicities)
        #self.update_videos_listbox(box)
        self.sort_listbox_widget(box, 'abc', toggle_sort=True)
        if self.there_are_filters():
            buttonWiget.change_color(background='#f04209')
        else:
            buttonWiget.change_color(background='#09f042')
        self.filtered_porn_hours = round((self.filtereddataframe['Duration'].sum()) / 3600, 2)
        self.total_unwatched_porn_hours = round((self.get_unwatched_porn_hours()) / 3600, 2)
        self.total_watched_porn_hours = round(self.total_porn_hours - self.total_unwatched_porn_hours, 2)
        watched_label = 'Total Porn Hours:\n{}\n\nTotal Watched:\n{}\n\nTotal Unwatched:\n{}\n\nFiltered Hours:\n{}\n\nTotal File Size:\n{}GB'.format(
                    self.total_porn_hours,
                    self.total_watched_porn_hours,
                    self.total_unwatched_porn_hours,
                    self.filtered_porn_hours,
                    self.total_file_size
                    )
        hours_lable.change_text(watched_label)
        alphachronocsv[2].change_color(background='#f04209')
        alphachronocsv[1].change_color(background='#f04209')
        alphachronocsv[0].change_color(background='#09f042')

    def complete_filter_with_path(self, videosbox, pathsbox, buttonWiget):
        self.path_in_filter = self.get_single_selection(pathsbox)
        #filter dataframe
        if not self.range_selected:
            if not self.viewing_unupdated:
                self.filter_dataframe(self.dataframe, self.animated, self.desired_pornstars, 
                                        self.filename, self.duration,
                                    self.comparator, 's', self.desired_genres, '', self.desired_ethnicities,
                                    self.path_in_filter, self.undesired_pornstars, self.undesired_genres,
                                    self.undesired_ethnicities)
            else:
                self.filter_dataframe(self.filtereddataframe, self.animated, self.desired_pornstars, 
                                        self.filename, self.duration,
                                    self.comparator, 's', self.desired_genres, '', self.desired_ethnicities,
                                    self.path_in_filter, self.undesired_pornstars, self.undesired_genres,
                                    self.undesired_ethnicities)
        else:
            if not self.viewing_unupdated:
                self.filter_dataframe(self.dataframe, self.animated, self.desired_pornstars, 
                                        self.filename, self.upper_duration,
                                    self.upper_comparator, 's', self.desired_genres, '', self.desired_ethnicities,
                                    self.path_in_filter, self.undesired_pornstars, self.undesired_genres,
                                    self.undesired_ethnicities)
                self.filter_dataframe(self.filtereddataframe, self.animated, self.desired_pornstars, 
                                        self.filename, self.lower_duration,
                                    self.lower_comparator, 's', self.desired_genres, '', self.desired_ethnicities,
                                    self.path_in_filter, self.undesired_pornstars, self.undesired_genres,
                                    self.undesired_ethnicities)
            else:
                self.filter_dataframe(self.dataframe, self.animated, self.desired_pornstars, 
                                        self.filename, self.upper_duration,
                                    self.upper_comparator, 's', self.desired_genres, '', self.desired_ethnicities,
                                    self.path_in_filter, self.undesired_pornstars, self.undesired_genres,
                                    self.undesired_ethnicities)
                self.filter_dataframe(self.filtereddataframe, self.animated, self.desired_pornstars, 
                                        self.filename, self.lower_duration,
                                    self.lower_comparator, 's', self.desired_genres, '', self.desired_ethnicities,
                                    self.path_in_filter, self.undesired_pornstars, self.undesired_genres,
                                    self.undesired_ethnicities)
        if self.there_are_filters():
            buttonWiget.change_color(background='#f04209')
        else:
            buttonWiget.change_color(background='#09f042')
        self.update_videos_listbox(videosbox)

    def search_and_filter(self, box_widget, search_widget, list_of_folders_widget, buttonWiget, hours_lable):
        self.filename = str(search_widget.inputboxes[0].get(1.0, "end-1c"))
        self.write_to_log(self.filename+' ')
        if self.filename == '':
            self.write_to_log(True)
        else:
            self.write_to_log(self.filename+' False')
        try:
            self.path_in_filter = self.get_single_selection(list_of_folders_widget)
            if self.path_in_filter == '':
                self.path_in_filter = self.root_path
        except:
            self.path_in_filter = self.root_path
        self.write_to_log(self.path_in_filter)
        #filter dataframe
        self.write_to_log(self.viewing_unupdated)
        if not self.range_selected:
            if not self.viewing_unupdated:
                self.filter_dataframe(self.dataframe, self.animated, self.desired_pornstars, 
                                        self.filename, self.duration,
                                    self.comparator, 's', self.desired_genres, '', self.desired_ethnicities,
                                    self.path_in_filter, self.undesired_pornstars, self.undesired_genres,
                                    self.undesired_ethnicities)
            else:
                self.filter_dataframe(self.filtereddataframe, self.animated, self.desired_pornstars, 
                                        self.filename, self.duration,
                                    self.comparator, 's', self.desired_genres, '', self.desired_ethnicities,
                                    self.path_in_filter, self.undesired_pornstars, self.undesired_genres,
                                    self.undesired_ethnicities)
        else:
            if not self.viewing_unupdated:
                self.filter_dataframe(self.dataframe, self.animated, self.desired_pornstars, 
                                        self.filename, self.upper_duration,
                                    self.upper_comparator, 's', self.desired_genres, '', self.desired_ethnicities,
                                    self.path_in_filter, self.undesired_pornstars, self.undesired_genres,
                                    self.undesired_ethnicities)
                self.filter_dataframe(self.filtereddataframe, self.animated, self.desired_pornstars, 
                                        self.filename, self.lower_duration,
                                    self.lower_comparator, 's', self.desired_genres, '', self.desired_ethnicities,
                                    self.path_in_filter, self.undesired_pornstars, self.undesired_genres,
                                    self.undesired_ethnicities)
            else:
                self.filter_dataframe(self.filtereddataframe, self.animated, self.desired_pornstars, 
                                        self.filename, self.upper_duration,
                                    self.upper_comparator, 's', self.desired_genres, '', self.desired_ethnicities,
                                    self.path_in_filter, self.undesired_pornstars, self.undesired_genres,
                                    self.undesired_ethnicities)
                self.filter_dataframe(self.filtereddataframe, self.animated, self.desired_pornstars, 
                                        self.filename, self.lower_duration,
                                    self.lower_comparator, 's', self.desired_genres, '', self.desired_ethnicities,
                                    self.path_in_filter, self.undesired_pornstars, self.undesired_genres,
                                    self.undesired_ethnicities)
        self.update_videos_listbox(box_widget)
        if self.there_are_filters():
            buttonWiget.change_color(background='#f04209')
        else:
            buttonWiget.change_color(background='#09f042')
        self.filtered_porn_hours = round((self.filtereddataframe['Duration'].sum()) / 3600, 2)
        self.total_unwatched_porn_hours = round((self.get_unwatched_porn_hours()) / 3600, 2)
        self.total_watched_porn_hours = round(self.total_porn_hours - self.total_unwatched_porn_hours, 2)
        watched_label = 'Total Porn Hours:\n{}\n\nTotal Watched:\n{}\n\nTotal Unwatched:\n{}\n\nFiltered Hours:\n{}\n\nTotal File Size:\n{}GB'.format(
                    self.total_porn_hours,
                    self.total_watched_porn_hours,
                    self.total_unwatched_porn_hours,
                    self.filtered_porn_hours,
                    self.total_file_size
                    )
        hours_lable.change_text(watched_label)

    def filter_missing_info(self, box_widget, search_widget, list_of_folders_widget, buttonWiget, Buttons=False,
                            hours_lable=45510):
        self.undesired_genres = []
        self.viewing_unupdated = False
        self.write_to_log('populating undesired list')
        for genre in self.get_list_of_contents(self.genretxt):
            if genre.strip() not in self.allowed:
                self.undesired_genres.append(genre)
        self.write_to_log('filtering')
        self.search_and_filter(box_widget, search_widget, list_of_folders_widget, buttonWiget, hours_lable)
        self.write_to_log('filtered')
        self.video_completeness = 'incomplete'
        if type(Buttons) == type(['alpha', 'chrono', 'csv']):
            Buttons[0].change_color(background='#09f042')
            Buttons[1].change_color(background='#f04209')
            Buttons[2].change_color(background='#f04209')
        self.filtered_porn_hours = round((self.filtereddataframe['Duration'].sum()) / 3600, 2)
        self.total_unwatched_porn_hours = round((self.get_unwatched_porn_hours()) / 3600, 2)
        self.total_watched_porn_hours = round(self.total_porn_hours - self.total_unwatched_porn_hours, 2)
        watched_label = 'Total Porn Hours:\n{}\n\nTotal Watched:\n{}\n\nTotal Unwatched:\n{}\n\nFiltered Hours:\n{}\n\nTotal File Size:\n{}GB'.format(
                    self.total_porn_hours,
                    self.total_watched_porn_hours,
                    self.total_unwatched_porn_hours,
                    self.filtered_porn_hours,
                    self.total_file_size
                    )
        hours_lable.change_text(watched_label)

    def negate_filtered_dataframe(self, filframe, fulframe, Path=''):
        #must filter tframe to only have the folders that filframe has
        dataframe = fulframe
        Headings = dataframe.columns.tolist()
        init = dataframe.filter(items=Headings)
        if not (Path==''):
            cond = init['Path'].str.contains(Path, na=False, regex=False)
            filtered_dataframe = init.loc[cond]
        else:
            filtered_dataframe = init
        filtereddataframe = filtered_dataframe.reset_index(drop=True)
        tframe = filtereddataframe
        for row in filframe.index:
            tframe = self.remove_row_from_dataframe(tframe, filframe['Filename'][row], filframe['Path'][row])
        return tframe

    def filter_complete_info(self, box_widget, search_widget, list_of_folders_widget, buttonWiget, Buttons=False,
                             hours_lable=11037):
        self.viewing_unupdated = True
        self.filter_missing_info(box_widget,
                                search_widget,
                                list_of_folders_widget,
                                buttonWiget,
                                False,
                                hours_lable
                                )
        self.filtereddataframe = self.negate_filtered_dataframe(self.filtereddataframe, self.dataframe,
                                                                self.get_single_selection(list_of_folders_widget))
        self.update_videos_listbox(box_widget)
        self.undesired_genres = []
        self.video_completeness = 'complete'
        if self.there_are_filters():
            buttonWiget.change_color(background='#f04209')
        else:
            buttonWiget.change_color(background='#09f042')
        self.viewing_unupdated = True
        if type(Buttons) == type(['alpha', 'chrono', 'csv']):
            Buttons[0].change_color(background='#09f042')
            Buttons[1].change_color(background='#f04209')
            Buttons[2].change_color(background='#f04209')
        self.filtered_porn_hours = round((self.filtereddataframe['Duration'].sum()) / 3600, 2)
        self.total_unwatched_porn_hours = round((self.get_unwatched_porn_hours()) / 3600, 2)
        self.total_watched_porn_hours = round(self.total_porn_hours - self.total_unwatched_porn_hours, 2)
        watched_label = 'Total Porn Hours:\n{}\n\nTotal Watched:\n{}\n\nTotal Unwatched:\n{}\n\nFiltered Hours:\n{}\n\nTotal File Size:\n{}GB'.format(
                    self.total_porn_hours,
                    self.total_watched_porn_hours,
                    self.total_unwatched_porn_hours,
                    self.filtered_porn_hours,
                    self.total_file_size
                    )
        hours_lable.change_text(watched_label)

    def filter_dataframe(self, dataframe, Animated='', Pornstars='', Filename='',
                         Duration='', Duration_Comparer='>', Duration_Unit='m',
                         Genres='', extention='', Ethnicities='', Path='', undersired_pornstars='', undersired_genres='',
                         undersired_ethincities='', set_global_filter=True):
        Headings = dataframe.columns.tolist()
        init = dataframe.filter(items=Headings)

        #Windows reports duration as seconds;  Must convert given to seconds
        Duration_Unit = Duration_Unit.lower()
        if (Duration_Unit == 's') or (Duration_Unit == 'seconds') or (Duration_Unit == 'second') or (Duration_Unit == 'sec') or (Duration_Unit == 'secs'):
            Duration = Duration
        elif (Duration_Unit == 'm') or (Duration_Unit == 'minutes') or (Duration_Unit == 'minute') or (Duration_Unit == 'min') or (Duration_Unit == 'mins'):
            Duration = Duration * 60
            
        if not (Path==''):
            cond = init['Path'].str.contains(Path, na=False, regex=False)
            filtered_dataframe = init.loc[cond]
        else:
            filtered_dataframe = init
        
        if not (extention==''):
            filtered_dataframe = filtered_dataframe.loc[filtered_dataframe['Filetype'] == Animated]
        else:
            filtered_dataframe = filtered_dataframe
        
        if not (Animated==''):
            filtered_dataframe = filtered_dataframe.loc[filtered_dataframe['Animated'] == Animated]
        else:
            filtered_dataframe = filtered_dataframe

        if not (Pornstars==''): #this is a list
            for Pornstar in Pornstars:
                filtered_dataframe = filtered_dataframe[(filtered_dataframe['Pornstars'] == Pornstar) | ((filtered_dataframe['Pornstars'].str.contains('; '+Pornstar, na=False))&~(filtered_dataframe['Pornstars'].str.contains(Pornstar+' ', na=False))) | (filtered_dataframe['Pornstars'].str.contains(Pornstar+';', na=False))]
        else:
            filtered_dataframe = filtered_dataframe

        if not (undersired_pornstars==''): #this is a list
            for Pornstar in undersired_pornstars:
                filtered_dataframe = filtered_dataframe[~((filtered_dataframe['Pornstars'] == Pornstar) | ((filtered_dataframe['Pornstars'].str.contains('; '+Pornstar, na=False))&~(filtered_dataframe['Pornstars'].str.contains(Pornstar+' ', na=False))) | (filtered_dataframe['Pornstars'].str.contains(Pornstar+';', na=False)))]
        else:
            filtered_dataframe = filtered_dataframe

        if not (Genres==''): #this is a list
            # for Genre in Genres:
            #     filtered_dataframe = filtered_dataframe.loc[filtered_dataframe['Genres'].__contains__(Genre)]
            for Genre in Genres:
                filtered_dataframe = filtered_dataframe[filtered_dataframe['Genres'].str.contains(Genre, na=False)]
        else:
            filtered_dataframe = filtered_dataframe

        if not (undersired_genres==''): #this is a list
            for genre in undersired_genres:
                filtered_dataframe = filtered_dataframe[~filtered_dataframe['Genres'].str.contains(genre, na=False)]
        else:
            filtered_dataframe = filtered_dataframe

        if not (Ethnicities==''): #this is a list
            # for Ethnicity in Ethnicities:
            #     filtered_dataframe = filtered_dataframe[filtered_dataframe['Ethnicities'].str.contains(Ethnicity, na=False)]
            for Ethnicity in Ethnicities:
                self.write_to_log('{}, {}'.format(Ethnicity, type(Ethnicity)))
                filtered_dataframe = filtered_dataframe[filtered_dataframe['Ethnicities'].str.contains(Ethnicity, na=False)]
        else:
            filtered_dataframe = filtered_dataframe

        if not (undersired_ethincities==''): #this is a list
            for Ethnicity in undersired_ethincities:
                filtered_dataframe = filtered_dataframe[~filtered_dataframe['Ethnicities'].str.contains(Ethnicity, na=False)]
        else:
            filtered_dataframe = filtered_dataframe

        if not (Filename==''):
            filtered_dataframe = filtered_dataframe.loc[filtered_dataframe['Filename'].str.contains(Filename, na=False, case=False)]
        else:
            filtered_dataframe = filtered_dataframe

        if not (Duration==''):
            if Duration_Comparer == '=':
                filtered_dataframe = filtered_dataframe.loc[filtered_dataframe['Duration'] == Duration]
            elif Duration_Comparer == '<':
                filtered_dataframe = filtered_dataframe.loc[filtered_dataframe['Duration'] < Duration]
            elif Duration_Comparer == '>':
                filtered_dataframe = filtered_dataframe.loc[filtered_dataframe['Duration'] > Duration]
            elif Duration_Comparer == '<=':
                filtered_dataframe = filtered_dataframe.loc[filtered_dataframe['Duration'] <= Duration]
            elif Duration_Comparer == '>=':
                filtered_dataframe = filtered_dataframe.loc[filtered_dataframe['Duration'] >= Duration]
            else:
                filtered_dataframe = filtered_dataframe.loc[filtered_dataframe['Duration'] < 277353]
        else:
            filtered_dataframe = filtered_dataframe
        if set_global_filter:
            self.filtereddataframe = filtered_dataframe.reset_index(drop=True)
        filtereddataframe = filtered_dataframe.reset_index(drop=True)
        #self.write_to_log(str(len(filtereddataframe))+' '+str(len(self.filtereddataframe))+' '+str(len(self.dataframe)))
        return filtereddataframe

    def list_from_dataframe(self, dataframe, Heading):
        Headings = dataframe.columns.tolist()
        init = dataframe.filter(items=Headings)
        init = init[Heading]
        return init.values.tolist()

    def list_of_filez_from_dataframe(self, dataframe, sort=True):
        paths = self.list_from_dataframe(dataframe, 'Path')
        names = self.list_from_dataframe(dataframe, 'Filename')
        filez = []
        for i in range(0, len(paths)):
            filez.append(os.path.join(paths[i], names[i]))
        if sort:
            filez.sort(key=str.lower, reverse=self.sorting_revese)
        return filez

    def get_lines_between_separator(self, starting_separator, TheConfigFile='Config.txt', ending_separator=''):
        #Opens config file and returns a list of every line betwix the separators
        starting_separator = str(starting_separator)
        if ending_separator == '':
            ending_separator = starting_separator
        else:
            ending_separator = str(ending_separator)
        spot = 0
        separatorIs = [5, 9]
        logger = open(TheConfigFile, 'r')
        desiredLines = logger.readlines()
        #print(desiredLines)
        separators = [starting_separator, ending_separator]
        #print(desiredLines)
        for i in range(0, len(desiredLines)): #Finds starting and ending lines with relevant info
            if spot > 1:
                pass
            else:
                if desiredLines[i].__contains__(separators[spot]):
                    separatorIs[spot] = i
                    spot = spot + 1
                    if spot == 3:
                        i = 2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2
        i = 0
        stuff_between_separators = []
        for i in range(separatorIs[0]+1, separatorIs[1]):#Checks through each line between first and second separator
            #print(i)
            line_no_space = desiredLines[i].split('\n')[0]
            line_no_space = str(line_no_space.rstrip())
            stuff_between_separators.append(line_no_space)
        self.write_to_log(str(stuff_between_separators))
        return stuff_between_separators
    
    def create_window(self, ttl='Details'):
        root = Tk()
        root.title(ttl)
        return root
    
    def string_to_list(self, splitter, string, space='  '):
        if (string == 'nan') or (string == None) or (string == '') or (string == float('nan')):
            string = []
        elif string.__contains__(';') and (type(string) == type('string')):
            string = string.split(splitter)
        else:
            string = [string]
        ns = []
        for item in string:
            if type(item) == type('item'):
                ns.append(item.strip() + space)
        return ns
    
    def window_initialize(self, w, h, window_root):
        try:
            window_root.destroy()
        except:
            pass
        window_root = self.create_window()
        window_root.geometry('{}x{}'.format(int(3.1*w), h))
        return window_root
    
    def add_to_txt_list(self, text_input_box, option, listbox_widget):
        if option.lower() not in ['pornstar', 'genre', 'ethnicity']:
            self.write_to_log('{} is not a valid option.  Choose <Pornstar, Genre, Ethnicity>'.format(option))
            return False
        else:
            self.write_to_log('Option is {}'.format(option))
            item = text_input_box.get_text_input()
            if option.lower() == 'pornstar':
                text_doc = self.porntxt
                liste = self.list_of_pornstars
                self.list_of_pornstars = self.add_to_list(liste, text_doc, item)
                liste = self.list_of_pornstars
            elif option.lower() == 'genre':
                text_doc = self.genretxt
                liste = self.list_of_genres
                self.list_of_genres = self.add_to_list(liste, text_doc, item)
                liste = self.list_of_genres
            else:
                text_doc = self.ethnicitytxt
                liste = self.list_of_ethnicities
                self.list_of_ethnicities = self.add_to_list(liste, text_doc, item)
                liste = self.list_of_ethnicities
            self.write_to_log('Selected text file is {}'.format(text_doc))
            self.write_to_log('New list is {}'.format(str(liste)))
        self.update_generic_listbox(listbox_widget, liste)
        self.alphabatize_txt_list(text_doc)
        self.start_file('git_update.bat', False)
    
    def remove_txt_from_list(self, text_input_box, option, listbox_widget):
        if option.lower() not in ['pornstar', 'genre', 'ethnicity']:
            self.write_to_log('{} is not a valid option.  Choose <Pornstar, Genre, Ethnicity>'.format(option))
            return False
        else:
            self.write_to_log('Option is {}'.format(option))
            item = text_input_box.get_text_input()
            if option.lower() == 'pornstar':
                text_doc = self.porntxt
                liste = self.list_of_pornstars
                self.list_of_pornstars = self.remove_from_list(liste, text_doc, item)
                liste = self.list_of_pornstars
            elif option.lower() == 'genre':
                text_doc = self.genretxt
                liste = self.list_of_genres
                self.list_of_genres = self.remove_from_list(liste, text_doc, item)
                liste = self.list_of_genres
            else:
                text_doc = self.ethnicitytxt
                liste = self.list_of_ethnicities
                self.list_of_ethnicities = self.remove_from_list(liste, text_doc, item)
                liste = self.list_of_ethnicities
            self.write_to_log('Selected text file is {}'.format(text_doc))
            self.write_to_log('New list is {}'.format(str(liste)))
        self.update_generic_listbox(listbox_widget, liste)
        self.alphabatize_txt_list(text_doc)
        self.start_file('git_update.bat', False)

    def remove_from_list(self, a_list, list_file, removal):
        if removal in a_list:
            self.write_to_log('{} is in the list from {}'.format(removal, list_file))
            a_list.remove(removal)
            self.write_to_log('\n'+removal+ ' '+str(list_file))
            a_list.sort(key=str.lower)
            #self.replace_text_in_textfile(list_file)
            self.replace_text_in_textfile(list_file, oldstring=removal+'\n', newstring='', justAddingToEnd=True)
        else:
            self.write_to_log('For some reason {} is not in the list from {}'.format(removal, list_file))
        return a_list
    
    def view_filters(self, w, h):
        try:
            self.filters_root.destroy()
        except:
            pass
        self.filters_root = self.create_window('Filters')
        self.filters_root.geometry('{}x{}'.format(int(1*w), h))
        pathLable = Label_Widget(self.filters_root)
        pathLable.add_widget(self.path_in_filter)
        pathLable.place_here(1, 0, 0, -1)
        pornstarList = Listbox_widget(self.filters_root)
        pornstarList.add_widget('Multiple', self.desired_pornstars, 555, 200,
                     int(w/3), int(1.7*h/2))
        pornstarList.change_color('#000000', '#97f595')
        pornstarList.config_width()
        pornstarList.place_here(1, 15, 1, 1)
        pornstarListEx = Listbox_widget(self.filters_root)
        pornstarListEx.add_widget('Multiple', self.undesired_pornstars, 555, 200,
                     int(w/3), int(1.7*h/2))
        pornstarListEx.change_color('#000000', '#fa84a0')
        pornstarListEx.config_width()
        pornstarListEx.place_here(pornstarList.x-(pornstarList.width/2),
                                  pornstarList.y+(pornstarList.height/2),
                                  0, 1)
        pornstarx = max(pornstarListEx.x, pornstarList.x)
        pornstarw = max(pornstarList.width, pornstarListEx.width)
        gList = Listbox_widget(self.filters_root)
        gList.add_widget('Multiple', self.desired_genres, 555, 200,
                     w/3, int(1.7*h/2))
        gList.config_width()
        gList.change_color('#000000', '#97f695')
        gList.place_here(pornstarx+(pornstarw/2),
                         pornstarList.y-(pornstarList.height/2), 1, 1)
        gListEx = Listbox_widget(self.filters_root)
        gListEx.add_widget('Multiple', self.undesired_genres, 555, 200,
                     w/3, int(1.7*h/2))
        gListEx.config_width()
        gListEx.change_color('#000000', '#fb84a0')
        gListEx.place_here(gList.x-(gList.width/2),
                                  gList.y+(gList.height/2),
                                  0, 1)
        genrex = max(gListEx.x, gList.x)
        genrew = max(gList.width, gListEx.width)
        eList = Listbox_widget(self.filters_root)
        eList.add_widget('Multiple', self.desired_ethnicities, 555, 200,
                     int(w/3)-1, int(1.7*h/2))
        eList.change_color('#000000', '#97f795')
        eList.config_width()
        eList.place_here(genrex+(genrew/2),
                         pornstarList.y-(pornstarList.height/2), 1, 1)
        eListEx = Listbox_widget(self.filters_root)
        eListEx.add_widget('Multiple', self.undesired_ethnicities, 555, 200,
                     int(w/3)-1, int(1.7*h/2))
        eListEx.change_color('#000000', '#fb85a0')
        eListEx.config_width()
        eListEx.place_here(eList.x-(eList.width/2),
                                  gList.y+(gList.height/2),
                                  0, 1)
        DurationLable = Label_Widget(self.filters_root)
        if self.range_selected:
            hoUP = int(self.upper_duration / (60*60))
            leftover = self.upper_duration - (hoUP*60*60)
            mUP = int(leftover / 60)
            sUP = leftover - (mUP*60)
            hoLO = int(self.lower_duration / (60*60))
            leftover = self.lower_duration - (hoLO*60*60)
            mLO = int(leftover / 60)
            sLO = leftover - (mLO*60)
            upsec = 'Duration {} {}H {}M {}S'.format(self.upper_comparator, hoUP, mUP,sUP)
            lowsec = 'Duration {} {}H {}M {}S'.format(self.lower_comparator, hoLO, mLO, sLO)
            DurationLable.add_widget(upsec + ' and ' + lowsec)
        else:
            ho = int(self.duration / (60*60))
            leftover = self.duration - (ho*60*60)
            m = int(leftover / 60)
            s = leftover - (m*60)
            DurationLable.add_widget('Duration {} {}H {}M {}S'.format(self.comparator, ho, m, s))
        DurationLable.place_here(1, pornstarListEx.y+int(pornstarListEx.height/2), 0, 2)
        AnimationLabel = Label_Widget(self.filters_root)
        if str(self.animated) == str(True):
            report = 'Animated' 
        elif str(self.animated) == str(False):
            report = 'Not Animated' 
        elif str(self.animated) == '':
            report = 'Animated and Non Animated' 
        else:
            report = 'Something is wrong'
        AnimationLabel.add_widget(report)
        AnimationLabel.place_here((DurationLable.x+(DurationLable.width/2)),
                                  pornstarListEx.y+int(pornstarListEx.height/2),
                                  0, 2)
        StringLabel = Label_Widget(self.filters_root)
        StringLabel.add_widget('Containing the String: \"{}\"'.format(self.filename))
        StringLabel.place_here((AnimationLabel.x+(AnimationLabel.width/2)),
                                  pornstarListEx.y+int(pornstarListEx.height/2),
                                  0, 2)
        CompletenessLabel = Label_Widget(self.filters_root)
        CompletenessLabel.add_widget('Updates are {}'.format(self.video_completeness))
        CompletenessLabel.place_here((StringLabel.x+(StringLabel.width/2)),
                                  pornstarListEx.y+int(pornstarListEx.height/2),
                                  0, 2)
        max_pic_width = min((1*w) - eList.x-(eList.width/2),
                            (1*w) - eListEx.x-(eListEx.width/2))
        max_pic_height = abs(StringLabel.y-pathLable.y)-int(max(StringLabel.height, pathLable.height)/2)-2
        true_pic_size = int(min(max_pic_height, max_pic_width))-8
        picName = self.scale_resize_image('details.png', true_pic_size, true_pic_size, 'scaleddetails')
        im = Image.open(picName)
        resize_image = im.resize((true_pic_size, true_pic_size))
        img = ImageTk.PhotoImage(resize_image, master=self.filters_root)
        picLable = Label(self.filters_root, image=img)
        picLable.image = img
        picLable.place(x=w-int(picLable.winfo_reqwidth()/2),
                       y=int(h/2)+2,
                       anchor='center')
    
    def view_details(self, listbox, w, h):
        video = self.get_single_selection(listbox)
        pathe, filename = os.path.split(video)
        starz = self.get_value_at_cell_without_row(self.dataframe, filename, pathe, 'Pornstars')
        starz = self.string_to_list(';', starz)
        genrez = self.get_value_at_cell_without_row(self.dataframe, filename, pathe, 'Genres')
        genrez = self.string_to_list(';', genrez)
        eths = self.get_value_at_cell_without_row(self.dataframe, filename, pathe, 'Ethnicities')
        eths = self.string_to_list(';', eths)
        duration = self.get_value_at_cell_without_row(self.dataframe, filename, pathe, 'Duration')
        hours = int(duration / (60*60))
        minutes = int((duration-(hours*60*60)) / 60)
        seconds = duration - (hours*60*60) - (minutes*60)
        if seconds >= 30:
            minutes = minutes + 1
        if hours >= 1:
            Time_Label_Text = 'Duration ~ {}H {}M'.format(hours, minutes)
        else:
            Time_Label_Text = 'Duration ~ {}M'.format(minutes)
        try:
            self.details_root.destroy()
        except:
            pass
        self.details_root = self.create_window()
        self.details_root.geometry('{}x{}'.format(int(3.1*w), h))
        #root.title('Details')
        pornstarList = Listbox_widget(self.details_root)
        pornstarList.add_widget('Multiple', starz, 555, 200,
                     int(w/3)-1, int(1.75*h))
        pornstarList.change_color('#01080f', '#effffe')
        pornstarList.place_here(1, 15, 1, 1)
        genreList = Listbox_widget(self.details_root)
        genreList.add_widget('Multiple', genrez, 555, 200,
                     int(w/3)-1, int(1.75*h))
        genreList.change_color('#01080f', '#effffe')
        genreList.place_here(1+pornstarList.x+pornstarList.width/2, 15, 1, 1)
        ethnicityList = Listbox_widget(self.details_root)
        ethnicityList.add_widget('Multiple', eths, 555, 200,
                     int(w/3)-1, int(h*1.75))
        ethnicityList.change_color('#01080f', '#effffe')
        ethnicityList.place_here(1+genreList.x+genreList.width/2, 15, 1, 1)
        StringLabel = Label_Widget(self.details_root)
        StringLabel.add_widget(Time_Label_Text)
        StringLabel.place_here( 0,
                                h-(StringLabel.height/1),
                                0, 0)

    # def get_images_from_video(self, increment_in_seconds,
    #                         video='D:\\Videos\\Petto\\ASylum FA Nihon SM Bois\The Bois\\Pink Belle Delphine BJ.MP4',
    #                         folder='F:\\temp\\testing'):
    #     vidcap = VideoCapture(video)
    #     pathe, filename = os.path.split(video)
    #     name = filename.split('.')[0]
    #     #ext = filename.split('.')[1]
    #     #success = vidcap.grab()
    #     dur = self.get_duration(video)
    #     fps = int(vidcap.get(CAP_PROP_FPS))
    #     increment = int(increment_in_seconds * fps)
    #     if folder.endswith('\\'):
    #         folder = folder + name
    #     else:
    #         folder = folder + '\\{}'.format(name)
    #     if not os.path.exists(folder):
    #         os.makedirs(folder)
    #     for frm in range(1, int(fps*dur), increment):
    #         vidcap.set(CAP_PROP_POS_FRAMES, frm)
    #         _, image = vidcap.read()
    #         try:
    #             imwrite(os.path.join(folder, "{}%d.jpg".format(name)) % frm, image)  # save frame as JPEG file 
    #         except Exception as ew:
    #             print(ew)

    # def get_images_from_video(self, increment_in_seconds,
    #                         video='D:\\Videos\\Petto\\ASylum FA Nihon SM Bois\The Bois\\Pink Belle Delphine BJ.MP4',
    #                         folder='F:\\temp\\testing'):
    #     vidcap = VideoCapture(video)
    #     pathe, filename = os.path.split(video)
    #     name = filename.split('.')[0]
    #     #ext = filename.split('.')[1]
    #     #success = vidcap.grab()
    #     dur = self.get_duration(video)
    #     fps = int(vidcap.get(CAP_PROP_FPS))
    #     increment = int(increment_in_seconds * fps)
    #     if folder.endswith('\\'):
    #         folder = folder + name
    #     else:
    #         folder = folder + '\\{}'.format(name)
    #     if not os.path.exists(folder):
    #         os.makedirs(folder)
    #     for frm in range(1, int(fps*dur), increment):
    #         vidcap.set(CAP_PROP_POS_FRAMES, frm)
    #         _, image = vidcap.read()
    #         try:
    #             imwrite(os.path.join(folder, "{}%d.jpg".format(name)) % frm, image)  # save frame as JPEG file 
    #         except Exception as ew:
    #             print(ew)
    #         #print('Saved frame {}'.format(frm)) 
    #     # frm = int(fps*dur)-1
    #     # vidcap.set(CAP_PROP_POS_FRAMES, frm)
    #     # _, image = vidcap.read()
    #     # imwrite(os.path.join(folder, "frame%d.jpg") % frm, image)  # save frame as JPEG file  
    #     #print('Saved frame {}'.format(frm))

    def scale_resize_image(self, imagename, width=902, height=480, new_name=''):
        #print(imagename)
        image = Image.open(imagename)
        image = image.resize((width, height))
        if new_name == '':
            new_name = imagename
        elif new_name.__contains__('.'):
            pass
        else:
            extension = imagename.split('.')[1]
            new_name = new_name + '.' + extension
        if os.path.exists(new_name):
            os.remove(new_name)
        image.save(new_name)
        self.write_to_log('Image is {}x{} named{}'.format(width, height, new_name))
        return new_name
    
    def clear_out_log_file(self, the_log_file='log.txt',
                           max_file_size_bytes=197999,
                           todays_date='69Evan420S11037E'):
        the_log_file_size = os.path.getsize(the_log_file)
        if the_log_file_size > max_file_size_bytes:
            logger = open(the_log_file, 'r')
            logger_lines = logger.readlines()
            logger.close()
            logger = open(the_log_file, 'w')
            for number, line in enumerate(logger_lines):
                if abs(len(logger_lines)-(9*len(logger_lines)/10)) > max_file_size_bytes / (15000/353):
                    if number > (97*len(logger_lines)/100) or (number == 0) or (line.__contains__(todays_date)):
                        logger.write(line)
                    if number > 1:
                        if (str(logger_lines[number-1]).__contains__(todays_date)):
                            logger.write(line)
                else:
                    if number > (9*len(logger_lines)/10) or (number == 0) or (line.__contains__(todays_date)):
                        logger.write(line)
                    if number > 1:
                        if (str(logger_lines[number-1]).__contains__(todays_date)):
                            logger.write(line)
            logger.close()
            the_log_file_size_old = the_log_file_size
            the_log_file_size = os.path.getsize(the_log_file)
            print('Log was {} bytes.  Now its about {}'.format(the_log_file_size_old,
                                                                           the_log_file_size))
            if the_log_file_size > max_file_size_bytes:
                logger = open(the_log_file, 'r')
                logger_lines = logger.read()
                logger.close()
                logger_lines = logger_lines.replace('\n\n', '\n')
                logger = open(the_log_file, 'w')
                logger.write(logger_lines)
                logger.close()
                the_log_file_size_old = the_log_file_size
                the_log_file_size = os.path.getsize(the_log_file)
                print('Had to remove double spaces\nLog was {} bytes.  Now its about {}'.format(
                                                                           the_log_file_size_old,
                                                                           the_log_file_size))
                if the_log_file_size > max_file_size_bytes: #this is the last line of defense
                    #current/x=max
                    #x=current/max
                    x = the_log_file_size / max_file_size_bytes
                    logger = open(the_log_file, 'r')
                    logger_lines = logger.readlines()
                    logger.close()
                    logger = open(the_log_file, 'w')
                    starting_point = ((len(logger_lines)/x) + (len(logger_lines))) / 2
                    for number, line in enumerate(logger_lines):
                        if number > (starting_point) or (number == 0):
                            logger.write(line)
                        if number > 1:
                            if (str(logger_lines[number-1]).__contains__(todays_date)):
                                logger.write(line)
                    logger.close()
                    the_log_file_size_old = the_log_file_size
                    the_log_file_size = os.path.getsize(the_log_file)
                    print('Enacted the Final Solution\nLog was {} bytes.  Now its about {}'.format(
                                                                           the_log_file_size_old,
                                                                           the_log_file_size))
        else:
            print(the_log_file_size)
    
    def write_to_log(self, text, the_file='log.txt'):
        now = datetime.now()
        dty = now.strftime('%m/%d/%Y %H:%M:%S')
        today = now.strftime('%m/%d/%Y')
        if not os.path.exists(the_file):
            log = open(the_file, 'w')
            log.write('This is the porn log\n\n')
            log.close()
        self.clear_out_log_file(the_file, todays_date=today)
        self.write2ANYfile(dty+'\n'+str(text)+'\n\n', the_file, 'a')
        print(text)



    # def normalize_images_in_directory(self, directory, w=902, h=480):
    #     files = os.listdir(directory)
    #     for file in files:
    #         self.scale_resize_image(os.path.join(directory, file), w, h)

    # def train_model(self, directory = 'D:\\Videos\\Captures\\Genres',
    #                 nb_train_samples=200, nb_validation_samples=100,
    #                 img_width=902, img_height=480, genre='JAV',
    #                 epochs=20, batch_size=16, size_of_pool=(6, 6)):
    #     print('Training')
    #     train_data_dir = directory
    #     if train_data_dir.endswith('\\'):
    #         train_data_dir = train_data_dir + genre
    #     else:
    #         train_data_dir = train_data_dir + '\\' + genre
    #     validation_data_dir = directory
    #     if validation_data_dir.endswith('\\'):
    #         validation_data_dir = validation_data_dir + genre
    #     else:
    #         validation_data_dir = validation_data_dir + '\\' + genre
    #     folders = [validation_data_dir+'\\Valid\\Bad', validation_data_dir+'\\Valid\\Good',
    #                train_data_dir+'\\Train\\Bad', train_data_dir+'\\Train\\Good']
    #     print('normalizing images')
    #     for folder in folders:
    #         self.normalize_images_in_directory(folder, img_width, img_height)
    #     print('normalizing complete')
    #     if K.image_data_format() == 'channels_first':
    #         input_shape = (3, img_width, img_height)
    #     else:
    #         input_shape = (img_width, img_height, 3)
            
    #     model = Sequential()
    #     model.add(Conv2D(32, (2, 2), input_shape=input_shape))
    #     #model.add(Activation('relu'))
    #     model.add(LeakyReLU(alpha=0.3))
    #     #model.add(MaxPooling2D(pool_size=(2, 2)))
    #     model.add(MaxPooling2D(pool_size=size_of_pool))
    #     model.add(Conv2D(32, (2, 2)))
    #     #model.add(Activation('relu'))
    #     model.add(LeakyReLU(alpha=0.3))
    #     model.add(MaxPooling2D(pool_size=size_of_pool))
    #     model.add(Conv2D(64, (2, 2)))
    #     #model.add(Activation('relu'))
    #     model.add(LeakyReLU(alpha=0.3))
    #     model.add(MaxPooling2D(pool_size=size_of_pool))
    #     model.add(Flatten())
    #     model.add(Dense(64))
    #     model.add(LeakyReLU(alpha=0.3))
    #     #model.add(Activation('relu'))
    #     model.add(Dropout(0.5))
    #     model.add(Dense(1))
    #     model.add(Activation('sigmoid'))

    #     model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

    #     train_datagen = ImageDataGenerator(
    #     rescale=1. / 255,
    #     shear_range=0.2,
    #     zoom_range=0.2,
    #     horizontal_flip=True)
    #     test_datagen = ImageDataGenerator(rescale=1. / 255)
    #     train_generator = train_datagen.flow_from_directory(
    #     train_data_dir,
    #     target_size=(img_width, img_height),
    #     batch_size=batch_size,
    #     class_mode='binary')
    #     validation_generator = test_datagen.flow_from_directory(
    #     validation_data_dir,
    #     target_size=(img_width, img_height),
    #     batch_size=batch_size,
    #     class_mode='binary')
    #     model.fit_generator(
    #     train_generator,
    #     steps_per_epoch=nb_train_samples // batch_size,
    #     epochs=epochs,
    #     validation_data=validation_generator,
    #     validation_steps=nb_validation_samples // batch_size)
    #     print('Training')

    #     model_file_name = genre + '.h5'
    #     model.save(model_file_name)
    #     print('Model Saved')

    # def load_modle(self,
    #                #_image='F:\\temp\\testing\\Laura Teen\\frame0.jpg', 
    #                #_image='F:\\temp\\testing\\Train\\Pink Belle Delphine BJ\\frame0.jpg', 
    #                #_image='D:\\Pictures\\Saved Pictures\\bdbjTEST.png', 
    #                _image='D:\\Pictures\\Saved Pictures\\bdbjTEST2.png', 
    #                #_image='D:\\Pictures\\Saved Pictures\\bdbjTEST - Copy.png', 
    #                genre='JAV', imWi=902, imHe=480
    #                 ):
    #     h5_model = '\\models\\' + genre + '.h5'
    #     model = models.load_model(h5_model)
    #     print('Model Loaded')
    #     _image = self.scale_resize_image(_image)
    #     imaj = image.load_img(_image, target_size=(imWi, imHe))
    #     img = np.array(imaj)
    #     img = img / 255.0
    #     img = img.reshape(1,imWi,imHe,3)
    #     label = model.predict(img)
    #     print("Predicted Class (0 - Bad , 1- Good): ", label)
    #     return label[0][0]
