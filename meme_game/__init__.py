from otree.api import *
import numpy as np
from numpy import random
import random
from random import sample
from random import choices
import pandas as pd
import csv
import copy
import os #allows you to look at system directories aka access file system
import re #for the raw interpretation of regular expressions i think?
from openpyxl import load_workbook
import json

c = Currency

doc = """
Meme experiment by Vi (◕ᴗ◕✿)  
"""


class Constants(BaseConstants):
    name_in_url = 'meme_game'
    players_per_group = None
    num_rounds = 4 #here you define the number of trials
    choices = ['Post', 'See'] 
    history_template = 'meme_game/history.html'
    df = pd.read_excel("_static/global/HR.xlsx",index_col="Numbers") #does it matter that it is csv or xsls
    df2 = pd.read_excel("_static/global/LR.xlsx",index_col="Numbers")


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer): #define here ALL variables i will save at player level

    treatment          = models.StringField(blank=True)
    sReward            = models.StringField(blank=True)
    iTrialDec          = models.StringField(choices=Constants.choices) #first decision where u can choose between seeing and posting
    iDec               = models.BooleanField(blank=True) #why is this a boolean
    iDec2              = models.IntegerField(blank=True) #the meme they choose during posting
    EmotionalStatus    = models.IntegerField(choices=[1,2,3,4,5])
    iImgFeed           = models.IntegerField(blank=True)
    iImgPost1          = models.IntegerField(blank=True)
    iImgPost2          = models.IntegerField(blank=True)
    iImgPost3          = models.IntegerField(blank=True)
    iImgPost4          = models.IntegerField(blank=True)
    iImgPost5          = models.IntegerField(blank=True)
    iImgPost6          = models.IntegerField(blank=True)
    sTag1              = models.StringField(blank=True)
    sTag2              = models.StringField(blank=True)
    sTag3              = models.StringField(blank=True)
    iLikes             = models.IntegerField(blank=True)
    iDislikes          = models.IntegerField(blank=True)
    dRTDec1            = models.FloatField(blank=True)
    dRTFeed            = models.FloatField(blank=True) 
    dRTPost            = models.FloatField(blank=True) #d because double, reaction time
    dRTTags            = models.FloatField(blank=True)
    dRTFeedback        = models.FloatField(blank=True)
    dRTEmotionalStatus = models.FloatField(blank=True) 
    sTreat             = models.StringField(blank=True)
    image_path         = models.StringField(blank=True)



# FUNCTIONS

# 1. numero de rondas

def creating_session(subsession):


    for player in subsession.get_players():
        # randomize to treatments
        if player.round_number == 1:
            player.participant.treatment = random.choice(["Control", "Emotional"])
        player.treatment = player.participant.treatment
        print('set player.treatment to', player.treatment)

        if player.round_number > 1:
            prev_player = player.in_round(player.round_number - 1)

        if player.round_number > Constants.num_rounds/2:
            player.sReward = 'LR'
            # print(os.getcwd())
            memelist = os.listdir('_static/LR')[1:-1] 
            # ! if you do not put the [1:-1] it crashes because there is a 
            # ! HIDDEN file inside of the mac folder called 'DS store' that breaks it :D
            # print(memelist)
            pattern = r"meme(?P<number>\d{3})\.jpg"
            # you are telling the pattern of the files inside of the folder, in my case a string...
            # ...that says meme, then a THREE DIGIT number + .jpg, and then you group it by the number
            # m = re.match(pattern, "meme200.jpg")
            # print(m)
            # int(m.group("number"))
            numbers = [int(re.match(pattern, x).group("number")) for x in memelist] 
            # take all of the numbers from the image files and put them on a list
            vImages                 = random.sample(numbers, 6) 
            # select 6 random numbers from the list, but they do not repeat each other
            player.iImgPost1        = vImages[0]
            player.iImgPost2        = vImages[1]
            player.iImgPost3        = vImages[2]
            player.iImgPost4        = vImages[3]
            player.iImgPost5        = vImages[4]
            player.iImgPost6        = vImages[5]
            # player.iImgPost6      = random.randint(low=101,high=len(os.listdir('_static/LR')))
            
        else:
            player.sReward = 'HR' 
            # dRange                  = range(1,len(os.listdir('_static/HR')))
            # vImages                 = random.sample(range(dRange), 6)
            vImages                 = random.sample(range(1,len(os.listdir('_static/HR'))), 6)
            player.iImgPost1        = vImages[0]
            player.iImgPost2        = vImages[1]
            player.iImgPost3        = vImages[2]
            player.iImgPost4        = vImages[3]
            player.iImgPost5        = vImages[4]
            player.iImgPost6        = vImages[5]
            
        # 2.  # depending on reward we check different images,
        # then we sample six images from respective folder and...
        # 3. save image post in the variable

        print('set player.sReward to', player.sReward)

        # Setup a treatment condition (changes each round)
        player.sTreat          = random.choice(['Like', 'Dislike'])
        print('set player.sTreat to', player.sTreat)

        player.iImgFeed         = random.randint(1,len(os.listdir('_static/feed_memes')))  
        #!!!!!!! subsamples... they referred to the vectorization

        print('set player.iImgFeed to', player.iImgFeed)
        print('set player.iImgPost1 to', player.iImgPost1)

