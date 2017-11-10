# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 16:54:58 2017

@author: dacrands
"""

import re
import pandas as pd
from pandas import DataFrame


def col_cleaner(arr):
    
    """
    In: array of strs containing numerical characters delimited by commas and
    NaN values (i.e., a Wikipedia table column)
    Out: array of ints
    """
    
    newList = list()
    for i in arr:
        if type(i) is str:
            newList.append(int(re.compile(r'\d{2,}').
                               search(i.replace(',', '')).group()))
        else:
            newList.append(0)

    return newList


#Scrape the wikipedia pages, create, rename, orgranize dframes
url = 'https://en.wikipedia.org/wiki/World_War_I_casualties'
ww1_data = pd.io.html.read_html(url)
dframe = DataFrame(ww1_data[0])
dframe = dframe[2:]
dframe = dframe.rename(columns={
                              0: 'countries',
                              1: 'pop',
                              2: 'dead/MIA',
                              3: 'allDead',
                              4: 'civisDead',
                              5: 'civisIndirectDead',
                              6: 'TotDeaths',
                              7: 'DeadPop%',
                              8: 'miliWounded'
                              })
dframe = dframe.transpose()

power_frame = dframe[[21, 14, 8, 24, 12, 19, 26, 27]]
power_frame = power_frame.transpose()

power_frame['dead/MIA'] = col_cleaner(power_frame['dead/MIA'])
power_frame['allDead'] = col_cleaner(power_frame['allDead'])
power_frame['civisDead'] = col_cleaner(power_frame['civisDead'])
power_frame['TotDeaths'] = col_cleaner(power_frame['TotDeaths'])

power_frame['countries'] = [
                           'USA',
                           'Italy',
                           'UK',
                           'Aus-Hung',
                           'France',
                           'Russia',
                           'Germany',
                           'Ottoman'
                           ]

civi_frame = power_frame.transpose()
civi_frame = civi_frame[[21, 26, 14, 8, 12, 24, 19, 27]]
civi_frame = civi_frame.transpose()

mili_frame = power_frame.transpose()
mili_frame = mili_frame[[21, 27, 14, 8, 24, 12, 19, 26]]
mili_frame = mili_frame.transpose()
