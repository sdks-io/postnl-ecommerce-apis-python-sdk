# -*- coding: utf-8 -*-

"""
postnlecommerceapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from postnlecommerceapis.api_helper import APIHelper
import postnlecommerceapis.exceptions.api_exception


class ConfirmingMethodNotAllowedException(postnlecommerceapis.exceptions.api_exception.APIException):
    def __init__(self, reason, response):
        """Constructor for the ConfirmingMethodNotAllowedException class

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            response (HttpResponse): The HttpResponse of the API call.

        """
        super(ConfirmingMethodNotAllowedException, self).__init__(reason, response)
        dictionary = APIHelper.json_deserialize(self.response.text)
        if isinstance(dictionary, dict):
            self.unbox(dictionary)

    def unbox(self, dictionary):
        """Populates the properties of this object by extracting them from a dictionary.

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        """
        self.message = dictionary.get("message") if dictionary.get("message") else None
        self.http_status_code = dictionary.get("http_status_code") if dictionary.get("http_status_code") else None
