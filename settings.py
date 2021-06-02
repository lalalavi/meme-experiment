from os import environ


SESSION_CONFIGS = [
    # dict(
    #     name='formatting_instructions',
    #     display_name="instructions life",
    #     num_demo_participants=3,
    #     app_sequence=['instructions'],
    # ),
    dict(
        name='Thesis_Experiment',
        display_name="meme life",
        num_demo_participants=100, # should this be one or 150
        app_sequence=['instructions','meme_game', 'questionnaire'],
    ),
    dict(
        name='Beta_Testing',
        display_name="Beta life",
        num_demo_participants=5, 
        app_sequence=['instructions','meme_game', 'questionnaire'],
    ),
     dict(
        name='formatting_questionnaire',
        display_name="questionnaire life",
        num_demo_participants=3,
        app_sequence=['questionnaire'],
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

# ROOMS = [
#     dict(
#         name='econ101',
#         display_name='Econ 101 class',
#         participant_label_file='_rooms/econ101.txt',
#     ),
#     dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
# ]

ROOMS = [
    dict(
        name='Thesis',
        display_name='Social Media experiment',
        # participant_label_file='_rooms/labels.txt',
        # use_secure_urls=True
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin' # IMPORTANT!! YOU USE THIS TO ACCESS OTREEHUB
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here is my Master Thesis experiment. ᕕ(ᐛ)ᕗ
"""


SECRET_KEY = '1540738163475'

INSTALLED_APPS = ['otree']
