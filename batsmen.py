import os

import pandas as pd
import matplotlib.pyplot as plt

from datacleaning import *


BattingAverage=[]
MRA=[]
StrikeRate=[]
BRPI=[]
OutRate=[]
HittingAbility=[]
for i in batsmen.NAME:
    #for computing average
    runs=batsmen[batsmen.NAME==i].BATTING_ODIs_Runs
    nos=batsmen[batsmen.NAME==i].BATTING_ODIs_NO
    inns=batsmen[batsmen.NAME==i].BATTING_ODIs_Inns
    avg=float(runs)/(float(inns)-float(nos))
    BattingAverage.append(avg)
    #for computing MRA
    hunds=batsmen[batsmen.NAME==i].BATTING_ODIs_100
    fifs=batsmen[batsmen.NAME==i].BATTING_ODIs_50
    mra=(hunds+fifs)/inns
    MRA.append(mra)
    #for computing StrikeRate
    balls_faced=batsmen[batsmen.NAME==i].BATTING_ODIs_BF
    strikerate=100*runs/balls_faced
    StrikeRate.append(strikerate)
    #for computing OutRate
    outrate=(inns-nos)/balls_faced
    OutRate.append(outrate)
    #for computing BRPI
    fours=batsmen[batsmen.NAME==i].BATTING_ODIs_4s
    sixes=batsmen[batsmen.NAME==i].BATTING_ODIs_6s
    four_runs=(fours)*4
    six_runs=(sixes)*6
    brpi=(four_runs+six_runs)/inns
    BRPI.append(brpi)
    #for computing HittingAbility
    hitting_ability=(fours+sixes)/balls_faced
    HittingAbility.append(hitting_ability)
    #for wicketkeepingability

    


# In[71]:


for i in range(len(MRA)):
    BattingAverage[i]=float(BattingAverage[i])
    StrikeRate[i]=float(StrikeRate[i])
    MRA[i]=float(MRA[i])
    OutRate[i]=float(OutRate[i])
    BRPI[i]=float(BRPI[i])
    HittingAbility[i]=float(HittingAbility[i])

BattingAverageRating=[]    
MRA_Rating=[]
BRPI_Rating=[]
HittingAbilityRating=[]
OutRateRating=[]
StrikeRateRating=[]
BattingRating=[]

for i in range(len(MRA)):
    BattingAverageRating.append((BattingAverage[i])/(sum(BattingAverage)/len(BattingAverage))*100)
    MRA_Rating.append(MRA[i]/(sum(MRA)/len(MRA))*100)
    BRPI_Rating.append(BRPI[i]/(sum(BRPI)/len(BRPI))*100)
    HittingAbilityRating.append(HittingAbility[i]/(sum(HittingAbility)/len(HittingAbility))*100)
    OutRateRating.append(OutRate[i]/(sum(OutRate)/len(OutRate))*100)
    StrikeRateRating.append(StrikeRate[i]/(sum(StrikeRate)/len(StrikeRate))*100)
    
    
for i in range(len(MRA)):
    BattingRating.append((BattingAverageRating[i]+MRA_Rating[i]+BRPI_Rating[i]+HittingAbilityRating[i]-OutRateRating[i]+StrikeRateRating[i])/6)
# In[72]:


batsmen['BattingAverageRating']=BattingAverageRating
batsmen['MRA_Rating']=MRA_Rating
batsmen['BRPI_Rating']=BRPI_Rating
batsmen['HittingAbilityRating']=HittingAbilityRating
batsmen['OutRateRating']=OutRateRating
batsmen['StrikeRateRating']=StrikeRateRating
batsmen['BattingAverage']=BattingAverage
batsmen['MRA']=MRA
batsmen['StrikeRate']=StrikeRate
batsmen['BRPI']=BRPI
batsmen['HittingAbility']=HittingAbility
batsmen['OutRtdate']=OutRate
batsmen['BattingAverageRating']=BattingAverageRating
batsmen['BattingRating']=BattingRating



