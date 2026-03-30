# Condiono2-5


Python library for calculating Pedersen and Hall electric conductivity in the ionospheres. It uses Adachi et. al. (2017) equations for it's calculations and data from IRI2016, NRLMSISE2 and IGRF.

The pyigrf_clara.py is based on a library made by *Ciaran Beggan* called pyIGRF and uses its equations for calculationg the values of the IGRF model.
It runs on IRGF-13 but that can be changed if the user gets new coefficients in a .shc file.

There are no tests to validate the input so beware of mistakes.

There is no main function but the module tudo_final.py has the basic workflow of the library. You just need to replace the name of the files and the igrf configurations to the desired one to get a result for your data.

For reading IRI2020 text files in the library iri2_0_4 you must change the value in the function _ler_arq the variable guardadado[31:] to guardadado[32:] as specified in the comments.

 

## Command Line Interface

The files interface.py and cli_igrf.py are CLI interfaces. They must be executed via the terminal. The first is for calculating the conductivity the second for calculating the igrf data on a grid.

 

## Data

Data compatible with this library can be found at :
https://ccmc.gsfc.nasa.gov/models/

IRI : https://ccmc.gsfc.nasa.gov/ror/requests/IT/IRI/iri_user_registration.php

NRLMSIS : https://ccmc.gsfc.nasa.gov/ror/requests/IT/NRLMSIS/nrlmsis_user_registration.php

 
Data used for testing this code can be downloaded at:

IRI2020 : https://ccmc.gsfc.nasa.gov/ror/results/viewrun.php?runnumber=Clara_Oliveira_081823_IT_1

NRLMSIS 2.0 : https://ccmc.gsfc.nasa.gov/ror/results/viewrun.php?runnumber=Clara_Oliveira_081823_IT_2

on the Request output data in bulk option. The data used in the paper is of the day 2008-01-01.


## Requirements

**libraries:** pandas, matplotlib, scipy, numpy, geopandas ≤ 0.12.2, xarray, time

 

## Jupyter Notebook

**plot_kyoto :** Plots data from the kyoto model and compares it to condiono modelPlots data from the kyoto model

**plotirienrlmsisedata :** Reads and Plots IRI and NRLMSISE data.

**testeCalcPlot_HallPedersen_0_8 :** Calculates and plots Hall and Pedersen conductivities. It does so from both the library of condiono and locally defined functions

**read_conductivity_data :** Shows an exemple of how to read the calculated data.

**Validacao :**  Shows how the data calculated was validated


## Modules



### Main body

**conductivty** : calculates conductivity.

**freqcol :** module that calculates the collision frequencies.

**nrlmsise2 :** Module for reading NRLMSISE2 in text format and storing it.

**iri2 :** Module for reading IRI2016 and IRI2020 in text format and storing it.

 

### Libraries for reading the NetCDF data from the respective given model

**read_netcdf :** Base class for reading NetCDF

**iri2netcdf :** Module for reading IRI data in NetCDF format and storing it.

**msise2netcdf :** Module for reading NRLMSISE2 data in NetCDF format and storing it.



### pyIGRF

**pyigrf_clara :** Module containing classes for calculating and plotting the IGRF model.

**io_options_clara :** Module with functions for calculating the magnetic field values, writing them in a file and for verifying the values inserted by the user used to calculate the geomagnetic field.

**igrf_utils :** Module with functions to compute the main field, its non linear coefficients and the formatting and rotation of the coordinates.



### Interface

**interface :** contains the CLI interface functions for the conductivity calculation part of the code. To use it in the command line, in the programm directory, write:

`py .\interface.py out_file_name.txt name_of_IRI_file.nc name_of_msise_file.nc name_of_igrf.csv`

**cli_pyigrf :**  contains the CLI interface of the pyigrf part of the code. To use it in the command line, in the programm directory, write:

`py .\cli_pyigrf.py igrf_output_file_name`

and the values will be calculated for the programs standard values. 
More info on the program can be found in the help section:

`py .\cli_pyigrf.py -h`



### Example Code

**tudo_final :** example of how to calculate the conductivity for a given dataset using the codes libraries. Just change the following variables to the appro-priate file names : namefileiri, filenamemsise2, resIGRF. The output files always have the same name and may overwrite themselves if not renamed ou taken from the program file. 

**teste_perfisdecond :** example of how to plot conductivity profiles from calculated values. 

