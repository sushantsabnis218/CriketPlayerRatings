
import pandas as pd
import matplotlib.pyplot as plt

players=pd.read_csv('150R.csv')
unretired_players=players[players.Status=='NR']
odi_players_attributes=['NAME','WicketKeeping','PlayingRole','BATTING_ODIs_Mat','BATTING_ODIs_Inns','BATTING_ODIs_NO','BATTING_ODIs_Runs','BATTING_ODIs_BF','BATTING_ODIs_100','BATTING_ODIs_50','BATTING_ODIs_4s','BATTING_ODIs_6s','BATTING_ODIs_Ct','BATTING_ODIs_St','BOWLING_ODIs_','BOWLING_ODIs_Inns','BOWLING_ODIs_Balls','BOWLING_ODIs_Runs','BOWLING_ODIs_Wkts','BOWLING_ODIs_4w','BOWLING_ODIs_5w']
batsman_wk_attributes=['NAME','WicketKeeping','BATTING_ODIs_Mat','BATTING_ODIs_Inns','BATTING_ODIs_NO','BATTING_ODIs_Runs','BATTING_ODIs_BF','BATTING_ODIs_100','BATTING_ODIs_50','BATTING_ODIs_4s','BATTING_ODIs_6s','BATTING_ODIs_Ct','BATTING_ODIs_St']
batsmen=unretired_players[batsman_wk_attributes][unretired_players.PlayingRole=='Batsman']
wicket_keepers=batsmen[batsmen.WicketKeeping=='Yes']
batsmen=batsmen[batsmen.WicketKeeping=='No']
bowler_attributes=['NAME','BOWLING_ODIs_Mat','BOWLING_ODIs_Inns','BOWLING_ODIs_Balls','BOWLING_ODIs_Runs','BOWLING_ODIs_Wkts','BOWLING_ODIs_4w','BOWLING_ODIs_5w']

bowlers=unretired_players[bowler_attributes][unretired_players.PlayingRole=='Bowler']
allrounder_attributes=['NAME','BATTING_ODIs_Mat','BATTING_ODIs_Inns','BATTING_ODIs_NO','BATTING_ODIs_Runs','BATTING_ODIs_BF','BATTING_ODIs_100','BATTING_ODIs_50','BATTING_ODIs_4s','BATTING_ODIs_6s','BATTING_ODIs_Ct','BOWLING_ODIs_Mat','BOWLING_ODIs_Inns','BOWLING_ODIs_Balls','BOWLING_ODIs_Runs','BOWLING_ODIs_Wkts','BOWLING_ODIs_4w','BOWLING_ODIs_5w']
allrounders=unretired_players[allrounder_attributes][unretired_players.PlayingRole=='Allrounder']


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
batsmen['OutRate']=OutRate
batsmen['BattingAverageRating']=BattingAverageRating
batsmen['BattingRating']=BattingRating



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


wicket_keepers['BattingAverage']=BattingAverage
wicket_keepers['MRA']=MRA
wicket_keepers['StrikeRate']=StrikeRate
wicket_keepers['BRPI']=BRPI
wicket_keepers['HittingAbility']=HittingAbility
wicket_keepers['OutRate']=OutRate
wicket_keepers['WKA']=WKA
wicket_keepers['BattingAverageRating']=BattingAverageRating
wicket_keepers['MRA_Rating']=MRA_Rating
wicket_keepers['BRPI_Rating']=BRPI_Rating
wicket_keepers['HittingAbilityRating']=HittingAbilityRating
wicket_keepers['OutRateRating']=OutRateRating
wicket_keepers['StrikeRateRating']=StrikeRateRating
wicket_keepers['WKA_Rating']=WKA_Rating
wicket_keepers['WicketKeeperRating']=WicketKeeperRating
# In[97]:


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




squad=pd.DataFrame()

selected_allrounders=allrounders[['NAME','AllRoundersRating']].sort_values('AllRoundersRating',ascending=False).head(3)
selected_batsmen=batsmen[['NAME','BattingRating']].sort_values('BattingRating',ascending=False).head(5)
selected_wicketkeepers=wicket_keepers[['NAME','WicketKeeperRating']].sort_values('WicketKeeperRating',ascending=False).head(2)
selected_bowlers=bowlers[['NAME','BowlingRating']].sort_values('BowlingRating').head(5)
squad=selected_batsmen
squad=squad.append(selected_allrounders,sort=False)
squad=squad.append(selected_bowlers,sort=False)
squad=squad.append(selected_wicketkeepers,sort=False)



# In[137]:
roles=[]
names=list(squad.NAME)

for i in  names:
    role=unretired_players[unretired_players.NAME==i].PlayingRole.values
    roles.append(role)
squad['PlayingRole']=roles

