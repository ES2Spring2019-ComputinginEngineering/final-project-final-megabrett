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
        B_T_U = np.zeros((total_row,))
        for row in reader:
            Cities.append(row[0])
            Latitude[index] = ((float(row[1]) - 25)/(47 - 25))
            Longitude[index] = ((float(row[2]) - 71)/(122 - 71))
            Population[index] = (float(row[3]) * (10 ** 6))
            B_T_U[index] = ((302000000 / 12) * (Population[index] * (10 ** 3)))
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
        print("Monthly Btu per City: ")
        print(B_T_U)
    return (Cities, Latitude, Longitude, Population, B_T_U)
        
Cities, Latitude, Longitude, Population, B_T_U = readData()

test_lat = input("What is the latitude of the point you want to test? (Choose a point between 25 and 47) ")
test_lat = ((float(test_lat) - 25)/(47-25))
test_lon = input("What is the longitude of the point you want to test? (Choose a point between 71 and 122) ")
test_lon = (-1) * ((float(test_lon) - 71)/(122 - 71))

def graphData(Latitude, Longitude, test_lon, test_lat):
    plt.plot(test_lon, test_lat, 'r.', label = 'Test Point')
    plt.plot(Longitude, Latitude, 'g.', label = 'Cities')
    plt.legend()
    plt.ylabel('Latitude')
    plt.xlabel('Longitude')
    plt.suptitle('Map of US Cities')
    plt.show()
    
graphData(Latitude, Longitude, test_lon, test_lat)