# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 17:39:19 2021

@author: rober
"""

import json
import pandas as pd

from pandas.io.json import json_normalize




villes = pd.read_json('C://Users//rober//OneDrive//Documents//test_ggmap//city.list.json',
   convert_dates=True)

villes_france = villes[villes["country"] == "FR"]

df_resume = pd.read_csv("C://Users//rober//OneDrive//Documents//test_ggmap//df_resume.csv")



villes_france = villes_france.rename(columns={'name': 'city'})
villes_france = villes_france.drop("country",1)
villes_france = villes_france.drop("id",1)
villes_france = pd.concat([villes_france, villes_france["coord"].apply(pd.Series)], axis=1)
villes_france = villes_france.drop("coord",1)


villes_france = villes_france.drop_duplicates(subset='city', keep="last")

villes_france = villes_france.sort_values(by=['city'])



df_final = df_resume.merge(villes_france, on="city")



df_final.to_csv('all_data_temperatures.csv', index=False)




