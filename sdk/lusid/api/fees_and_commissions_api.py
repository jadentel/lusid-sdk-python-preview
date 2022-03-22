# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4134
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from lusid.api_client import ApiClient
from lusid.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)
from lusid.models.lusid_problem_details import LusidProblemDetails
from lusid.models.lusid_validation_problem_details import LusidValidationProblemDetails
from lusid.models.resource_list_of_fee_calculation_details import ResourceListOfFeeCalculationDetails


class FeesAndCommissionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_applicable_fees(self, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] GetApplicableFees: Get the Fees and Commissions that may be applicable to a transaction.  # noqa: E501

        Additionally, matching can be based on the instrument's properties, its portfolio properties, and any additional property keys present in the data file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_applicable_fees(async_req=True)
        >>> result = thread.get()

        :param instrument_identifier_type: Optional. The unique identifier type to use, eg 'Figi' or 'LusidInstrumentId'.
        :type instrument_identifier_type: str
        :param instrument_identifier: Optional. The Instrument Identifier to get properties for.
        :type instrument_identifier: str
        :param portfolio_scope: Optional. The scope of the portfolio to fetch additional properties from.
        :type portfolio_scope: str
        :param portfolio_code: Optional. The code of the portfolio to fetch additional properties from.
        :type portfolio_code: str
        :param additional_search_keys: Any other property keys or fields and their corresponding values that should be matched for fees. Eg. \"Instrument/default/Name=exampleValue\" or \"AdditionalKey2=Value2\".              The list of fields available is as follows : \"RuleName\", \"Country\", \"FeeType\", \"FeeRate\", \"MinFee\", \"MaxFee\", \"PropertyKey\",               \"TransactionType\", \"Counterparty\", \"SettlementCurrency\", \"TransactionCurrency\", \"ExecutionBroker\",               \"Custodian\", \"Exchange\"
        :type additional_search_keys: list[str]
        :param file_name: Optionally provide the filename of an alternative to the default fees file ({fees.csv})              in your {fees-and-commissions} Drive folder, to support different fee structures.              For example, you might use one to understand the effect of different fees when considering a change in broker.
        :type file_name: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResourceListOfFeeCalculationDetails
        """
        kwargs['_return_http_data_only'] = True
        return self.get_applicable_fees_with_http_info(**kwargs)  # noqa: E501

    def get_applicable_fees_with_http_info(self, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] GetApplicableFees: Get the Fees and Commissions that may be applicable to a transaction.  # noqa: E501

        Additionally, matching can be based on the instrument's properties, its portfolio properties, and any additional property keys present in the data file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_applicable_fees_with_http_info(async_req=True)
        >>> result = thread.get()

        :param instrument_identifier_type: Optional. The unique identifier type to use, eg 'Figi' or 'LusidInstrumentId'.
        :type instrument_identifier_type: str
        :param instrument_identifier: Optional. The Instrument Identifier to get properties for.
        :type instrument_identifier: str
        :param portfolio_scope: Optional. The scope of the portfolio to fetch additional properties from.
        :type portfolio_scope: str
        :param portfolio_code: Optional. The code of the portfolio to fetch additional properties from.
        :type portfolio_code: str
        :param additional_search_keys: Any other property keys or fields and their corresponding values that should be matched for fees. Eg. \"Instrument/default/Name=exampleValue\" or \"AdditionalKey2=Value2\".              The list of fields available is as follows : \"RuleName\", \"Country\", \"FeeType\", \"FeeRate\", \"MinFee\", \"MaxFee\", \"PropertyKey\",               \"TransactionType\", \"Counterparty\", \"SettlementCurrency\", \"TransactionCurrency\", \"ExecutionBroker\",               \"Custodian\", \"Exchange\"
        :type additional_search_keys: list[str]
        :param file_name: Optionally provide the filename of an alternative to the default fees file ({fees.csv})              in your {fees-and-commissions} Drive folder, to support different fee structures.              For example, you might use one to understand the effect of different fees when considering a change in broker.
        :type file_name: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object, the HTTP status code, and the headers.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: (ResourceListOfFeeCalculationDetails, int, HTTPHeaderDict)
        """

        local_var_params = locals()

        all_params = [
            'instrument_identifier_type',
            'instrument_identifier',
            'portfolio_scope',
            'portfolio_code',
            'additional_search_keys',
            'file_name'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_applicable_fees" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and ('portfolio_scope' in local_var_params and  # noqa: E501
                                                        len(local_var_params['portfolio_scope']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `portfolio_scope` when calling `get_applicable_fees`, length must be less than or equal to `64`")  # noqa: E501
        if self.api_client.client_side_validation and ('portfolio_scope' in local_var_params and  # noqa: E501
                                                        len(local_var_params['portfolio_scope']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `portfolio_scope` when calling `get_applicable_fees`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'portfolio_scope' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['portfolio_scope']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `portfolio_scope` when calling `get_applicable_fees`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('portfolio_code' in local_var_params and  # noqa: E501
                                                        len(local_var_params['portfolio_code']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `portfolio_code` when calling `get_applicable_fees`, length must be less than or equal to `64`")  # noqa: E501
        if self.api_client.client_side_validation and ('portfolio_code' in local_var_params and  # noqa: E501
                                                        len(local_var_params['portfolio_code']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `portfolio_code` when calling `get_applicable_fees`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'portfolio_code' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['portfolio_code']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `portfolio_code` when calling `get_applicable_fees`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        if self.api_client.client_side_validation and 'file_name' in local_var_params and not re.search(r'^[A-Za-z0-9_\-\.]+[A-Za-z0-9_\-\. ]*$', local_var_params['file_name']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `file_name` when calling `get_applicable_fees`, must conform to the pattern `/^[A-Za-z0-9_\-\.]+[A-Za-z0-9_\-\. ]*$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instrument_identifier_type' in local_var_params and local_var_params['instrument_identifier_type'] is not None:  # noqa: E501
            query_params.append(('instrumentIdentifierType', local_var_params['instrument_identifier_type']))  # noqa: E501
        if 'instrument_identifier' in local_var_params and local_var_params['instrument_identifier'] is not None:  # noqa: E501
            query_params.append(('instrumentIdentifier', local_var_params['instrument_identifier']))  # noqa: E501
        if 'portfolio_scope' in local_var_params and local_var_params['portfolio_scope'] is not None:  # noqa: E501
            query_params.append(('portfolioScope', local_var_params['portfolio_scope']))  # noqa: E501
        if 'portfolio_code' in local_var_params and local_var_params['portfolio_code'] is not None:  # noqa: E501
            query_params.append(('portfolioCode', local_var_params['portfolio_code']))  # noqa: E501
        if 'additional_search_keys' in local_var_params and local_var_params['additional_search_keys'] is not None:  # noqa: E501
            query_params.append(('additionalSearchKeys', local_var_params['additional_search_keys']))  # noqa: E501
            collection_formats['additionalSearchKeys'] = 'multi'  # noqa: E501
        if 'file_name' in local_var_params and local_var_params['file_name'] is not None:  # noqa: E501
            query_params.append(('fileName', local_var_params['file_name']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"


        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.11.4134'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            200: "ResourceListOfFeeCalculationDetails",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/feesandcommissions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def list_all_fees(self, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] ListAllFees: List the rules available for fees and commissions.  # noqa: E501

        By default, will list ALL rules available. Additional keys and be specified to list a smaller subset of rules.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_all_fees(async_req=True)
        >>> result = thread.get()

        :param additional_search_keys: Any other property keys or fields and their corresponding values that should be matched to reduce the list of rules returned. Eg. \"Instrument/default/Name=exampleValue\" or \"AdditionalKey2=Value2\".              The minimum list of fields available is as follows : \"RuleName\", \"Country\", \"FeeCalculationMethod\", \"FeeMultiplier\", \"MinFeeCalculationMethod\",              \"MinFeeMultiplier\", \"MaxFeeCalculationMethod\", \"MaxFeeMultiplier\", \"PropertyKey\",              \"TransactionType\", \"Counterparty\", \"SettlementCurrency\", \"TransactionCurrency\", \"ExecutionBroker\",              \"Custodian\", \"Exchange\"
        :type additional_search_keys: list[str]
        :param file_name: Optionally provide the filename of an alternative to the default fees file ({fees.csv})              in your Drive {fees-and-commissions} folder, to support different fee structures.              For example, you might use one to understand the effect of different fees when considering a change in broker.
        :type file_name: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResourceListOfFeeCalculationDetails
        """
        kwargs['_return_http_data_only'] = True
        return self.list_all_fees_with_http_info(**kwargs)  # noqa: E501

    def list_all_fees_with_http_info(self, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] ListAllFees: List the rules available for fees and commissions.  # noqa: E501

        By default, will list ALL rules available. Additional keys and be specified to list a smaller subset of rules.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_all_fees_with_http_info(async_req=True)
        >>> result = thread.get()

        :param additional_search_keys: Any other property keys or fields and their corresponding values that should be matched to reduce the list of rules returned. Eg. \"Instrument/default/Name=exampleValue\" or \"AdditionalKey2=Value2\".              The minimum list of fields available is as follows : \"RuleName\", \"Country\", \"FeeCalculationMethod\", \"FeeMultiplier\", \"MinFeeCalculationMethod\",              \"MinFeeMultiplier\", \"MaxFeeCalculationMethod\", \"MaxFeeMultiplier\", \"PropertyKey\",              \"TransactionType\", \"Counterparty\", \"SettlementCurrency\", \"TransactionCurrency\", \"ExecutionBroker\",              \"Custodian\", \"Exchange\"
        :type additional_search_keys: list[str]
        :param file_name: Optionally provide the filename of an alternative to the default fees file ({fees.csv})              in your Drive {fees-and-commissions} folder, to support different fee structures.              For example, you might use one to understand the effect of different fees when considering a change in broker.
        :type file_name: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object, the HTTP status code, and the headers.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: (ResourceListOfFeeCalculationDetails, int, HTTPHeaderDict)
        """

        local_var_params = locals()

        all_params = [
            'additional_search_keys',
            'file_name'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_all_fees" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'file_name' in local_var_params and not re.search(r'^[A-Za-z0-9_\-\.]+[A-Za-z0-9_\-\. ]*$', local_var_params['file_name']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `file_name` when calling `list_all_fees`, must conform to the pattern `/^[A-Za-z0-9_\-\.]+[A-Za-z0-9_\-\. ]*$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'additional_search_keys' in local_var_params and local_var_params['additional_search_keys'] is not None:  # noqa: E501
            query_params.append(('additionalSearchKeys', local_var_params['additional_search_keys']))  # noqa: E501
            collection_formats['additionalSearchKeys'] = 'multi'  # noqa: E501
        if 'file_name' in local_var_params and local_var_params['file_name'] is not None:  # noqa: E501
            query_params.append(('fileName', local_var_params['file_name']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"


        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.11.4134'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            200: "ResourceListOfFeeCalculationDetails",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/feesandcommissions/rules', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
