
import os

import pandas as pd
import matplotlib.pyplot as plt
from batsmen import *
from wicketkeeping import *
from bowlers import *
from allrounders import *
from datacleaning import *




def graph_batsmen():
    batsmen_name=list(batsmen.NAME)

    mra_listforplot=[]
    avg_listforplot=[]
    stk_listforplot=[]
    brpi_listforplot=[]
    
    for i in batsmen_name:
        mra_listforplot.append(float(batsmen[batsmen.NAME==i].MRA_Rating))
        avg_listforplot.append(float(batsmen[batsmen.NAME==i].BattingAverageRating))
        stk_listforplot.append(float(batsmen[batsmen.NAME==i].StrikeRateRating))
        brpi_listforplot.append(float(batsmen[batsmen.NAME==i].BRPI_Rating))

    bar3=[]
    bar4=[]
    
    for i in range(len(mra_listforplot)):
    	bar3.append(mra_listforplot[i]+avg_listforplot[i])
    	bar4.append(bar3[i]+stk_listforplot[i])
    	
    plt.bar(batsmen_name,brpi_listforplot,label='BRPI Rating',color='y',bottom=bar4)
    plt.bar(batsmen_name,stk_listforplot,label='Strike Rate Rating',color='g',bottom=bar3)
    plt.bar(batsmen_name,mra_listforplot,label='MRA_Rating',color='r',bottom=avg_listforplot)
    plt.bar(batsmen_name,avg_listforplot,label='Average_Rating',color='b')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

#graphs for allrounders as bastmen
def graph_allrounder_as_bastmen():
    allrounders_name=list(allrounders.NAME)

    mra_listforplot=[]
    avg_listforplot=[]
    stk_listforplot=[]
    brpi_listforplot=[]

    for i in allrounders_name:
        mra_listforplot.append(float(allrounders[allrounders.NAME==i].MRA_Rating))
        avg_listforplot.append(float(allrounders[allrounders.NAME==i].BattingAverageRating))
        stk_listforplot.append(float(allrounders[allrounders.NAME==i].StrikeRateRating))
        brpi_listforplot.append(float(allrounders[allrounders.NAME==i].BRPI_Rating))

    bar3=[]
    bar4=[]

    for i in range(len(mra_listforplot)):
    	bar3.append(mra_listforplot[i]+avg_listforplot[i])
    	bar4.append(bar3[i]+stk_listforplot[i])

    plt.bar(allrounders_name,brpi_listforplot,label='BRPI Rating',color='y',bottom=bar4)
    plt.bar(allrounders_name,stk_listforplot,label='Strike Rate Rating',color='g',bottom=bar3)
    plt.bar(allrounders_name,mra_listforplot,label='MRA_Rating',color='r',bottom=avg_listforplot)
    plt.bar(allrounders_name,avg_listforplot,label='Average_Rating',color='b')

    plt.xticks(rotation=45)
    plt.legend()
    plt.show()


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



#graph for bowlers
def graph_bowler():
    bowlers_name=list(bowlers.NAME)

    eco_listforplot=[]
    stkb_listforplot=[]
    avgb_listforplot=[]
    wpi_listforplot=[]

    for i in bowlers_name:
        eco_listforplot.append(float(bowlers[bowlers.NAME==i].EconomyRating))
        stkb_listforplot.append(float(bowlers[bowlers.NAME==i].StrikeRateBRating))
        avgb_listforplot.append(float(bowlers[bowlers.NAME==i].AverageBRating))
        wpi_listforplot.append(float(bowlers[bowlers.NAME==i].WPI_Rating))

        
    bar3=[]
    bar4=[]

    for i in range(len(eco_listforplot)):
        bar3.append(eco_listforplot[i]+stkb_listforplot[i])
        bar4.append(bar3[i]+avgb_listforplot[i])

        
    plt.bar(bowlers_name,wpi_listforplot,label='WPI_Rating',color='y',bottom=bar4)
    plt.bar(bowlers_name,avgb_listforplot,label='AverageBRating',color='g',bottom=bar3)
    plt.bar(bowlers_name,stkb_listforplot,label='StrikeRateBRating',color='r',bottom=eco_listforplot)
    plt.bar(bowlers_name,eco_listforplot,label='Economy',color='b')

    plt.xticks(rotation=90)
    plt.legend()
    plt.show()




graph_batsmen()
graph_bowler()
graph_allrounder_as_bowler()
graph_allrounder_as_bastmen()
