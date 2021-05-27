from otree.api import *

doc = """
Post-experimental questionnaire
"""


class Constants(BaseConstants):
    name_in_url = 'Results'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    iAge                = models.IntegerField(label="For statistical purposes, please enter your age:", min=18, max=100)
    iGender             = models.IntegerField(
                        choices=[[1, 'Male'],[2, 'Female'],[3, 'Non-binary/ third gender'],[4, 'Prefer not to answer'], ],
                        label="Please select your gender:",)   
    sNationality        = models.StringField(label="*Optional. Please enter your nationality:", blank=True)  
    iEducation          = models.IntegerField(
                        choices=[[1, 'Primary education'],[2, 'High school or equivalent'],[3, 'Vocational school (Dutch: MBO)'],[4, 'Higher education (Dutch: HBO)'],[5, 'Bachelors degree (Dutch: WO bachelor)'],[6, 'Masters degree (Dutch: WO master)'],[7, 'Doctorate (e.g., PhD, EdD)'],[7, 'Other'], ],
                        label="Highest level of education obtained",) 
    iEnglish            = models.IntegerField(
                        choices=[[1, 'Native speaker'],[2, 'Near native/fluent'],[3, 'Excellent command / highly proficient in spoken and written English'],[4, 'Very good command'],[5, 'Good command / good working knowledge'],[6, 'Basic communication skills / working knowledge'],],
                        label="How would you rank your own English language skills?",) 
    iSocialmediause     = models.IntegerField(
                        choices=[[1, 'Almost Constantly'],[2, 'Several times a day'],[3, 'About once a day'],[4, 'Several times a week'],[5, 'Less often'],[6, 'Never'],],
                        label="How often do you use social media?",) 
    sHours              = models.StringField(label="If you reported using social media daily, provide an estimate of how much time you normally spend on a day inside all social media platforms:", blank=True)
    iTypicallikes       = models.IntegerField(label="If applicable, how many likes (or similar) do you typically get when you post on social media (for example on Instagram, Twitter, Facebook, Reddit)?", blank=True)
    iInstafollowers     = models.IntegerField(label="If applicable, how many followers/friends/subscribers (or similar) do you have on Instagram?", blank=True)
    iTwitterfollowers   = models.IntegerField(label="If applicable, how many followers/friends/subscribers (or similar) do you have on Twitter?", blank=True)
    iFBfriends          = models.IntegerField(label="If applicable, how many followers/friends/subscribers (or similar) do you have on Facebook?", blank=True)
    iSMS1               = models.IntegerField(
                        choices=[[1, 'Yes'],[2, 'No'], ],
                        label="...regularly found that you can't think of anything else but the moment that you will be able to use social media again?",)
    iSMS2               = models.IntegerField(
                        choices=[[1, 'Yes'],[2, 'No'], ],
                        label="...regularly felt dissatisfied because you wanted to spend more time on social media?",)
    iSMS3               = models.IntegerField(
                        choices=[[1, 'Yes'],[2, 'No'], ],
                        label="...often felt bad when you could not use social media?",)
    iSMS4               = models.IntegerField(
                        choices=[[1, 'Yes'],[2, 'No'], ],
                        label="...tried to spend less time on social media, but failed?",)
    iSMS5               = models.IntegerField(
                        choices=[[1, 'Yes'],[2, 'No'], ],
                        label="...regularly neglected other activities (e.g. hobbies, sport) because you wanted to use social media?",)
    iSMS6               = models.IntegerField(
                        choices=[[1, 'Yes'],[2, 'No'], ],
                        label="...regularly had arguments with others because of your social media use?",)                     
    iSMS7               = models.IntegerField(
                        choices=[[1, 'Yes'],[2, 'No'], ],
                        label="...regularly lied to your parents or friends about the amount of time you spend on social media?",)               
    iSMS8               = models.IntegerField(
                        choices=[[1, 'Yes'],[2, 'No'], ],
                        label="...often used social media to escape from negative feelings?",)   
    iSMS9               = models.IntegerField(
                        choices=[[1, 'Yes'],[2, 'No'], ],
                        label="...had serious conflict with your parents, brother(s) or sister(s) because of your social media use?",)   

    # email = models.StringField(label="Please enter your e-mail adress if you want to be in the random selection to be paid according to your outcomes:", blank=True)

# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = [
        'iAge', 
        'iGender', 
        'sNationality',
        'iEnglish',
        'iEducation', 
        'iSocialmediause', 
        'sHours', 
        'iTypicallikes', 
        'iInstafollowers',
        'iTwitterfollowers',
        'iFBfriends',
        ]

# SMS refers to social media scale
class SMS(Page):
    form_model = 'player'
    form_fields = ['iSMS1', 'iSMS2', 'iSMS3', 'iSMS4', 'iSMS5', 'iSMS6', 'iSMS7', 'iSMS8', 'iSMS9',]

class End(Page):
    pass
    

page_sequence = [Demographics, SMS, End]