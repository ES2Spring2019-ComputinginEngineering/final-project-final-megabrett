# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 16:13:38 2019

"""
import numpy as np
import csv
import matplotlib.pyplot as plt

csv_file = open('Latitude and Longitude of major us cities.csv')
total_row = sum(1 for row in csv_file)

def readData():
    line_count = 0
    index = 0
    with open('Latitude and Longitude of major us cities.csv') as csvfile:
        reader = csv.reader(csvfile)
        Cities = np.zeros((total_row,))
        Latitude = np.zeros((total_row,))
        Longitude = np.zeros((total_row,))
        Population = np.zeros((total_row,))
        for row in reader:
            Cities[index] = ((row[0]))
            Latitude[index] = ((float(row[1]) - 25)/(47 - 25))
            Longitude[index] = ((float(row[2]) - 71)/(122 - 71))
            Population[index] = int(row[3])
            line_count += 1
            index += 1
        print("Cities: ")
        print(Cities)
        print("Latitude: ")
        print(Latitude)
        print("Longitude: ")
        print(Longitude)
        print("Population: ")
        print(Population)
    return (Cities, Latitude, Longitude, Population)
        
(Cities, Latitude, Longitude, Population) = readData()