

########
# this file is mainly for taking notes
########

# !
# todo
# * different colors
# ? another color

# SOME UNUSED CODE but was useful to learn about it

#   <img src="{{ static image_path }}"/>

# EmotionalStatus   = models.IntegerField(widget=widgets.RadioSelect, choices=[ [1, 'Quitebadyooo'], [2], [3], [4], [5], [6], [7, 'excellent'] ])
# EmotionalStatus   = models.IntegerField(widget=widgets.RadioSelect, choices=[ [1, 'Strongly negative'], [2, 'Negative'], [3, 'Somewhat negative'], [4, 'Neutral'], [5, 'Somewhat positive'], [6, 'Positive'], [7, 'Strongly positive'] ])
# Should emotional status be 5 or 7

# # learning how to read CSV FILES :D
# x = {
#     "n1"  : Constants.df["Likes"].values.tolist(),
#     "n2"  : Constants.df["Dislikes"].values.tolist(),
# }

# sorted_string = json.dumps(x)

# set vectors
# let numbers = js_vars.sorted_string;
# let vButtons = document.getElementsByClassName('lol').getAttribute("src");  

# SOME STUFF FROM PAGE 1. TO MEME OR NOT TO MEME
# 

# <!--  could work but does not (taken from chris examples, quiz)
# <div>
#     <button type="button" onclick="sendClick(this)" value="Post" id="Post">
#     </button>
#     <button type="button" onclick="sendClick(this)" value="See" id="See">
#     </button>
# </div

#  {{ if past_players.iTrialDec == "Post" }} 
        #     {{ include Constants.history_template }}
        # {{ endif }}

#  <div class="img-wrapper">
 # <img id='lastp' src= {{ static Image }} style="width:100%"/>
        

#   <div><img id='??' src= {{ static Image }} /></div>

# <td><div><img src= "{{ static Image }}" style="width:100%"></div></td>  !!!

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

# <script>
# 	// let white = js_vars.white;
#     // let heart = js_vars.heart;

# 	// emptyHeart=R.image(white).attr({"height":"90","width":"90","x":100,"y":295});
# 	// emptyHeart=R.image("white").attr({"height":"90","width":"90","x":200,"y":295});
# 	// emptyHeart=R.image(white).attr({"height":"90","width":"90","x":300,"y":295});
# 	// emptyHeart=R.image(white).attr({"height":"90","width":"90","x":400,"y":295});
# 	// emptyHeart=R.image(white).attr({"height":"90","width":"90","x":500,"y":295});
# 	// emptyHeart=R.image(white).attr({"height":"90","width":"90","x":600,"y":295});
# 	// emptyHeart=R.image(white).attr({"height":"90","width":"90","x":700,"y":295});
# 	// emptyHeart=R.image(white).attr({"height":"90","width":"90","x":800,"y":295});
# 	// emptyHeart=R.image(white).attr({"height":"90","width":"90","x":900,"y":295});
# 	// emptyHeart=R.image(white).attr({"height":"90","width":"90","x":1000,"y":295});

# 	// emptyHeart=R.image(white).attr({"height":"90","width":"90","x":145,"y":425});
# 	// emptyHeart=R.image(white).attr({"height":"90","width":"90","x":245,"y":425});
# 	// emptyHeart=R.image(white).attr({"height":"90","width":"90","x":345,"y":425});
# 	// emptyHeart=R.image(white).attr({"height":"90","width":"90","x":445,"y":425});
# 	// emptyHeart=R.image(white).attr({"height":"90","width":"90","x":545,"y":425});
# 	// emptyHeart=R.image(white).attr({"height":"90","width":"90","x":645,"y":425});
# 	// emptyHeart=R.image(white).attr({"height":"90","width":"90","x":745,"y":425});
# 	// emptyHeart=R.image(white).attr({"height":"90","width":"90","x":845,"y":425});
# 	// emptyHeart=R.image(white).attr({"height":"90","width":"90","x":945,"y":425});


# 	// if(iLikes>0){setTimeout( function(){var Like=R.image(heart).attr({fill: "#900", stroke: "#000", "stroke-width": 1, "height":"90","width":"90","x":100,"y":295});},400);} //Lay a Heart over the Meme if Liked
# 	// if(iLikes>1){setTimeout( function(){var Like=R.image("heart").attr({"height":"90","width":"90","x":200,"y":295});},700);
# 	// }
# 	// if(iLikes>2){setTimeout( function(){var Like=R.image(heart).attr({"height":"90","width":"90","x":300,"y":295});},1000); 
# 	// }if(iLikes>3){setTimeout( function(){var Like=R.image(heart).attr({"height":"90","width":"90","x":400,"y":295});},1300); 
# 	// }
# 	// if(iLikes>4){setTimeout( function(){var Like=R.image(heart).attr({"height":"90","width":"90","x":500,"y":295});},1600); 
# 	// }
# 	// if(iLikes>5){setTimeout( function(){var Like=R.image(heart).attr({"height":"90","width":"90","x":600,"y":295});},1900); 
# 	// }
# 	// if(iLikes>6){setTimeout( function(){var Like=R.image(heart).attr({"height":"90","width":"90","x":700,"y":295});},2200); 
# 	// }
# 	// if(iLikes>7){setTimeout( function(){var Like=R.image(heart).attr({"height":"90","width":"90","x":800,"y":295});},2500); 
# 	// }
# 	// if(iLikes>8){setTimeout( function(){var Like=R.image(heart).attr({"height":"90","width":"90","x":900,"y":295});},2800); 
# 	// }
# 	// if(iLikes>9){setTimeout( function(){var Like=R.image(heart).attr({"height":"90","width":"90","x":1000,"y":295});},3100); 
# 	// }
# 	// if(iLikes>10){setTimeout( function(){var Like=R.image(heart).attr({"height":"90","width":"90","x":145,"y":425});},3400); 
# 	// }
# 	// if(iLikes>11){setTimeout( function(){var Like=R.image(heart).attr({"height":"90","width":"90","x":245,"y":425});},3700); 
# 	// }
# 	// if(iLikes>12){setTimeout( function(){var Like=R.image(heart).attr({"height":"90","width":"90","x":345,"y":425});},4000); 
# 	// }
# 	// if(iLikes>13){setTimeout( function(){var Like=R.image(heart).attr({"height":"90","width":"90","x":445,"y":425});},4300); 
# 	// }
# 	// if(iLikes>14){setTimeout( function(){var Like=R.image(heart).attr({"height":"90","width":"90","x":545,"y":425});},4600); 
# 	// }
# 	// if(iLikes>15){setTimeout( function(){var Like=R.image(heart).attr({"height":"90","width":"90","x":645,"y":425});},4900); 
# 	// }
# 	// if(iLikes>16){setTimeout( function(){var Like=R.image(heart).attr({"height":"90","width":"90","x":745,"y":425});},5200); 
# 	// }
# 	// if(iLikes>17){setTimeout( function(){var Like=R.image(heart).attr({"height":"90","width":"90","x":845,"y":425});},5500); 
# 	// }
# 	// if(iLikes>18){setTimeout( function(){var Like=R.image(heart).attr({fill: "#900", stroke: "#000", "stroke-width": 1, "height":"90","width":"90","x":945,"y":425});},5800); 
# 	// }