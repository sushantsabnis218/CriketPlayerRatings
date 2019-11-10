import os
import pandas as pd
import matplotlib.pyplot as plt

players=pd.read_csv('150R.csv')


# In[45]:


unretired_players=players[players.Status=='NR']


# In[46]:


odi_players_attributes=['NAME','WicketKeeping','PlayingRole','BATTING_ODIs_Mat','BATTING_ODIs_Inns','BATTING_ODIs_NO','BATTING_ODIs_Runs','BATTING_ODIs_BF','BATTING_ODIs_100','BATTING_ODIs_50','BATTING_ODIs_4s','BATTING_ODIs_6s','BATTING_ODIs_Ct','BATTING_ODIs_St','BOWLING_ODIs_','BOWLING_ODIs_Inns','BOWLING_ODIs_Balls','BOWLING_ODIs_Runs','BOWLING_ODIs_Wkts','BOWLING_ODIs_4w','BOWLING_ODIs_5w']



# In[47]:


batsman_wk_attributes=['NAME','WicketKeeping','BATTING_ODIs_Mat','BATTING_ODIs_Inns','BATTING_ODIs_NO','BATTING_ODIs_Runs','BATTING_ODIs_BF','BATTING_ODIs_100','BATTING_ODIs_50','BATTING_ODIs_4s','BATTING_ODIs_6s','BATTING_ODIs_Ct','BATTING_ODIs_St']


# In[48]:


batsmen=unretired_players[batsman_wk_attributes][unretired_players.PlayingRole=='Batsman']


# In[49]:


wicket_keepers=batsmen[batsmen.WicketKeeping=='Yes']


# In[50]:


batsmen=batsmen[batsmen.WicketKeeping=='No']


# In[51]:


bowler_attributes=['NAME','BOWLING_ODIs_Mat','BOWLING_ODIs_Inns','BOWLING_ODIs_Balls','BOWLING_ODIs_Runs','BOWLING_ODIs_Wkts','BOWLING_ODIs_4w','BOWLING_ODIs_5w']


# In[52]:


bowlers=unretired_players[bowler_attributes][unretired_players.PlayingRole=='Bowler']


# In[53]:


allrounder_attributes=['NAME','BATTING_ODIs_Mat','BATTING_ODIs_Inns','BATTING_ODIs_NO','BATTING_ODIs_Runs','BATTING_ODIs_BF','BATTING_ODIs_100','BATTING_ODIs_50','BATTING_ODIs_4s','BATTING_ODIs_6s','BATTING_ODIs_Ct','BOWLING_ODIs_Mat','BOWLING_ODIs_Inns','BOWLING_ODIs_Balls','BOWLING_ODIs_Runs','BOWLING_ODIs_Wkts','BOWLING_ODIs_4w','BOWLING_ODIs_5w']


# In[57]:


allrounders=unretired_players[allrounder_attributes][unretired_players.PlayingRole=='Allrounder']

