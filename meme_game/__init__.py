from otree.api import *
import numpy as np
from numpy import random
from random import sample
from random import choices
import pandas as pd
import csv
import copy

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'meme_game'
    players_per_group = None
    num_rounds = 1 #here you define the number of trials
    choices = ['Post', 'See'] 


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer): #define here ALL variables i will save at player level

    iTrialDec          = models.StringField(choices=Constants.choices) #first decision where u can choose between seeing and posting
    iDec               = models.BooleanField(blank=True) #why is this a boolean
    iDec2              = models.IntegerField(blank=True) #the meme they choose during posting
    dRT1               = models.FloatField(blank=True)   #d because double
    dRT2               = models.FloatField(blank=True)
    dRT3               = models.FloatField(blank=True)
    iImgFeed           = models.IntegerField(blank=True)
    iImgPost           = models.IntegerField(blank=True)
    Image2             = models.IntegerField(blank=True)
    Image3             = models.IntegerField(blank=True)
    Image4             = models.IntegerField(blank=True)
    Image5             = models.IntegerField(blank=True)
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
        player.iImgPost         = random.randint(low=1,high=10) 
        print('set player.iImgFeed to', player.iImgFeed)
        print('set player.iImgPost to', player.iImgPost)


# PAGES

#  class ToMemeOrNotToMeme(Page):
#     form_model = 'player' #from who are you extracting the info
#     form_fields = [
#         'iDec', 
#         'dRT1',
#     ]
#     @staticmethod
#     def vars_for_template(player): #otree function for the html
#         return {
#             'Image'    :  "".join(['meme_game/meme', str(player.iImg) , '.jpg']) ,
#         }

class ToMemeOrNotToMeme(Page):
    form_model = 'player'
    form_fields = [
        'iTrialDec',
        'dRT1',
    ]

    @staticmethod
    def vars_for_template(player: Player):
        return dict(past_players=player.in_previous_rounds())


#mypage is really the feed 
#have to add timer
class MyPage(Page):
    form_model = 'player' #from who are you extracting the info
    form_fields = [
        'iDec',
        'dRT2',
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
    # @staticmethod
    # def vars_for_template(player): #otree function for the html
    #     participant     = player.participant
    #     iRound          = player.round_number
    #     return {
    #         # 'Color0'    : values[0],
    #         # 'Color1'    : values[1],
    #         # 'Color2'    : values[2],
    #         # 'Color3'    : values[3],
    #         # 'treatment' : player.sTreat2,
    #     }

class Posting(Page):
    form_model = 'player' 
    form_fields = [
        'iImgPost',
        'Image2',
        'Image3',
        'Image4',
        'Image5',
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
            'Image'    :  "".join(['HR/meme', str(player.iImgPost) , '.jpg']) ,
            'Image2'    :  "".join(['HR/meme', str(player.iImgPost)+str(1) , '.jpg']) ,
            'Image3'    :  "".join(['HR/meme', str(player.iImgPost)+str(2) , '.jpg']) ,
            'Image4'    :  "".join(['HR/meme', str(player.iImgPost)+str(4) , '.jpg']) ,
            'Image5'    :  "".join(['HR/meme', str(player.iImgPost)+str(6) , '.jpg']) ,
            'Image6'    :  "".join(['HR/meme', str(player.iImgPost)+str(3) , '.jpg']) ,
        }
        #this might not work bc im concatating the string and not actually summing numbers
        # if i do it like this i need to get 110 memes in both HR and LR 

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
# Posting: different displays
# Tags: 
# Feedbackpage (!!!!)
# EmotionalStatus: sol
# History display
# QUESTIONNAIRE APP with social media and demographics question

page_sequence = [ToMemeOrNotToMeme, MyPage, HowDoYaFeel,  Posting, addTags,  ResultsWaitPage, Results]
