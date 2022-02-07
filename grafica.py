#!/usr/bin/env python
# coding: utf-8

# In[39]:



data = players_stats[players_stats['Height'].notna()]
height = data["Height"]
from statistics import mean
mean(height)

import matplotlib.pyplot as plot

plot.hist(x=height, bins=5, color='#F2AB6D', rwidth=0.85)
plot.title('Histograma de alturas')
plot.xlabel('Cm')
plot.ylabel('Frecuencia')
plot.axvline(mean(height), ymin=0, ymax=170)

plot.show() #dibujamos el histograma


# In[ ]:




