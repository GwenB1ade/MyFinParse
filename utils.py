from parser.currency import get_best_currency, get_currency
import pandas as pd

from schemas.bank_schemas import BankSchema, BestCurrencySchema


def convert_to_dataframe(banks: list[BankSchema]) -> pd.DataFrame:
    data = {
        'Bank name': [],
        'Buy USD': [],
        'Sell USD': [],
        'Buy EUR': [],
        'Sell EUR': []
    }
    
    for bank in banks:
        data['Bank name'].append(bank.name)
        data['Buy USD'].append(bank.bank_buy_usd)
        data['Sell USD'].append(bank.bank_sell_usd)
        data['Buy EUR'].append(bank.bank_buy_eur)
        data['Sell EUR'].append(bank.bank_sell_eur)
    
    df = pd.DataFrame(
        data
    )
    
    return df


def convert_best_currency_to_dataframe(bc: BestCurrencySchema) -> pd.DataFrame:
    data = {
        'Currency': ['USD', 'EUR'],
        'Buy': [bc.buy_usd, bc.buy_eur],
        'Sell': [bc.sell_usd, bc.sell_eur]
    }
    
    return pd.DataFrame(data)