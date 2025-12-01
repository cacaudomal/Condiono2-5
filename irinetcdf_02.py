# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 17:28:22 2024

@author: tedea
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 16:03:34 2022

@author: Clara Castilho Oliveira

 Dependencies: 
 -------------
     : matplotlib, pandas
     
"""

import matplotlib.pyplot as plt
import pandas as pd
import read_netcdf_01 as rn   
        
class irincdf():
    def __init__(self,filename):
        self.iri = self._read(filename) 
        pass
    def __str__(self):
        
        return "measuring units:\n"+str(list(self.d.munit.items()))
        
    def _read(self,filename):
        return rn.basencdf(filename)
    
    def plot_densidade_e(self, ne, h, data=""):
        """
        FUNCTION FOR PLOTTING THE ELECTRON DENSITY HEIGHT PROFILE. 

        Parameters
        ----------
        ne : PANDA SERIES - FLOATS
            ELECTRON DENSITY[m^-3].
        h : PANDA SERIES
            HEIGHT [km].
        data : STRING, optional
            DATE IN WHICH THE DATA WAS AQUIRED. The default is "".

        Returns
        -------
        None.

        """
        fig = plt.figure(figsize=(5,5))
        
        plt.plot(ne,h,label = "$N_e$ "+data)
        plt.xlabel("Electron density ($m^{-3}$)")
        plt.ylabel("Height (km)")
       
        plt.title("Electron density \n " + data)
        
        plt.legend()
        plt.grid()
       
        plt.show()
        fig.savefig("plot_" + data +'.png', dpi = 300, transparent=True)
#=================

        