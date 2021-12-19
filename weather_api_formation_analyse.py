#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 15:06:04 2021

@author: fitec
"""

import pandas as pd
import csv


data_ville = pd.read_csv("/home/fitec/formation_fitec/git_docker/flask/openweather/weatherOpenMap_2021_12_17_21_47_14.csv")




liste_ville = sorted(list(set(data_ville['city'])))


df_resume = pd.DataFrame(columns=["city","temp","temp_max","temp_min"])




for ville_boucle in liste_ville : 
    
    
    mini_df = data_ville[data_ville["city"]==ville_boucle]
    

    
    max_t = max(mini_df["temp_max"])
    min_t = min(mini_df["temp_min"])
    mean_t = round(sum(mini_df["temp"])/len(mini_df["temp"]),2)



    new_row = {'city':ville_boucle, 'temp':mean_t, 'temp_max':max_t, 'temp_min':min_t}

    df_resume = df_resume.append(new_row, ignore_index=True)

    


print(df_resume)



df_resume.to_csv("df_resume.csv",index=False)

























