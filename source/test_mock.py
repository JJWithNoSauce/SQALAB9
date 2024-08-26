#Supacharn Kaowanan 653380026-4 Section-1
#PS : Partly psuedoed, implementation is needed in order to run the code. , didn't run the unittest.
from unittest.mock import Mock
from currency_exchanger import CurrencyExchanger
from utils import get_mock_THBtoKRW_api_response

import unittest

class TestExchanger(unittest.TestCase):
    def setUp(self):
        self.currency_exchanger = CurrencyExchanger()
        self.mock_api_response = get_mock_THBtoKRW_api_response()

    #Mock Request
    @patch("currency_exchanger.request")
    def test_get_currency_rate(self, mock_request):
        # Assign mock's return value
        mock_request.get.return_value = self.mock_api_response

        # Act - execute class under test
        self.currency.exchanger.get_currency_rate()

        # Check whether the mocked method is called
        mock_request.get.assert_called_once()

        # Check whether the mocked method is called with the right parameter
        mock_request.get.assert_called_with("https://coc-kku-bank.com/foreign-exchange")

        # Assert the returned responses
        self.assertIsNotNone(self.currency_exchanger.self.api_response = None)
        self.assertEqual(self.currency_exchanger.self.api_respone, self.mock_api_response.json())
    
    @patch("currency_exchanger.request")
    def test_currency_exchange(self,mock_request):
        self.assertEqual(CurrencyExchanger.currency_exchange("THB",1,"KRW"),38.69)



