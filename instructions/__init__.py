from otree.api import *
from statistics import mode
import time

doc = """
Includes consent, instructions, and comprehension test for the meme experiment (◕ᴗ◕✿) 
"""

class Constants(BaseConstants):
    name_in_url = 'instructions'
    players_per_group = None
    num_rounds = 1
    UvA_logo = 'global/figures/UvA_logo.png'
    FlatFee = "3 euros"

    ## Slides for introduction
    SlidePath = 'Instructions/slide'
    SlidesIntro = [
        dict(
            Title = 'Introduction',
            path='Introduction/slide0.html',
            ),
        dict(
            Title = 'Informed Consent',
            path='Introduction/slide1.html',
            ),        
    ]
    Slides = [
        dict(
            Title = 'The Experiment',
            path=SlidePath+'0.html',
            ),
        dict(
            Title = 'Your Decisions',
            path=SlidePath+'1.html'
            ),
        dict(
            Title = 'The product characteristics',
            path=SlidePath+'2.html'
            ),
        dict(
            Title = 'Purchasing Platform',
            path=SlidePath+'3.html'
            ),
        # dict(
        #     Title = 'The product characteristics',
        #     path=SlidePath+'4.html'
        #     ),
        dict(
            Title = 'Is it all clear? Please answer these questions correctly to proceed:',
            path=SlidePath+'4.html'
            ),
    ]

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    sProlific_ID        = models.StringField()
    sSlideSequence      = models.StringField(blank=True)
    sSlideTime          = models.StringField(blank=True)
    dPixelRatio         = models.FloatField()



###################################################################################################
#  Pages ᕕ(ᐛ)ᕗ
###################################################################################################

class Introduction(Page):

    @staticmethod
    def vars_for_template(player):
        return dict(
            UvA_logo = Constants.UvA_logo,
            Slides = Constants.SlidesIntro,
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        p = player.participant
        # Initialize Focus variables#        
        p.startTime          = time.time()
        p.iOutFocus          = 0
        p.iFullscreenChanges = 0
        p.dTimeOutFocus      = 0
        player.sProlific_ID     = p.label


class Calibration(Page):
    form_model = 'player'
    form_fields = [ 'dPixelRatio' ]


    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        part = player.participant
        part.dPixelRatio = player.dPixelRatio

class Instructions(Page):
    form_model = 'player'
    form_fields = [ 
        'sSlideSequence',
        'sSlideTime',
        ]
    
    @staticmethod
    def vars_for_template(player):
        return dict(
            Slides = Constants.Slides,
            # lAttr = player.participant.lAttr,
    )

    @staticmethod
    def js_vars(player: Player):
        session = player.session
        p = player.participant
        return {
            'bRequireFS'        : session.config['bRequireFS'],
            'bCheckFocus'       : session.config['bCheckFocus'],
            'dPixelRatio'       : p.dPixelRatio,
        }

class consent(Page):
    form_model = 'player'
    form_fields = ['consent']

class instruct_0(Page):
    pass

class instruct_1(Page):
    pass

class understanding(Page):
    pass
    # form_model = 'player'
    # form_fields = ['q1', 'q2', 'q3'] 
    
    # # guarantee that the people choose the right option 
    # def error_message(self, values):
    #     if (values['q1'] != 3) or (values['q2'] != 2) or (values['q3'] != 1): #type the number directly bc we defined them as numbers in the class
    #         return 'Some of your answers contain an error'


page_sequence = [Introduction, Calibration, Instructions]