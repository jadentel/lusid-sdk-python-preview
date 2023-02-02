# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.5202
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


class CashFlowValueAllOf(object):
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
        'payment_date': 'datetime',
        'diagnostics': 'ResultValueDictionary',
        'cash_flow_lineage': 'CashFlowLineage',
        'payment_amount': 'float',
        'payment_ccy': 'str',
        'result_value_type': 'str'
    }

    attribute_map = {
        'payment_date': 'paymentDate',
        'diagnostics': 'diagnostics',
        'cash_flow_lineage': 'cashFlowLineage',
        'payment_amount': 'paymentAmount',
        'payment_ccy': 'paymentCcy',
        'result_value_type': 'resultValueType'
    }

    required_map = {
        'payment_date': 'required',
        'diagnostics': 'optional',
        'cash_flow_lineage': 'optional',
        'payment_amount': 'required',
        'payment_ccy': 'required',
        'result_value_type': 'required'
    }

    def __init__(self, payment_date=None, diagnostics=None, cash_flow_lineage=None, payment_amount=None, payment_ccy=None, result_value_type=None, local_vars_configuration=None):  # noqa: E501
        """CashFlowValueAllOf - a model defined in OpenAPI"
        
        :param payment_date:  The payment date of the cash flow (required)
        :type payment_date: datetime
        :param diagnostics: 
        :type diagnostics: lusid.ResultValueDictionary
        :param cash_flow_lineage: 
        :type cash_flow_lineage: lusid.CashFlowLineage
        :param payment_amount:  The amount paid or received (required)
        :type payment_amount: float
        :param payment_ccy:  The currency of the transaction (required)
        :type payment_ccy: str
        :param result_value_type:  The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset (required)
        :type result_value_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._payment_date = None
        self._diagnostics = None
        self._cash_flow_lineage = None
        self._payment_amount = None
        self._payment_ccy = None
        self._result_value_type = None
        self.discriminator = None

        self.payment_date = payment_date
        if diagnostics is not None:
            self.diagnostics = diagnostics
        if cash_flow_lineage is not None:
            self.cash_flow_lineage = cash_flow_lineage
        self.payment_amount = payment_amount
        self.payment_ccy = payment_ccy
        self.result_value_type = result_value_type

    @property
    def payment_date(self):
        """Gets the payment_date of this CashFlowValueAllOf.  # noqa: E501

        The payment date of the cash flow  # noqa: E501

        :return: The payment_date of this CashFlowValueAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._payment_date

    @payment_date.setter
    def payment_date(self, payment_date):
        """Sets the payment_date of this CashFlowValueAllOf.

        The payment date of the cash flow  # noqa: E501

        :param payment_date: The payment_date of this CashFlowValueAllOf.  # noqa: E501
        :type payment_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and payment_date is None:  # noqa: E501
            raise ValueError("Invalid value for `payment_date`, must not be `None`")  # noqa: E501

        self._payment_date = payment_date

    @property
    def diagnostics(self):
        """Gets the diagnostics of this CashFlowValueAllOf.  # noqa: E501


        :return: The diagnostics of this CashFlowValueAllOf.  # noqa: E501
        :rtype: lusid.ResultValueDictionary
        """
        return self._diagnostics

    @diagnostics.setter
    def diagnostics(self, diagnostics):
        """Sets the diagnostics of this CashFlowValueAllOf.


        :param diagnostics: The diagnostics of this CashFlowValueAllOf.  # noqa: E501
        :type diagnostics: lusid.ResultValueDictionary
        """

        self._diagnostics = diagnostics

    @property
    def cash_flow_lineage(self):
        """Gets the cash_flow_lineage of this CashFlowValueAllOf.  # noqa: E501


        :return: The cash_flow_lineage of this CashFlowValueAllOf.  # noqa: E501
        :rtype: lusid.CashFlowLineage
        """
        return self._cash_flow_lineage

    @cash_flow_lineage.setter
    def cash_flow_lineage(self, cash_flow_lineage):
        """Sets the cash_flow_lineage of this CashFlowValueAllOf.


        :param cash_flow_lineage: The cash_flow_lineage of this CashFlowValueAllOf.  # noqa: E501
        :type cash_flow_lineage: lusid.CashFlowLineage
        """

        self._cash_flow_lineage = cash_flow_lineage

    @property
    def payment_amount(self):
        """Gets the payment_amount of this CashFlowValueAllOf.  # noqa: E501

        The amount paid or received  # noqa: E501

        :return: The payment_amount of this CashFlowValueAllOf.  # noqa: E501
        :rtype: float
        """
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, payment_amount):
        """Sets the payment_amount of this CashFlowValueAllOf.

        The amount paid or received  # noqa: E501

        :param payment_amount: The payment_amount of this CashFlowValueAllOf.  # noqa: E501
        :type payment_amount: float
        """
        if self.local_vars_configuration.client_side_validation and payment_amount is None:  # noqa: E501
            raise ValueError("Invalid value for `payment_amount`, must not be `None`")  # noqa: E501

        self._payment_amount = payment_amount

    @property
    def payment_ccy(self):
        """Gets the payment_ccy of this CashFlowValueAllOf.  # noqa: E501

        The currency of the transaction  # noqa: E501

        :return: The payment_ccy of this CashFlowValueAllOf.  # noqa: E501
        :rtype: str
        """
        return self._payment_ccy

    @payment_ccy.setter
    def payment_ccy(self, payment_ccy):
        """Sets the payment_ccy of this CashFlowValueAllOf.

        The currency of the transaction  # noqa: E501

        :param payment_ccy: The payment_ccy of this CashFlowValueAllOf.  # noqa: E501
        :type payment_ccy: str
        """
        if self.local_vars_configuration.client_side_validation and payment_ccy is None:  # noqa: E501
            raise ValueError("Invalid value for `payment_ccy`, must not be `None`")  # noqa: E501

        self._payment_ccy = payment_ccy

    @property
    def result_value_type(self):
        """Gets the result_value_type of this CashFlowValueAllOf.  # noqa: E501

        The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset  # noqa: E501

        :return: The result_value_type of this CashFlowValueAllOf.  # noqa: E501
        :rtype: str
        """
        return self._result_value_type

    @result_value_type.setter
    def result_value_type(self, result_value_type):
        """Sets the result_value_type of this CashFlowValueAllOf.

        The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset  # noqa: E501

        :param result_value_type: The result_value_type of this CashFlowValueAllOf.  # noqa: E501
        :type result_value_type: str
        """
        if self.local_vars_configuration.client_side_validation and result_value_type is None:  # noqa: E501
            raise ValueError("Invalid value for `result_value_type`, must not be `None`")  # noqa: E501
        allowed_values = ["ResultValue", "ResultValueDictionary", "ResultValue0D", "ResultValueDecimal", "ResultValueInt", "ResultValueString", "CashFlowValue", "CashFlowValueSet", "ResultValueLifeCycleEventValue", "ResultValueDateTimeOffset"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and result_value_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `result_value_type` ({0}), must be one of {1}"  # noqa: E501
                .format(result_value_type, allowed_values)
            )

        self._result_value_type = result_value_type

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
        if not isinstance(other, CashFlowValueAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CashFlowValueAllOf):
            return True

        return self.to_dict() != other.to_dict()
