# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.5136
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


class ResetEvent(object):
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
        'value': 'float',
        'reset_type': 'str',
        'fixing_source': 'str',
        'event_status': 'str',
        'fixing_date': 'datetime',
        'instrument_event_type': 'str'
    }

    attribute_map = {
        'value': 'value',
        'reset_type': 'resetType',
        'fixing_source': 'fixingSource',
        'event_status': 'eventStatus',
        'fixing_date': 'fixingDate',
        'instrument_event_type': 'instrumentEventType'
    }

    required_map = {
        'value': 'optional',
        'reset_type': 'required',
        'fixing_source': 'optional',
        'event_status': 'required',
        'fixing_date': 'required',
        'instrument_event_type': 'required'
    }

    def __init__(self, value=None, reset_type=None, fixing_source=None, event_status=None, fixing_date=None, instrument_event_type=None, local_vars_configuration=None):  # noqa: E501
        """ResetEvent - a model defined in OpenAPI"
        
        :param value:  The quantity associated with the reset. This will only be populated if the information is known.
        :type value: float
        :param reset_type:  The type of the reset; e.g. RIC, Currency-pair (required)
        :type reset_type: str
        :param fixing_source:  Fixing identification source, if available.
        :type fixing_source: str
        :param event_status:  What is the event status, is it a known (ie historic) or unknown (ie projected) event? (required)
        :type event_status: str
        :param fixing_date:  The date the reset fixes, or is observed upon. (required)
        :type fixing_date: datetime
        :param instrument_event_type:  The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent (required)
        :type instrument_event_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._value = None
        self._reset_type = None
        self._fixing_source = None
        self._event_status = None
        self._fixing_date = None
        self._instrument_event_type = None
        self.discriminator = None

        self.value = value
        self.reset_type = reset_type
        self.fixing_source = fixing_source
        self.event_status = event_status
        self.fixing_date = fixing_date
        self.instrument_event_type = instrument_event_type

    @property
    def value(self):
        """Gets the value of this ResetEvent.  # noqa: E501

        The quantity associated with the reset. This will only be populated if the information is known.  # noqa: E501

        :return: The value of this ResetEvent.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ResetEvent.

        The quantity associated with the reset. This will only be populated if the information is known.  # noqa: E501

        :param value: The value of this ResetEvent.  # noqa: E501
        :type value: float
        """

        self._value = value

    @property
    def reset_type(self):
        """Gets the reset_type of this ResetEvent.  # noqa: E501

        The type of the reset; e.g. RIC, Currency-pair  # noqa: E501

        :return: The reset_type of this ResetEvent.  # noqa: E501
        :rtype: str
        """
        return self._reset_type

    @reset_type.setter
    def reset_type(self, reset_type):
        """Sets the reset_type of this ResetEvent.

        The type of the reset; e.g. RIC, Currency-pair  # noqa: E501

        :param reset_type: The reset_type of this ResetEvent.  # noqa: E501
        :type reset_type: str
        """
        if self.local_vars_configuration.client_side_validation and reset_type is None:  # noqa: E501
            raise ValueError("Invalid value for `reset_type`, must not be `None`")  # noqa: E501

        self._reset_type = reset_type

    @property
    def fixing_source(self):
        """Gets the fixing_source of this ResetEvent.  # noqa: E501

        Fixing identification source, if available.  # noqa: E501

        :return: The fixing_source of this ResetEvent.  # noqa: E501
        :rtype: str
        """
        return self._fixing_source

    @fixing_source.setter
    def fixing_source(self, fixing_source):
        """Sets the fixing_source of this ResetEvent.

        Fixing identification source, if available.  # noqa: E501

        :param fixing_source: The fixing_source of this ResetEvent.  # noqa: E501
        :type fixing_source: str
        """

        self._fixing_source = fixing_source

    @property
    def event_status(self):
        """Gets the event_status of this ResetEvent.  # noqa: E501

        What is the event status, is it a known (ie historic) or unknown (ie projected) event?  # noqa: E501

        :return: The event_status of this ResetEvent.  # noqa: E501
        :rtype: str
        """
        return self._event_status

    @event_status.setter
    def event_status(self, event_status):
        """Sets the event_status of this ResetEvent.

        What is the event status, is it a known (ie historic) or unknown (ie projected) event?  # noqa: E501

        :param event_status: The event_status of this ResetEvent.  # noqa: E501
        :type event_status: str
        """
        if self.local_vars_configuration.client_side_validation and event_status is None:  # noqa: E501
            raise ValueError("Invalid value for `event_status`, must not be `None`")  # noqa: E501

        self._event_status = event_status

    @property
    def fixing_date(self):
        """Gets the fixing_date of this ResetEvent.  # noqa: E501

        The date the reset fixes, or is observed upon.  # noqa: E501

        :return: The fixing_date of this ResetEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._fixing_date

    @fixing_date.setter
    def fixing_date(self, fixing_date):
        """Sets the fixing_date of this ResetEvent.

        The date the reset fixes, or is observed upon.  # noqa: E501

        :param fixing_date: The fixing_date of this ResetEvent.  # noqa: E501
        :type fixing_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and fixing_date is None:  # noqa: E501
            raise ValueError("Invalid value for `fixing_date`, must not be `None`")  # noqa: E501

        self._fixing_date = fixing_date

    @property
    def instrument_event_type(self):
        """Gets the instrument_event_type of this ResetEvent.  # noqa: E501

        The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent  # noqa: E501

        :return: The instrument_event_type of this ResetEvent.  # noqa: E501
        :rtype: str
        """
        return self._instrument_event_type

    @instrument_event_type.setter
    def instrument_event_type(self, instrument_event_type):
        """Sets the instrument_event_type of this ResetEvent.

        The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent  # noqa: E501

        :param instrument_event_type: The instrument_event_type of this ResetEvent.  # noqa: E501
        :type instrument_event_type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_event_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_event_type`, must not be `None`")  # noqa: E501
        allowed_values = ["TransitionEvent", "InformationalEvent", "OpenEvent", "CloseEvent", "StockSplitEvent", "BondDefaultEvent", "CashDividendEvent", "AmortisationEvent", "CashFlowEvent", "ExerciseEvent", "ResetEvent", "TriggerEvent", "RawVendorEvent", "InformationalErrorEvent"]  # noqa: E501
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
        if not isinstance(other, ResetEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResetEvent):
            return True

        return self.to_dict() != other.to_dict()
