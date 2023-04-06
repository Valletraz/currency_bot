import requests
import json
from config import keys
from tconfig import CURRATE_TOKEN


# class ConvertException(Exception):
#     pass

class APIException(Exception):
    pass


# class CryptoConverter:
#     @staticmethod
#     def convert(quote: str, base: str, amount: str):
#         if quote == base:
#             raise ConvertException(f'Невозможно перевести одинаковые валюты {base}.')
#
#         try:
#             quote_ticker = keys[quote]
#         except KeyError:
#             raise ConvertException(f'Не удалось обработать валюты {quote}')
#
#         try:
#             base_ticker = keys[base]
#         except KeyError:
#             raise ConvertException(f'Не удалось обработать валюты {base}')
#
#         try:
#             amount = float(amount)
#         except ValueError:
#             raise ConvertException(f'Не удалось обработать количество {amount}')
#
#         r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
#         total_base = json.loads(r.content)[keys[base]]
#
#         return total_base

class CurrencyConvertor:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюты {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюты {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://currate.ru/api/?get=rates&pairs={keys[quote]}{keys[base]}&key={CURRATE_TOKEN}')
        cur_pair = keys[quote] + keys[base]
        print(cur_pair)
        total_base = json.loads(r.content)['data'][cur_pair]

        # {"status": "200", "message": "rates", "data": {"EURRUB": "71.3846", "USDRUB": "58.059"}}
        # https://currate.ru/api/?get=currency_list&key={CURRATE_TOKEN}
        # https://currate.ru/api/?get=rates&pairs={keys[quote]}{keys[base]}&key={CURRATE_TOKEN}


        return total_base
