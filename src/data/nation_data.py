from src.data import dataverse


def download():
    ref = 'doi:10.7910/DVN/BMRPVH/SPI1XO'
    filename = 'nation_data.tab'
    status, headers, encoding = dataverse.download(ref, filename)
    return status, headers, encoding


s, h, e = download()
print('STATUS:\t\t' + str(s))
print('HEADERS:\t' + h)
print('ENCODING:\t' + e)
