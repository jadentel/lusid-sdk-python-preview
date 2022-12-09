# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.5057
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


class CashFlowEvent(object):
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
        'amount': 'float',
        'currency': 'str',
        'event_type': 'str',
        'event_status': 'str',
        'payment_date': 'datetime',
        'instrument_event_type': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'currency': 'currency',
        'event_type': 'eventType',
        'event_status': 'eventStatus',
        'payment_date': 'paymentDate',
        'instrument_event_type': 'instrumentEventType'
    }

    required_map = {
        'amount': 'optional',
        'currency': 'required',
        'event_type': 'required',
        'event_status': 'required',
        'payment_date': 'required',
        'instrument_event_type': 'required'
    }

    def __init__(self, amount=None, currency=None, event_type=None, event_status=None, payment_date=None, instrument_event_type=None, local_vars_configuration=None):  # noqa: E501
        """CashFlowEvent - a model defined in OpenAPI"
        
        :param amount:  The quantity (amount) that will be paid, if known. This value will be negative if it is paid, and positive  if it is received.
        :type amount: float
        :param currency:  The payment currency of the cash flow. (required)
        :type currency: str
        :param event_type:  What type of internal event does this represent; coupon, principal, premium etc. (required)
        :type event_type: str
        :param event_status:  What is the event status, is it a known (ie historic) or unknown (ie projected) event? (required)
        :type event_status: str
        :param payment_date:  The date on which the cashflow is scheduled to be paid into the recipient's bank account. (required)
        :type payment_date: datetime
        :param instrument_event_type:  The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent (required)
        :type instrument_event_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._amount = None
        self._currency = None
        self._event_type = None
        self._event_status = None
        self._payment_date = None
        self._instrument_event_type = None
        self.discriminator = None

        self.amount = amount
        self.currency = currency
        self.event_type = event_type
        self.event_status = event_status
        self.payment_date = payment_date
        self.instrument_event_type = instrument_event_type

    @property
    def amount(self):
        """Gets the amount of this CashFlowEvent.  # noqa: E501

        The quantity (amount) that will be paid, if known. This value will be negative if it is paid, and positive  if it is received.  # noqa: E501

        :return: The amount of this CashFlowEvent.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CashFlowEvent.

        The quantity (amount) that will be paid, if known. This value will be negative if it is paid, and positive  if it is received.  # noqa: E501

        :param amount: The amount of this CashFlowEvent.  # noqa: E501
        :type amount: float
        """

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this CashFlowEvent.  # noqa: E501

        The payment currency of the cash flow.  # noqa: E501

        :return: The currency of this CashFlowEvent.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CashFlowEvent.

        The payment currency of the cash flow.  # noqa: E501

        :param currency: The currency of this CashFlowEvent.  # noqa: E501
        :type currency: str
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def event_type(self):
        """Gets the event_type of this CashFlowEvent.  # noqa: E501

        What type of internal event does this represent; coupon, principal, premium etc.  # noqa: E501

        :return: The event_type of this CashFlowEvent.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this CashFlowEvent.

        What type of internal event does this represent; coupon, principal, premium etc.  # noqa: E501

        :param event_type: The event_type of this CashFlowEvent.  # noqa: E501
        :type event_type: str
        """
        if self.local_vars_configuration.client_side_validation and event_type is None:  # noqa: E501
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501

        self._event_type = event_type

    @property
    def event_status(self):
        """Gets the event_status of this CashFlowEvent.  # noqa: E501

        What is the event status, is it a known (ie historic) or unknown (ie projected) event?  # noqa: E501

        :return: The event_status of this CashFlowEvent.  # noqa: E501
        :rtype: str
        """
        return self._event_status

    @event_status.setter
    def event_status(self, event_status):
        """Sets the event_status of this CashFlowEvent.

        What is the event status, is it a known (ie historic) or unknown (ie projected) event?  # noqa: E501

        :param event_status: The event_status of this CashFlowEvent.  # noqa: E501
        :type event_status: str
        """
        if self.local_vars_configuration.client_side_validation and event_status is None:  # noqa: E501
            raise ValueError("Invalid value for `event_status`, must not be `None`")  # noqa: E501

        self._event_status = event_status

    @property
    def payment_date(self):
        """Gets the payment_date of this CashFlowEvent.  # noqa: E501

        The date on which the cashflow is scheduled to be paid into the recipient's bank account.  # noqa: E501

        :return: The payment_date of this CashFlowEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._payment_date

    @payment_date.setter
    def payment_date(self, payment_date):
        """Sets the payment_date of this CashFlowEvent.

        The date on which the cashflow is scheduled to be paid into the recipient's bank account.  # noqa: E501

        :param payment_date: The payment_date of this CashFlowEvent.  # noqa: E501
        :type payment_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and payment_date is None:  # noqa: E501
            raise ValueError("Invalid value for `payment_date`, must not be `None`")  # noqa: E501

        self._payment_date = payment_date

    @property
    def instrument_event_type(self):
        """Gets the instrument_event_type of this CashFlowEvent.  # noqa: E501

        The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent  # noqa: E501

        :return: The instrument_event_type of this CashFlowEvent.  # noqa: E501
        :rtype: str
        """
        return self._instrument_event_type

    @instrument_event_type.setter
    def instrument_event_type(self, instrument_event_type):
        """Sets the instrument_event_type of this CashFlowEvent.

        The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent  # noqa: E501

        :param instrument_event_type: The instrument_event_type of this CashFlowEvent.  # noqa: E501
        :type instrument_event_type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_event_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_event_type`, must not be `None`")  # noqa: E501
        allowed_values = ["TransitionEvent", "InformationalEvent", "OpenEvent", "CloseEvent", "StockSplitEvent", "BondDefaultEvent", "CashDividendEvent", "AmortisationEvent", "CashFlowEvent", "ExerciseEvent", "ResetEvent"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and instrument_event_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `instrument_event_type` ({0}), must be one of {1}"  # noqa: E501
                .format(instrument_event_type, allowed_values)
            )

        self._instrument_event_type = instrument_event_type

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
        if not isinstance(other, CashFlowEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CashFlowEvent):
            return True

        return self.to_dict() != other.to_dict()
