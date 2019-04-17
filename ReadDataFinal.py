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
        Cities = []
        Latitude = np.zeros((total_row,))
        Longitude = np.zeros((total_row,))
        Population = np.zeros((total_row,))
        for row in reader:
            Cities.append(row[0])
            Latitude[index] = ((float(row[1]) - 25)/(47 - 25))
            Longitude[index] = ((float(row[2]) - 71)/(122 - 71))
            Population[index] = (float(row[3]) * (10 ** 6))
            line_count += 1
            index += 1
        Longitude = Longitude * (-1)
        print("Cities: ")
        print(Cities)
        print("Latitude: ")
        print(Latitude)
        print("Longitude: ")
        print(Longitude)
        print("Population: ")
        print(Population)
    return (Cities, Latitude, Longitude, Population)
        
Cities, Latitude, Longitude, Population = readData()

def graphData(Latitude, Longitude):
    plt.plot(Longitude, Latitude, 'g.', label = 'Cities')
    plt.legend()
    plt.ylabel('Latitude')
    plt.xlabel('Longitude')
    plt.suptitle('Map of US Cities')
    plt.show()
    
graphData(Latitude, Longitude)