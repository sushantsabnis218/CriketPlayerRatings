import pandas as pd
import matplotlib.pyplot as plt
from batsmen import *

print('doing somthing')
names=list(batsmen.NAME)
ratings=list(batsmen.BattingRating)

plt.bar(names,ratings,color='y')
plt.title('Batsmen Ratings')
plt.xticks(rotation=70)
plt.show()




