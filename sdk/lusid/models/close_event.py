# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4719
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


class CloseEvent(object):
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
        'anchor_date': 'datetime',
        'instrument_event_type': 'str'
    }

    attribute_map = {
        'anchor_date': 'anchorDate',
        'instrument_event_type': 'instrumentEventType'
    }

    required_map = {
        'anchor_date': 'optional',
        'instrument_event_type': 'required'
    }

    def __init__(self, anchor_date=None, instrument_event_type=None, local_vars_configuration=None):  # noqa: E501
        """CloseEvent - a model defined in OpenAPI"
        
        :param anchor_date:  The date on which the instrument closes/matures
        :type anchor_date: datetime
        :param instrument_event_type:  The Type of Event. The available values are: TransitionEvent, InternalEvent, CouponEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent (required)
        :type instrument_event_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._anchor_date = None
        self._instrument_event_type = None
        self.discriminator = None

        if anchor_date is not None:
            self.anchor_date = anchor_date
        self.instrument_event_type = instrument_event_type

    @property
    def anchor_date(self):
        """Gets the anchor_date of this CloseEvent.  # noqa: E501

        The date on which the instrument closes/matures  # noqa: E501

        :return: The anchor_date of this CloseEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._anchor_date

    @anchor_date.setter
    def anchor_date(self, anchor_date):
        """Sets the anchor_date of this CloseEvent.

        The date on which the instrument closes/matures  # noqa: E501

        :param anchor_date: The anchor_date of this CloseEvent.  # noqa: E501
        :type anchor_date: datetime
        """

        self._anchor_date = anchor_date

    @property
    def instrument_event_type(self):
        """Gets the instrument_event_type of this CloseEvent.  # noqa: E501

        The Type of Event. The available values are: TransitionEvent, InternalEvent, CouponEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent  # noqa: E501

        :return: The instrument_event_type of this CloseEvent.  # noqa: E501
        :rtype: str
        """
        return self._instrument_event_type

    @instrument_event_type.setter
    def instrument_event_type(self, instrument_event_type):
        """Sets the instrument_event_type of this CloseEvent.

        The Type of Event. The available values are: TransitionEvent, InternalEvent, CouponEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent  # noqa: E501

        :param instrument_event_type: The instrument_event_type of this CloseEvent.  # noqa: E501
        :type instrument_event_type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_event_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_event_type`, must not be `None`")  # noqa: E501
        allowed_values = ["TransitionEvent", "InternalEvent", "CouponEvent", "OpenEvent", "CloseEvent", "StockSplitEvent", "BondDefaultEvent", "CashDividendEvent"]  # noqa: E501
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
        if not isinstance(other, CloseEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CloseEvent):
            return True

        return self.to_dict() != other.to_dict()
