# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2417
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class PricingContext(object):
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
        'model_rules': 'list[VendorModelRule]',
        'model_choice': 'dict(str, ModelSelection)',
        'options': 'PricingOptions',
        'result_data_rules': 'list[ResultDataKeyRule]'
    }

    attribute_map = {
        'model_rules': 'modelRules',
        'model_choice': 'modelChoice',
        'options': 'options',
        'result_data_rules': 'resultDataRules'
    }

    required_map = {
        'model_rules': 'optional',
        'model_choice': 'optional',
        'options': 'optional',
        'result_data_rules': 'optional'
    }

    def __init__(self, model_rules=None, model_choice=None, options=None, result_data_rules=None):  # noqa: E501
        """
        PricingContext - a model defined in OpenAPI

        :param model_rules:  The set of model rules that are available. There may be multiple rules for Vendors, but only one per model-instrument pair.  Which of these preference sets is used depends upon the model choice selection if specified, or failing that the global default model specification  in the options.
        :type model_rules: list[lusid.VendorModelRule]
        :param model_choice:  The choice of which model selection (vendor library, pricing model) to use in evaluation of a given instrument type.
        :type model_choice: dict[str, lusid.ModelSelection]
        :param options: 
        :type options: lusid.PricingOptions
        :param result_data_rules:  Set of rules that control querying of unit results either for direct queries into aggregation or for  overriding intermediate calculations. For example, a dirty price is made up from a clean price and the accrued interest.  One might consider overriding the accrued interest calculated by a model (perhaps one wants to match an external value or simply disagrees with the  calculated result) and use that in calculation of the dirty price.
        :type result_data_rules: list[lusid.ResultDataKeyRule]

        """  # noqa: E501

        self._model_rules = None
        self._model_choice = None
        self._options = None
        self._result_data_rules = None
        self.discriminator = None

        self.model_rules = model_rules
        self.model_choice = model_choice
        if options is not None:
            self.options = options
        self.result_data_rules = result_data_rules

    @property
    def model_rules(self):
        """Gets the model_rules of this PricingContext.  # noqa: E501

        The set of model rules that are available. There may be multiple rules for Vendors, but only one per model-instrument pair.  Which of these preference sets is used depends upon the model choice selection if specified, or failing that the global default model specification  in the options.  # noqa: E501

        :return: The model_rules of this PricingContext.  # noqa: E501
        :rtype: list[VendorModelRule]
        """
        return self._model_rules

    @model_rules.setter
    def model_rules(self, model_rules):
        """Sets the model_rules of this PricingContext.

        The set of model rules that are available. There may be multiple rules for Vendors, but only one per model-instrument pair.  Which of these preference sets is used depends upon the model choice selection if specified, or failing that the global default model specification  in the options.  # noqa: E501

        :param model_rules: The model_rules of this PricingContext.  # noqa: E501
        :type: list[VendorModelRule]
        """

        self._model_rules = model_rules

    @property
    def model_choice(self):
        """Gets the model_choice of this PricingContext.  # noqa: E501

        The choice of which model selection (vendor library, pricing model) to use in evaluation of a given instrument type.  # noqa: E501

        :return: The model_choice of this PricingContext.  # noqa: E501
        :rtype: dict(str, ModelSelection)
        """
        return self._model_choice

    @model_choice.setter
    def model_choice(self, model_choice):
        """Sets the model_choice of this PricingContext.

        The choice of which model selection (vendor library, pricing model) to use in evaluation of a given instrument type.  # noqa: E501

        :param model_choice: The model_choice of this PricingContext.  # noqa: E501
        :type: dict(str, ModelSelection)
        """

        self._model_choice = model_choice

    @property
    def options(self):
        """Gets the options of this PricingContext.  # noqa: E501


        :return: The options of this PricingContext.  # noqa: E501
        :rtype: PricingOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this PricingContext.


        :param options: The options of this PricingContext.  # noqa: E501
        :type: PricingOptions
        """

        self._options = options

    @property
    def result_data_rules(self):
        """Gets the result_data_rules of this PricingContext.  # noqa: E501

        Set of rules that control querying of unit results either for direct queries into aggregation or for  overriding intermediate calculations. For example, a dirty price is made up from a clean price and the accrued interest.  One might consider overriding the accrued interest calculated by a model (perhaps one wants to match an external value or simply disagrees with the  calculated result) and use that in calculation of the dirty price.  # noqa: E501

        :return: The result_data_rules of this PricingContext.  # noqa: E501
        :rtype: list[ResultDataKeyRule]
        """
        return self._result_data_rules

    @result_data_rules.setter
    def result_data_rules(self, result_data_rules):
        """Sets the result_data_rules of this PricingContext.

        Set of rules that control querying of unit results either for direct queries into aggregation or for  overriding intermediate calculations. For example, a dirty price is made up from a clean price and the accrued interest.  One might consider overriding the accrued interest calculated by a model (perhaps one wants to match an external value or simply disagrees with the  calculated result) and use that in calculation of the dirty price.  # noqa: E501

        :param result_data_rules: The result_data_rules of this PricingContext.  # noqa: E501
        :type: list[ResultDataKeyRule]
        """

        self._result_data_rules = result_data_rules

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
        if not isinstance(other, PricingContext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
