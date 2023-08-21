from challange1 import csvtolist

#Take input
print("Enter year to see results")
year = input()
#extract index of year in list of year in dictionary

c02_emission_dict = csvtolist()
c02_emission_list = []
if year in c02_emission_dict['CO2 per capita']:
    year_index = c02_emission_dict['CO2 per capita'].index(year)
#creat a list of emission in that year in all countries
#loop over the dictionary value and in list loop till index & append that year
for key,value in c02_emission_dict.items():
    if key == 'CO2 per capita':
        continue
    c02_emission_list += [float(i) for i in value if value.index(i)==year_index]

max_emission = max(c02_emission_list)
min_emission = min(c02_emission_list)
average_emission = (float(max_emission)+float(min_emission))/2

#search for the key(country) for which above values match
country1, country2 = '',''
for k,v in c02_emission_dict.items():
    if key == 'CO2 per capita':
        continue
    elif str(max_emission) in v:
        country1 = k
    elif str(min_emission) in v:
        country2 = k

print(f"In {year}, countries with maximum emission is {country1} and minimum emission is {country2} repectilvely\nAverage C02 emission in {year} were {average_emission}")
