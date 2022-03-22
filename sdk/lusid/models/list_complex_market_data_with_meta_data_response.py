# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4134
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid.configuration import Configuration


class ListComplexMarketDataWithMetaDataResponse(object):
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
        'scope': 'str',
        'market_data_id': 'ComplexMarketDataId',
        'market_data': 'ComplexMarketData'
    }

    attribute_map = {
        'scope': 'scope',
        'market_data_id': 'marketDataId',
        'market_data': 'marketData'
    }

    required_map = {
        'scope': 'optional',
        'market_data_id': 'optional',
        'market_data': 'optional'
    }

    def __init__(self, scope=None, market_data_id=None, market_data=None, local_vars_configuration=None):  # noqa: E501
        """ListComplexMarketDataWithMetaDataResponse - a model defined in OpenAPI"
        
        :param scope:  The scope that the listed ComplexMarketData entity is stored in.
        :type scope: str
        :param market_data_id: 
        :type market_data_id: lusid.ComplexMarketDataId
        :param market_data: 
        :type market_data: lusid.ComplexMarketData

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._scope = None
        self._market_data_id = None
        self._market_data = None
        self.discriminator = None

        self.scope = scope
        if market_data_id is not None:
            self.market_data_id = market_data_id
        if market_data is not None:
            self.market_data = market_data

    @property
    def scope(self):
        """Gets the scope of this ListComplexMarketDataWithMetaDataResponse.  # noqa: E501

        The scope that the listed ComplexMarketData entity is stored in.  # noqa: E501

        :return: The scope of this ListComplexMarketDataWithMetaDataResponse.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this ListComplexMarketDataWithMetaDataResponse.

        The scope that the listed ComplexMarketData entity is stored in.  # noqa: E501

        :param scope: The scope of this ListComplexMarketDataWithMetaDataResponse.  # noqa: E501
        :type scope: str
        """

        self._scope = scope

    @property
    def market_data_id(self):
        """Gets the market_data_id of this ListComplexMarketDataWithMetaDataResponse.  # noqa: E501


        :return: The market_data_id of this ListComplexMarketDataWithMetaDataResponse.  # noqa: E501
        :rtype: lusid.ComplexMarketDataId
        """
        return self._market_data_id

    @market_data_id.setter
    def market_data_id(self, market_data_id):
        """Sets the market_data_id of this ListComplexMarketDataWithMetaDataResponse.


        :param market_data_id: The market_data_id of this ListComplexMarketDataWithMetaDataResponse.  # noqa: E501
        :type market_data_id: lusid.ComplexMarketDataId
        """

        self._market_data_id = market_data_id

    @property
    def market_data(self):
        """Gets the market_data of this ListComplexMarketDataWithMetaDataResponse.  # noqa: E501


        :return: The market_data of this ListComplexMarketDataWithMetaDataResponse.  # noqa: E501
        :rtype: lusid.ComplexMarketData
        """
        return self._market_data

    @market_data.setter
    def market_data(self, market_data):
        """Sets the market_data of this ListComplexMarketDataWithMetaDataResponse.


        :param market_data: The market_data of this ListComplexMarketDataWithMetaDataResponse.  # noqa: E501
        :type market_data: lusid.ComplexMarketData
        """

        self._market_data = market_data

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListComplexMarketDataWithMetaDataResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListComplexMarketDataWithMetaDataResponse):
            return True

        return self.to_dict() != other.to_dict()
