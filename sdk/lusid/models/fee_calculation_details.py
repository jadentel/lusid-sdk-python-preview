# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3462
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


class FeeCalculationDetails(object):
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
        'rule_type': 'str',
        'rule_information': 'str',
        'additional_information': 'dict(str, str)',
        'property_key': 'str',
        'calculation_method': 'str',
        'amount': 'float',
        'min': 'float',
        'max': 'float'
    }

    attribute_map = {
        'rule_type': 'ruleType',
        'rule_information': 'ruleInformation',
        'additional_information': 'additionalInformation',
        'property_key': 'propertyKey',
        'calculation_method': 'calculationMethod',
        'amount': 'amount',
        'min': 'min',
        'max': 'max'
    }

    required_map = {
        'rule_type': 'required',
        'rule_information': 'required',
        'additional_information': 'required',
        'property_key': 'required',
        'calculation_method': 'required',
        'amount': 'required',
        'min': 'required',
        'max': 'required'
    }

    def __init__(self, rule_type=None, rule_information=None, additional_information=None, property_key=None, calculation_method=None, amount=None, min=None, max=None, local_vars_configuration=None):  # noqa: E501
        """FeeCalculationDetails - a model defined in OpenAPI"
        
        :param rule_type:  Rule Type (required)
        :type rule_type: str
        :param rule_information:  Rule Sub Type (required)
        :type rule_information: str
        :param additional_information:  Other property keys populated for the fee (required)
        :type additional_information: dict(str, str)
        :param property_key:  The property key which uniquely identifies the property. The format for the property key is {domain}/{scope}/{code}, e.g. 'Portfolio/Manager/Id'. (required)
        :type property_key: str
        :param calculation_method:  Method of calculating the fees or commission eg. BPS or Fraction (required)
        :type calculation_method: str
        :param amount:  Calculation value (required)
        :type amount: float
        :param min:  Calculation value (required)
        :type min: float
        :param max:  Calculation value (required)
        :type max: float

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._rule_type = None
        self._rule_information = None
        self._additional_information = None
        self._property_key = None
        self._calculation_method = None
        self._amount = None
        self._min = None
        self._max = None
        self.discriminator = None

        self.rule_type = rule_type
        self.rule_information = rule_information
        self.additional_information = additional_information
        self.property_key = property_key
        self.calculation_method = calculation_method
        self.amount = amount
        self.min = min
        self.max = max

    @property
    def rule_type(self):
        """Gets the rule_type of this FeeCalculationDetails.  # noqa: E501

        Rule Type  # noqa: E501

        :return: The rule_type of this FeeCalculationDetails.  # noqa: E501
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        """Sets the rule_type of this FeeCalculationDetails.

        Rule Type  # noqa: E501

        :param rule_type: The rule_type of this FeeCalculationDetails.  # noqa: E501
        :type rule_type: str
        """
        if self.local_vars_configuration.client_side_validation and rule_type is None:  # noqa: E501
            raise ValueError("Invalid value for `rule_type`, must not be `None`")  # noqa: E501

        self._rule_type = rule_type

    @property
    def rule_information(self):
        """Gets the rule_information of this FeeCalculationDetails.  # noqa: E501

        Rule Sub Type  # noqa: E501

        :return: The rule_information of this FeeCalculationDetails.  # noqa: E501
        :rtype: str
        """
        return self._rule_information

    @rule_information.setter
    def rule_information(self, rule_information):
        """Sets the rule_information of this FeeCalculationDetails.

        Rule Sub Type  # noqa: E501

        :param rule_information: The rule_information of this FeeCalculationDetails.  # noqa: E501
        :type rule_information: str
        """
        if self.local_vars_configuration.client_side_validation and rule_information is None:  # noqa: E501
            raise ValueError("Invalid value for `rule_information`, must not be `None`")  # noqa: E501

        self._rule_information = rule_information

    @property
    def additional_information(self):
        """Gets the additional_information of this FeeCalculationDetails.  # noqa: E501

        Other property keys populated for the fee  # noqa: E501

        :return: The additional_information of this FeeCalculationDetails.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._additional_information

    @additional_information.setter
    def additional_information(self, additional_information):
        """Sets the additional_information of this FeeCalculationDetails.

        Other property keys populated for the fee  # noqa: E501

        :param additional_information: The additional_information of this FeeCalculationDetails.  # noqa: E501
        :type additional_information: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and additional_information is None:  # noqa: E501
            raise ValueError("Invalid value for `additional_information`, must not be `None`")  # noqa: E501

        self._additional_information = additional_information

    @property
    def property_key(self):
        """Gets the property_key of this FeeCalculationDetails.  # noqa: E501

        The property key which uniquely identifies the property. The format for the property key is {domain}/{scope}/{code}, e.g. 'Portfolio/Manager/Id'.  # noqa: E501

        :return: The property_key of this FeeCalculationDetails.  # noqa: E501
        :rtype: str
        """
        return self._property_key

    @property_key.setter
    def property_key(self, property_key):
        """Sets the property_key of this FeeCalculationDetails.

        The property key which uniquely identifies the property. The format for the property key is {domain}/{scope}/{code}, e.g. 'Portfolio/Manager/Id'.  # noqa: E501

        :param property_key: The property_key of this FeeCalculationDetails.  # noqa: E501
        :type property_key: str
        """
        if self.local_vars_configuration.client_side_validation and property_key is None:  # noqa: E501
            raise ValueError("Invalid value for `property_key`, must not be `None`")  # noqa: E501

        self._property_key = property_key

    @property
    def calculation_method(self):
        """Gets the calculation_method of this FeeCalculationDetails.  # noqa: E501

        Method of calculating the fees or commission eg. BPS or Fraction  # noqa: E501

        :return: The calculation_method of this FeeCalculationDetails.  # noqa: E501
        :rtype: str
        """
        return self._calculation_method

    @calculation_method.setter
    def calculation_method(self, calculation_method):
        """Sets the calculation_method of this FeeCalculationDetails.

        Method of calculating the fees or commission eg. BPS or Fraction  # noqa: E501

        :param calculation_method: The calculation_method of this FeeCalculationDetails.  # noqa: E501
        :type calculation_method: str
        """
        if self.local_vars_configuration.client_side_validation and calculation_method is None:  # noqa: E501
            raise ValueError("Invalid value for `calculation_method`, must not be `None`")  # noqa: E501

        self._calculation_method = calculation_method

    @property
    def amount(self):
        """Gets the amount of this FeeCalculationDetails.  # noqa: E501

        Calculation value  # noqa: E501

        :return: The amount of this FeeCalculationDetails.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this FeeCalculationDetails.

        Calculation value  # noqa: E501

        :param amount: The amount of this FeeCalculationDetails.  # noqa: E501
        :type amount: float
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def min(self):
        """Gets the min of this FeeCalculationDetails.  # noqa: E501

        Calculation value  # noqa: E501

        :return: The min of this FeeCalculationDetails.  # noqa: E501
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this FeeCalculationDetails.

        Calculation value  # noqa: E501

        :param min: The min of this FeeCalculationDetails.  # noqa: E501
        :type min: float
        """
        if self.local_vars_configuration.client_side_validation and min is None:  # noqa: E501
            raise ValueError("Invalid value for `min`, must not be `None`")  # noqa: E501

        self._min = min

    @property
    def max(self):
        """Gets the max of this FeeCalculationDetails.  # noqa: E501

        Calculation value  # noqa: E501

        :return: The max of this FeeCalculationDetails.  # noqa: E501
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this FeeCalculationDetails.

        Calculation value  # noqa: E501

        :param max: The max of this FeeCalculationDetails.  # noqa: E501
        :type max: float
        """
        if self.local_vars_configuration.client_side_validation and max is None:  # noqa: E501
            raise ValueError("Invalid value for `max`, must not be `None`")  # noqa: E501

        self._max = max

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
        if not isinstance(other, FeeCalculationDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FeeCalculationDetails):
            return True

        return self.to_dict() != other.to_dict()
