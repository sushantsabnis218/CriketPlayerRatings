import os
import pandas as pd
import matplotlib.pyplot as plt
from squad import *
from batsmen import *
from wicketkeeping import *
from bowlers import *
from allrounders import *
from datacleaning import *

roles=[]
names=list(squad.NAME)
bornp=[]
srbatsman=[]
ind=0
exp=[]
mtch=[]
cat=[]
stumps=[]
avgeargebo=[]
economy=[]
strikeratebo=[]
averageba=[]
strikerateba=[]
wickets=[]
totruns=[]
hundreds=[]
fifties=[]

for i in  names:
	
	wk=(unretired_players[unretired_players.NAME==i].WicketKeeping.values)[0]
	if wk=='Yes':
		role='WicketKeeper'
	else:
		role=(unretired_players[unretired_players.NAME==i].PlayingRole.values)[0]
	born=(unretired_players[unretired_players.NAME==i].Born.values)[0]
	matches=(unretired_players[unretired_players.NAME==i].BATTING_ODIs_Mat.values)[0]
	catches=(unretired_players[unretired_players.NAME==i].BATTING_ODIs_Ct.values)[0]
	stmp='NA'
	cat.append(catches)
	bornp.append(born)
	exp.append(matches)
	roles.append(role)
	#print(i,role,born,matches)
	srba='NA'
	avgba='NA'
	hunds='NA'
	fifs='NA'
	runs='NA'
	stmp='NA'
	eco='NA'
	strbo='NA'
	wkts='NA'
	avgbo='NA'
	if role=='Batsman':
		srba=(batsmen[batsmen.NAME==i].StrikeRate.values)
		srba=srba.astype(dtype=float)
		srba=float(srba[0])
		avgba=(batsmen[batsmen.NAME==i].BattingAverage.values)
		avgba=avgba.astype(dtype=float)
		avgba=float(avgba[0])
		hunds=(unretired_players[unretired_players.NAME==i].BATTING_ODIs_100.values)[0]
		fifs=(unretired_players[unretired_players.NAME==i].BATTING_ODIs_50.values)[0]
		runs=(unretired_players[unretired_players.NAME==i].BATTING_ODIs_Runs.values)[0]
		
	if role=='WicketKeeper':
		stmp=(unretired_players[unretired_players.NAME==i].BATTING_ODIs_St.values)[0]
		srba=(wicket_keepers[wicket_keepers.NAME==i].StrikeRate.values)
		srba=srba.astype(dtype=float)
		srba=float(srba[0])
		avgba=(wicket_keepers[wicket_keepers.NAME==i].BattingAverage.values)
		avgba=avgba.astype(dtype=float)
		avgba=float(avgba[0])
		hunds=(unretired_players[unretired_players.NAME==i].BATTING_ODIs_100.values)[0]
		fifs=(unretired_players[unretired_players.NAME==i].BATTING_ODIs_50.values)[0]
		runs=(unretired_players[unretired_players.NAME==i].BATTING_ODIs_Runs.values)[0]
	if role=='Bowler':
		eco=(bowlers[bowlers.NAME==i].Economy.values)
		eco=eco.astype(dtype=float)
		eco=float(eco[0])
		strbo=(bowlers[bowlers.NAME==i].StrikeRateB.values)
		strbo=strbo.astype(dtype=float)
		strbo=float(strbo[0])
		wkts=(unretired_players[unretired_players.NAME==i].BOWLING_ODIs_Wkts.values)[0]
		avgbo=(bowlers[bowlers.NAME==i].AverageB.values)
		avgbo=avgbo.astype(dtype=float)
		avgbo=float(avgbo[0])
	if role=='Allrounder':
		srba=(allrounders[allrounders.NAME==i].StrikeRate.values)
		srba=srba.astype(dtype=float)
		srba=float(srba[0])
		avgba=(allrounders[allrounders.NAME==i].Average.values)
		avgba=avgba.astype(dtype=float)
		avgba=float(avgba[0])
		hunds=(unretired_players[unretired_players.NAME==i].BATTING_ODIs_100.values)[0]
		fifs=(unretired_players[unretired_players.NAME==i].BATTING_ODIs_50.values)[0]
		runs=(unretired_players[unretired_players.NAME==i].BATTING_ODIs_Runs.values)[0]
		eco=(allrounders[allrounders.NAME==i].Economy.values)
		eco=eco.astype(dtype=float)
		eco=float(eco[0])
		strbo=(allrounders[allrounders.NAME==i].StrikeRateB.values)
		strbo=strbo.astype(dtype=float)
		strbo=float(strbo[0])
		wkts=(unretired_players[unretired_players.NAME==i].BOWLING_ODIs_Wkts.values)[0]
		avgbo=(allrounders[allrounders.NAME==i].AverageB.values)
		avgbo=avgbo.astype(dtype=float)
		avgbo=float(avgbo[0])
	strikerateba.append(srba)
	avgeargebo.append(avgbo)
	hundreds.append(hunds)
	fifties.append(fifs)
	totruns.append(runs)
	stumps.append(stmp)
	strikeratebo.append(strbo)
	wickets.append(wkts)
	averageba.append(avgba)

