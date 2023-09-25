# -*- coding: utf-8 -*-

"""
postnlecommerceapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from apimatic_core.utilities.comparison_helper import ComparisonHelper
from postnlecommerceapis.api_helper import APIHelper


class BarcodeControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(BarcodeControllerTests, cls).setUpClass()
        cls.controller = cls.client.barcode
        cls.response_catcher = cls.controller.http_call_back

    # Request example:
    #```
    #curl -X GET "https://api-sandbox.postnl.nl/shipment/v1_1/barcode?CustomerCode=DEVC&amp;CustomerNumber=11223344&amp;Type=3S&amp;Serie=000000000-999999999&amp;Range=NL" \
    # -H "Accept: application/json" \
    # -H "apikey: APIKEY-HERE" 
    #```
    #
    def test_generate_a_unique_barcode(self):
        # Parameters for the API call
        customer_code = 'DEVC'
        customer_number = '11223344'
        mtype = '3S'
        serie = None
        range = 'NL'

        # Perform the API call through the SDK function
        result = self.controller.generate_a_unique_barcode(customer_code, customer_number, mtype, serie, range)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

