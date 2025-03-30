from pydantic import BaseModel


class BankSchema(BaseModel):
    name: str
    bank_buy_usd: float
    bank_sell_usd: float
    bank_buy_eur: float
    bank_sell_eur: float


class BestCurrencySchema(BaseModel):
    buy_usd: float
    sell_usd: float
    buy_eur: float
    sell_eur: float