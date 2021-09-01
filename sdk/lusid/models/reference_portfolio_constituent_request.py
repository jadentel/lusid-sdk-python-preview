# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3445
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


class ReferencePortfolioConstituentRequest(object):
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
        'instrument_identifiers': 'dict(str, str)',
        'properties': 'dict(str, PerpetualProperty)',
        'weight': 'float',
        'currency': 'str'
    }

    attribute_map = {
        'instrument_identifiers': 'instrumentIdentifiers',
        'properties': 'properties',
        'weight': 'weight',
        'currency': 'currency'
    }

    required_map = {
        'instrument_identifiers': 'required',
        'properties': 'optional',
        'weight': 'required',
        'currency': 'optional'
    }

    def __init__(self, instrument_identifiers=None, properties=None, weight=None, currency=None, local_vars_configuration=None):  # noqa: E501
        """ReferencePortfolioConstituentRequest - a model defined in OpenAPI"
        
        :param instrument_identifiers:  Unique instrument identifiers (required)
        :type instrument_identifiers: dict(str, str)
        :param properties: 
        :type properties: dict[str, lusid.PerpetualProperty]
        :param weight:  (required)
        :type weight: float
        :param currency: 
        :type currency: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._instrument_identifiers = None
        self._properties = None
        self._weight = None
        self._currency = None
        self.discriminator = None

        self.instrument_identifiers = instrument_identifiers
        self.properties = properties
        self.weight = weight
        self.currency = currency

    @property
    def instrument_identifiers(self):
        """Gets the instrument_identifiers of this ReferencePortfolioConstituentRequest.  # noqa: E501

        Unique instrument identifiers  # noqa: E501

        :return: The instrument_identifiers of this ReferencePortfolioConstituentRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._instrument_identifiers

    @instrument_identifiers.setter
    def instrument_identifiers(self, instrument_identifiers):
        """Sets the instrument_identifiers of this ReferencePortfolioConstituentRequest.

        Unique instrument identifiers  # noqa: E501

        :param instrument_identifiers: The instrument_identifiers of this ReferencePortfolioConstituentRequest.  # noqa: E501
        :type instrument_identifiers: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and instrument_identifiers is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_identifiers`, must not be `None`")  # noqa: E501

        self._instrument_identifiers = instrument_identifiers

    @property
    def properties(self):
        """Gets the properties of this ReferencePortfolioConstituentRequest.  # noqa: E501


        :return: The properties of this ReferencePortfolioConstituentRequest.  # noqa: E501
        :rtype: dict[str, lusid.PerpetualProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ReferencePortfolioConstituentRequest.


        :param properties: The properties of this ReferencePortfolioConstituentRequest.  # noqa: E501
        :type properties: dict[str, lusid.PerpetualProperty]
        """

        self._properties = properties

    @property
    def weight(self):
        """Gets the weight of this ReferencePortfolioConstituentRequest.  # noqa: E501


        :return: The weight of this ReferencePortfolioConstituentRequest.  # noqa: E501
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this ReferencePortfolioConstituentRequest.


        :param weight: The weight of this ReferencePortfolioConstituentRequest.  # noqa: E501
        :type weight: float
        """
        if self.local_vars_configuration.client_side_validation and weight is None:  # noqa: E501
            raise ValueError("Invalid value for `weight`, must not be `None`")  # noqa: E501

        self._weight = weight

    @property
    def currency(self):
        """Gets the currency of this ReferencePortfolioConstituentRequest.  # noqa: E501


        :return: The currency of this ReferencePortfolioConstituentRequest.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ReferencePortfolioConstituentRequest.


        :param currency: The currency of this ReferencePortfolioConstituentRequest.  # noqa: E501
        :type currency: str
        """

        self._currency = currency

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
        if not isinstance(other, ReferencePortfolioConstituentRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReferencePortfolioConstituentRequest):
            return True

        return self.to_dict() != other.to_dict()
