# Getting Energy Usage/Person
import numpy as np

def createEnergyandCityLists():
    cities = []
    print(cities)
    city_energy = []
    pop = []
    file = open("Monthly-Electricity-Consumption-for-Major-US-Cities.xlsx")
    print(file)
    """split_character = ';'
    for line in file:
        data_line = line.split(split_character)  # split each line
        #print(data_line)
        cities.append(data_line[0])  # add first element, name of city, in order
        city_energy.append(data_line[1])  # add second element, energy usage of city (in mega watts), in order
        pop.append(data_line[2])  # add third element, population (millions of people), in order
    file.close()
    city_energy_array = np.asarray(city_energy)
    pop_array = np.asarray(pop)
    energy_per_person_array = np.divide(city_energy_array, pop_array)
    energy_per_person = np.array(energy_per_person_array.tolist())
    #print(energy_per_person)"""
    return cities #, city_energy, pop, energy_per_person
    
createEnergyandCityLists()
#def graphEnergyData(cities, , ):