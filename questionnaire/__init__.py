from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Questionnaire'
    players_per_group = None
    num_rounds = 1
    ## Path for images
    # imgFile_Quality     = '/static/global/figures/Infographic_graphs/qual_lin.png'
    # imgFile_QualityCv   = '/static/global/figures/Infographic_graphs/qual_concave.png'
    # imgFile_QualityCx   = '/static/global/figures/Infographic_graphs/qual_convex.png'
    # imgFile_Linear      = '/static/global/figures/Infographic_graphs/sus_linear.png'
    # imgFile_Concave     = '/static/global/figures/Infographic_graphs/sus_concave.png'
    # imgFile_Convex      = '/static/global/figures/Infographic_graphs/sus_convex.png' 

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    # Variables for Demographics
    D1 = models.StringField()
    D2 = models.StringField()
    D3 = models.StringField()
    D4 = models.StringField()
    D5 = models.StringField()
    D6 = models.StringField(blank=True)
    D7 = models.StringField(blank=True)
    D8 = models.StringField()

    # Variables for Demographics
    QT1 = models.StringField()
    QT2 = models.StringField()
    QT3 = models.StringField()
    QT4 = models.StringField()
    QT5 = models.StringField()
    QT6 = models.StringField()


    # Variables for Social Media Disorder scale
    SMD1 = models.StringField()
    SMD2 = models.StringField()
    SMD3 = models.StringField()
    SMD4 = models.StringField()
    SMD5 = models.StringField()
    SMD5 = models.StringField()
    SMD6 = models.StringField()
    SMD7 = models.StringField()
    SMD8 = models.StringField()
    SMD9 = models.StringField()
 
    # Variables for BIS questionnaire
    BIS1 = models.StringField()
    BIS2 = models.StringField()
    BIS3 = models.StringField()
    BIS4 = models.StringField()
    BIS5 = models.StringField()
    BIS6 = models.StringField()
    BIS7 = models.StringField()
    BIS8 = models.StringField()
    BIS9 = models.StringField()
    BIS10 = models.StringField()
    BIS11 = models.StringField()
    BIS12 = models.StringField()
    BIS13 = models.StringField()
    BIS14 = models.StringField()
    BIS15 = models.StringField()
    BIS16 = models.StringField()
    BIS17 = models.StringField()
    BIS18 = models.StringField()
    BIS19 = models.StringField()
    BIS20 = models.StringField()
    BIS21 = models.StringField()
    BIS22 = models.StringField()
    BIS23 = models.StringField()
    BIS24 = models.StringField()
    BIS25 = models.StringField()
    BIS26 = models.StringField()
    BIS27 = models.StringField()
    BIS28 = models.StringField()
    BIS29 = models.StringField()
    BIS30 = models.StringField()

    # Validation Questions
    V1 = models.StringField()
    V2 = models.StringField()
    V3 = models.StringField()


# PAGES
class Questionnaire(Page):
    form_model = 'player'
    form_fields = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8',
    'QT1', 'QT2', 'QT3', 'QT4', 'QT5', 'QT6',
    'BIS1', 'BIS2', 'BIS3', 'BIS4', 'BIS5', 'BIS6', 'BIS7', 'BIS8', 'BIS9', 'BIS10', 'BIS11', 'BIS12', 'BIS13', 'BIS14', 'BIS15', 'BIS16', 'BIS17', 'BIS18', 'BIS19', 'BIS20', 'BIS21', 'BIS22', 'BIS23', 'BIS24', 'BIS25', 'BIS26', 'BIS27', 'BIS28', 'BIS29', 'BIS30', 
    'SMD1', 'SMD2', 'SMD3', 'SMD4', 'SMD5', 'SMD6', 'SMD7', 'SMD8', 'SMD9',
    ]

    # 'V1', 'V2', 'V3'

    # @staticmethod
    # def js_vars(player: Player):
    #     return dict(
    #         Ql = Constants.imgFile_Quality,
    #         Qcv = Constants.imgFile_QualityCv,
    #         Qcx = Constants.imgFile_QualityCx,
    #         Sl = Constants.imgFile_Linear, 
    #         Scv = Constants.imgFile_Concave,
    #         Scx = Constants.imgFile_Convex,
    #     )

    # @staticmethod
    # def before_next_page(player, timeout_happened):
    #     # Validate questionnaire
    #     valid1 = int(int(player.V1)==2)
    #     valid2 = int(int(player.V2)==4)
    #     valid3 = int(int(player.V3)==1)
    #     player.participant.validQuestionnaire = valid1 + valid2 + valid3


page_sequence = [Questionnaire]
