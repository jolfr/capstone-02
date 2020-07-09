from src.data.download_from_dataverse import download


def main():
    status, headers, encoding = download_nation()
    print('STATUS:\n' + status)
    print('HEADERS:\n' + headers)
    print('ENCODING:\n' + encoding)


def download_nation():
    doi = '10.7910/DVN/BMRPVH/SPI1XO'
    filename = 'nation_data.dta'
    status, headers, encoding = download(doi, filename)
    return status, headers, encoding
