#Supacharn Kaowanan 653380026-4 Section-1
#PS : Assumed that the code is partly psuedoed, implementation is needed in order to run the code. Not expected to be executable, though the idea is there even if it's a bit unclear.
import requests
from datetime import datetime
from unittest.mock import Mock


class CurrencyExchanger:
    def __init__(self, base_currency="THB", target_currency="USD"):
        self.currency_api = "https://coc-kku-bank.com/foreign-exchange"
        self.base_currency = base_currency
        self.target_currency = target_currency
        self.ex_date = datetime.today().date()
        self.api_response = None

    def get_currency_rate(self):
        try:
            # get the exchange rate
            p = {'from': self.base_currency, 'to': self.target_currency}
            response = requests.get(self.currency_api, params=p)
            if response.status_code in (200, 201):
                self.api_response = response.json()
        except requests.exceptions.RequestException:
            self.api_response = None

    def currency_exchange(self, currencyA,AmountA,currencyB):
        target_a = self.get_currency_rate(currencyA)
        target_b = self.get_currency_rate(currencyB)
        # Implement function to calculate the currency from base currency to the target currency
        
        if(target_a <= target_b):
            converted_result = (AmountA) * (target_b)
        else if(target_b <= target_a):
            converted_result = (AmountA) / (target_b)

        return converted_result
