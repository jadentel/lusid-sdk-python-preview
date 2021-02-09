# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2571
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class InlineAggregationRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'request': 'AggregationRequest',
        'instruments': 'list[WeightedInstrument]'
    }

    attribute_map = {
        'request': 'request',
        'instruments': 'instruments'
    }

    required_map = {
        'request': 'required',
        'instruments': 'required'
    }

    def __init__(self, request=None, instruments=None):  # noqa: E501
        """
        InlineAggregationRequest - a model defined in OpenAPI

        :param request:  (required)
        :type request: lusid.AggregationRequest
        :param instruments:  The set of instruments, weighted by the quantities held that are required.  It is identified by an identifier tag that can be used to identify it externally.  For a single, unique trade or transaction this can be thought of as equivalent to the transaction identifier, or  a composite of the sub-holding keys for a regular sub-holding. When there are multiple transactions sharing the same underlying instrument  such as purchase of shares on multiple dates where tax implications are different this would not be the case. (required)
        :type instruments: list[lusid.WeightedInstrument]

        """  # noqa: E501

        self._request = None
        self._instruments = None
        self.discriminator = None

        self.request = request
        self.instruments = instruments

    @property
    def request(self):
        """Gets the request of this InlineAggregationRequest.  # noqa: E501


        :return: The request of this InlineAggregationRequest.  # noqa: E501
        :rtype: AggregationRequest
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this InlineAggregationRequest.


        :param request: The request of this InlineAggregationRequest.  # noqa: E501
        :type: AggregationRequest
        """
        if request is None:
            raise ValueError("Invalid value for `request`, must not be `None`")  # noqa: E501

        self._request = request

    @property
    def instruments(self):
        """Gets the instruments of this InlineAggregationRequest.  # noqa: E501

        The set of instruments, weighted by the quantities held that are required.  It is identified by an identifier tag that can be used to identify it externally.  For a single, unique trade or transaction this can be thought of as equivalent to the transaction identifier, or  a composite of the sub-holding keys for a regular sub-holding. When there are multiple transactions sharing the same underlying instrument  such as purchase of shares on multiple dates where tax implications are different this would not be the case.  # noqa: E501

        :return: The instruments of this InlineAggregationRequest.  # noqa: E501
        :rtype: list[WeightedInstrument]
        """
        return self._instruments

    @instruments.setter
    def instruments(self, instruments):
        """Sets the instruments of this InlineAggregationRequest.

        The set of instruments, weighted by the quantities held that are required.  It is identified by an identifier tag that can be used to identify it externally.  For a single, unique trade or transaction this can be thought of as equivalent to the transaction identifier, or  a composite of the sub-holding keys for a regular sub-holding. When there are multiple transactions sharing the same underlying instrument  such as purchase of shares on multiple dates where tax implications are different this would not be the case.  # noqa: E501

        :param instruments: The instruments of this InlineAggregationRequest.  # noqa: E501
        :type: list[WeightedInstrument]
        """
        if instruments is None:
            raise ValueError("Invalid value for `instruments`, must not be `None`")  # noqa: E501

        self._instruments = instruments

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineAggregationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
