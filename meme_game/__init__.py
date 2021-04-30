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
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    iDec               = models.BooleanField(blank=True)
    dRT                = models.FloatField(blank=True)   #double
    iImg               = models.IntegerField(blank=True)
    sTreat             = models.StringField(blank=True)


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
class MyPage(Page):
    form_model = 'player' #de quien saco la informacion
    form_fields = [
        'iDec', 
        'dRT',
    ] #todas las variables q quieres salvar de una pagina
    @staticmethod
    def vars_for_template(player): #this is for the html
        return {
            'Image'    :  "".join(['meme_game/meme', str(player.iImg) , '.jpg']) ,
        }

    @staticmethod
    def js_vars(player: Player):
        return {
            'sTreat'    :  player.sTreat,
        }

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
