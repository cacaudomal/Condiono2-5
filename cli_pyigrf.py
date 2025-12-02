# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 22:18:58 2025

@author: tedea
"""

import argparse
import pyigrf_clara_0_6 as igrf

parser = argparse.ArgumentParser(prog = "pyigrf_cli",
    description="Calculates the IGRF model data."
    )

parser.add_argument('igrf',
                    type = str,
                    metavar = 'igrf',
                    help = "igrf model output file name")

parser.add_argument("-ih","--initial_h",
                    type = float,
                    default = 0,
                    help = "initial height in km. (default = 0)")

parser.add_argument("-dh","--delta_h",
                    type = float,
                    default = 20,
                    help = "height intervals in km. (default = 20)")

parser.add_argument("-lh","--lim_h",
                    type = float,
                    default = 500,
                    help= "superior limit for height in km,(default = 500)")

parser.add_argument("-y","--year",
                    type = int,
                    default = 2008,
                    help = "year the igrf model was calculated for.(default = 2008)")

parser.add_argument("-dlat","--delta_latitude", 
                    type = float,
                    default = 10,
                    help = "Interval of latitude data. (default = 10)")

parser.add_argument('-flat','--latitude_final', 
                    type = float,
                    default = 90,
                    help = 'final latitude of IGRF data. (default = 90)')

parser.add_argument('-ilat','--latitude_initial', 
                    type = float,
                    default = -80,
                    help = 'initial latitude of IGRF data. (default = -90)')

parser.add_argument("-dlon","--delta_longitude", 
                    type = float,
                    default = 20,
                    help = "Interval(delta) of longitude data. (default = 20)")

parser.add_argument('-flon','--longitude_final', 
                    type = float,
                    default = 180,
                    help = 'final longitude of IGRF data. (default = 180)')

parser.add_argument('-ilon','--longitude_initial', 
                    type = float,
                    default = -180,
                    help = 'initial longitude of IGRF data. (default = -180)')

args = parser.parse_args()

igrfilename = args.igrf
ih = args.initial_h
dh = args.delta_h
lim_h = args.lim_h
year = args.year
dlat = args.delta_latitude
flat = args.latitude_final
dlon = args.delta_longitude
flon = args.longitude_final
ilon = args.longitude_initial
ilat = args.latitude_initial
#calcigrf = dado.calc_grid(intervalo_h = 20,
# lim_h = 500, 
# intervalo_lat=10,
# lim_lat=90, 
# intervalo_lon=20, 
# lim_lon=180)

print("\nfilename:",igrfilename,
      '\nYear', year,
      "\nInitial Height",ih,
      "\nheight variation:",dh,
      "\nMaximum Height:",lim_h,
      "\nInitial Latitude",ilat,
      "\nLatitude intervals: ",dlat,
      "\nMaximun Latitude",flat,
      "\nInitial Longitude",ilon,
      "\nLongitude intervals: ",dlon,
      "\nFinal longitude",flon)

dado = igrf.IGRF(ilat, ilon, ih, year, igrfilename)
print("\nDado",dado)

dado.calc_grid(dh,lim_h,dlat,flat,dlon,flon)