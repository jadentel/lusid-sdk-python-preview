# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.516
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


class OptionEntry(object):
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
        'strike': 'float',
        'date': 'datetime'
    }

    attribute_map = {
        'strike': 'strike',
        'date': 'date'
    }

    required_map = {
        'strike': 'required',
        'date': 'required'
    }

    def __init__(self, strike=None, date=None, local_vars_configuration=None):  # noqa: E501
        """OptionEntry - a model defined in OpenAPI"
        
        :param strike:  The strike on this date (required)
        :type strike: float
        :param date:  The date at which the option can be actioned at this strike (required)
        :type date: datetime

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._strike = None
        self._date = None
        self.discriminator = None

        self.strike = strike
        self.date = date

    @property
    def strike(self):
        """Gets the strike of this OptionEntry.  # noqa: E501

        The strike on this date  # noqa: E501

        :return: The strike of this OptionEntry.  # noqa: E501
        :rtype: float
        """
        return self._strike

    @strike.setter
    def strike(self, strike):
        """Sets the strike of this OptionEntry.

        The strike on this date  # noqa: E501

        :param strike: The strike of this OptionEntry.  # noqa: E501
        :type strike: float
        """
        if self.local_vars_configuration.client_side_validation and strike is None:  # noqa: E501
            raise ValueError("Invalid value for `strike`, must not be `None`")  # noqa: E501

        self._strike = strike

    @property
    def date(self):
        """Gets the date of this OptionEntry.  # noqa: E501

        The date at which the option can be actioned at this strike  # noqa: E501

        :return: The date of this OptionEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this OptionEntry.

        The date at which the option can be actioned at this strike  # noqa: E501

        :param date: The date of this OptionEntry.  # noqa: E501
        :type date: datetime
        """
        if self.local_vars_configuration.client_side_validation and date is None:  # noqa: E501
            raise ValueError("Invalid value for `date`, must not be `None`")  # noqa: E501

        self._date = date

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
        if not isinstance(other, OptionEntry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OptionEntry):
            return True

        return self.to_dict() != other.to_dict()
