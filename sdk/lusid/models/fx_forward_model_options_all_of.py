# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4410
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


class FxForwardModelOptionsAllOf(object):
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
        'forward_rate_observable_type': 'str',
        'discounting_method': 'str',
        'convert_to_report_ccy': 'bool',
        'model_options_type': 'str'
    }

    attribute_map = {
        'forward_rate_observable_type': 'forwardRateObservableType',
        'discounting_method': 'discountingMethod',
        'convert_to_report_ccy': 'convertToReportCcy',
        'model_options_type': 'modelOptionsType'
    }

    required_map = {
        'forward_rate_observable_type': 'required',
        'discounting_method': 'required',
        'convert_to_report_ccy': 'required',
        'model_options_type': 'required'
    }

    def __init__(self, forward_rate_observable_type=None, discounting_method=None, convert_to_report_ccy=None, model_options_type=None, local_vars_configuration=None):  # noqa: E501
        """FxForwardModelOptionsAllOf - a model defined in OpenAPI"
        
        :param forward_rate_observable_type:  The available values are: ForwardPoints, ForwardRate, RatesCurve, FxForwardCurve, Invalid (required)
        :type forward_rate_observable_type: str
        :param discounting_method:  The available values are: Standard, ConstantTimeValueOfMoney, Invalid (required)
        :type discounting_method: str
        :param convert_to_report_ccy:  Convert all FX flows to the report currency  By setting this all FX forwards will be priced using Forward Curves that have Report Currency as the base. (required)
        :type convert_to_report_ccy: bool
        :param model_options_type:  The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions (required)
        :type model_options_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._forward_rate_observable_type = None
        self._discounting_method = None
        self._convert_to_report_ccy = None
        self._model_options_type = None
        self.discriminator = None

        self.forward_rate_observable_type = forward_rate_observable_type
        self.discounting_method = discounting_method
        self.convert_to_report_ccy = convert_to_report_ccy
        self.model_options_type = model_options_type

    @property
    def forward_rate_observable_type(self):
        """Gets the forward_rate_observable_type of this FxForwardModelOptionsAllOf.  # noqa: E501

        The available values are: ForwardPoints, ForwardRate, RatesCurve, FxForwardCurve, Invalid  # noqa: E501

        :return: The forward_rate_observable_type of this FxForwardModelOptionsAllOf.  # noqa: E501
        :rtype: str
        """
        return self._forward_rate_observable_type

    @forward_rate_observable_type.setter
    def forward_rate_observable_type(self, forward_rate_observable_type):
        """Sets the forward_rate_observable_type of this FxForwardModelOptionsAllOf.

        The available values are: ForwardPoints, ForwardRate, RatesCurve, FxForwardCurve, Invalid  # noqa: E501

        :param forward_rate_observable_type: The forward_rate_observable_type of this FxForwardModelOptionsAllOf.  # noqa: E501
        :type forward_rate_observable_type: str
        """
        if self.local_vars_configuration.client_side_validation and forward_rate_observable_type is None:  # noqa: E501
            raise ValueError("Invalid value for `forward_rate_observable_type`, must not be `None`")  # noqa: E501
        allowed_values = ["ForwardPoints", "ForwardRate", "RatesCurve", "FxForwardCurve", "Invalid"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and forward_rate_observable_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `forward_rate_observable_type` ({0}), must be one of {1}"  # noqa: E501
                .format(forward_rate_observable_type, allowed_values)
            )

        self._forward_rate_observable_type = forward_rate_observable_type

    @property
    def discounting_method(self):
        """Gets the discounting_method of this FxForwardModelOptionsAllOf.  # noqa: E501

        The available values are: Standard, ConstantTimeValueOfMoney, Invalid  # noqa: E501

        :return: The discounting_method of this FxForwardModelOptionsAllOf.  # noqa: E501
        :rtype: str
        """
        return self._discounting_method

    @discounting_method.setter
    def discounting_method(self, discounting_method):
        """Sets the discounting_method of this FxForwardModelOptionsAllOf.

        The available values are: Standard, ConstantTimeValueOfMoney, Invalid  # noqa: E501

        :param discounting_method: The discounting_method of this FxForwardModelOptionsAllOf.  # noqa: E501
        :type discounting_method: str
        """
        if self.local_vars_configuration.client_side_validation and discounting_method is None:  # noqa: E501
            raise ValueError("Invalid value for `discounting_method`, must not be `None`")  # noqa: E501
        allowed_values = ["Standard", "ConstantTimeValueOfMoney", "Invalid"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and discounting_method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `discounting_method` ({0}), must be one of {1}"  # noqa: E501
                .format(discounting_method, allowed_values)
            )

        self._discounting_method = discounting_method

    @property
    def convert_to_report_ccy(self):
        """Gets the convert_to_report_ccy of this FxForwardModelOptionsAllOf.  # noqa: E501

        Convert all FX flows to the report currency  By setting this all FX forwards will be priced using Forward Curves that have Report Currency as the base.  # noqa: E501

        :return: The convert_to_report_ccy of this FxForwardModelOptionsAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._convert_to_report_ccy

    @convert_to_report_ccy.setter
    def convert_to_report_ccy(self, convert_to_report_ccy):
        """Sets the convert_to_report_ccy of this FxForwardModelOptionsAllOf.

        Convert all FX flows to the report currency  By setting this all FX forwards will be priced using Forward Curves that have Report Currency as the base.  # noqa: E501

        :param convert_to_report_ccy: The convert_to_report_ccy of this FxForwardModelOptionsAllOf.  # noqa: E501
        :type convert_to_report_ccy: bool
        """
        if self.local_vars_configuration.client_side_validation and convert_to_report_ccy is None:  # noqa: E501
            raise ValueError("Invalid value for `convert_to_report_ccy`, must not be `None`")  # noqa: E501

        self._convert_to_report_ccy = convert_to_report_ccy

    @property
    def model_options_type(self):
        """Gets the model_options_type of this FxForwardModelOptionsAllOf.  # noqa: E501

        The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions  # noqa: E501

        :return: The model_options_type of this FxForwardModelOptionsAllOf.  # noqa: E501
        :rtype: str
        """
        return self._model_options_type

    @model_options_type.setter
    def model_options_type(self, model_options_type):
        """Sets the model_options_type of this FxForwardModelOptionsAllOf.

        The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions  # noqa: E501

        :param model_options_type: The model_options_type of this FxForwardModelOptionsAllOf.  # noqa: E501
        :type model_options_type: str
        """
        if self.local_vars_configuration.client_side_validation and model_options_type is None:  # noqa: E501
            raise ValueError("Invalid value for `model_options_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Invalid", "OpaqueModelOptions", "EmptyModelOptions", "IndexModelOptions", "FxForwardModelOptions", "FundingLegModelOptions"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and model_options_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `model_options_type` ({0}), must be one of {1}"  # noqa: E501
                .format(model_options_type, allowed_values)
            )

        self._model_options_type = model_options_type

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
        if not isinstance(other, FxForwardModelOptionsAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FxForwardModelOptionsAllOf):
            return True

        return self.to_dict() != other.to_dict()
