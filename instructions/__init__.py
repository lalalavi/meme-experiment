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


#def creating_session(subsession: Subsession):
    #for p in subsession.get_players():
        #stimuli = read_csv()
        #p.num_trials = len(stimuli)
        #for stim in stimuli:
        #   Trial.create(player=p, **stim)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.IntegerField(
        choices=[
        [1, 'I would like to participate'],
        ],
        widget=widgets.RadioSelect,
        label="",
    )  
    

def get_current_trial(player: Player):
    return Trial.filter(player=player, choice=None)[0]


def is_finished(player: Player):
    return player.num_completed == player.num_trials


class Trial(ExtraModel):
    player = models.Link(Player)


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

class instruct_4(Page):
    pass

page_sequence = [consent, instruct_0, instruct_1, instruct_2, instruct_3, instruct_4]
