from otree.api import *

doc = """
Instructions
"""


class Constants(BaseConstants):
    name_in_url = 'instructions'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.IntegerField(
            choices=[[1, 'I would like to participate'],],
            widget=widgets.RadioSelect,
            label="",)  
    
# PAGES
class consent(Page):
    form_model = 'player'
    form_fields = ['consent']

class instruct_0(Page):
    pass

class instruct_1(Page):
    pass

class instruct_2(Page):
    pass

class instruct_3(Page):
    pass

page_sequence = [consent, instruct_0, instruct_1, instruct_2, instruct_3]