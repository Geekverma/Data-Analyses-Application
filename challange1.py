import re
l = {}

def csvtolist():
    with open("Emissions.csv","r") as emi_pr_year:
        for item in emi_pr_year:
            key = re.search("[a-z2A-Z ]+",item)
            item = item[len(key.group())+1:].split(',')
            l[key.group()]=item
        
    return l


