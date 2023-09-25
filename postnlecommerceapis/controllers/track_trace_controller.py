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
from postnlecommerceapis.models.shippingstatus_response import ShippingstatusResponse
from postnlecommerceapis.models.shippingstatus_response_signature import ShippingstatusResponseSignature
from postnlecommerceapis.models.shippingstatus_response_updated_shipment import ShippingstatusResponseUpdatedShipment
from postnlecommerceapis.exceptions.shippingstatus_response_error_exception import ShippingstatusResponseErrorException
from postnlecommerceapis.exceptions.shippingstatus_unauthorized_exception import ShippingstatusUnauthorizedException
from postnlecommerceapis.exceptions.shippingstatus_method_not_allowed_exception import ShippingstatusMethodNotAllowedException
from postnlecommerceapis.exceptions.shippingstatus_too_many_request_exception import ShippingstatusTooManyRequestException


class TrackTraceController(BaseController):

    """A Controller to access Endpoints in the postnlecommerceapis API."""
    def __init__(self, config):
        super(TrackTraceController, self).__init__(config)

    def returns_the_statuses_for_a_particular_barcode(self,
                                                      barcode,
                                                      detail=False,
                                                      language=None,
                                                      max_days=None):
        """Does a GET request to /shipment/v2/status/barcode/{barcode}.

        Request example:
        ```
        curl -X GET
        "https://api-sandbox.postnl.nl/shipment/v2/status/barcode/3SDEVC1726492
        58" \
         -H "Accept: application/json" \
         -H "apikey: APIKEY-HERE" \
        ```

        Args:
            barcode (str): Barcode of the shipment. This is a unique value.
            detail (bool, optional): Option to include old statuses in the
                response
            language (LanguageEnum, optional): Language of the returned
                shipment and status descriptions (default is Dutch).
            max_days (str, optional): Limit the number of days that will be
                searched (decrease this amount for better performance).

        Returns:
            ShippingstatusResponse: Response from the API. Status object

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/shipment/v2/status/barcode/{barcode}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('barcode')
                            .value(barcode)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('detail')
                         .value(detail))
            .query_param(Parameter()
                         .key('language')
                         .value(language))
            .query_param(Parameter()
                         .key('maxDays')
                         .value(max_days))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ShippingstatusResponse.from_dictionary)
            .local_error('400', 'Invalid request', ShippingstatusResponseErrorException)
            .local_error('401', 'Invalid apikey', ShippingstatusUnauthorizedException)
            .local_error('405', 'Method not allowed', ShippingstatusMethodNotAllowedException)
            .local_error('429', 'Too many requests', ShippingstatusTooManyRequestException)
            .local_error('500', 'Internal server error', ShippingstatusResponseErrorException)
        ).execute()

    def get_status_information_by_customer_reference(self,
                                                     customer_code,
                                                     customer_number,
                                                     reference_id,
                                                     detail=False,
                                                     language=None,
                                                     max_days=None):
        """Does a GET request to /shipment/v2/status/reference/{referenceId}.

        Request example:
        ```
        curl -X GET
        "https://api-sandbox.postnl.nl/shipment/v2/status/reference?detail=true
        &language=NL&customerCode={{CustomerCode}}&customerNumber={{CustomerNum
        ber}}&reference=REF98173245876329" \
         -H "Accept: application/json" \
         -H "apikey: APIKEY-HERE" 
        ```

        Args:
            customer_code (str): Customer code as known at PostNL Pakketten
            customer_number (str): Customer number as known at PostNL
                Pakketten
            reference_id (str): The customer reference belonging to the
                shipment
            detail (bool, optional): Option to include old statuses in the
                response
            language (LanguageEnum, optional): Language of the returned
                shipment and status descriptions (default is Dutch).
            max_days (str, optional): Limit the number of days that will be
                searched (decrease this amount for better performance). By
                default this is 90 days in the past.

        Returns:
            ShippingstatusResponse: Response from the API. Status object

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/shipment/v2/status/reference/{referenceId}')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('customerCode')
                         .value(customer_code))
            .query_param(Parameter()
                         .key('customerNumber')
                         .value(customer_number))
            .template_param(Parameter()
                            .key('referenceId')
                            .value(reference_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('detail')
                         .value(detail))
            .query_param(Parameter()
                         .key('language')
                         .value(language))
            .query_param(Parameter()
                         .key('maxDays')
                         .value(max_days))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ShippingstatusResponse.from_dictionary)
            .local_error('400', 'Invalid request', ShippingstatusResponseErrorException)
            .local_error('401', 'Invalid apikey', ShippingstatusUnauthorizedException)
            .local_error('405', 'Method not allowed', ShippingstatusMethodNotAllowedException)
            .local_error('429', 'Too many requests', ShippingstatusTooManyRequestException)
            .local_error('500', 'Internal server error', ShippingstatusResponseErrorException)
        ).execute()

    def returns_the_signature_of_a_particular_shipment(self,
                                                       barcode):
        """Does a GET request to /shipment/v2/status/signature/{barcode}.

        Request example:
        ```
        curl -X GET
        "https://api-sandbox.postnl.nl/shipment/v2/status/signature/3SDEVC17264
        9258" \
         -H "Accept: application/json" \
         -H "apikey: APIKEY-HERE" 
        ```

        Args:
            barcode (str): Barcode of the shipment

        Returns:
            ShippingstatusResponseSignature: Response from the API. A
                signature

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/shipment/v2/status/signature/{barcode}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('barcode')
                            .value(barcode)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ShippingstatusResponseSignature.from_dictionary)
            .local_error('400', 'Invalid request', ShippingstatusResponseErrorException)
            .local_error('401', 'Invalid apikey', ShippingstatusUnauthorizedException)
            .local_error('405', 'Method not allowed', ShippingstatusMethodNotAllowedException)
            .local_error('429', 'Too many requests', ShippingstatusTooManyRequestException)
            .local_error('500', 'Internal server error', ShippingstatusResponseErrorException)
        ).execute()

    def returns_the_updated_statuses_for_a_particular_customer_number(self,
                                                                      customernumber,
                                                                      period=None):
        """Does a GET request to /shipment/v2/status/{customernumber}/updatedshipments.

        Request example:
        ```
        curl -X GET
        "https://api-sandbox.postnl.nl/shipment/v2/status/11223344/updatedshipm
        ents?period=2022-12-25T10:00:00&amp;period=2022-12-25T10:12:00" \
         -H "Accept: application/json" \
         -H "apikey: APIKEY-HERE" \
        ```

        Args:
            customernumber (str): Your customer number
            period (List[str], optional): Optional array which defines a
                specific period in which to return updated shipments. For
                optimal results, schedule calls at a frequency between 5-15
                minutes and align the requested period accordingly to ensure
                complete coverage of past updates. Shorter periods yield
                improved response times. The API accommodates a maximum
                requested period of 2 hours, granting access to shipment data
                up to 48 hours in the past. Please use the following format:
                YYYY-MM-DDTHH:MM:SS and repeat this variable to define the
                period (e.g.
                /updatedshipments?period=2022-11-07T12:00:00.000&period=2022-11
                -07T12:05:00.000).

        Returns:
            List[ShippingstatusResponseUpdatedShipment]: Response from the
                API. Updated statuses

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/shipment/v2/status/{customernumber}/updatedshipments')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('customernumber')
                            .value(customernumber)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('period')
                         .value(period))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ShippingstatusResponseUpdatedShipment.from_dictionary)
            .local_error('400', 'Invalid request', ShippingstatusResponseErrorException)
            .local_error('401', 'Invalid apikey', ShippingstatusUnauthorizedException)
            .local_error('405', 'Method not allowed', ShippingstatusMethodNotAllowedException)
            .local_error('429', 'Too many requests', ShippingstatusTooManyRequestException)
            .local_error('500', 'Internal server error', ShippingstatusResponseErrorException)
        ).execute()