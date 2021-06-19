#!/usr/bin/env python
# coding: utf-8

# In[6]:


pip install mplsoccer


# In[5]:


import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer.pitch import Pitch
import seaborn as sns


# In[6]:


#Leggi i dati
df = pd.read_csv('https://raw.githubusercontent.com/mckayjohns/passmap/main/messibetis.csv')


# In[7]:


df['x'] = df['x']*1.2
df['y'] = df['y']*.8
df['endX'] = df['endX']*1.2
df['endY'] = df['endY']*.8


# In[8]:


df.head(10)


# In[9]:


fig ,ax = plt.subplots(figsize=(13.5,8))
fig.set_facecolor('#22312b')
ax.patch.set_facecolor('#22312b')


pitch = Pitch(pitch_type='statsbomb', orientation='horizontal',
              pitch_color='#22312b', line_color='#c7d5cc', figsize=(13, 8),
              constrained_layout=False, tight_layout=True)


pitch.draw(ax=ax)
plt.gca().invert_yaxis()

#Heatmap
kde = sns.kdeplot(
        df['x'],
        df['y'],
        shade = True,
        shade_lowest=False,
        alpha=.5,
        n_levels=10,
        cmap = 'magma'
)


#loop per ogni passaggio
for x in range(len(df['x'])):
    if df['outcome'][x] == 'Successful':
        plt.plot((df['x'][x],df['endX'][x]),(df['y'][x],df['endY'][x]),color='green')
        plt.scatter(df['x'][x],df['y'][x],color='green')
    if df['outcome'][x] == 'Unsuccessful':
        plt.plot((df['x'][x],df['endX'][x]),(df['y'][x],df['endY'][x]),color='red')
        plt.scatter(df['x'][x],df['y'][x],color='red')
        
plt.xlim(0,120)
plt.ylim(0,80)

plt.title('Mappa passaggi Messi vs RealBetis',color='white',size=20)

