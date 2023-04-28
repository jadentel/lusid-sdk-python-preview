# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.121
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


class JELinesQueryParameters(object):
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
        'start_date': 'str',
        'end_date': 'str',
        'filter': 'str',
        'property_keys': 'list[str]'
    }

    attribute_map = {
        'start_date': 'startDate',
        'end_date': 'endDate',
        'filter': 'filter',
        'property_keys': 'propertyKeys'
    }

    required_map = {
        'start_date': 'optional',
        'end_date': 'optional',
        'filter': 'optional',
        'property_keys': 'optional'
    }

    def __init__(self, start_date=None, end_date=None, filter=None, property_keys=None, local_vars_configuration=None):  # noqa: E501
        """JELinesQueryParameters - a model defined in OpenAPI"
        
        :param start_date:  The start date of the JELines.
        :type start_date: str
        :param end_date:  The end date of the JELInes
        :type end_date: str
        :param filter:  Expression to filter the result set.
        :type filter: str
        :param property_keys:  A list of property keys from the 'Instrument', 'Transaction', 'Portfolio', 'Account', 'LegalEntity' or 'CustodianAccount' domain to decorate onto the JELine.
        :type property_keys: list[str]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._start_date = None
        self._end_date = None
        self._filter = None
        self._property_keys = None
        self.discriminator = None

        self.start_date = start_date
        self.end_date = end_date
        self.filter = filter
        self.property_keys = property_keys

    @property
    def start_date(self):
        """Gets the start_date of this JELinesQueryParameters.  # noqa: E501

        The start date of the JELines.  # noqa: E501

        :return: The start_date of this JELinesQueryParameters.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this JELinesQueryParameters.

        The start date of the JELines.  # noqa: E501

        :param start_date: The start_date of this JELinesQueryParameters.  # noqa: E501
        :type start_date: str
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this JELinesQueryParameters.  # noqa: E501

        The end date of the JELInes  # noqa: E501

        :return: The end_date of this JELinesQueryParameters.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this JELinesQueryParameters.

        The end date of the JELInes  # noqa: E501

        :param end_date: The end_date of this JELinesQueryParameters.  # noqa: E501
        :type end_date: str
        """

        self._end_date = end_date

    @property
    def filter(self):
        """Gets the filter of this JELinesQueryParameters.  # noqa: E501

        Expression to filter the result set.  # noqa: E501

        :return: The filter of this JELinesQueryParameters.  # noqa: E501
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this JELinesQueryParameters.

        Expression to filter the result set.  # noqa: E501

        :param filter: The filter of this JELinesQueryParameters.  # noqa: E501
        :type filter: str
        """
        if (self.local_vars_configuration.client_side_validation and
                filter is not None and len(filter) > 16384):
            raise ValueError("Invalid value for `filter`, length must be less than or equal to `16384`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                filter is not None and len(filter) < 0):
            raise ValueError("Invalid value for `filter`, length must be greater than or equal to `0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                filter is not None and not re.search(r'^[\s\S]*$', filter)):  # noqa: E501
            raise ValueError(r"Invalid value for `filter`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._filter = filter

    @property
    def property_keys(self):
        """Gets the property_keys of this JELinesQueryParameters.  # noqa: E501

        A list of property keys from the 'Instrument', 'Transaction', 'Portfolio', 'Account', 'LegalEntity' or 'CustodianAccount' domain to decorate onto the JELine.  # noqa: E501

        :return: The property_keys of this JELinesQueryParameters.  # noqa: E501
        :rtype: list[str]
        """
        return self._property_keys

    @property_keys.setter
    def property_keys(self, property_keys):
        """Sets the property_keys of this JELinesQueryParameters.

        A list of property keys from the 'Instrument', 'Transaction', 'Portfolio', 'Account', 'LegalEntity' or 'CustodianAccount' domain to decorate onto the JELine.  # noqa: E501

        :param property_keys: The property_keys of this JELinesQueryParameters.  # noqa: E501
        :type property_keys: list[str]
        """

        self._property_keys = property_keys

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
        if not isinstance(other, JELinesQueryParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JELinesQueryParameters):
            return True

        return self.to_dict() != other.to_dict()
