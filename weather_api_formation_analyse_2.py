#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 15:41:49 2021

@author: fitec
"""

import pandas as pd
import csv

import papierstat

from papierstat.datasets import load_enedis_dataset
df = load_enedis_dataset()
df.head(n=2).T



import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.set_extent([-5, 10, 42, 52])

ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.plot(df.long, df.lat, '.')
ax.set_title('France');


# data_ville = pd.read_csv("/home/fitec/formation_fitec/git_docker/flask/openweather/weatherOpenMap_2021_12_17_21_47_14.csv")


# data_ville_resume = pd.read_csv("/home/fitec/formation_fitec/git_docker/flask/openweather/df_resume.csv")
