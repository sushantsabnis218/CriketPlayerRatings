import os

import pandas as pd
import matplotlib.pyplot as plt
from batsmen import *
from wicketkeeping import *
from bowlers import *
from allrounders import *
from datacleaning import *

#graphs for allrounders as bowler
def graph_allrounder_as_bowler():
    allrounders_name=list(allrounders.NAME)

    eco_listforplot=[]
    stkb_listforplot=[]
    avgb_listforplot=[]
    wpi_listforplot=[]

    for i in allrounders_name:
        eco_listforplot.append(float(allrounders[allrounders.NAME==i].EconomyRating))
        stkb_listforplot.append(float(allrounders[allrounders.NAME==i].StrikeRateBRating))
        avgb_listforplot.append(float(allrounders[allrounders.NAME==i].AverageBRating))
        wpi_listforplot.append(float(allrounders[allrounders.NAME==i].WPI_Rating))

        
    bar3=[]
    bar4=[]

    for i in range(len(eco_listforplot)):
    	bar3.append(eco_listforplot[i]+stkb_listforplot[i])
    	bar4.append(bar3[i]+avgb_listforplot[i])

        
    plt.bar(allrounders_name,wpi_listforplot,label='WPI_Rating',color='y',bottom=bar4)
    plt.bar(allrounders_name,avgb_listforplot,label='AverageBRating',color='g',bottom=bar3)
    plt.bar(allrounders_name,stkb_listforplot,label='StrikeRateBRating',color='r',bottom=eco_listforplot)
    plt.bar(allrounders_name,eco_listforplot,label='Economy',color='b')

    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

graph_allrounder_as_bowler()

