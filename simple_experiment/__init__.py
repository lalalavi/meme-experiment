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
    IMG_ON_PAGE = 6

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    ## Treatment Variables 
    sTreatment              = models.StringField(blank=True) 
    sReward                 = models.StringField(blank=True)
    sRandom                 = models.StringField(blank=True)
    sRandom2                = models.StringField(blank=True)
    ## Attention Variables 
    sFeedback               = models.LongStringField(blank=True)    # Order of feedback seen
    sTimeFeedback           = models.LongStringField(blank=True)    # Time each of them was looked at
    sScreenFeedback         = models.LongStringField(blank=True)    # Order of feedback seen PAST post
    sScreenTimeFeedback     = models.LongStringField(blank=True)    # Time PAST feedback was looked at
    sFixations              = models.LongStringField(blank=True) 
    sOrderFixations         = models.LongStringField(blank=True) 
    ## Participant input Variables 
    iFeedLikes              = models.IntegerField(blank=True)
    iFeedDislikes           = models.IntegerField(blank=True)
    iPost                   = models.IntegerField(blank=True)       # the meme they choose during posting
    iEmotionalStatus        = models.IntegerField()                 # this is required
    sTag1                   = models.StringField(blank=True)
    sTag2                   = models.StringField(blank=True)
    sTag3                   = models.StringField(blank=True)
    ## Meme information Variables
    iLikes                  = models.IntegerField(blank=True)
    iDislikes               = models.IntegerField(blank=True)
    iImgPost1               = models.IntegerField(blank=True)
    iImgPost2               = models.IntegerField(blank=True)
    iImgPost3               = models.IntegerField(blank=True)
    iImgPost4               = models.IntegerField(blank=True)
    iImgPost5               = models.IntegerField(blank=True)
    iImgPost6               = models.IntegerField(blank=True)
    ## RT variables     
    dRTLatency              = models.FloatField(blank=True)         #d because the type is double
    dRTPost                 = models.FloatField(blank=True) 
    dRTTags                 = models.FloatField(blank=True)
    dRTFeedback             = models.FloatField(blank=True)
    dRTEmotionalStatus      = models.FloatField(blank=True) 

###################################################################################################
#  FUNCTION ᕕ(ᐛ)ᕗ
###################################################################################################

def creating_session(subsession):
    for player in subsession.get_players():
        p = player.participant
        if player.round_number == 1:
            #between randomization
            p.sTreatment = random.choice(['Control', 'Emotional', 'Fullinfo'])
            #within randomization 
            p.sRandom = random.choice(['LR', 'HR']) 
            p.sRandom2 = random.choice(['LR', 'HR'])
            while p.sRandom == p.sRandom2: #repeat randomization until it is different for each half
                p.sRandom2 = random.choice(['LR', 'HR'])
            #IMAGES 
            LRmemelist = os.listdir('_static/LR')[1:-1] 
            pattern = r"meme(?P<number>\d{3})\.jpg"
            LRnumbers = [int(re.match(pattern, x).group("number")) for x in LRmemelist]  # take all of the numbers from the image files and put them on a list
            LRnumbers = random.sample(LRnumbers, len(LRnumbers))        #shuffle so order is not the same across participants
            LRnumbers = [LRnumbers[n-Constants.IMG_ON_PAGE:n] for n in range(Constants.IMG_ON_PAGE,len(LRnumbers), Constants.IMG_ON_PAGE)]
            p.LRmemematrix = LRnumbers
            HRnumbers = range(1,len(os.listdir('_static/HR')))
            HRnumbers = [HRnumbers[n-Constants.IMG_ON_PAGE:n] for n in range(Constants.IMG_ON_PAGE,len(HRnumbers), Constants.IMG_ON_PAGE)]                
            p.HRmemematrix = HRnumbers
        player.sTreatment = p.sTreatment
        player.sRandom = p.sRandom 
        player.sRandom2 = p.sRandom2 
     
        if player.round_number > 1:
            prev_player = player.in_round(player.round_number - 1)
        

###################################################################################################
#  Pages ᕕ(ᐛ)ᕗ
###################################################################################################

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
        'sScreenFeedback', 'sScreenTimeFeedback', 'sOrderFixations', 'sFixations',
        'dRTLatency',
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
            'treatment'      :  player.sTreatment ,
            'round_number'   :  player.round_number ,
        }


class Posting(Page):
    form_model = 'player' 
    form_fields = [
        'iImgPost1','iImgPost2','iImgPost3','iImgPost4','iImgPost5','iImgPost6',
        'iPost', 'sReward', 'dRTPost',
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
            vImages = participant.LRmemematrix 
        else:
            vImages = participant.HRmemematrix 

        player.iImgPost1        = vImages[player.round_number - 1][0]
        player.iImgPost2        = vImages[player.round_number - 1][1]
        player.iImgPost3        = vImages[player.round_number - 1][2]
        player.iImgPost4        = vImages[player.round_number - 1][3]
        player.iImgPost5        = vImages[player.round_number - 1][4]
        player.iImgPost6        = vImages[player.round_number - 1][5]
        
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
        'iLikes','iDislikes','dRTFeedback', 'sFeedback', 'sTimeFeedback',
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
# change mouseover for mouseenter in VT buttons
# buttons under last post sometimes are hidden under post in splitscreen
# Post button div in split screen messes with the hiding function

page_sequence = [ready, SplitScreen, Posting, addTags, Feedback, HowDoYaFeel]
