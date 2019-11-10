import pandas as pd
import matplotlib.pyplot as plt
from bowlers import *
from datacleaning import *

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

graph_bowler()


