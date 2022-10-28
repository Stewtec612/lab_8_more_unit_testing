'''
Test bitcoin program by mocking an example of the response the api would give the user



'''

import unittest 
from unittest import TestCase
from unittest.mock import patch 

import bitcoin_converter


class TestBitCoin(TestCase):

    @patch('bitcoin_converter.get_bitcoin_data')
    def test_convert_dollars(self, example_api_response):

        example_api_response.return_value = {"time":{"updated":"Oct 27, 2022 10:00:00 UTC",
            "updatedISO":"2022-10-27T10:00:00+00:00",
            "updateduk":"Oct 27, 2022 at 10:00 GMT"},
            "chartName":"Bitcoin",
            "bpi":{"USD":{"code":"USD","symbol":"&#36;","rate":"17,962.7805","description":"United States Dollar","rate_float":17962.7805},
            "GBP":{"code":"GBP","symbol":"&pound;","rate":"13,532.0990","description":"British Pound Sterling","rate_float":13532.099},
            "EUR":{"code":"EUR","symbol":"&euro;","rate":"15,121.6075","description":"Euro","rate_float":15121.6075}}}


        expected_amount = 5388834.15
        dollars = bitcoin_converter.convert_bitcoin_to_dollars(300)
        self.assertEqual(expected_amount, dollars)


if __name__ == '__main__':
    unittest.main()