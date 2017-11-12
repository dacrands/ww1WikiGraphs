# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 23:41:44 2017

@author: dacrands
"""
import seaborn as sb
import matplotlib.pyplot as plt
import matplotlib as mpl
from ww1wikidata import civi_frame, mili_frame
mpl.rcParams['patch.force_edgecolor'] = True

sb.set(font_scale=1.6)
plt.rcParams['axes.titlepad'] = 25
plt.rcParams["axes.labelsize"] = 24
plt.rcParams["axes.labelpad"] = 10
plt.rcParams['axes.facecolor'] = '#e3e5e8'
plt.rcParams['font.family'] = 'Times New Roman'

# Civilian Graph
civi_graph = sb.factorplot(x='civisDead', y='countries', data=civi_frame,
                           size=7, aspect=1.5, kind="bar",
                           alpha=0.7, palette="Reds")

plt.title("WWI Civilian Casualties", fontsize=40)
civi_graph.set_ylabels("Countries" )
civi_graph.set_xlabels("Civillian Deaths (in millions)")
plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 1))
plt.yticks(rotation=17)
sb.despine(left=True, bottom=True)

# Military graph
mili_graph = sb.factorplot(x='dead/MIA', y='countries', data=mili_frame,
                           size=7, aspect=1.5, kind="bar",
                           palette="Blues", alpha=0.7)

plt.title("WWI Military Casualties", fontsize=40)
mili_graph.set_ylabels("Countries")
mili_graph.set_xlabels("Military Deaths (in Millions)")
plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 5))
plt.yticks(rotation=16)
sb.despine(left=True, bottom=True)

civi_graph.savefig("civi-graph.png")
mili_graph.savefig("mili-graph.png")
