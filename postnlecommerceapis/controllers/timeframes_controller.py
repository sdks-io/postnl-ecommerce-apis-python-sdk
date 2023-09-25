# -*- coding: utf-8 -*-

"""
postnlecommerceapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from postnlecommerceapis.api_helper import APIHelper
from postnlecommerceapis.configuration import Server
from postnlecommerceapis.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from postnlecommerceapis.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from apimatic_core.authentication.multiple.and_auth_group import And
from apimatic_core.authentication.multiple.or_auth_group import Or
from postnlecommerceapis.models.timeframe_response import TimeframeResponse
from postnlecommerceapis.exceptions.timeframe_response_invalid_exception import TimeframeResponseInvalidException
from postnlecommerceapis.exceptions.post_cif_timeframe_unauthorized_exception import PostCIFTimeframeUnauthorizedException
from postnlecommerceapis.exceptions.post_cif_timeframe_method_not_allowed_exception import PostCIFTimeframeMethodNotAllowedException
from postnlecommerceapis.exceptions.post_cif_timeframe_too_many_request_exception import PostCIFTimeframeTooManyRequestException
from postnlecommerceapis.exceptions.timeframe_response_error_exception import TimeframeResponseErrorException


class TimeframesController(BaseController):

    """A Controller to access Endpoints in the postnlecommerceapis API."""
    def __init__(self, config):
        super(TimeframesController, self).__init__(config)

    def retrieve_expected_delivery_timeframes(self,
                                              allow_sunday_sorting,
                                              start_date,
                                              end_date,
                                              country_code,
                                              postal_code,
                                              house_number,
                                              options,
                                              house_nr_ext=None,
                                              city=None,
                                              street=None):
        """Does a GET request to /shipment/v2_1/calculate/timeframes.

        Request example:
        ```
        curl -X GET
        "https://api-sandbox.postnl.nl/shipment/v2_1/calculate/timeframes?Allow
        SundaySorting=false&StartDate=30-06-2022&EndDate=02-07-2022&CountryCode
        =NL&PostalCode=2132WT&HouseNumber=42&HouseNrExt=A&City=Hoofddorp&Street
        =Siriusdreef&Options=Daytime%2CEvening" \
         -H "Accept: application/json" \
         -H "apikey: APIKEY-HERE" \
        ```

        Args:
            allow_sunday_sorting (bool): Whether or not the requesting party
                allows for Sunday sorting (which leads to delivery on
                Monday).
            start_date (str): Date of the beginning of the timeframe. Format:
                dd-MM-yyyy
            end_date (str): Date of the enddate of the timeframe.
                Format:dd-MM-yyyy. Enddate may not be before StartDate.
            country_code (CountryCode1Enum): The ISO2 country code of the
                delivery address
            postal_code (str): Zipcode of the delivery address
            house_number (int): The house number of the delivery address
            options (List[Options1Enum]): The delivery options for which
                expected timeframes should be calculated. At least one
                delivery option must be specified. Multiple values should be
                comma-separated.
            house_nr_ext (str, optional): House number extension of the
                delivery address
            city (str, optional): City of the delivery address
            street (str, optional): The street name of the delivery address

        Returns:
            TimeframeResponse: Response from the API. Calculated delivery
                timeframes

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/shipment/v2_1/calculate/timeframes')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('AllowSundaySorting')
                         .value(allow_sunday_sorting))
            .query_param(Parameter()
                         .key('StartDate')
                         .value(start_date))
            .query_param(Parameter()
                         .key('EndDate')
                         .value(end_date))
            .query_param(Parameter()
                         .key('CountryCode')
                         .value(country_code))
            .query_param(Parameter()
                         .key('PostalCode')
                         .value(postal_code))
            .query_param(Parameter()
                         .key('HouseNumber')
                         .value(house_number))
            .query_param(Parameter()
                         .key('Options')
                         .value(options))
            .query_param(Parameter()
                         .key('HouseNrExt')
                         .value(house_nr_ext))
            .query_param(Parameter()
                         .key('City')
                         .value(city))
            .query_param(Parameter()
                         .key('Street')
                         .value(street))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(TimeframeResponse.from_dictionary)
            .local_error('400', 'Invalid request', TimeframeResponseInvalidException)
            .local_error('401', 'Unauthorized', PostCIFTimeframeUnauthorizedException)
            .local_error('405', 'Method not allowed', PostCIFTimeframeMethodNotAllowedException)
            .local_error('429', 'Too many requests', PostCIFTimeframeTooManyRequestException)
            .local_error('500', 'Invalid request', TimeframeResponseErrorException)
        ).execute()