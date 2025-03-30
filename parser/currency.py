import requests
from bs4 import BeautifulSoup
from schemas.bank_schemas import BankSchema, BestCurrencySchema


URL = 'https://myfin.by/currency/grodno?utm_source=myfin&utm_medium=organic&utm_campaign=menu&working=0'


def get_html():
    html = requests.get(URL).text 
    return html

def get_currency() -> list[BankSchema]:
    soap = BeautifulSoup(get_html(), 'html.parser')
    all_currencies = soap.find_all('tr', class_ = 'currencies-courses__row-main')
    banks_name = []
    banks = []
    for i in all_currencies:
        bank_info = i.find_next('td', class_ = 'pos-r')
        bank_name: str = bank_info.text
        if bank_name not in banks_name:
            banks_name.append(bank_name)
            bank_currencies = bank_info.find_all_next('td', class_ = 'currencies-courses__currency-cell', limit = 4 )
            bank_currencies = [i.text for i in bank_currencies]
            bank = BankSchema(
                name = bank_name.strip(),
                bank_buy_usd = bank_currencies[0],
                bank_sell_usd = bank_currencies[1],
                bank_buy_eur = bank_currencies[2],
                bank_sell_eur = bank_currencies[3]
            )
            banks.append(bank)
    
    return banks


def get_best_currency():
    soap = BeautifulSoup(get_html(), 'html.parser')
    bests = soap.find_all('div', class_ = 'course-brief-info__body', limit = 2)[1].find_all('div', class_ = 'course-brief-info__r', limit = 2)
    c = []
    for row in bests:
        currencies = row.find_all('div', class_ = 'course-brief-info__b')
        for i in currencies:
            c.append(i.text) if i.text != '' else None
            
    return BestCurrencySchema(
        buy_usd = c[0],
        sell_usd = c[1],
        buy_eur = c[2],
        sell_eur = c[3]
    )
    


