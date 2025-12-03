# Condiono2-5
Python library for calculating Pedersen and Hall electric conductivity in the ionospheres. It uses Adachi et. al. (2017) equations for it's calculations and data from IRI2016, NRLMSISE2 and IGRF.

The pyigrf_clara.py is based on a library made by Ciaran Beggan called pyIGRF and uses its equations for calculationg the values of the IGRF model.

There is no main function but the module tudo_final.py has the basic workflow of the library. You just need to replace the name of the files and the igrf configurations to the desired one. 

## Command Line Interface
The files interface.py and cli_igrf.py are CLI interfaces. They must be executed via the terminal (obviously). The first is for calculating the conductivity the second for calculating the igrf data on a grid.

## Data
Data compatible with this library can be found at : 
https://ccmc.gsfc.nasa.gov/models/

## Requirements 
**libraries:** pandas, matplotlib, scipy, numpy, geopandas ≤ 0.12.2, xarray, time

## Jupyter Notebook

**plot_kyoto** : Plots data from the kyoto model and compares it to condiono modelPlots data from the kyoto model

**plotirienrlmsisedata** : Reads and Plots IRI and NRLMSISE data.

**testeCalcPlot_HallPedersen_0_8** : Calculates and plots Hall and Pedersen conductivities. It does so from both the library of condiono and locally defined functions

**read_conductivity_data** : Shows an exemple of how to read the calculated data. 

**Validacao** :  Shows how the data calculated was validated
