def createLists():
    split_char = ","
    city_lats = []
    city_longs = []
    city_energy_usage = []
    file1 = open("Monthly-Electricity-Consumption-for-Major-US_Cities.csv")
    for line in itertools.islice(file1, 1, None):  # don't read first line of the file
        data_line = line.split(split_character)
        city_lats.append(float(data_line[3]))
        city_longs.append(float(data_line[4]))
        city_energy_usage.append(float(data_line[1]))
    file1.close()
    plant_lats = []
    plant_longs = []
    plant_energy_prod = []
    file2 = open("largest nuclear power stations in the us.csv")
    for line in itertools.islice(file2, 1, None):  # don't read first line of the file
        data_line = line.split(split_character)
        plant_lats.append(float(data_line[2]))
        plant_longs.append(float(data_line[3]))
        plant_energy_prod.append(float(data_line[1]))
    file2.close()
    return city_lats, city_longs, plant_lats, plant_longs, plant_energy_prod, city_energy_usage

def energyComparison(city_lats, city_longs, plant_lats, plant_longs,
                     plant_energy_prod, city_energy_usage):
    
    return

