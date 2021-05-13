from otree.api import *
import numpy as np
from numpy import random
from random import sample
from random import choices
import pandas as pd
import csv
import copy
import os #allows you to look at system directories aka access file system

c = Currency

doc = """
Meme experiment by Vi (◕ᴗ◕✿)  
"""


class Constants(BaseConstants):
    name_in_url = 'meme_game'
    players_per_group = None
    num_rounds = 3 #here you define the number of trials
    choices = ['Post', 'See'] 
    


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer): #define here ALL variables i will save at player level

    iTrialDec          = models.StringField(choices=Constants.choices) #first decision where u can choose between seeing and posting
    iDec               = models.BooleanField(blank=True) #why is this a boolean
    iDec2              = models.IntegerField(blank=True) #the meme they choose during posting
    dRTDec1            = models.FloatField(blank=True)
    dRTPost            = models.FloatField(blank=True) #d because double, reaction time
    dRTTags            = models.FloatField(blank=True)
    dRTEmotionalStatus = models.FloatField(blank=True) 
    iImgFeed           = models.IntegerField(blank=True)
    iImgPost1          = models.IntegerField(blank=True)
    iImgPost2          = models.IntegerField(blank=True)
    iImgPost3          = models.IntegerField(blank=True)
    iImgPost4          = models.IntegerField(blank=True)
    iImgPost5          = models.IntegerField(blank=True)
    iImgPost6          = models.IntegerField(blank=True)
    iFeedback          = models.IntegerField(blank=True)
    sTreat             = models.StringField(blank=True)
    sReward            = models.StringField(blank=True)
    EmotionalStatus    = models.IntegerField(choices=[1,2,3,4,5])


# 
# FUNCTIONS

# 1. numero de rondas

def creating_session(subsession):

    # randomize to treatments
    for player in subsession.get_players():
        # 1. check round number (# Check variable names)
        if player.round_number > Constants.num_rounds/2:
            player.sReward = 'LR'
            player.iImgPost1        = random.randint(low=101,high=len(os.listdir('_static/LR')))
            player.iImgPost2        = random.randint(low=101,high=len(os.listdir('_static/LR')))
            player.iImgPost3        = random.randint(low=101,high=len(os.listdir('_static/LR')))
            player.iImgPost4        = random.randint(low=101,high=len(os.listdir('_static/LR')))
            player.iImgPost5        = random.randint(low=101,high=len(os.listdir('_static/LR')))
            player.iImgPost6        = random.randint(low=101,high=len(os.listdir('_static/LR')))
        else:
            player.sReward = 'HR' 
            player.iImgPost1        = random.randint(low=1,high=len(os.listdir('_static/HR')))
            player.iImgPost2        = random.randint(low=1,high=len(os.listdir('_static/HR')))
            player.iImgPost3        = random.randint(low=1,high=len(os.listdir('_static/HR')))
            player.iImgPost4        = random.randint(low=1,high=len(os.listdir('_static/HR')))
            player.iImgPost5        = random.randint(low=1,high=len(os.listdir('_static/HR')))
            player.iImgPost6        = random.randint(low=1,high=len(os.listdir('_static/HR')))

        print('set player.sReward to', player.sReward)
        # depending on reward we check different images
        # 2. sample six  images from respective folder

        # 3. save image post in the variable
        # Setup a treatment condition (changes each round)
        player.sTreat          = random.choice(['Like', 'Dislike'])
        print('set player.sTreat to', player.sTreat)


        player.iImgFeed         = random.randint(low=1,high=95)  #!!!!!!! subsamples
        
        # create 
        print('set player.iImgFeed to', player.iImgFeed)
        print('set player.iImgPost1 to', player.iImgPost1)


# PAGES

class ToMemeOrNotToMeme(Page):
    form_model = 'player'
    form_fields = [
        'iTrialDec',
        'dRTDec1'
    ]

#mypage is really the feed 
#have to add timer

class MyPage(Page):
    form_model = 'player' #from who are you extracting the info
    form_fields = [
        'iDec',
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

class addTags(Page):
    form_model = 'player' 
    form_fields = [
        'dRTTags',
    ] 

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
        #this might not work bc im concatating the string and not actually summing numbers
        # if i do it like this i need to get 110 memes in both HR and LR 
        # str(player.iImgPost)+str(3)  <- previous approach

class HowDoYaFeel(Page):
    form_model = 'player' 
    form_fields = [
        'EmotionalStatus',
        'dRTEmotionalStatus'
    ] 

class ResultsWaitPage(WaitPage):
    pass


class Feedback(Page):
    form_model = 'player'

    pass

#! THINGS TO  BE CODED 
# ToMemeOrNotToMeme: better layout
# IS DISPLAYED STUFF
# Tags: do i want to save them, or do i want to save if they did them
# Feedbackpage (!!!!)
# EmotionalStatus: solve the ()
# History display
# QUESTIONNAIRE APP with social media and demographics question
# ,  ResultsWaitPage, Results

page_sequence = [ToMemeOrNotToMeme, Posting, MyPage, HowDoYaFeel, addTags, Feedback]
