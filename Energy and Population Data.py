# Getting Energy Usage/Person
import numpy as np

def createEnergyandCityLists():
    cities = []
    city_energy = []
    pop = []
    energy_per_person = []
    file = open("Monthly-Electricity-Consumption-for-Major-US-Cities.csv")
    split_character = ','
    for line in file:
        data_line = line.split(split_character)  # split each line
        cities.append(data_line[0])  # add first element, name of city, in order
        city_energy.append(float(data_line[1]))  # add second element, energy usage of city (in gigawatts), in order
        data_line[2] = data_line[2].strip("\n")  # get rid of \n character on end of each element
        pop.append(float(data_line[2]))  # add third element, population (millions of people), in order
    file.close()
    print("cities list is: "+str(cities))
    print("city energy list is: "+str(city_energy))
    print("pop list is: "+str(pop))
    i = 0  # counter
    while i < len(city_energy):
        energy = city_energy[i]
        population = pop[i]*100000  # gives exact population
        en_use_per_person = (energy/population)*1000  # gives energy use per person in megawatts
        energy_per_person.append(en_use_per_person)
        i += 1
    print("energy per person list is: "+str(energy_per_person))
    return cities, city_energy, pop, energy_per_person
    
createEnergyandCityLists()

def graphEnergyData(cities, city_energy, energy_per_person):
    
    return