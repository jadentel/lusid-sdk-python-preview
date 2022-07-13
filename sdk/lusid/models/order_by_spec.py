# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4595
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


class OrderBySpec(object):
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
        'key': 'str',
        'sort_order': 'str'
    }

    attribute_map = {
        'key': 'key',
        'sort_order': 'sortOrder'
    }

    required_map = {
        'key': 'required',
        'sort_order': 'required'
    }

    def __init__(self, key=None, sort_order=None, local_vars_configuration=None):  # noqa: E501
        """OrderBySpec - a model defined in OpenAPI"
        
        :param key:  The key that uniquely identifies a queryable address in Lusid. (required)
        :type key: str
        :param sort_order:  The available values are: Ascending, Descending (required)
        :type sort_order: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._key = None
        self._sort_order = None
        self.discriminator = None

        self.key = key
        self.sort_order = sort_order

    @property
    def key(self):
        """Gets the key of this OrderBySpec.  # noqa: E501

        The key that uniquely identifies a queryable address in Lusid.  # noqa: E501

        :return: The key of this OrderBySpec.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this OrderBySpec.

        The key that uniquely identifies a queryable address in Lusid.  # noqa: E501

        :param key: The key of this OrderBySpec.  # noqa: E501
        :type key: str
        """
        if self.local_vars_configuration.client_side_validation and key is None:  # noqa: E501
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def sort_order(self):
        """Gets the sort_order of this OrderBySpec.  # noqa: E501

        The available values are: Ascending, Descending  # noqa: E501

        :return: The sort_order of this OrderBySpec.  # noqa: E501
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this OrderBySpec.

        The available values are: Ascending, Descending  # noqa: E501

        :param sort_order: The sort_order of this OrderBySpec.  # noqa: E501
        :type sort_order: str
        """
        if self.local_vars_configuration.client_side_validation and sort_order is None:  # noqa: E501
            raise ValueError("Invalid value for `sort_order`, must not be `None`")  # noqa: E501
        allowed_values = ["Ascending", "Descending"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and sort_order not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `sort_order` ({0}), must be one of {1}"  # noqa: E501
                .format(sort_order, allowed_values)
            )

        self._sort_order = sort_order

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
        if not isinstance(other, OrderBySpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrderBySpec):
            return True

        return self.to_dict() != other.to_dict()
