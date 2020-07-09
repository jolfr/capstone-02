import os
import requests


def download(doi, filename):
    print('Beginning ' + filename + ' download with requests')

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    url = 'https://dataverse.harvard.edu/api/access/datafile/:persistentId?persistentId=doi:' + doi
    file_path = '../../data/external/' + filename
    r = requests.get(url)

    with open(file_path, 'wb') as f:
        f.write(r.content)

    # Return HTTP meta-data
    return r.status_code, r.headers['content-type'], r.encoding
