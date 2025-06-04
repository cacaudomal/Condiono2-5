# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 16:29:16 2025

@author: User
"""

import pandas as pd
import matplotlib.pyplot as plt

import pyigrf_clara_0_6 as igrf
import conductivity0_9_5 as cond
import irinetcdf_02 as iri

#====== IGRF
resIGRF = "teste2024"
dado = igrf.IGRF(-80,-180,100,2008,resIGRF + '_2') #preciso garantir que estão nas mesmas coordenadas

#calcigrf = dado.calc_grid(intervalo_h = 20, lim_h = 500, intervalo_lat=10, lim_lat=90, intervalo_lon=20, lim_lon=180)
calcigrf = dado.get_grid(resIGRF + '_2' + "_grid.csv")

dado.Dfgrid['Longitude'] = 180 + dado.Dfgrid['Longitude'] #so it will be from 0 to 360 instead
dado.Dfgrid = dado.going_to_multiindex(dado.Dfgrid)
dado.Dfgrid.index.names = ['ht','lat','lon'] #putting the same index names as the rest of the data to allow join operations

##===========
# Reading conductivity data
condH = pd.read_csv("Condutividade_de_Hall.csv")
condP = pd.read_csv("Condutividade_de_Pedersen.csv")

#going to multiindex
condH.sort_values(['time','ht','lat','lon'],inplace=True)
condH = condH.set_index(['time','ht','lat','lon'])

condP.sort_values(['time','ht','lat','lon'],inplace=True)
condP = condP.set_index(['time','ht','lat','lon'])

#plotting conductivity profiles
plt.plot(condH.loc["0 days 03:15:00",:,-50,60],condH.index.get_level_values('ht').unique(),label="-50 lat 60 lon 03:15:00 Hall")
plt.plot(condH.loc["0 days 03:15:00",:,-50,240],condH.index.get_level_values('ht').unique(),label="-50 lat 240 lon 03:15:00 Hall")
# plt.plot(condP.loc["0 days 03:15:00",:,-50,60],condP.index.get_level_values('ht').unique(),label="-50 lat 60 lon 03:15:00 Pedersen")

# plt.plot(condH.loc["0 days 18:45:00",:,-50,240],condH.index.get_level_values('ht').unique(),label="-50 lat 240 lon 18:45:00 Hall")
# plt.plot(condP.loc["0 days 18:45:00",:,-50,240],condP.index.get_level_values('ht').unique(),label="-50 lat 240 lon 18:45:00 Pedersen")

plt.grid()
plt.legend()
plt.show()


## reading iri data to plot its values
namefileiri = "IRI.3D.2008001.nc"
iriteste = iri.irincdf(namefileiri)
#iriteste.d.plot_densidade_e()
#iriteste.plot_densidade_e(ne, h)