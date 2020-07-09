import os
import requests


def download(ref, filename):
    print('Beginning ' + filename + ' download with requests')

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    url = 'https://dataverse.harvard.edu/api/access/datafile/:persistentId?persistentId=' + ref
    file_path = '../../data/external/' + filename
    r = requests.get(url)
    r.raise_for_status()

    with open(file_path, 'wb') as f:
        f.write(r.content)

    return r.status_code, r.headers['content-type'], r.encoding
