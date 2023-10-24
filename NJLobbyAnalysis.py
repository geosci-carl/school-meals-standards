# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 19:06:48 2023

@author: Carl Fredrick G. Aquino (geosci.carl@gmail.com)
"""
# import required packages
import pandas as pd
import matplotlib.pyplot as plt

# import CSV (data from https://www.elec.nj.gov/pdffiles/press_releases/pr_2023/pr_03092023.pdf)
njlobby = pd.read_csv('data/NJLobbyingSectors20-22.csv', thousands=',')

# plot
plt.rcParams['font.size'] = '16'
ax = njlobby.plot.bar(x='SECTOR', y='AMOUNT', figsize=(10,10))
plt.legend(["Lobbying Dollars Spent Per Sector"])
ax.set_xlabel('Sector')
ax.set_ylabel('USD (millions)')

# export plot
plt.savefig("Plots/LobbyingBarplot.png", bbox_inches='tight')