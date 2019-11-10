import pandas as pd
import matplotlib.pyplot as plt
from wicketkeeping import *

print('doing somthing')
names=list(wicket_keepers.NAME)
ratings=list(wicket_keepers.WicketKeeperRating)

plt.bar(names,ratings,color='b')
plt.title('WicketKeeperRating')
plt.xticks(rotation=45)
plt.show()




