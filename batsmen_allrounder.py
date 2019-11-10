import os

import pandas as pd
import matplotlib.pyplot as plt
from batsmen import *
from wicketkeeping import *
from bowlers import *
from allrounders import *
from datacleaning import *

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

graph_allrounder_as_bastmen()
