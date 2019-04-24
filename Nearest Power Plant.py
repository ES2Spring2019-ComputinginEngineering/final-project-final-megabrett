# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 00:53:57 2019

@author: Megan
"""
import numpy as np
import ReadDataFinal as rd

def latsAndLonsofPowerPlants():
    energy = []  # list of energies produced by each plant; gigaWatts
    latitudes = []
    longitudes = []
    file = open("largest nuclear power stations in the us.csv")
    split_character = ','
    for line in file:
        data_line = line.split(split_character)
        energy.append(data_line[1])
        latitudes.append(data_line[2])
        longitudes.append(data_line[3])
    file.close()
    print("the energy productions are "+str(energy))
    print("the latitudes are "+str(latitudes))
    print("the longitudes are "+str(longitudes))
    return energy, latitudes, longitudes

energy, latitudes, longitudes = latsAndLonsofPowerPlants()