#squad['PlayingRole']=roles
#print(squad)
'''
print('\nNAMES:',names)
print('\nRoles:',roles)
print('\nExp:',exp)
print('\nBirth:',bornp)
print('\nCatches:',cat)
print('\nBaSR:',strikerateba)
print('\nAvgBo',avgeargebo)
print('\nHuns:',hundreds)
print('\nFifs:',fifties)
print('\nRuns',totruns)
print('\nSt:',stumps)
print('\nSRbo:',strikeratebo)
print('\nWkts:',wickets)
print('\nAvgBA:',averageba)'''

role_list_title=['Name :-','Role :-','Matches :- ','Birth Date and Place :-',' Catches:-','Batting Strike Rate:-','Bowling Average;-','Hundreds:-','Fifties:-','Runs;-','Stumpings:-','Bowling Strike Rate :-','Wickets:-','Batting Average:-']

#print(role_list_title)

'''
#print(squad)
text_var=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
for i in range(15):
  #print('NAMES:',names[i])
  text_var[i].append(list(('NAMES:',names[i])))
  #print('Roles:',roles[i])
  text_var[i].append(list(('Roles:',roles[i])))
  #print('Exp:',exp[i])
  text_var[i].append(list(('Exp:',exp[i])))
  #print('Birth:',bornp[i])
  text_var[i].append(list(('Birth:',bornp[i])))
  #print('Catches:',cat[i])
  text_var[i].append(list(('Catches:',cat[i])))
  #print('BaSR:',strikerateba[i])
  text_var[i].append(list(('BaSR:',strikerateba[i])))
  #print('AvgBo',avgeargebo[i])
  text_var[i].append(list(('AvgBo',avgeargebo[i])))
  #print('Huns:',hundreds[i])
  text_var[i].append(list(('Huns:',hundreds[i])))
  #print('Fifs:',fifties[i])
  text_var[i].append(list(('Fifs:',fifties[i])))
  #print('Runs',totruns[i])
  text_var[i].append(list(('Runs',totruns[i])))
  #print('St:',stumps[i])
  text_var[i].append(list(('St:',stumps[i])))
  #print('SRbo:',strikeratebo[i])
  text_var[i].append(list(('SRbo:',strikeratebo[i])))
  #print('Wkts:',wickets[i])
  text_var[i].append(list(('Wkts:',wickets[i])))
  #print('AvgBA:',averageba[i])
  text_var[i].append(list(('AvgBA:',averageba[i])))


print(text_var[0])
'''

text_var=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
for i in range(15):
  #print('NAMES:',names[i])
  text_var[i].append(list((role_list_title[0],names[i])))
  #print('Roles:',roles[i])
  text_var[i].append(list((role_list_title[1],roles[i])))
  #print('Exp:',exp[i])
  text_var[i].append(list((role_list_title[2],exp[i])))
  #print('Birth:',bornp[i])
  text_var[i].append(list((role_list_title[3],bornp[i])))
  #print('Catches:',cat[i])
  text_var[i].append(list((role_list_title[4],cat[i])))
  #print('BaSR:',strikerateba[i])
  text_var[i].append(list((role_list_title[5],strikerateba[i])))
  #print('AvgBo',avgeargebo[i])
  text_var[i].append(list((role_list_title[6],avgeargebo[i])))
  #print('Huns:',hundreds[i])
  text_var[i].append(list((role_list_title[7],hundreds[i])))
  #print('Fifs:',fifties[i])
  text_var[i].append(list((role_list_title[8],fifties[i])))
  #print('Runs',totruns[i])
  text_var[i].append(list((role_list_title[9],totruns[i])))
  #print('St:',stumps[i])
  text_var[i].append(list((role_list_title[10],stumps[i])))
  #print('SRbo:',strikeratebo[i])
  text_var[i].append(list((role_list_title[11],strikeratebo[i])))
  #print('Wkts:',wickets[i])
  text_var[i].append(list((role_list_title[12],wickets[i])))
  #print('AvgBA:',averageba[i])
  text_var[i].append(list((role_list_title[13],averageba[i])))

#for i1 in range(15):
#print(text_var[1])


