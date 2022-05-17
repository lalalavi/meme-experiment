from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Questionnaire'
    players_per_group = None
    num_rounds = 1
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
    D9 = models.StringField()
    D10 = models.StringField(blank=True)  #like this right now because I do not know how to do shortOpen questions properly
    D11 = models.StringField(blank=True)
    D12 = models.StringField(blank=True)
    D13 = models.StringField(blank=True)
    D14 = models.StringField(blank=True)
    D15 = models.StringField(blank=True)


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
    form_fields = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13',
    'BIS1', 'BIS2', 'BIS3', 'BIS4', 'BIS5', 'BIS6', 'BIS7', 'BIS8', 'BIS9', 'BIS10', 'BIS11', 'BIS12', 'BIS13', 'BIS14', 'BIS15', 'BIS16', 'BIS17', 'BIS18', 'BIS19', 'BIS20', 'BIS21', 'BIS22', 'BIS23', 'BIS24', 'BIS25', 'BIS26', 'BIS27', 'BIS28', 'BIS29', 'BIS30', 
    'SMD1', 'SMD2', 'SMD3', 'SMD4', 'SMD5', 'SMD6', 'SMD7', 'SMD8', 'SMD9',
    'V1', 'V2', 'V3',
    ]


    @staticmethod
    def before_next_page(player, timeout_happened):
        # Validate questionnaire
        valid1 = int(int(player.V1)==2)
        valid2 = int(int(player.V2)==4)
        valid3 = int(int(player.V3)==1)
        player.participant.validQuestionnaire = valid1 + valid2 + valid3


page_sequence = [Questionnaire]
