def createLists():
    split_char = ","
    city_lats = []
    city_longs = []
    city_energy_usage = []  #gigawatts per month
    file1 = open("Monthly-Electricity-Consumption-for-Major-US_Cities.csv")
    for line in file1:
        data_line = line.split(split_char)
        city_lats.append(float(data_line[3]))
        city_longs.append(float(data_line[4]))
        city_energy_usage.append(float(data_line[1]))
    file1.close()
    plant_lats = []
    plant_longs = []
    plant_energy_prod = []  #gigawatts per month
    file2 = open("largest nuclear power stations in the us.csv")
    for line in file2:
        data_line = line.split(split_char)
        plant_lats.append(float(data_line[2]))
        plant_longs.append(float(data_line[3]))
        plant_energy_prod.append(float(data_line[1]))
    file2.close()
    return city_lats, city_longs, plant_lats, plant_longs, plant_energy_prod, city_energy_usage

def energyComparison(city_lats, city_longs, plant_lats, plant_longs,
                     plant_energy_prod, city_energy_usage):
    
    return

