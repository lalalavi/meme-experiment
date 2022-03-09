from os import environ

SESSION_CONFIGS = [
    dict(
        name='Beta_Experiment',
        display_name="Beta life",
        num_demo_participants=10, 
        app_sequence=['simple_experiment'],
    ),
    dict(
        name='Beta_Instructions',
        display_name="Instructions yo",
        num_demo_participants=10, 
        app_sequence=['instructions'],
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['dExpiry']
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
ᕕ(ᐛ)ᕗ
oh boi back to the drawing board 
 """

SECRET_KEY = '6932973588929'
