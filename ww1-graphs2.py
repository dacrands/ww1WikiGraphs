# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 23:41:44 2017

@author: dacrands
"""
import re
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import matplotlib as mpl
from pandas import DataFrame
mpl.rcParams['patch.force_edgecolor'] = True
  
def col_cleaner(lst):
    
    """Uses regex to attain lower-bounds of cols by converting strs to ints"""
    
    newList=[]
    
    for i in lst:
        
        if type(i) is str:
            newList.append(int(re.compile(r'\d{2,}').search(i.replace(',','')).group()))

        else:
            newList.append(0)
            
    return newList 

"""
Scrape the wikipedia pages, rename, orgranize, create dframes
"""

url = 'https://en.wikipedia.org/wiki/World_War_I_casualties'
ww1_data = pd.io.html.read_html(url)
dframe = DataFrame(ww1_data[0])
dframe = dframe[2:]
dframe = dframe.rename(columns={0:'countries',
                              1:'pop',
                              2:'dead/MIA',
                              3:'allDead',
                              4:'civisDead',
                              5:'civisIndirectDead',
                              6:'TotDeaths',
                              7:'DeadPop%',
                              8:'miliWounded'
                               })
dframe = dframe.transpose()

power_frame = dframe[[21,14,8,24,12,19,26,27]]
power_frame = power_frame.transpose()
power_frame['dead/MIA'] = col_cleaner(power_frame['dead/MIA'])
power_frame['allDead'] = col_cleaner(power_frame['allDead'])
power_frame['civisDead'] = col_cleaner(power_frame['civisDead'])
power_frame['TotDeaths'] = col_cleaner(power_frame['TotDeaths'])
power_frame['countries'] = ['USA',
                           'Italy',
                           'UK',
                           'Aus-Hung',
                           'France',
                           'Russia',
                           'Germany',
                           'Ottoman'
                           ]

civi_frame = power_frame.transpose()
civi_frame = civi_frame[[21,26,14,8,12,24,19,27]]
civi_frame = civi_frame.transpose()

mili_frame = power_frame.transpose()
mili_frame = mili_frame[[21,27,14,8,24,12,19,26]]
mili_frame = mili_frame.transpose()

"""
Set the matplotib params, create the military and civlian graphs,
save them as PNG files.

"""

sb.set(font_scale=1.6)
plt.rcParams['axes.titlepad'] = 25
plt.rcParams["axes.labelsize"] = 24
plt.rcParams["axes.labelpad"] = 10  
plt.rcParams['axes.facecolor'] = '#cecacb'
plt.rcParams['font.family'] = 'Times New Roman'

# Civilian Graph
civi_graph = sb.factorplot(x ='civisDead',
                           y ='countries',
                           data=civi_frame,
                           size=7, 
                           aspect=1.5,
                           kind="bar",
                           alpha=0.7,
                           palette="Reds"
                          )

plt.title("WWI Civilian Casualties",
          fontsize=40,
          fontweight='heavy')

civi_graph.set_ylabels("Countries", fontweight='bold')

civi_graph.set_xlabels("Civillian Deaths (in millions)", fontweight='bold')

plt.yticks(rotation=17)

plt.ticklabel_format(style='sci', 
                     axis='x', 
                     scilimits=(0,1)
                    )

sb.despine(left=True, bottom=True)

# Military graph
mili_graph = sb.factorplot(x='dead/MIA',
                           y='countries',
                           data=mili_frame,
                           size=7, 
                           aspect=1.5, 
                           kind="bar",
                           palette="Blues",
                           alpha=0.7
                          )

plt.title("WWI Military Casualties",
          fontsize=40,
          fontweight="heavy"
         )

mili_graph.set_ylabels("Countries", fontweight="bold")

mili_graph.set_xlabels("Military Deaths (in Millions)",
                       fontweight="bold"
                      )

plt.yticks(rotation=16)

plt.ticklabel_format(style='sci', 
                     axis='x', 
                     scilimits=(0,5)
                    )

sb.despine(left=True, bottom=True)

civi_graph.savefig("civi-graph2.png")
mili_graph.savefig("mili-graph2.png")
