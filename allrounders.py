import os

import pandas as pd
import matplotlib.pyplot as plt
from datacleaning import *

Average=[]
MRA=[]
StrikeRate=[]
OutRate=[]
BRPI=[]
HittingAbility=[]
Economy=[]
StrikeRateB=[]
AverageB=[]
WPI=[]
for i in allrounders.NAME:
    #for computing average
    runs=allrounders[allrounders.NAME==i].BATTING_ODIs_Runs
    nos=allrounders[allrounders.NAME==i].BATTING_ODIs_NO
    inns=allrounders[allrounders.NAME==i].BATTING_ODIs_Inns
    avg=runs/(inns-nos)
    Average.append(avg)
    #for computing MRA
    hunds=allrounders[allrounders.NAME==i].BATTING_ODIs_100
    fifs=allrounders[allrounders.NAME==i].BATTING_ODIs_50
    mra=(hunds+fifs)/inns
    MRA.append(mra)
    #for computing StrikeRate
    balls_faced=allrounders[allrounders.NAME==i].BATTING_ODIs_BF
    strikerate=100*runs/balls_faced
    StrikeRate.append(strikerate)
    #for computing OutRate
    outrate=(inns-nos)/balls_faced
    OutRate.append(outrate)
    #for computing BRPI
    fours=allrounders[allrounders.NAME==i].BATTING_ODIs_4s
    sixes=allrounders[allrounders.NAME==i].BATTING_ODIs_6s
    four_runs=(fours)*4
    six_runs=(sixes)*6
    brpi=(four_runs+six_runs)/inns
    BRPI.append(brpi)
    #for computing HittingAbility
    hitting_ability=(fours+sixes)/balls_faced
    HittingAbility.append(hitting_ability)
    #for bowling abilities
    wickets=allrounders[allrounders.NAME==i].BOWLING_ODIs_Wkts
    runs=allrounders[allrounders.NAME==i].BOWLING_ODIs_Runs
    balls_bowled=allrounders[allrounders.NAME==i].BOWLING_ODIs_Balls
    inns=allrounders[allrounders.NAME==i].BOWLING_ODIs_Inns
    economy=(runs/balls_bowled)*6
    strikerateb=balls_bowled/wickets
    avgb=runs/wickets
    wpi=wickets/inns
    Economy.append(economy)
    StrikeRateB.append(strikerateb)
    AverageB.append(avgb)
    WPI.append(wpi)


# In[20]:


for i in range(len(MRA)):
    Average[i]=float(Average[i])
    StrikeRate[i]=float(StrikeRate[i])
    MRA[i]=float(MRA[i])
    HittingAbility[i]=float(HittingAbility[i])
    BRPI[i]=float(BRPI[i])
    OutRate[i]=float(OutRate[i])
    Economy[i]=float(Economy[i])
    StrikeRateB[i]=float(StrikeRateB[i])
    WPI[i]=float(WPI[i])
    AverageB[i]=float(AverageB[i])

BattingAverageRating=[]    
MRA_Rating=[]
BRPI_Rating=[]
HittingAbilityRating=[]
OutRateRating=[]
StrikeRateRating=[]
BattingRating=[]
AllRoundersRating=[]


for i in range(len(MRA)):
    BattingAverageRating.append((Average[i])/(sum(Average)/len(Average))*100)
    MRA_Rating.append(MRA[i]/(sum(MRA)/len(MRA))*100)
    BRPI_Rating.append(BRPI[i]/(sum(BRPI)/len(BRPI))*100)
    HittingAbilityRating.append(HittingAbility[i]/(sum(HittingAbility)/len(HittingAbility))*100)
    OutRateRating.append(OutRate[i]/(sum(OutRate)/len(OutRate))*100)
    StrikeRateRating.append(StrikeRate[i]/(sum(StrikeRate)/len(StrikeRate))*100)
    
    
EconomyRating=[]
StrikeRateBRating=[]
AverageBRating=[]
WPI_Rating=[]
BowlingRating=[]

# In[99]:
for i in range(len(Economy)):
    EconomyRating.append(Economy[i]/(sum(Economy)/len(Economy))*100)
    StrikeRateBRating.append(StrikeRateB[i]/(sum(StrikeRateB)/len(StrikeRateB))*100)
    AverageBRating.append(AverageB[i]/(sum(AverageB)/len(AverageB))*100)
    WPI_Rating.append(WPI[i]/(sum(WPI)/len(WPI))*100)

for i in range(len(Economy)):
    bowlrat=((EconomyRating[i]+StrikeRateBRating[i]+AverageBRating[i]-WPI_Rating[i])/4)
    batrat=((BattingAverageRating[i]+MRA_Rating[i]+BRPI_Rating[i]+HittingAbilityRating[i]-OutRateRating[i]+StrikeRateRating[i])/6)
    BattingRating.append(batrat)
    BowlingRating.append(bowlrat)
    AllRoundersRating.append(((batrat-bowlrat)/2))


# In[21]:


allrounders['Average']=Average
allrounders['StrikeRate']=StrikeRate
allrounders['MRA']=MRA
allrounders['HittingAbility']=HittingAbility
allrounders['BRPI']=BRPI
allrounders['OutRate']=OutRate
allrounders['Economy']=Economy
allrounders['StrikeRateB']=StrikeRateB
allrounders['WPI']=WPI
allrounders['AverageB']=AverageB
allrounders['BattingAverageRating']=BattingAverageRating
allrounders['MRA_Rating']=MRA_Rating
allrounders['BRPI_Rating']=BRPI_Rating
allrounders['HittingAbilityRating']=HittingAbilityRating
allrounders['OutRateRating']=OutRateRating
allrounders['StrikeRateRating']=StrikeRateRating
allrounders['EconomyRating']=EconomyRating
allrounders['StrikeRateBRating']=StrikeRateBRating
allrounders['AverageBRating']=AverageBRating
allrounders['WPI_Rating']=WPI_Rating
allrounders['BattingRating']=BattingRating
allrounders['BowlingRating']=BowlingRating
allrounders['AllRoundersRating']=AllRoundersRating
