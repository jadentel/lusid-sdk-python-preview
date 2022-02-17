# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3976
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


class GroupedResultOfAddressKey(object):
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
        'columns': 'list[str]',
        'values': 'list[AtomValue]'
    }

    attribute_map = {
        'columns': 'columns',
        'values': 'values'
    }

    required_map = {
        'columns': 'optional',
        'values': 'optional'
    }

    def __init__(self, columns=None, values=None, local_vars_configuration=None):  # noqa: E501
        """GroupedResultOfAddressKey - a model defined in OpenAPI"
        
        :param columns:  The columns, or keys, for a particular group of results
        :type columns: list[str]
        :param values:  The values for the list of results
        :type values: list[lusid.AtomValue]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._columns = None
        self._values = None
        self.discriminator = None

        self.columns = columns
        self.values = values

    @property
    def columns(self):
        """Gets the columns of this GroupedResultOfAddressKey.  # noqa: E501

        The columns, or keys, for a particular group of results  # noqa: E501

        :return: The columns of this GroupedResultOfAddressKey.  # noqa: E501
        :rtype: list[str]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this GroupedResultOfAddressKey.

        The columns, or keys, for a particular group of results  # noqa: E501

        :param columns: The columns of this GroupedResultOfAddressKey.  # noqa: E501
        :type columns: list[str]
        """

        self._columns = columns

    @property
    def values(self):
        """Gets the values of this GroupedResultOfAddressKey.  # noqa: E501

        The values for the list of results  # noqa: E501

        :return: The values of this GroupedResultOfAddressKey.  # noqa: E501
        :rtype: list[lusid.AtomValue]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this GroupedResultOfAddressKey.

        The values for the list of results  # noqa: E501

        :param values: The values of this GroupedResultOfAddressKey.  # noqa: E501
        :type values: list[lusid.AtomValue]
        """

        self._values = values

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
        if not isinstance(other, GroupedResultOfAddressKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GroupedResultOfAddressKey):
            return True

        return self.to_dict() != other.to_dict()
