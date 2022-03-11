from otree.api import *
import numpy as np
import pandas as pd
import re 
import random
import os
import time


c = Currency

doc = """
ᶘ ᵒᴥᵒᶅ i see memes
"""

class Constants(BaseConstants):
    name_in_url = 'simple_experiment'
    players_per_group = None
    num_rounds = 20
    df = pd.read_excel("_static/global/HR.xlsx",index_col="Numbers")
    df2 = pd.read_excel("_static/global/LR.xlsx",index_col="Numbers")
    total_time = 300 #5 minutes

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ## Treatment Variables 
    sTreatment         = models.StringField(blank=True) 
    sReward            = models.StringField(blank=True)
    sRandom            = models.StringField(blank=True)
    sRandom2           = models.StringField(blank=True)
    ## Attention Variables (??)
    sButtonClick       = models.LongStringField(blank=True) 
    sTimeClick         = models.LongStringField(blank=True)
    ## Participant input Variables 
    iFeedLikes         = models.IntegerField(blank=True)
    iFeedDislikes      = models.IntegerField(blank=True)
    iPost              = models.IntegerField(blank=True) # the meme they choose during posting
    iEmotionalStatus   = models.IntegerField() #this is required
    sTag1              = models.StringField(blank=True)
    sTag2              = models.StringField(blank=True)
    sTag3              = models.StringField(blank=True)
    ## Meme information Variables
    iLikes             = models.IntegerField(blank=True)
    iDislikes          = models.IntegerField(blank=True)
    iImgPost1          = models.IntegerField(blank=True)
    iImgPost2          = models.IntegerField(blank=True)
    iImgPost3          = models.IntegerField(blank=True)
    iImgPost4          = models.IntegerField(blank=True)
    iImgPost5          = models.IntegerField(blank=True)
    iImgPost6          = models.IntegerField(blank=True)
    ## RT variables
    # dExpiry            = models.IntegerField(blank=True)
    dRTDec1            = models.FloatField(blank=True)
    dRTFeed            = models.FloatField(blank=True) 
    dRTPost            = models.FloatField(blank=True) #d because the type is double, reaction time
    dRTTags            = models.FloatField(blank=True)
    dRTFeedback        = models.FloatField(blank=True)
    dRTEmotionalStatus = models.FloatField(blank=True) 



###########################################################################################
#  FUNCTION ᕕ(ᐛ)ᕗ
###########################################################################################

def creating_session(subsession):
    for player in subsession.get_players():
        if player.round_number == 1:
            player.participant.sTreatment = random.choice(['Control', 'Emotional']) #between randomization
            player.participant.sRandom = random.choice(['LR', 'HR']) #within randomization
            player.participant.sRandom2 = random.choice(['LR', 'HR'])
            while player.participant.sRandom == player.participant.sRandom2: #makes sure half of
                player.participant.sRandom2 = random.choice(['LR', 'HR'])
        player.sTreatment = player.participant.sTreatment
        player.sRandom = player.participant.sRandom 
        player.sRandom2 = player.participant.sRandom2 
        if player.round_number > 1:
            prev_player = player.in_round(player.round_number - 1)

###########################################################################################
#  Pages ᕕ(ᐛ)ᕗ
###########################################################################################

class ready(Page):
    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        participant.dExpiry = time.time() + Constants.total_time   # This initializes the time counter
        participant.dExpiry = round(participant.dExpiry)

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class SplitScreen(Page):
    form_model = 'player' 
    form_fields = [
        'iFeedLikes','iFeedDislikes',
    ] 

    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant
        return participant.dExpiry - time.time()

    @staticmethod
    def vars_for_template(player): 
        url_list=[]
        for meme in [x for x in range(1,70)]: #excludes the 1
            url_list.append(f'memes/feed{meme}.jpg') 
        if player.round_number == 1:
            return dict(url_list=url_list)
        else: 
            prev_player = player.in_round(player.round_number - 1)
            return {
                    'prev_player'   :  player.in_round(player.round_number - 1), #define the last round
                    'image_path'    :  "".join([prev_player.sReward,'/meme', str(prev_player.iPost) , '.jpg']) ,
                    'dislikes'      :  prev_player.iDislikes ,
                    'likes'         :  prev_player.iLikes ,
                    'roundnumber'   :  prev_player.round_number ,
                    'url_list'      :  url_list , 
            }
        
    @staticmethod
    def is_displayed(player):
        participant = player.participant
        time_left = participant.dExpiry - time.time()
        return time_left > 3

    @staticmethod
    def js_vars(player: Player):
        return {
            'treatment'   :  player.sTreatment ,
        }


