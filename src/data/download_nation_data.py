from src.data import download_from_dataverse as dataverse


def download_nation():
    doi = '10.7910/DVN/BMRPVH/SPI1XO'
    filename = 'nation_data.dta'
    status, headers, encoding = dataverse.download(doi=doi, filename=filename)
    return status, headers, encoding


s, h, e = download_nation()
print('STATUS:\t\t' + str(s))
print('HEADERS:\t' + h)
print('ENCODING:\t' + e)
