from challange1 import csvtolist
import csv
import sys



country_one = sys.argv[1]
country_two = sys.argv[2]
country_three = sys.argv[3]
read_csv = csvtolist()
fields = ['CO2 per capita','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010']
with open("Emissions.csv","r")  as file_one:
    with open("test.csv","w") as file_two:
        writer = csv.writer(file_two)
        writer.writerow(fields)
        for item in file_one:                           
            if country_one.lower() in item.lower():
                writer.writerow(item.split(','))

            elif country_two.lower() in item.lower():
                writer.writerow(item.split(','))

            elif country_three.lower() in item.lower():
                writer.writerow(item.split(','))
            
           
                        
        
            
   
