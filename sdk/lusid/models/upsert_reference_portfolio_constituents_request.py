# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3419
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class UpsertReferencePortfolioConstituentsRequest(object):
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
        'effective_from': 'str',
        'weight_type': 'str',
        'period_type': 'str',
        'period_count': 'int',
        'constituents': 'list[ReferencePortfolioConstituentRequest]'
    }

    attribute_map = {
        'effective_from': 'effectiveFrom',
        'weight_type': 'weightType',
        'period_type': 'periodType',
        'period_count': 'periodCount',
        'constituents': 'constituents'
    }

    required_map = {
        'effective_from': 'required',
        'weight_type': 'required',
        'period_type': 'optional',
        'period_count': 'optional',
        'constituents': 'required'
    }

    def __init__(self, effective_from=None, weight_type=None, period_type=None, period_count=None, constituents=None):  # noqa: E501
        """
        UpsertReferencePortfolioConstituentsRequest - a model defined in OpenAPI

        :param effective_from:  The first date from which the weights will apply (required)
        :type effective_from: str
        :param weight_type:  The available values are: Static, Floating, Periodical (required)
        :type weight_type: str
        :param period_type:  The available values are: Daily, Weekly, Monthly, Quarterly, Annually
        :type period_type: str
        :param period_count: 
        :type period_count: int
        :param constituents:  Set of constituents (instrument/weight pairings) (required)
        :type constituents: list[lusid.ReferencePortfolioConstituentRequest]

        """  # noqa: E501

        self._effective_from = None
        self._weight_type = None
        self._period_type = None
        self._period_count = None
        self._constituents = None
        self.discriminator = None

        self.effective_from = effective_from
        self.weight_type = weight_type
        self.period_type = period_type
        self.period_count = period_count
        self.constituents = constituents

    @property
    def effective_from(self):
        """Gets the effective_from of this UpsertReferencePortfolioConstituentsRequest.  # noqa: E501

        The first date from which the weights will apply  # noqa: E501

        :return: The effective_from of this UpsertReferencePortfolioConstituentsRequest.  # noqa: E501
        :rtype: str
        """
        return self._effective_from

    @effective_from.setter
    def effective_from(self, effective_from):
        """Sets the effective_from of this UpsertReferencePortfolioConstituentsRequest.

        The first date from which the weights will apply  # noqa: E501

        :param effective_from: The effective_from of this UpsertReferencePortfolioConstituentsRequest.  # noqa: E501
        :type: str
        """
        if effective_from is None:
            raise ValueError("Invalid value for `effective_from`, must not be `None`")  # noqa: E501

        self._effective_from = effective_from

    @property
    def weight_type(self):
        """Gets the weight_type of this UpsertReferencePortfolioConstituentsRequest.  # noqa: E501

        The available values are: Static, Floating, Periodical  # noqa: E501

        :return: The weight_type of this UpsertReferencePortfolioConstituentsRequest.  # noqa: E501
        :rtype: str
        """
        return self._weight_type

    @weight_type.setter
    def weight_type(self, weight_type):
        """Sets the weight_type of this UpsertReferencePortfolioConstituentsRequest.

        The available values are: Static, Floating, Periodical  # noqa: E501

        :param weight_type: The weight_type of this UpsertReferencePortfolioConstituentsRequest.  # noqa: E501
        :type: str
        """
        if weight_type is None:
            raise ValueError("Invalid value for `weight_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Static", "Floating", "Periodical"]  # noqa: E501
        if weight_type not in allowed_values:
            raise ValueError(
                "Invalid value for `weight_type` ({0}), must be one of {1}"  # noqa: E501
                .format(weight_type, allowed_values)
            )

        self._weight_type = weight_type

    @property
    def period_type(self):
        """Gets the period_type of this UpsertReferencePortfolioConstituentsRequest.  # noqa: E501

        The available values are: Daily, Weekly, Monthly, Quarterly, Annually  # noqa: E501

        :return: The period_type of this UpsertReferencePortfolioConstituentsRequest.  # noqa: E501
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this UpsertReferencePortfolioConstituentsRequest.

        The available values are: Daily, Weekly, Monthly, Quarterly, Annually  # noqa: E501

        :param period_type: The period_type of this UpsertReferencePortfolioConstituentsRequest.  # noqa: E501
        :type: str
        """
        allowed_values = [None,"Daily", "Weekly", "Monthly", "Quarterly", "Annually"]  # noqa: E501
        if period_type not in allowed_values:
            raise ValueError(
                "Invalid value for `period_type` ({0}), must be one of {1}"  # noqa: E501
                .format(period_type, allowed_values)
            )

        self._period_type = period_type

    @property
    def period_count(self):
        """Gets the period_count of this UpsertReferencePortfolioConstituentsRequest.  # noqa: E501


        :return: The period_count of this UpsertReferencePortfolioConstituentsRequest.  # noqa: E501
        :rtype: int
        """
        return self._period_count

    @period_count.setter
    def period_count(self, period_count):
        """Sets the period_count of this UpsertReferencePortfolioConstituentsRequest.


        :param period_count: The period_count of this UpsertReferencePortfolioConstituentsRequest.  # noqa: E501
        :type: int
        """

        self._period_count = period_count

    @property
    def constituents(self):
        """Gets the constituents of this UpsertReferencePortfolioConstituentsRequest.  # noqa: E501

        Set of constituents (instrument/weight pairings)  # noqa: E501

        :return: The constituents of this UpsertReferencePortfolioConstituentsRequest.  # noqa: E501
        :rtype: list[ReferencePortfolioConstituentRequest]
        """
        return self._constituents

    @constituents.setter
    def constituents(self, constituents):
        """Sets the constituents of this UpsertReferencePortfolioConstituentsRequest.

        Set of constituents (instrument/weight pairings)  # noqa: E501

        :param constituents: The constituents of this UpsertReferencePortfolioConstituentsRequest.  # noqa: E501
        :type: list[ReferencePortfolioConstituentRequest]
        """
        if constituents is None:
            raise ValueError("Invalid value for `constituents`, must not be `None`")  # noqa: E501

        self._constituents = constituents

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
        if not isinstance(other, UpsertReferencePortfolioConstituentsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
