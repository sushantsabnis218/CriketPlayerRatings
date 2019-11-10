import pandas as pd
import matplotlib.pyplot as plt
from bowlers import *

names=list(bowlers.NAME)
ratings=list(bowlers.BowlingRating)

plt.bar(names,ratings,color='b')
plt.title('Bowling Ratings')
plt.xticks(rotation=70)
plt.show()




