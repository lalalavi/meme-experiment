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
from openpyxl import load_workbook
import json

c = Currency

doc = """
Meme experiment by Vi (◕ᴗ◕✿)  
"""


class Constants(BaseConstants):
    name_in_url = 'meme_game'
    players_per_group = None
    num_rounds = 10 #here you define the number of trials
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
    last               = models.IntegerField(blank=True)



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

         # 1. check round number (# Check variable names)
        if player.round_number > Constants.num_rounds/2:
            player.sReward = 'LR'
            # dRange                  = range(101, len(os.listdir('_static/LR')))
            # vImages                 = random.sample(range(dRange), 6)
            vImages                 = random.sample(range(1,len(os.listdir('_static/HR'))), 6) #need to make this actually work
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
        #!!!!!!! subsamples ?

        print('set player.iImgFeed to', player.iImgFeed)
        print('set player.iImgPost1 to', player.iImgPost1)

# def past_players=player.in_previous_rounds()

# PAGES

class ToMemeOrNotToMeme(Page):
    form_model = 'player'
    form_fields = [
        'iTrialDec',
        'dRTDec1',
    ]
    
    @staticmethod
    def vars_for_template(player): 
        if player.round_number > 1:
            return dict(prev_player = player.in_round(player.round_number - 1)) #define the last round
            if prev_player.iTrialDec == 'Post':
                return {
                    'lala'    :  "".join([player.in_round(player.round_number - 1).sReward,'/meme', str(player.in_round(player.round_number - 1).iDec2) , '.jpg']),
                    # 'prev_player' : player.in_round(player.round_number - 1)
                }

class history(Page):
    form_model = 'player' #from who are you extracting the info

    @staticmethod
    def vars_for_template(player): 
        return {
            'Image'    :  "".join([prev_player.sReward,'/meme', str(prev_player.iDec2) , '.jpg']) ,
        }
    
    # @staticmethod
    # def vars_for_template(player: Player):
    #     return dict(past_players=player.in_previous_rounds())
    
    @staticmethod
    def is_displayed(player):
        return player.round_number > 1

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
            'Image6'    :  "".join([player.sReward,'/meme', str(player.iImgPost6) , '.jpg'])    
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
        return {
            'img'        : player.iDec2,
            'l'          : Constants.df.loc[player.iDec2,"Likes"],
            'd'          : Constants.df.loc[player.iDec2,"Dislikes"]
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
