from otree.api import *

doc = """
Includes consent, instructions, and comprehension test for the meme experiment (◕ᴗ◕✿) 
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
    # q1 = models.IntegerField(
    #     label="Q1: Pick the TRUE statement",
    #     choices=[
    #         [1, 'The feedback of the memes I choose is not real'] ,
    #         [2, 'The maximum amount of likes I can receive is 40'] ,
    #         [3, 'The maximum amount of likes I can receive is 34'] 
    #         ],
    #      blank=True)
    # q2 = models.IntegerField(
    #     label="Q2: Pick the TRUE statement",
    #     choices=[
    #         [1, 'I am required to put tags in my posts'],
    #         [2, 'I am required to inform of my emotional status'] ,
    #         [3, 'I am required to post from time to time']
    #     ],
    #     blank=True)
    # q3 = models.IntegerField(
    #     label="Q3: Pick the TRUE statement",
    #     choices=[
    #         [1, 'I select a meme by pressing a number on my keyboard'],
    #         [2, 'I select a meme by clicking on it with my mouse'] ,
    #     ],
    #     blank=True)    

# PAGES
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

class ready(Page):
    pass

page_sequence = [consent, instruct_0, instruct_1, understanding, ready]