import os
import requests

print('Beginning file download with requests')

os.chdir(os.path.dirname(os.path.abspath(__file__)))

url = 'https://dataverse.harvard.edu/api/access/datafile/:persistentId?persistentId=doi:10.7910/DVN/BMRPVH/SPI1XO'
filename = '../../data/external/nation_data.sta'
r = requests.get(url)

with open(filename, 'wb') as f:
    f.write(r.content)

# Retrieve HTTP meta-data
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
