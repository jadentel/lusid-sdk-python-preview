# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3437
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class TransactionConfigurationData(object):
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
        'aliases': 'list[TransactionConfigurationTypeAlias]',
        'movements': 'list[TransactionConfigurationMovementData]',
        'properties': 'dict(str, PerpetualProperty)'
    }

    attribute_map = {
        'aliases': 'aliases',
        'movements': 'movements',
        'properties': 'properties'
    }

    required_map = {
        'aliases': 'required',
        'movements': 'required',
        'properties': 'optional'
    }

    def __init__(self, aliases=None, movements=None, properties=None):  # noqa: E501
        """
        TransactionConfigurationData - a model defined in OpenAPI

        :param aliases:  List of transaction codes that map to this specific transaction model (required)
        :type aliases: list[lusid.TransactionConfigurationTypeAlias]
        :param movements:  Movement data for the transaction code (required)
        :type movements: list[lusid.TransactionConfigurationMovementData]
        :param properties:  Properties attached to the underlying holding.
        :type properties: dict[str, lusid.PerpetualProperty]

        """  # noqa: E501

        self._aliases = None
        self._movements = None
        self._properties = None
        self.discriminator = None

        self.aliases = aliases
        self.movements = movements
        self.properties = properties

    @property
    def aliases(self):
        """Gets the aliases of this TransactionConfigurationData.  # noqa: E501

        List of transaction codes that map to this specific transaction model  # noqa: E501

        :return: The aliases of this TransactionConfigurationData.  # noqa: E501
        :rtype: list[TransactionConfigurationTypeAlias]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """Sets the aliases of this TransactionConfigurationData.

        List of transaction codes that map to this specific transaction model  # noqa: E501

        :param aliases: The aliases of this TransactionConfigurationData.  # noqa: E501
        :type: list[TransactionConfigurationTypeAlias]
        """
        if aliases is None:
            raise ValueError("Invalid value for `aliases`, must not be `None`")  # noqa: E501

        self._aliases = aliases

    @property
    def movements(self):
        """Gets the movements of this TransactionConfigurationData.  # noqa: E501

        Movement data for the transaction code  # noqa: E501

        :return: The movements of this TransactionConfigurationData.  # noqa: E501
        :rtype: list[TransactionConfigurationMovementData]
        """
        return self._movements

    @movements.setter
    def movements(self, movements):
        """Sets the movements of this TransactionConfigurationData.

        Movement data for the transaction code  # noqa: E501

        :param movements: The movements of this TransactionConfigurationData.  # noqa: E501
        :type: list[TransactionConfigurationMovementData]
        """
        if movements is None:
            raise ValueError("Invalid value for `movements`, must not be `None`")  # noqa: E501

        self._movements = movements

    @property
    def properties(self):
        """Gets the properties of this TransactionConfigurationData.  # noqa: E501

        Properties attached to the underlying holding.  # noqa: E501

        :return: The properties of this TransactionConfigurationData.  # noqa: E501
        :rtype: dict(str, PerpetualProperty)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this TransactionConfigurationData.

        Properties attached to the underlying holding.  # noqa: E501

        :param properties: The properties of this TransactionConfigurationData.  # noqa: E501
        :type: dict(str, PerpetualProperty)
        """

        self._properties = properties

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
        if not isinstance(other, TransactionConfigurationData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
