import matplotlib.pyplot as plt
from challange1 import csvtolist
import numpy as np

c02_emission_dict = csvtolist()
c02_emission_list = []
print("Enter country to see result")
country = input()

for key,val in c02_emission_dict.items():
    if key == 'CO2 per capita':
        continue
    elif key.lower() == country.lower():
        c02_emission_list = [float(i) for i in val]
        year = np.array([i for i in range(1997,2011)])
        emission = np.array(sorted(c02_emission_list))
        plt.plot(year,emission)
        plt.show()
