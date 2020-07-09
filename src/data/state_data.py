from src.data import dataverse


def download_state():
    doi = '10.7910/DVN/BMRPVH/MR5DYF'
    filename = 'state_data.dta'
    status, headers, encoding = dataverse.download(doi=doi, filename=filename)
    return status, headers, encoding


s, h, e = download_state()
print('STATUS:\t\t' + str(s))
print('HEADERS:\t' + h)
print('ENCODING:\t' + e)
