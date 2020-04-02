import requests, json

URL = "http://api.nbp.pl/api/exchangerates/rates/A/"


def getCurrencyRate(currency):
    currURL = URL + currency + "?format=json"
    result = requests.get(currURL).text
    result = json.loads(result)
    currencyRate = {
        'name': result['currency'],
        'code': result['code'],
        'rate': result['rates'][0]['mid']
    }
    return currencyRate


def exchangePLN(amount, currencyRate):
    return round(amount / currencyRate['rate'], 2)


def getListOfExchangedCurrencies(pln, currencies):
    currencyRateResults = list()
    for i in currencies:
        oneResult = getCurrencyRate(i)
        oneResult['exchanged'] = exchangePLN(pln, oneResult)
        currencyRateResults.append(oneResult)
    return currencyRateResults
