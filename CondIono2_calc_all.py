# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 13:31:18 2025

@author: tedea
"""

# -*- coding: utf-8 -*-
"""
Created on Thus Oct 29 15:31:44 2024
@author: Clara Castilho Oliveira
"""
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

import freqcol_0_6 as fc
import pyigrf_clara_0_6 as igrf
import conductivity0_9_6 as cond
#from pathlib import Path

import irinetcdf_02 as iri
import msise2Netcdf as msise

import time
def condiono2(namefile,namefileiri,namefilemsise,namefileigrf):
    #====  Reading data ====
    inicio = time.time() #Function for getting the starting time of the program
    
    # IRI
    #namefileiri = "IRI.3D.2008001.nc"
    iriteste = iri.irincdf(namefileiri)
    
    # NRLMSISE
    #filenamemsise2 = "NRLMSIS2.0.3D.2008001.nc"
    msisetest = msise.nrlmsisenetcdf(namefilemsise)
    
    # IGRF
    #resIGRF = "teste2024"
    dado = igrf.IGRF(-80,-180,100,2008,namefileigrf) #its necessary to assure they are in the same coordinates.
    
    #calcigrf = dado.calc_grid(intervalo_h = 20, lim_h = 500, intervalo_lat=10, lim_lat=90, intervalo_lon=20, lim_lon=180)
    dado.get_grid(namefileigrf)
    
    dado.Dfgrid['Longitude'] = 180 + dado.Dfgrid['Longitude'] #so it will be from 0 to 360 instead
    dado.Dfgrid = dado.going_to_multiindex(dado.Dfgrid)
    dado.Dfgrid.index.names = ['ht','lat','lon'] #putting the same index names as the rest of the data to allow join operations
    
    
    #==== Calculating Conductivities
    print("starting calculations")
    #= Calculating colision frequencies
    freqc = fc.freqcol(msisetest.msise.data["N2"],
                msisetest.msise.data["O2"],
                msisetest.msise.data["O"],
                iriteste.iri.data['Te'],
                iriteste.iri.data['Tn'],
                iriteste.iri.data['Ti'])
    print("Colision Frequencies Calculated")
    #= Calculating Angular Gyrofrequency
    gyrofreq = cond.gyrofrequency(dado.Dfgrid["B(T)"])
    
    print("gyrofrequedncy calculated")
    
    #= Calculating Relative Contruibution Parammeter
    conductivity = cond.condiono_adachi()
    
    conductivity.calc_prelativa_all(iriteste.iri.data["O+"],
                            iriteste.iri.data["NO+"],
                            iriteste.iri.data["O2+"],
                            iriteste.iri.data["Ne"])
    print("Parameter of relative contribution calculated")
    
    # #Alining Data by putting everything in a same Data Frame
    conductivity.calcvaluesdf = gyrofreq.result.join(freqc.result.copy(),
                              how = 'inner') #inner para ficarem só as coordenadas que ambos dataframes tem
    print("Joining matrixes")
    
    # #= Ordering multiindex of conductivity data
    conductivity.calcvaluesdf = conductivity.calcvaluesdf.reset_index().sort_values(['time','ht','lat','lon']).set_index(['time','ht','lat','lon'])
    
    
    # #= Calculating Hall and Pedersen Conductivities
    print("Calculating conductivities")
    # # Hall
    conductivity.calc_Hall(conductivity.calcvaluesdf["fen"],
                            conductivity.calcvaluesdf["fin1"],
                            conductivity.calcvaluesdf["fin2"], 
                            conductivity.calcvaluesdf['wi1'],
                            conductivity.calcvaluesdf['wi2'],
                            conductivity.calcvaluesdf['we'],
                            conductivity.p1,
                            conductivity.p2,
                            iriteste.iri.data['Ne'],
                            dado.Dfgrid["B(T)"]).dropna()
    
    # #the igrf data keeps pulling the time index to the deeper level, gotta beware of 
    # #that when plotting
    print("Hall conductivity calculated")
    # # Pedersen
    conductivity.calc_Pedersen(conductivity.calcvaluesdf["fen"],
                            conductivity.calcvaluesdf["fin1"],
                            conductivity.calcvaluesdf["fin2"], 
                            conductivity.calcvaluesdf['wi1'],
                            conductivity.calcvaluesdf['wi2'],
                            conductivity.calcvaluesdf['we'],
                            conductivity.p1,
                            conductivity.p2,
                            iriteste.iri.data['Ne'],
                            dado.Dfgrid["B(T)"]).dropna()
    print("Pedersen conductivity calculated")
    
    # #=== saving calculated data 
    conductivity.save_to_csv(conductivity.CondH.dropna(), namefile+"Hall_Conductivity")
    print("d1")
    
    conductivity.save_to_csv(conductivity.CondP.dropna(), namefile+"Pedersen_Conductivity")
    print("d2")
    
    print("Saved conductivities to file")
    #calculating height integrated data for a given day
    
    h = 100
    hintegratedHall = conductivity.calc_height_integrated_conductivity(conductivity.CondH.loc[:,:,:,'0 days 00:00:00'].dropna(),h)
    
    # #==== Plotting
    
    # when = 0 
    
    gyrofreq.plot_gyrmap(gyrofreq.result,h=h,time="2008", localscope=True, savemap = True,filename="gyrofrequency_clara_teste")
    
    conductivity.plot_2dgrid(conductivity.CondH.loc[:,:,:,'0 days 00:00:00'].dropna(),h,'Hall Conductivity at ' + str(h) + " km altitude" )
    conductivity.plot_2dgrid(conductivity.CondP.loc[:,:,:,'0 days 00:00:00'].dropna(),h,'Pedersen Conductivity at ' + str(h) + " km altitude" )
    
    #conductivity.plot_2dgrid_hintegrated2(hintegratedHall,title = ' Height integratred Halls conductivity at ' + str(h) + " km altitude")
    
    fim = time.time()
    print("Program exectuion time: ",fim-inicio,"seconds")
