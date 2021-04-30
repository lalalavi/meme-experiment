

########
# i am not sure
########

# !
# todo
# what is the difference between app_sequecence and page_sequence (pages is what the person sees)
# * different colors
# ? another color


SESSION_CONFIGS = [
    dict(
        name='meme_experiment',
        app_sequence=['instructions', 'action'. 'ending'],
        num_demo_participants=3,
    ),
]

class Constants(BaseConstants):
    name_in_url = 'meme_experiment'
    players_per_group = 30
    num_rounds = 60
    instructions_template = '_templates/instructions.html'
    # """Amount allocated to each player"""
    endowment = 7
    multiplier = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(label='What is your age?', min=13, max=125)
    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )
    crt_bat = models.IntegerField(
        label='''
        A bat and a ball cost 22 dollars in total.
        The bat costs 20 dollars more than the ball.
        How many dollars does the ball cost?'''
    )
    crt_widget = models.IntegerField(
        label='''
        "If it takes 5 machines 5 minutes to make 5 widgets,
        how many minutes would it take 100 machines to make 100 widgets?"
        '''
    )
    crt_lake = models.IntegerField(
        label='''
        In a lake, there is a patch of lily pads.
        Every day, the patch doubles in size.
        If it takes 48 days for the patch to cover the entire lake,
        how many days would it take for the patch to cover half of the lake?
        '''
    )


/********************
* TASK-GENERAL CODE *
********************/

// Globals defined initially.
var maxblocks = 2;
var keydownfun = function() {};

// Task objects
var STIMS = new Array();

// Mutable global variables
var responsedata = [],
    currenttrial = 1,
    datastring = "",
    lastperfect = false;


/*************
* Finishing  up related stuff  *
*************/

// All pages to be loaded
var pages = [
    "1LobbyRoom3.html",
    "1LobbyRoom4.html",
    "1LobbyRoom5.html",
    "1LobbyRoom6.html",
    "1LobbyRoom7.html",
    "1LobbyRoom8.html",
    "1LobbyRoom9.html",
    "1LobbyRoom10.html", 
    "1LobbyRoom11.html",
    "1LobbyRoom12.html",
    "1LobbyRoom13.html",
    "1LobbyRoom14.html",
    "1LobbyRoom15.html",
	"instructions/instruct_0.html",
"instructions/instruct_1.html",
"instructions/instruct_2.html",
"instructions/instruct_3.html",
"instructions/instruct_4.html",
"instructions/ending.html",
	"instructions/haiku_instruct_start.html",
	"instructions/haiku_instruct_end.html",
	"instructions/instruct_break_p.html",
	"instructions/instruct_break_s.html",
	"instructions/instruct_test.html",
	"instructions/instruct_test_break.html",
	"instructions/instruct_kickout.html",
	"stage.html",
	"idquestionnaire.html",
	"primequestionnaire.html",
	"Kickout.html",
	"postquestionnaire.html",
	"stateScreen.html",
	"postquestionnaire1f.html",
	"postquestionnaire2f.html",
	"postquestionnaire3f.html",
	"postquestionnaire4f.html",
	"postquestionnaire5f.html",
	"postquestionnaire6f.html",
	"postquestionnaire7f.html",
	"postquestionnaire8f.html",
	"postquestionnaire1m.html",
	"postquestionnaire2m.html",
	"postquestionnaire3m.html",
	"postquestionnaire4m.html",
	"postquestionnaire5m.html",
	"postquestionnaire6m.html",
	"postquestionnaire7m.html",
	"postquestionnaire8m.html",
	"debriefing.html",
	"debriefing2.html",
	"addTags1.html",
	"addTags2.html",
	"addTags3.html",
	"addTags4.html",
	"addTags5.html",
	"addTags6.html",
	"addTags7.html",
	"addTags8.html",
	"addTags9.html",
	"addTags10.html",
	"addTags11.html",
	"addTags12.html",
	"addTags13.html",
	"addTags14.html",
	"addTags15.html",
	"addTags16.html",
	"addTags17.html",
	"addTags18.html",
	"addTags19.html",
	"addTags20.html",
		"addTags21.html",
			"addTags22.html",
				"addTags23.html",
					"addTags24.html",
						"addTags25.html",
							"addTags26.html",
								"addTags27.html",
									"addTags28.html",
										"addTags29.html",
											"addTags30.html",
	'SocialMediaScale1.html',
		'SocialMediaScale2.html',
				'SocialMediaScale3.html',
						'SocialMediaScale4.html',
								'SocialMediaScale5.html',
										'SocialMediaScale6.html',
												'SocialMediaScale7.html',
														'SocialMediaScale8.html',
																'SocialMediaScale9.html',	
																'socialmediaquestions.html',
																'generalcomments.html'
];

/********************
* HTML snippets
********************/
var pages = {};

var showpage = function(pagename) {
	$('body').html( pages[pagename] );
};

var pagenames = ["postquestionnaire","instruct_quiz","test"];

var is_practice = false;//'step_two'; //this is the first stage subjects pratice on....
var block_num=1;
var trial_num = 1;
var all_trials_num=1;
var class_trials_num=1;    
var nogo_record = [];
var getLikes=1;

var classification_task = 0;

var memenumbers=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180];
var feednumbers=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95];
var TagNum=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30];  
        


# FUNCTIONS
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender']


class CognitiveReflectionTest(Page):
    form_model = 'player'
    form_fields = ['crt_bat', 'crt_widget', 'crt_lake']


page_sequence = [Demographics, CognitiveReflectionTest]

# PAGES
class Introduction(Page):
    """Description of the game: How to play and returns expected"""

    pass


class Contribute(Page):
    """Player: Choose how much to contribute"""

    form_model = 'player'
    form_fields = ['contribution']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs
    body_text = "Waiting for other participants to contribute."


class Results(Page):
    """Players payoff: How much each has earned"""


page_sequence = [Introduction, Contribute, ResultsWaitPage, Results]

