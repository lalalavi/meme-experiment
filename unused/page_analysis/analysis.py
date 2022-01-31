from sys import argv
from csv import DictReader, DictWriter
import pandas as pd

'''
To run this script:
python analysis.py in the terminal

'''

#################################################################################### 
# POST LATENCY
#################################################################################### 

# latency refers to the time that passes between post decisions

'''
if the player decides to post, 
then the latency is the time they spent in the decision page at the current trial 
+ all the time passed in the previous "seeing" rounds if there were any (Totaltrial variable),
after that, it needs to be reset to 0

if the player decides to see, 
then the latency increases by the time that they spent that trial.
'''

df0 = pd.read_excel('100.xlsx')
latency = 0 #Initialize variable
g = df0.groupby("id")

l_list = []
for user in g.groups: 
    df = g.get_group(user)
    for i, row in df.iterrows():
        # print(row["player.iTrialDec"], row["id"])
        if row["player.iTrialDec"] == 'Post':
            # print(user,row["player.dRTDec1"])
            l = latency + row["player.dRTDec1"] 
            l_list.append(l)
            # after this we need to reset it to 0
            latency = 0
        elif row["player.iTrialDec"] == 'See': 
            latency = latency + row["Totaltrial"]
            # df.loc[i,"LATENCY"] = latency
            l_list.append(latency)
    #     break
    # break

df0["tag.effort"]=df["player.sTag1":"player.sTag3"].apply(lambda x: 1/len(x) if len(x)!=0 else 0,axis=1)



df0["LATENCY"] = l_list
print(df0)
df0.to_excel("resultado.xlsx")
#

#################################################################################### 
# TAG EFFORT
#################################################################################### 


'''
if the player decides to post, 
...and puts no tags, then effort is 0
...and puts 1 tag, then effort is 0,33
...and puts 2 tags, then effort is 0,66
...and puts 3 tags, then effort is 1
'''


