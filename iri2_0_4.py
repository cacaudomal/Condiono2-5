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
#from pathlib import Path


class iri():
    """
    CLASS FOR READING AND STORING DATA FROM THE IRI MODEL.
    
    ...
            
    Attributes
    ----------
    nome_arq : STRING
        NAME OF THE IRI FILE WHERE THE DATA IS STORED    
    
    Methods
    ----------
        cria_dado_dataframe(self)
        _ler_arq(self,nomearq)
        _string_para_float(self,dado)
    """
    
    def __init__(self,nome_arq):
        self.nome_arq = nome_arq
        
        self.cria_dado_dataframe()
        
        self.to_percentage()
        self.eletron_cm3to_m3()
        
        print("IRI - data read with success.")
        
    
    def _ler_arq(self,nomearq):
        """
        FUNCTION THAT READS FILES FROM IRI 2020, SAVE EACH LINE TO A LIST, RETURNS
        THE VALUES STARTING AT LINE 32 AND DISCARDS THE REST. 

        Parameters
        ----------
        nomearq : STRING
            NAME OF THE FILE WHERE THE DATA IS STORED. IRI2020

        Returns
        -------
        guardadado : LIST
            LIST OF STRINGS CONTAINING EACH LINE DATA.
                WE SKIP TO LINE 32 BECAUSE ITS WHERE THE NAME OF THE COLUMNS IS AT. tHE DATA STAR AT LINE 33

        """
        with open(nomearq,"r") as arq: 
            dado = arq.readlines() #le todas as linas do arquivo
        #print("ler_arq dado:\n",dado)
        
        guardadado = []
        for i in range(len(dado)):
            guardadado.append(dado[i].split())
        #print("\nle iri : ",guardadado[32])
        
        return guardadado[31:] # 32 for IRI2020 and 31 for IRI2016
                                # 33 is the las line of the header and line 32 has the header of the dataframe
    
    def _string_para_float(self,dado):
        """
        Method that separates a list of strings containing only numbers in a list of float lists 
        
        Parameters
        ----------
        dado : LIST OF STRING 
            DATA TO BE CONVERTED

        Returns
        -------
        result : LIST OF FLOATS
            DATA CONVERTED TO FLOAT
            
        """
        result = [list(map(float,i)) for i in dado] #faz o typecast de todos os valores de cada linha da lista de listas de str para float
        
        return result    
         
    
    def cria_dado_dataframe(self):
        arqlido = self._ler_arq(self.nome_arq)
        splitdata = self._string_para_float(arqlido[1:])
        
        self.data = pd.DataFrame(splitdata, columns = ["H(km)","Ne(cm-3)","Ne/NmF2","Tn/K","Ti/K","Te/K","O+","N+","H+","He+","O2+","NO+","Clust","TEC","t/%"])
        
    
    def calc_rho_numion(self, ne, rho_ion):
       """
       CALCULATES THE NUMBER DENSITY OF IONS  FROM THE ELECTRON DENSITY AND ATMOSPHERIC IONS CONCENTRATION
      
       Parameters
       ----------
       rho_ion : PANDA SERIES - FLOAT
           IONIC CONCENTRATION [%]
       ne : PANDA SERIES - FLOAT
           ELECTRON DENSITY [electrons/m^3]
    
       Returns:
       ----------
       rhoion : PANDA SERIES - FLOAT
           ion number density [m^-3]
       
       """
       rhoion =  ne * rho_ion/100 #densidade do íon em [m^-3]
     
       return rhoion
 
    
    def eletron_cm3to_m3(self):
        """
        CREATES COLUMNS WITH THE ELECTRION DENSITY VALUES IN m-³ IN THE GIVEN DATAFRAME


        Returns
        -------
        None.

        """
        self.data["Ne(m-3)"] = self.data["Ne(cm-3)"] * 1e6
        
        
    def to_percentage(self):
        '''
        CONVERTS IONIC CONCENTRATION*10 TO IONIC CONCENTRATION AND SAVES IN A DATAFRAME.
        Returns
        -------
        None.

        '''
        self.rhodado = self.data[["O+","N+","H+","He+","O2+","NO+"]] * 0.1


    def rhonumion_all(self,Ne):
        
        #Ne = self.dado["Ne(m-3)"]
        #x = pd.DataFrame(columns = ["O+","N+","H+","He+","O2+","NO+"])
        a = self.calc_rho_numion(Ne,self.rhodado["O+"])
        b = self.calc_rho_numion(Ne,self.rhodado["N+"])
        c = self.calc_rho_numion(Ne,self.rhodado["H+"])
        d = self.calc_rho_numion(Ne,self.rhodado["He+"])
        e = self.calc_rho_numion(Ne,self.rhodado["O2+"])
        f = self.calc_rho_numion(Ne,self.rhodado["NO+"])
        #print("\n\n\nabcd:",a,b,c,d,e,f)
        self.rhonum_dado = pd.concat([a,b,c,d,e,f], axis=1, keys=["O+","N+","H+","He+","O2+","NO+"])
        
        return self.rhodado
        
    
    def plot_densidade_e(self, ne, h, data=""):
        """
        FUNTION FOR PLOTTING A ELECTRON DENSITY HEIGHT PROFILE.

        Parameters
        ----------
        ne : PANDA SERIES 
            ELECTRON DENSITY [m^-3]
        h : PANDA SERIES
            LIST OF HEIGHTS [km].
        data : STRING, optional
            DATE AT WHICH THE DATA WAS AQUIRED. The default is "".

        Returns
        -------
        None.

        """
        plt.figure(figsize=(5,5))
        plt.semilogx(ne,h,label = "$N_e$ "+data)
        plt.xlabel("Electron Density ($m^{-3}$)")
        plt.ylabel("Height (km)")
       
        plt.title("Electron Density \n " + data)
        
        plt.legend()
        plt.grid()
       
        plt.show()
    
        
    def plot_rhoion(self):
        plt.figure(figsize=(5,5))

        plt.plot(self.rhodado,self.data["H(km)"])
        
        plt.ylabel("Height (km)")
        plt.xlabel("Ion density ($m^{-3}$)")
        plt.title("Ion density \n ")
        
        plt.legend()
        plt.grid()
        plt.xscale("log")
        
        plt.show()
        
        
#============================================        
        
# class irincdf():
#     def __init__(self,filename):
#         self.iridata = self._read(filename) 
#         pass
    
#     def _read(self,filename):
#         d = {}
#         for i in ["O+","N+","H+","He+","O2+","NO+","Ne","Tn","Ti","Te"]:
#             d[i] = rn.basencdf(filename, i)
            
#         return d
    
    
# filename = "IRI.3D.2008001.nc"
# iri(filename)


#unitname = "Ne"

#b = irincdf(filename)
# d['O+'].munit

#nomearqIRI = Path("Dado_txt/dadoIRI/IRI2016_lat19_lon69_z80-300_s5_data30MAR2012_h12UT.txt")
#a = iri(nomearqIRI)
# #print(a.dado.dtypes)

# a.to_percentage()
# a.eletron_cm3to_m3()

# g = b.dado["Ne(cm-3)"] - e.dado["Ne(cm-3)"]
# d.plot_densidade_e(g,b.dado["H(km)"]," 2008 - 2000 às 00:00LT")