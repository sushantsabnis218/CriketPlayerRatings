import os

import pandas as pd
import matplotlib.pyplot as plt
from datacleaning import *

Economy=[]
StrikeRateB=[]
AverageB=[]
WPI=[]
for i in bowlers.NAME:
    wickets=bowlers[bowlers.NAME==i].BOWLING_ODIs_Wkts
    runs=bowlers[bowlers.NAME==i].BOWLING_ODIs_Runs
    balls_bowled=bowlers[bowlers.NAME==i].BOWLING_ODIs_Balls
    inns=bowlers[bowlers.NAME==i].BOWLING_ODIs_Inns
    economy=(runs/balls_bowled)*6
    avgb=runs/wickets
    strikerateb=balls_bowled/wickets
    wpi=wickets/inns
    Economy.append(economy)
    StrikeRateB.append(strikerateb)
    AverageB.append(avgb)
    WPI.append(wpi)


# In[98]:


for i in range(len(WPI)):
    Economy[i]=float(Economy[i])
    StrikeRateB[i]=float(StrikeRateB[i])
    AverageB[i]=float(AverageB[i])
    WPI[i]=float(WPI[i])

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
    BowlingRating.append((EconomyRating[i]+StrikeRateBRating[i]+AverageBRating[i]-WPI_Rating[i])/4)

bowlers['WPI']=WPI
bowlers['Economy']=Economy
bowlers['AverageB']=AverageB
bowlers['StrikeRateB']=StrikeRateB
bowlers['EconomyRating']=EconomyRating
bowlers['StrikeRateBRating']=StrikeRateBRating
bowlers['AverageBRating']=AverageBRating
bowlers['WPI_Rating']=WPI_Rating
bowlers['BowlingRating']=BowlingRating

