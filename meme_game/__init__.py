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


class Player(BasePlayer):
    iTrialDec          = models.StringField(choices=Constants.choices)
    iDec               = models.BooleanField(blank=True)
    dRT1               = models.FloatField(blank=True)   #d because double
    dRT2               = models.FloatField(blank=True)
    dRT3               = models.FloatField(blank=True)
    iImg               = models.IntegerField(blank=True)
    sTreat             = models.StringField(blank=True)
#define here ALL variables i will save

# FUNCTIONS

def creating_session(subsession):
    # randomize to treatments
    for player in subsession.get_players():
        # Setup a treatment condition (changes each round)
        player.sTreat          = random.choice(['Like', 'Dislike'])
        print('set player.sTreat3 to', player.sTreat)
        player.iImg             = random.randint(low=1,high=3) 
        print('set player.iImg to', player.iImg)

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
        'dRT2',
    ] #todas las variables q quieres salvar de una pagina
    @staticmethod
    def vars_for_template(player): #otree function for the html
        return {
            'Image'    :  "".join(['meme_game/meme', str(player.iImg) , '.jpg']) ,
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
    @staticmethod
    def vars_for_template(player): #otree function for the html
        participant     = player.participant
        iRound          = player.round_number
        return {
            # 'Color0'    : values[0],
            # 'Color1'    : values[1],
            # 'Color2'    : values[2],
            # 'Color3'    : values[3],
            # 'treatment' : player.sTreat2,
        }

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass

#PAGES TO BE CODED ToMemeOrNotToMeme, Posting, Tags, Feedbackpage, EmotionalStatus

page_sequence = [ToMemeOrNotToMeme, MyPage, addTags, ResultsWaitPage, Results]
