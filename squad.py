import os

import pandas as pd
import matplotlib.pyplot as plt
from batsmen import *
from wicketkeeping import *
from bowlers import *
from allrounders import *
from datacleaning import *

squad=pd.DataFrame()


# In[123]:


selected_allrounders=allrounders[['NAME','AllRoundersRating']].sort_values('AllRoundersRating',ascending=False).head(3)


# In[124]:


selected_batsmen=batsmen[['NAME','BattingRating']].sort_values('BattingRating',ascending=False).head(5)


# In[126]:


selected_wicketkeepers=wicket_keepers[['NAME','WicketKeeperRating']].sort_values('WicketKeeperRating',ascending=False).head(2)


# In[128]:


selected_bowlers=bowlers[['NAME','BowlingRating']].sort_values('BowlingRating').head(5)


# In[133]:


squad=selected_batsmen


# In[134]:


squad=squad.append(selected_allrounders,sort=False)


# In[135]:


squad=squad.append(selected_bowlers,sort=False)


# In[136]:


squad=squad.append(selected_wicketkeepers,sort=False)


# In[137]:
roles=[]
names=list(squad.NAME)

for i in  names:
    role=(unretired_players[unretired_players.NAME==i].PlayingRole.values)
    roles.append(role)
squad['PlayingRole']=roles




