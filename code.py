

########
# this file is mainly for taking notes
########

# !
# todo
# * different colors
# ? another color

# SOME UNUSED CODE but was useful to learn about it


# EmotionalStatus    = models.IntegerField(widget=widgets.RadioSelect, choices=[ [1, 'Quitebadyooo'], [2], [3], [4], [5], [6], [7, 'excellent'] ])
# EmotionalStatus   = models.IntegerField(widget=widgets.RadioSelect, choices=[ [1, 'Strongly negative'], [2, 'Negative'], [3, 'Somewhat negative'], [4, 'Neutral'], [5, 'Somewhat positive'], [6, 'Positive'], [7, 'Strongly positive'] ])
# Should emotional status be 5 or 7

# # learning how to read CSV FILES :D
# x = {
#     "n1"  : Constants.df["Likes"].values.tolist(),
#     "n2"  : Constants.df["Dislikes"].values.tolist(),
# }

# sorted_string = json.dumps(x)


# SOME STUFF FROM PAGE 1. TO MEME OR NOT TO MEME
# 

# <!--  could work but does not (taken from chris examples, quiz)
# <div>
#     <button type="button" onclick="sendClick(this)" value="Post" id="Post">
#     </button>
#     <button type="button" onclick="sendClick(this)" value="See" id="See">
#     </button>
# </div>


# <script>
#     let trialId = null;

#     function liveRecv(data) {
#         if (data.status === 'finished') {
#             document.getElementById('form').submit();
#         } else {
#             let stimulus = data.stimulus;
#             trialId = stimulus.id;

#             for (let item of ['question', 'optionA', 'optionB']) {
#                 document.getElementById(item).innerText = stimulus[item];
#             }
#         }
#     }

#     function sendClick(btn) {
#         liveSend({'choice': btn.value, 'trialId': trialId});
#     }

#     document.addEventListener("DOMContentLoaded", function (event) {
#         // send empty message to load initial question, or in case page is refreshed.
#         liveSend({});
#     });
# </script> -->