import requests
import os.path
import xml.etree.ElementTree as ET

EXCHANGE_RATE_FILE = 'eurofxref-daily.xml'
EXCHANGE_URL = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml'


def isExist(path):
    return os.path.exists(path)


def strToPostiveNumber(n):
    try:
        number = float(n)
    except ValueError:
        raise ValueError('the value {} can not convert to integer'.format(n))

    if number < 0:
        raise ValueError('the value {} is must larger than 0'.format(n))

    return number


def download_file(url, filename=None):
    if filename:
        local_filename = filename
    else:
        local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:    # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
    return local_filename

def xmlToDict(file):
    tree = ET.parse(file)
    root = tree.getroot()
    exchange_dict = {}
    for country in root.findall('.//*[@rate]'):
        exchange_dict[country.get('currency')] = float(country.get('rate'))
    return exchange_dict


def askPrompt():
    if not isExist(EXCHANGE_RATE_FILE):
        download_file(url=EXCHANGE_URL, filename=EXCHANGE_RATE_FILE)
    exchange_dict = xmlToDict(EXCHANGE_RATE_FILE)

    changes = strToPostiveNumber(
        input('How many euros are you exchanging?'))
    currency = input('Which currency you want to exchange?')
    if currency in exchange_dict:
        rate = exchange_dict.get(currency)
        print('{} euros at an exchange rate of {} is {:.2f} U.S. dollars.'.
              format(changes, rate * 100, changes * rate))
    else:
        print(
            'sorry, the currency is not support. below are we support currency:\n{}'.
            format(','.join(exchange_dict.keys())))


if __name__ == '__main__':
    askPrompt()