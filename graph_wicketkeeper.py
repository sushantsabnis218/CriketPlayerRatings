import pandas as pd
import matplotlib.pyplot as plt
from wicketkeeping import *

def graph_wicketkeepers():
    wicketkeepers_name=list(wicket_keepers.NAME)

    mra_listforplot=[]
    avg_listforplot=[]
    stk_listforplot=[]
    brpi_listforplot=[]
    wka_listforplot=[]
    
    for i in wicketkeepers_name:
        mra_listforplot.append(float(wicket_keepers[wicket_keepers.NAME==i].MRA_Rating))
        avg_listforplot.append(float(wicket_keepers[wicket_keepers.NAME==i].BattingAverageRating))
        stk_listforplot.append(float(wicket_keepers[wicket_keepers.NAME==i].StrikeRateRating))
        brpi_listforplot.append(float(wicket_keepers[wicket_keepers.NAME==i].BRPI_Rating))
        wka_listforplot.append(float(wicket_keepers[wicket_keepers.NAME==i].WKA_Rating))
    bar3=[]
    bar4=[]
    bar5=[]
    for i in range(len(mra_listforplot)):
    	bar3.append(avg_listforplot[i]+mra_listforplot[i])
    	bar4.append(bar3[i]+stk_listforplot[i])
    	bar5.append(bar4[i]+brpi_listforplot[i])

    plt.bar(wicketkeepers_name,wka_listforplot,label='WKA Rating',color="c",bottom=bar5)
    plt.bar(wicketkeepers_name,brpi_listforplot,label='BRPI Rating',color='y',bottom=bar4)
    plt.bar(wicketkeepers_name,stk_listforplot,label='Strike Rate Rating',color='g',bottom=bar3)
    plt.bar(wicketkeepers_name,mra_listforplot,label='MRA_Rating',color='r',bottom=avg_listforplot)
    plt.bar(wicketkeepers_name,avg_listforplot,label='Average_Rating',color='b')
    plt.title('WicketKeepers Statistical Attributes Rating')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()


graph_wicketkeepers()

