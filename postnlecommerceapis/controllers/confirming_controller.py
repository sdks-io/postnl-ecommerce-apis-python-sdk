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
from postnlecommerceapis.models.confirming_response import ConfirmingResponse
from postnlecommerceapis.exceptions.confirming_response_error_exception import ConfirmingResponseErrorException
from postnlecommerceapis.exceptions.confirming_unauthorized_exception import ConfirmingUnauthorizedException
from postnlecommerceapis.exceptions.confirming_method_not_allowed_exception import ConfirmingMethodNotAllowedException
from postnlecommerceapis.exceptions.confirming_too_many_request_exception import ConfirmingTooManyRequestException
from postnlecommerceapis.exceptions.confirming_response_error_1_exception import ConfirmingResponseError1Exception


class ConfirmingController(BaseController):

    """A Controller to access Endpoints in the postnlecommerceapis API."""
    def __init__(self, config):
        super(ConfirmingController, self).__init__(config)

    def confirm_a_shipment_to_post_nl(self,
                                      body):
        """Does a POST request to /shipment/v2/confirm.

        Confirm a shipment to PostNL

        Args:
            body (ConfirmingRequest): TODO: type description here.

        Returns:
            ConfirmingResponse: Response from the API. A confirmation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/shipment/v2/confirm')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ConfirmingResponse.from_dictionary)
            .local_error('400', 'Error payload', ConfirmingResponseErrorException)
            .local_error('401', 'Invalid apikey', ConfirmingUnauthorizedException)
            .local_error('405', 'Method not allowed', ConfirmingMethodNotAllowedException)
            .local_error('429', 'Too many requests', ConfirmingTooManyRequestException)
            .local_error('500', 'Internal server error', ConfirmingResponseError1Exception)
        ).execute()