class Posting(Page):
    form_model = 'player' 
    form_fields = [
        'iImgPost1','iImgPost2','iImgPost3','iImgPost4','iImgPost5','iImgPost6',
        'iPost', 'dRTPost', 'sReward',
    ] 
    
    @staticmethod
    def vars_for_template(player):
        participant = player.participant
        # time_elapsed = round(get_timeout_seconds(player)) #round(get_timeout_seconds)
        time_left = round(participant.dExpiry - time.time()) 

        if time_left > Constants.total_time/2:  
            player.sReward = player.sRandom
        else:
            player.sReward = player.sRandom2
        
        if player.sReward == 'LR':
            memelist = os.listdir('_static/LR')[1:-1] 
            pattern = r"meme(?P<number>\d{3})\.jpg"
            numbers = [int(re.match(pattern, x).group("number")) for x in memelist]  # take all of the numbers from the image files and put them on a list
            vImages = random.sample(numbers, 6) 
        else:
            vImages = random.sample(range(1,len(os.listdir('_static/HR'))), 6)
        
        player.iImgPost1        = vImages[0]
        player.iImgPost2        = vImages[1]
        player.iImgPost3        = vImages[2]
        player.iImgPost4        = vImages[3]
        player.iImgPost5        = vImages[4]
        player.iImgPost6        = vImages[5]
        
        return {
            'Image'     :  "".join([player.sReward,'/meme', str(player.iImgPost1), '.jpg']) ,
            'Image2'    :  "".join([player.sReward,'/meme', str(player.iImgPost2), '.jpg']) ,
            'Image3'    :  "".join([player.sReward,'/meme', str(player.iImgPost3), '.jpg']) ,
            'Image4'    :  "".join([player.sReward,'/meme', str(player.iImgPost4), '.jpg']) ,
            'Image5'    :  "".join([player.sReward,'/meme', str(player.iImgPost5), '.jpg']) ,
            'Image6'    :  "".join([player.sReward,'/meme', str(player.iImgPost6), '.jpg']) ,   
        }
    

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
    def get_timeout_seconds(player):
        participant = player.participant
        return participant.dExpiry - time.time()

    @staticmethod
    def is_displayed(player):
        participant = player.participant
        time_left = participant.dExpiry - time.time()
        return time_left > 3


class addTags(Page):
    form_model = 'player' 
    form_fields = [
        'sTag1','sTag2','sTag3','dRTTags',
    ] 

    @staticmethod
    def vars_for_template(player): 
        return {
            'Image'    :  "".join([player.sReward,'/meme', str(player.iPost) , '.jpg']) , 
        }

    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant
        return participant.dExpiry - time.time()

    @staticmethod
    def is_displayed(player):
        participant = player.participant
        time_left = participant.dExpiry - time.time()
        return time_left > 3


class Feedback(Page):
    form_model = 'player'
    form_fields = [
        'iLikes','iDislikes','dRTFeedback',
    ] 

    @staticmethod
    def vars_for_template(player):
        if player.sReward == 'HR': 
            return {
                'img'        : player.iPost,
                'l'          : Constants.df.loc[player.iPost,"Likes"],
                'd'          : Constants.df.loc[player.iPost,"Dislikes"],
            }
        else:
            return {
                'img'        : player.iPost,
                'l'          : Constants.df2.loc[player.iPost,"Likes"],
                'd'          : Constants.df2.loc[player.iPost,"Dislikes"],
            }

    @staticmethod
    def js_vars(player: Player):
        return {
            'treatment'   :  player.sTreatment ,
        }

    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant
        return participant.dExpiry - time.time()

    @staticmethod
    def is_displayed(player):
        participant = player.participant
        time_left = participant.dExpiry - time.time()
        return time_left > 3


class HowDoYaFeel(Page):
    form_model = 'player' 
    form_fields = [
        'iEmotionalStatus','dRTEmotionalStatus',
    ] 

    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant
        return participant.dExpiry - time.time()

    @staticmethod
    def is_displayed(player):
        participant = player.participant
        time_left = participant.dExpiry - time.time()
        return time_left > 3


#! THINGS TO THINK
# CSS PROPERTIES... position: absolute; transform: translate(-50%,-50%); top: 90vh; left: 90vw;
# check out what is django?


page_sequence = [ready, SplitScreen, Posting, addTags, Feedback, HowDoYaFeel]
