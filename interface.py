# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 14:18:39 2025

@author: tedea
"""
import argparse


#import freqcol_0_6 as fc
# import pyigrf_clara_0_6 as igrf
# import irinetcdf_02 as iri
# import msise2Netcdf as msise
import CondIono2_calc_all as cond

parser = argparse.ArgumentParser(prog = "CondIono",
    description="""
    Reads the IGRF, IRI, NRLMSISE models data and calculates the hall and pedersen conductivities."""
    )
parser.add_argument("namefile", 
                    type = str,
                    help = "name of the file to store the conductivities values"
                    )
parser.add_argument("iri",
                    type = str,
                    metavar="iri",
                    help="The IRI model name file.")

parser.add_argument("nrlmsise",
                    type = str,
                    metavar="msise",
                    help ="The NRLMSISE model name file." )

# parser.add_argument("igrf_options",
#                     type = str,
#                     choices = IGRF_OPTIONS.keys(),
#                     help = "Do you want to (c)alculate the IGRF model or (r)ead a previously calculated model?" )

parser.add_argument('igrf',
                    type = str,
                    metavar = 'igrf',
                    help = "igrf model input file name")

parser.add_argument("-y","--year",
                    type = int,
                    default = 2008,
                    help = "year the igrf model was calculated for.(default = 2008)")

parser.add_argument("-ht","--height", 
                    type = float,
                    default = 100,
                    help = "heigh of the IGRF data.(default = 100)")

parser.add_argument('-lat','--latitude_max', 
                    type = float,
                    default=-80,
                    help = 'max latitude of IGRF data. (default = -80)')
parser.add_argument('-lon','--longitude_max', 
                    type=float,
                    default = -180,
                    help = 'max longitude of IGRF data. (default = -180)')


# def read_data(irifilename, msisefilename, igrffilename,max_lat,max_lon,h,year):
#     iridata = iri.irincdf(irifilename)
    
#     msisedata = msise.nrlmsisenetcdf(msisefilename)
    
#     igrfdata = igrf.IGRF(max_lat,max_lon,h,year,igrffilename)
#     igrfdata.get_grid(igrffilename)
#     print("\n\nigrfdata :\n ", igrfdata.Dfgrid)
   
#     igrfdata.Dfgrid['Longitude'] = 180 + igrfdata.Dfgrid['Longitude'] #so it will be from 0 to 360 instead
#     igrfdata.Dfgrid = igrfdata.going_to_multiindex(igrfdata.Dfgrid)
#     igrfdata.Dfgrid.index.names = ['ht','lat','lon']    
    
#     return iridata, msisedata,igrfdata


args = parser.parse_args()

filename = args.namefile

irifilename = args.iri
msisefilename = args.nrlmsise
igrffilename = args.igrf

print("\nThe files are :",
      "\nnamefile:",
      filename,
      "\nIRI     :",
      irifilename,
      "\nNRLMSISE:",
      msisefilename,
      "\nIGRF    :",
      igrffilename)

# iridata, msisedata,igrfdata = read_data(irifilename, msisefilename, igrffilename,args.latitude_max,args.longitude_max,args.height,args.year)
print('\nread data\n')

cond.condiono2(filename, irifilename, msisefilename, igrffilename)
# freqc = fc.freqcol(msisedata.msise.data["N2"],
#             msisedata.msise.data["O2"],
#             msisedata.msise.data["O"],
#             iridata.iri.data['Te'],
#             iridata.iri.data['Tn'],
#             iridata.iri.data['Ti'])

# print("\nfreqc :\n",freqc)

"""
colocar na linha de comando
py .\interface.py putoutfile.txt IRI.3D.2008001.nc NRLMSIS2.0.3D.2008001.nc teste2024_2_grid.csv
"""