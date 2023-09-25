# -*- coding: utf-8 -*-

"""
postnlecommerceapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerceapis.api_helper import APIHelper
from postnlecommerceapis.models.friday_1 import Friday1
from postnlecommerceapis.models.monday_1 import Monday1
from postnlecommerceapis.models.saturday_1 import Saturday1
from postnlecommerceapis.models.sunday_1 import Sunday1
from postnlecommerceapis.models.thursday_1 import Thursday1
from postnlecommerceapis.models.tuesday_1 import Tuesday1
from postnlecommerceapis.models.wednesday_1 import Wednesday1


class OpeningHours1(object):

    """Implementation of the 'OpeningHours1' model.

    The standard opening times of the pickup location

    Attributes:
        monday (Monday1): TODO: type description here.
        tuesday (Tuesday1): TODO: type description here.
        wednesday (Wednesday1): TODO: type description here.
        thursday (Thursday1): TODO: type description here.
        friday (Friday1): TODO: type description here.
        saturday (Saturday1): TODO: type description here.
        sunday (Sunday1): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "monday": 'Monday',
        "tuesday": 'Tuesday',
        "wednesday": 'Wednesday',
        "thursday": 'Thursday',
        "friday": 'Friday',
        "saturday": 'Saturday',
        "sunday": 'Sunday'
    }

    _optionals = [
        'monday',
        'tuesday',
        'wednesday',
        'thursday',
        'friday',
        'saturday',
        'sunday',
    ]

    def __init__(self,
                 monday=APIHelper.SKIP,
                 tuesday=APIHelper.SKIP,
                 wednesday=APIHelper.SKIP,
                 thursday=APIHelper.SKIP,
                 friday=APIHelper.SKIP,
                 saturday=APIHelper.SKIP,
                 sunday=APIHelper.SKIP):
        """Constructor for the OpeningHours1 class"""

        # Initialize members of the class
        if monday is not APIHelper.SKIP:
            self.monday = monday 
        if tuesday is not APIHelper.SKIP:
            self.tuesday = tuesday 
        if wednesday is not APIHelper.SKIP:
            self.wednesday = wednesday 
        if thursday is not APIHelper.SKIP:
            self.thursday = thursday 
        if friday is not APIHelper.SKIP:
            self.friday = friday 
        if saturday is not APIHelper.SKIP:
            self.saturday = saturday 
        if sunday is not APIHelper.SKIP:
            self.sunday = sunday 

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
        monday = Monday1.from_dictionary(dictionary.get('Monday')) if 'Monday' in dictionary.keys() else APIHelper.SKIP
        tuesday = Tuesday1.from_dictionary(dictionary.get('Tuesday')) if 'Tuesday' in dictionary.keys() else APIHelper.SKIP
        wednesday = Wednesday1.from_dictionary(dictionary.get('Wednesday')) if 'Wednesday' in dictionary.keys() else APIHelper.SKIP
        thursday = Thursday1.from_dictionary(dictionary.get('Thursday')) if 'Thursday' in dictionary.keys() else APIHelper.SKIP
        friday = Friday1.from_dictionary(dictionary.get('Friday')) if 'Friday' in dictionary.keys() else APIHelper.SKIP
        saturday = Saturday1.from_dictionary(dictionary.get('Saturday')) if 'Saturday' in dictionary.keys() else APIHelper.SKIP
        sunday = Sunday1.from_dictionary(dictionary.get('Sunday')) if 'Sunday' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(monday,
                   tuesday,
                   wednesday,
                   thursday,
                   friday,
                   saturday,
                   sunday)