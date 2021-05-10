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
    dRT2               = models.FloatField(blank=True)  #d because double, reaction time
    iImgFeed           = models.IntegerField(blank=True)
    iImgPost1          = models.IntegerField(blank=True)
    iImgPost2          = models.IntegerField(blank=True)
    iImgPost3          = models.IntegerField(blank=True)
    iImgPost4          = models.IntegerField(blank=True)
    iImgPost5          = models.IntegerField(blank=True)
    iImgPost6          = models.IntegerField(blank=True)
    iFeedback          = models.IntegerField(blank=True)
    sTreat             = models.StringField(blank=True)
    EmotionalStatus    = models.IntegerField(choices=[1,2,3,4,5])

# EmotionalStatus    = models.IntegerField(widget=widgets.RadioSelect, choices=[ [1, 'Quitebadyooo'], [2], [3], [4], [5], [6], [7, 'excellent'] ])
# EmotionalStatus   = models.IntegerField(widget=widgets.RadioSelect, choices=[ [1, 'Strongly negative'], [2, 'Negative'], [3, 'Somewhat negative'], [4, 'Neutral'], [5, 'Somewhat positive'], [6, 'Positive'], [7, 'Strongly positive'] ])
# Should emotional status be 5 or 7
# 
# FUNCTIONS

def creating_session(subsession):
    # randomize to treatments
    for player in subsession.get_players():
        # Setup a treatment condition (changes each round)
        player.sTreat          = random.choice(['Like', 'Dislike'])
        print('set player.sTreat3 to', player.sTreat)
        player.iImgFeed         = random.randint(low=1,high=3)  #!!!!!!!!!!!!
        player.iImgPost1        = random.randint(low=1,high=len(os.listdir('_static/HR')))
        player.iImgPost2        = random.randint(low=1,high=len(os.listdir('_static/HR')))
        player.iImgPost3        = random.randint(low=1,high=len(os.listdir('_static/HR')))
        player.iImgPost4        = random.randint(low=1,high=len(os.listdir('_static/HR')))
        player.iImgPost5        = random.randint(low=1,high=len(os.listdir('_static/HR')))
        player.iImgPost6        = random.randint(low=1,high=len(os.listdir('_static/HR')))
        # create 
        print('set player.iImgFeed to', player.iImgFeed)
        print('set player.iImgPost1 to', player.iImgPost1)


# PAGES

class ToMemeOrNotToMeme(Page):
    form_model = 'player'
    form_fields = [
        'iTrialDec',
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
            'Image'    :  "".join(['meme_game/meme', str(player.iImgFeed) , '.jpg']) ,
        }

    @staticmethod
    def js_vars(player: Player):
        return {
            'sTreat'    :  player.sTreat,
        }

class addTags(Page):
    form_model = 'player' 
    form_fields = [
        'dRT2',
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
    ] 

    @staticmethod
    def vars_for_template(player): #otree function for the html
        # i=1
	    # j=int(i)+1
	    # k=int(i)+2
	    # l=int(i)+3
	    # m=int(i)+4
	    # n=int(i)+5
        return {
            'Image'    :  "".join(['HR/meme', str(player.iImgPost1) , '.jpg']) ,
            'Image2'    :  "".join(['HR/meme', str(player.iImgPost2) , '.jpg']) ,
            'Image3'    :  "".join(['HR/meme', str(player.iImgPost3), '.jpg']) ,
            'Image4'    :  "".join(['HR/meme', str(player.iImgPost4), '.jpg']) ,
            'Image5'    :  "".join(['HR/meme', str(player.iImgPost5) , '.jpg']) ,
            'Image6'    :  "".join(['HR/meme', str(player.iImgPost6) , '.jpg']) ,
        }
        #this might not work bc im concatating the string and not actually summing numbers
        # if i do it like this i need to get 110 memes in both HR and LR 
        # str(player.iImgPost)+str(3)  <- previous approach

class HowDoYaFeel(Page):
    form_model = 'player' 
    form_fields = [
        'EmotionalStatus',
    ] 

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass

#! THINGS TO  BE CODED 
# ToMemeOrNotToMeme: better layout
# Posting: bigger label name
# Tags: 
# Feedbackpage (!!!!)
# EmotionalStatus: solve the ()
# History display
# QUESTIONNAIRE APP with social media and demographics question
# ,  ResultsWaitPage, Results

page_sequence = [ToMemeOrNotToMeme, Posting, MyPage, HowDoYaFeel, addTags]
