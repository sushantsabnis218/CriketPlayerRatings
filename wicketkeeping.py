import os

import pandas as pd
import matplotlib.pyplot as plt

from datacleaning import *
from batsmen import *

BattingAverage=[]
MRA=[]
StrikeRate=[]
BRPI=[]
OutRate=[]
HittingAbility=[]
WKA=[]     #for wicketkeepingability
for i in wicket_keepers.NAME:
    #for computing average
    runs=wicket_keepers[wicket_keepers.NAME==i].BATTING_ODIs_Runs
    nos=wicket_keepers[wicket_keepers.NAME==i].BATTING_ODIs_NO
    inns=wicket_keepers[wicket_keepers.NAME==i].BATTING_ODIs_Inns
    avg=runs/(inns-nos)
    BattingAverage.append(avg)
    #for computing MRA
    hunds=wicket_keepers[wicket_keepers.NAME==i].BATTING_ODIs_100
    fifs=wicket_keepers[wicket_keepers.NAME==i].BATTING_ODIs_50
    mra=(hunds+fifs)/inns
    MRA.append(mra)
    #for computing StrikeRate
    balls_faced=wicket_keepers[wicket_keepers.NAME==i].BATTING_ODIs_BF
    strikerate=100*runs/balls_faced
    StrikeRate.append(strikerate)
    #for computing OutRate
    outrate=(inns-nos)/balls_faced
    OutRate.append(outrate)
    #for computing BRPI
    fours=wicket_keepers[wicket_keepers.NAME==i].BATTING_ODIs_4s
    sixes=wicket_keepers[wicket_keepers.NAME==i].BATTING_ODIs_6s
    four_runs=(fours)*4
    six_runs=(sixes)*6
    brpi=(four_runs+six_runs)/inns
    BRPI.append(brpi)
    #for computing HittingAbility
    hitting_ability=(fours+sixes)/balls_faced
    HittingAbility.append(hitting_ability)
    #for computing wka
    catches=wicket_keepers[wicket_keepers.NAME==i].BATTING_ODIs_Ct
    stumpings=wicket_keepers[wicket_keepers.NAME==i].BATTING_ODIs_St
    matches=wicket_keepers[wicket_keepers.NAME==i].BATTING_ODIs_Mat
    wka=(catches+stumpings)/matches
    WKA.append(wka)
 


# In[90]:


for i in range(len(MRA)):
    BattingAverage[i]=float(BattingAverage[i])
    StrikeRate[i]=float(StrikeRate[i])
    MRA[i]=float(MRA[i])
    OutRate[i]=float(OutRate[i])
    BRPI[i]=float(BRPI[i])
    HittingAbility[i]=float(HittingAbility[i])
    WKA[i]=float(WKA[i])

BattingAverageRating=[]    
MRA_Rating=[]
BRPI_Rating=[]
HittingAbilityRating=[]
OutRateRating=[]
StrikeRateRating=[]
WKA_Rating=[]
WicketKeeperRating=[]

for i in range(len(MRA)):
    BattingAverageRating.append((BattingAverage[i])/(sum(BattingAverage)/len(BattingAverage))*100)
    MRA_Rating.append(MRA[i]/(sum(MRA)/len(MRA))*100)
    BRPI_Rating.append(BRPI[i]/(sum(BRPI)/len(BRPI))*100)
    HittingAbilityRating.append(HittingAbility[i]/(sum(HittingAbility)/len(HittingAbility))*100)
    OutRateRating.append(OutRate[i]/(sum(OutRate)/len(OutRate))*100)
    StrikeRateRating.append(StrikeRate[i]/(sum(StrikeRate)/len(StrikeRate))*100)
    WKA_Rating.append(WKA[i]/(sum(WKA)/len(WKA))*100)
    
    
for i in range(len(MRA)):
    WicketKeeperRating.append((BattingAverageRating[i]+MRA_Rating[i]+BRPI_Rating[i]+HittingAbilityRating[i]-OutRateRating[i]+StrikeRateRating[i]+WKA_Rating[i])/7)

# In[91]:


wicket_keepers['BattingAverage']=BattingAverage  # Average of Battting
wicket_keepers['MRA']=MRA # mile  stone reaching ability kiti kheli shakto
wicket_keepers['StrikeRate']=StrikeRate
wicket_keepers['BRPI']=BRPI# Boundry rate per inning
wicket_keepers['HittingAbility']=HittingAbility # six and four 
wicket_keepers['OutRate']=OutRate # negative attribute 
wicket_keepers['WKA']=WKA # wicket keeping ability
wicket_keepers['BattingAverageRating']=BattingAverageRating # ratiing 
wicket_keepers['MRA_Rating']=MRA_Rating
wicket_keepers['BRPI_Rating']=BRPI_Rating
wicket_keepers['HittingAbilityRating']=HittingAbilityRating
wicket_keepers['OutRateRating']=OutRateRating
wicket_keepers['StrikeRateRating']=StrikeRateRating
wicket_keepers['WKA_Rating']=WKA_Rating
wicket_keepers['WicketKeeperRating']=WicketKeeperRating