# printing statements to check how everything is going

# PAGES

class ToMemeOrNotToMeme(Page):
    form_model = 'player'
    form_fields = [
        'iTrialDec',
        'dRTDec1',
        'image_path'
    ]
    
    @staticmethod
    def vars_for_template(player): 
        if player.round_number > 1: #if you do return too early, you fuck it up! return is the last thing you should do
            prev_player = player.in_round(player.round_number - 1)
            if prev_player.iTrialDec == 'Post': 
                return {
                    'prev_player'   :  player.in_round(player.round_number - 1), #define the last round
                    'image_path'    :  "".join([prev_player.sReward,'/meme', str(prev_player.iDec2) , '.jpg']) ,
                    'dislikes'      :  prev_player.iDislikes ,
                    'likes'         :  prev_player.iLikes ,
                    'roundnumber'   :  prev_player.round_number ,
                }
            else: 
                return {
                    'prev_player'   :  player.in_round(player.round_number - 1), #define the last round
                }
            # curly brackets before return is the same as a dictionary

class Feed(Page):
    form_model = 'player' #from who are you extracting the info
    form_fields = [
        'iDec',
        'dRTFeed',
    ] #todas las variables q quieres salvar de una pagina

    @staticmethod
    def vars_for_template(player): #otree function for the html
        return {
            'Image'    :  "".join(['feed_memes/feed', str(player.iImgFeed) , '.jpg']) ,
        }

    @staticmethod
    def js_vars(player: Player):
        return {
            'sTreat'    :  player.sTreat,
        }
    
    @staticmethod
    def is_displayed(player):
        return player.iTrialDec == 'See'
        # is_displayed allows you to decide in what moment do you want to show the page

class addTags(Page):
    form_model = 'player' 
    form_fields = [
        'sTag1',
        'sTag2',
        'sTag3',
        'dRTTags',
    ] 
    
    @staticmethod
    def is_displayed(player):
        return player.iTrialDec == 'Post'

class Posting(Page):
    form_model = 'player' 
    form_fields = [
        'iImgPost1',
        'iImgPost2',
        'iImgPost3',
        'iImgPost4',
        'iImgPost5',
        'iImgPost6',
        'iDec2',
        'dRTPost',
    ] 

    @staticmethod
    def vars_for_template(player): 
        return {
            'Image'    :  "".join([player.sReward,'/meme', str(player.iImgPost1) , '.jpg']) ,
            'Image2'    :  "".join([player.sReward,'/meme', str(player.iImgPost2) , '.jpg']) ,
            'Image3'    :  "".join([player.sReward,'/meme', str(player.iImgPost3), '.jpg']) ,
            'Image4'    :  "".join([player.sReward,'/meme', str(player.iImgPost4), '.jpg']) ,
            'Image5'    :  "".join([player.sReward,'/meme', str(player.iImgPost5) , '.jpg']) ,
            'Image6'    :  "".join([player.sReward,'/meme', str(player.iImgPost6) , '.jpg']) ,   
        }
        # this might not work bc im concatating the string and not actually summing numbers
        # if i do it like this i need to get 110 memes in both HR and LR 
        # str(player.iImgPost)+str(3)  <- previous approach
    
    @staticmethod
    def js_vars(player: Player):
        return {
            'ImageID'     :  player.iImgPost1 ,
            'Image2ID'    :  player.iImgPost2 ,
            'Image3ID'    :  player.iImgPost3 ,
            'Image4ID'    :  player.iImgPost4 ,
            'Image5ID'    :  player.iImgPost5 ,
            'Image6ID'    :  player.iImgPost6 ,
    }

    @staticmethod
    def is_displayed(player):
        return player.iTrialDec == 'Post'

class HowDoYaFeel(Page):
    form_model = 'player' 
    form_fields = [
        'EmotionalStatus',
        'dRTEmotionalStatus',
    ] 

    @staticmethod
    def is_displayed(player):
        return player.iTrialDec == 'Post'

class ResultsWaitPage(WaitPage):

    @staticmethod
    def is_displayed(player):
        return player.iTrialDec == 'Post'


class Feedback(Page):
    form_model = 'player'
    form_fields = [
        'iLikes',
        'iDislikes',
        'dRTFeedback'
    ] 

    @staticmethod
    def vars_for_template(player):
        if player.sReward == 'HR': 
            return {
                'img'        : player.iDec2,
                'l'          : Constants.df.loc[player.iDec2,"Likes"],
                'd'          : Constants.df.loc[player.iDec2,"Dislikes"]
            }
        else:
            return {
                'img'        : player.iDec2,
                'l'          : Constants.df2.loc[player.iDec2,"Likes"],
                'd'          : Constants.df2.loc[player.iDec2,"Dislikes"]
            }

    @staticmethod
    def is_displayed(player):
        return player.iTrialDec == 'Post'

    @staticmethod
    def js_vars(player: Player):
        return {
            'treatment'   :  player.treatment ,
        }

#! THINGS TO  BE CODED 
# ToMemeOrNotToMeme: better layout
# QUESTIONNAIRE APP with social media and demographics question
# ResultsWaitPage

page_sequence = [ToMemeOrNotToMeme, Feed, Posting, addTags, Feedback, HowDoYaFeel]