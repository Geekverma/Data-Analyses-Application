import matplotlib.pyplot as plt
from challange1 import csvtolist
import numpy as np

c02_emission_dict = csvtolist()
c02_emission_list_one = []
c02_emission_list_two = []
year = np.array([i for i in range(1997,2011)])
print("Enter countries to see result")
country_1 = input()
country_2 = input()

for key,val in c02_emission_dict.items():
    if key == 'CO2 per capita':
        continue
    elif key.lower() == country_1.lower():
        c02_emission_list_one = [float(i) for i in val]       
        emission_one = np.array(sorted(c02_emission_list_one))

    elif key.lower() == country_2.lower():
        c02_emission_list_two = [float(i) for i in val]
        emission_two = np.array(sorted(c02_emission_list_two))
if c02_emission_list_one and c02_emission_list_two:
    plt.plot(year,emission_one)
    plt.plot(year,emission_two)
    plt.xlabel("year")
    plt.ylabel("emissions")
    plt.legend()
    plt.show()
    
