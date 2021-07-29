# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3333
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class AddBusinessDaysToDateRequest(object):
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
        'business_day_offset': 'int',
        'holiday_codes': 'list[str]',
        'start_date': 'datetime',
        'as_at': 'datetime'
    }

    attribute_map = {
        'business_day_offset': 'businessDayOffset',
        'holiday_codes': 'holidayCodes',
        'start_date': 'startDate',
        'as_at': 'asAt'
    }

    required_map = {
        'business_day_offset': 'required',
        'holiday_codes': 'required',
        'start_date': 'optional',
        'as_at': 'optional'
    }

    def __init__(self, business_day_offset=None, holiday_codes=None, start_date=None, as_at=None):  # noqa: E501
        """
        AddBusinessDaysToDateRequest - a model defined in OpenAPI

        :param business_day_offset:  (required)
        :type business_day_offset: int
        :param holiday_codes:  (required)
        :type holiday_codes: list[str]
        :param start_date: 
        :type start_date: datetime
        :param as_at: 
        :type as_at: datetime

        """  # noqa: E501

        self._business_day_offset = None
        self._holiday_codes = None
        self._start_date = None
        self._as_at = None
        self.discriminator = None

        self.business_day_offset = business_day_offset
        self.holiday_codes = holiday_codes
        if start_date is not None:
            self.start_date = start_date
        self.as_at = as_at

    @property
    def business_day_offset(self):
        """Gets the business_day_offset of this AddBusinessDaysToDateRequest.  # noqa: E501


        :return: The business_day_offset of this AddBusinessDaysToDateRequest.  # noqa: E501
        :rtype: int
        """
        return self._business_day_offset

    @business_day_offset.setter
    def business_day_offset(self, business_day_offset):
        """Sets the business_day_offset of this AddBusinessDaysToDateRequest.


        :param business_day_offset: The business_day_offset of this AddBusinessDaysToDateRequest.  # noqa: E501
        :type: int
        """
        if business_day_offset is None:
            raise ValueError("Invalid value for `business_day_offset`, must not be `None`")  # noqa: E501

        self._business_day_offset = business_day_offset

    @property
    def holiday_codes(self):
        """Gets the holiday_codes of this AddBusinessDaysToDateRequest.  # noqa: E501


        :return: The holiday_codes of this AddBusinessDaysToDateRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._holiday_codes

    @holiday_codes.setter
    def holiday_codes(self, holiday_codes):
        """Sets the holiday_codes of this AddBusinessDaysToDateRequest.


        :param holiday_codes: The holiday_codes of this AddBusinessDaysToDateRequest.  # noqa: E501
        :type: list[str]
        """
        if holiday_codes is None:
            raise ValueError("Invalid value for `holiday_codes`, must not be `None`")  # noqa: E501

        self._holiday_codes = holiday_codes

    @property
    def start_date(self):
        """Gets the start_date of this AddBusinessDaysToDateRequest.  # noqa: E501


        :return: The start_date of this AddBusinessDaysToDateRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this AddBusinessDaysToDateRequest.


        :param start_date: The start_date of this AddBusinessDaysToDateRequest.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def as_at(self):
        """Gets the as_at of this AddBusinessDaysToDateRequest.  # noqa: E501


        :return: The as_at of this AddBusinessDaysToDateRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._as_at

    @as_at.setter
    def as_at(self, as_at):
        """Sets the as_at of this AddBusinessDaysToDateRequest.


        :param as_at: The as_at of this AddBusinessDaysToDateRequest.  # noqa: E501
        :type: datetime
        """

        self._as_at = as_at

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
        if not isinstance(other, AddBusinessDaysToDateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
