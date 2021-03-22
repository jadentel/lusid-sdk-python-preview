# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2785
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class InstrumentCashFlow(object):
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
        'amount': 'float',
        'currency': 'str',
        'source_transaction_id': 'str',
        'source_instrument_id': 'str',
        'diagnostics': 'dict(str, str)',
        'links': 'list[Link]'
    }

    attribute_map = {
        'payment_date': 'paymentDate',
        'amount': 'amount',
        'currency': 'currency',
        'source_transaction_id': 'sourceTransactionId',
        'source_instrument_id': 'sourceInstrumentId',
        'diagnostics': 'diagnostics',
        'links': 'links'
    }

    required_map = {
        'payment_date': 'required',
        'amount': 'optional',
        'currency': 'required',
        'source_transaction_id': 'required',
        'source_instrument_id': 'required',
        'diagnostics': 'required',
        'links': 'optional'
    }

    def __init__(self, payment_date=None, amount=None, currency=None, source_transaction_id=None, source_instrument_id=None, diagnostics=None, links=None):  # noqa: E501
        """
        InstrumentCashFlow - a model defined in OpenAPI

        :param payment_date:  The date at which the given cash flow is due to be paid (SettlementDate is used somewhat interchangeably with PaymentDate.) (required)
        :type payment_date: datetime
        :param amount:  The quantity (amount) that will be paid. Note that this can be empty if the payment is in the future and a model is used that cannot estimate it.
        :type amount: float
        :param currency:  The payment currency of the cash flow. (required)
        :type currency: str
        :param source_transaction_id:  The identifier for the parent transaction on the instrument that will pay/receive this cash flow. (required)
        :type source_transaction_id: str
        :param source_instrument_id:  The unqiue Lusid Instrument Id (LUID) of the instrument that the holding is in. (required)
        :type source_instrument_id: str
        :param diagnostics:  Whilst a cash flow is defined by an (amount,ccy) pair and the date it is paid on there is additional information required for diagnostics. This includes a range of information and can be empty in the case of a simple cash quantity or where further information is not available. Typical information includes items such as reset dates, RIC, accrual start/end, number of days and curve data. (required)
        :type diagnostics: dict(str, str)
        :param links: 
        :type links: list[lusid.Link]

        """  # noqa: E501

        self._payment_date = None
        self._amount = None
        self._currency = None
        self._source_transaction_id = None
        self._source_instrument_id = None
        self._diagnostics = None
        self._links = None
        self.discriminator = None

        self.payment_date = payment_date
        self.amount = amount
        self.currency = currency
        self.source_transaction_id = source_transaction_id
        self.source_instrument_id = source_instrument_id
        self.diagnostics = diagnostics
        self.links = links

    @property
    def payment_date(self):
        """Gets the payment_date of this InstrumentCashFlow.  # noqa: E501

        The date at which the given cash flow is due to be paid (SettlementDate is used somewhat interchangeably with PaymentDate.)  # noqa: E501

        :return: The payment_date of this InstrumentCashFlow.  # noqa: E501
        :rtype: datetime
        """
        return self._payment_date

    @payment_date.setter
    def payment_date(self, payment_date):
        """Sets the payment_date of this InstrumentCashFlow.

        The date at which the given cash flow is due to be paid (SettlementDate is used somewhat interchangeably with PaymentDate.)  # noqa: E501

        :param payment_date: The payment_date of this InstrumentCashFlow.  # noqa: E501
        :type: datetime
        """
        if payment_date is None:
            raise ValueError("Invalid value for `payment_date`, must not be `None`")  # noqa: E501

        self._payment_date = payment_date

    @property
    def amount(self):
        """Gets the amount of this InstrumentCashFlow.  # noqa: E501

        The quantity (amount) that will be paid. Note that this can be empty if the payment is in the future and a model is used that cannot estimate it.  # noqa: E501

        :return: The amount of this InstrumentCashFlow.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this InstrumentCashFlow.

        The quantity (amount) that will be paid. Note that this can be empty if the payment is in the future and a model is used that cannot estimate it.  # noqa: E501

        :param amount: The amount of this InstrumentCashFlow.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this InstrumentCashFlow.  # noqa: E501

        The payment currency of the cash flow.  # noqa: E501

        :return: The currency of this InstrumentCashFlow.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this InstrumentCashFlow.

        The payment currency of the cash flow.  # noqa: E501

        :param currency: The currency of this InstrumentCashFlow.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def source_transaction_id(self):
        """Gets the source_transaction_id of this InstrumentCashFlow.  # noqa: E501

        The identifier for the parent transaction on the instrument that will pay/receive this cash flow.  # noqa: E501

        :return: The source_transaction_id of this InstrumentCashFlow.  # noqa: E501
        :rtype: str
        """
        return self._source_transaction_id

    @source_transaction_id.setter
    def source_transaction_id(self, source_transaction_id):
        """Sets the source_transaction_id of this InstrumentCashFlow.

        The identifier for the parent transaction on the instrument that will pay/receive this cash flow.  # noqa: E501

        :param source_transaction_id: The source_transaction_id of this InstrumentCashFlow.  # noqa: E501
        :type: str
        """
        if source_transaction_id is None:
            raise ValueError("Invalid value for `source_transaction_id`, must not be `None`")  # noqa: E501

        self._source_transaction_id = source_transaction_id

    @property
    def source_instrument_id(self):
        """Gets the source_instrument_id of this InstrumentCashFlow.  # noqa: E501

        The unqiue Lusid Instrument Id (LUID) of the instrument that the holding is in.  # noqa: E501

        :return: The source_instrument_id of this InstrumentCashFlow.  # noqa: E501
        :rtype: str
        """
        return self._source_instrument_id

    @source_instrument_id.setter
    def source_instrument_id(self, source_instrument_id):
        """Sets the source_instrument_id of this InstrumentCashFlow.

        The unqiue Lusid Instrument Id (LUID) of the instrument that the holding is in.  # noqa: E501

        :param source_instrument_id: The source_instrument_id of this InstrumentCashFlow.  # noqa: E501
        :type: str
        """
        if source_instrument_id is None:
            raise ValueError("Invalid value for `source_instrument_id`, must not be `None`")  # noqa: E501

        self._source_instrument_id = source_instrument_id

    @property
    def diagnostics(self):
        """Gets the diagnostics of this InstrumentCashFlow.  # noqa: E501

        Whilst a cash flow is defined by an (amount,ccy) pair and the date it is paid on there is additional information required for diagnostics. This includes a range of information and can be empty in the case of a simple cash quantity or where further information is not available. Typical information includes items such as reset dates, RIC, accrual start/end, number of days and curve data.  # noqa: E501

        :return: The diagnostics of this InstrumentCashFlow.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._diagnostics

    @diagnostics.setter
    def diagnostics(self, diagnostics):
        """Sets the diagnostics of this InstrumentCashFlow.

        Whilst a cash flow is defined by an (amount,ccy) pair and the date it is paid on there is additional information required for diagnostics. This includes a range of information and can be empty in the case of a simple cash quantity or where further information is not available. Typical information includes items such as reset dates, RIC, accrual start/end, number of days and curve data.  # noqa: E501

        :param diagnostics: The diagnostics of this InstrumentCashFlow.  # noqa: E501
        :type: dict(str, str)
        """
        if diagnostics is None:
            raise ValueError("Invalid value for `diagnostics`, must not be `None`")  # noqa: E501

        self._diagnostics = diagnostics

    @property
    def links(self):
        """Gets the links of this InstrumentCashFlow.  # noqa: E501


        :return: The links of this InstrumentCashFlow.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this InstrumentCashFlow.


        :param links: The links of this InstrumentCashFlow.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

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
        if not isinstance(other, InstrumentCashFlow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
