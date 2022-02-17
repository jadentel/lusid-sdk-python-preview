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


class AtomValueDecimal(object):
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
        'value': 'float',
        'atom_value_type': 'str'
    }

    attribute_map = {
        'value': 'value',
        'atom_value_type': 'atomValueType'
    }

    required_map = {
        'value': 'optional',
        'atom_value_type': 'required'
    }

    def __init__(self, value=None, atom_value_type=None, local_vars_configuration=None):  # noqa: E501
        """AtomValueDecimal - a model defined in OpenAPI"
        
        :param value:  The value itself
        :type value: float
        :param atom_value_type:  The available values are: AtomValueInt, AtomValueDecimal, AtomValueString, AtomValue0D, AtomValue (required)
        :type atom_value_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._value = None
        self._atom_value_type = None
        self.discriminator = None

        if value is not None:
            self.value = value
        self.atom_value_type = atom_value_type

    @property
    def value(self):
        """Gets the value of this AtomValueDecimal.  # noqa: E501

        The value itself  # noqa: E501

        :return: The value of this AtomValueDecimal.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this AtomValueDecimal.

        The value itself  # noqa: E501

        :param value: The value of this AtomValueDecimal.  # noqa: E501
        :type value: float
        """

        self._value = value

    @property
    def atom_value_type(self):
        """Gets the atom_value_type of this AtomValueDecimal.  # noqa: E501

        The available values are: AtomValueInt, AtomValueDecimal, AtomValueString, AtomValue0D, AtomValue  # noqa: E501

        :return: The atom_value_type of this AtomValueDecimal.  # noqa: E501
        :rtype: str
        """
        return self._atom_value_type

    @atom_value_type.setter
    def atom_value_type(self, atom_value_type):
        """Sets the atom_value_type of this AtomValueDecimal.

        The available values are: AtomValueInt, AtomValueDecimal, AtomValueString, AtomValue0D, AtomValue  # noqa: E501

        :param atom_value_type: The atom_value_type of this AtomValueDecimal.  # noqa: E501
        :type atom_value_type: str
        """
        if self.local_vars_configuration.client_side_validation and atom_value_type is None:  # noqa: E501
            raise ValueError("Invalid value for `atom_value_type`, must not be `None`")  # noqa: E501
        allowed_values = ["AtomValueInt", "AtomValueDecimal", "AtomValueString", "AtomValue0D", "AtomValue"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and atom_value_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `atom_value_type` ({0}), must be one of {1}"  # noqa: E501
                .format(atom_value_type, allowed_values)
            )

        self._atom_value_type = atom_value_type

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
        if not isinstance(other, AtomValueDecimal):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AtomValueDecimal):
            return True

        return self.to_dict() != other.to_dict()
