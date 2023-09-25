# -*- coding: utf-8 -*-

"""
postnlecommerceapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerceapis.api_helper import APIHelper


class Options2(object):

    """Implementation of the 'Options2' model.

    The delivery option for which the timeframe is calculated. See [Delivery
    Options](#tag/Reference-codes/Delivery-options) for possible values.

    Attributes:
        string (String1Enum): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "string": 'string'
    }

    _optionals = [
        'string',
    ]

    def __init__(self,
                 string=APIHelper.SKIP):
        """Constructor for the Options2 class"""

        # Initialize members of the class
        if string is not APIHelper.SKIP:
            self.string = string 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        string = dictionary.get("string") if dictionary.get("string") else APIHelper.SKIP
        # Return an object of this model
        return cls(string)