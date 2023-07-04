# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.310
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


class TranslateTradeTicketRequest(object):
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
        'tickets': 'dict(str, TradeTicket)',
        'dialect': 'str'
    }

    attribute_map = {
        'tickets': 'tickets',
        'dialect': 'dialect'
    }

    required_map = {
        'tickets': 'required',
        'dialect': 'required'
    }

    def __init__(self, tickets=None, dialect=None, local_vars_configuration=None):  # noqa: E501
        """TranslateTradeTicketRequest - a model defined in OpenAPI"
        
        :param tickets:  The collection of trade tickets to translate.                Each trade ticket should be keyed by a unique correlation id. This id is ephemeral  and is not stored by LUSID. It serves only as a way to easily identify each instrument in the response. (required)
        :type tickets: dict[str, lusid.TradeTicket]
        :param dialect:  The target dialect that the given instruments should be translated to. (required)
        :type dialect: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._tickets = None
        self._dialect = None
        self.discriminator = None

        self.tickets = tickets
        self.dialect = dialect

    @property
    def tickets(self):
        """Gets the tickets of this TranslateTradeTicketRequest.  # noqa: E501

        The collection of trade tickets to translate.                Each trade ticket should be keyed by a unique correlation id. This id is ephemeral  and is not stored by LUSID. It serves only as a way to easily identify each instrument in the response.  # noqa: E501

        :return: The tickets of this TranslateTradeTicketRequest.  # noqa: E501
        :rtype: dict[str, lusid.TradeTicket]
        """
        return self._tickets

    @tickets.setter
    def tickets(self, tickets):
        """Sets the tickets of this TranslateTradeTicketRequest.

        The collection of trade tickets to translate.                Each trade ticket should be keyed by a unique correlation id. This id is ephemeral  and is not stored by LUSID. It serves only as a way to easily identify each instrument in the response.  # noqa: E501

        :param tickets: The tickets of this TranslateTradeTicketRequest.  # noqa: E501
        :type tickets: dict[str, lusid.TradeTicket]
        """
        if self.local_vars_configuration.client_side_validation and tickets is None:  # noqa: E501
            raise ValueError("Invalid value for `tickets`, must not be `None`")  # noqa: E501

        self._tickets = tickets

    @property
    def dialect(self):
        """Gets the dialect of this TranslateTradeTicketRequest.  # noqa: E501

        The target dialect that the given instruments should be translated to.  # noqa: E501

        :return: The dialect of this TranslateTradeTicketRequest.  # noqa: E501
        :rtype: str
        """
        return self._dialect

    @dialect.setter
    def dialect(self, dialect):
        """Sets the dialect of this TranslateTradeTicketRequest.

        The target dialect that the given instruments should be translated to.  # noqa: E501

        :param dialect: The dialect of this TranslateTradeTicketRequest.  # noqa: E501
        :type dialect: str
        """
        if self.local_vars_configuration.client_side_validation and dialect is None:  # noqa: E501
            raise ValueError("Invalid value for `dialect`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                dialect is not None and len(dialect) > 256):
            raise ValueError("Invalid value for `dialect`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                dialect is not None and len(dialect) < 1):
            raise ValueError("Invalid value for `dialect`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                dialect is not None and not re.search(r'^[a-zA-Z]*$', dialect)):  # noqa: E501
            raise ValueError(r"Invalid value for `dialect`, must be a follow pattern or equal to `/^[a-zA-Z]*$/`")  # noqa: E501

        self._dialect = dialect

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
        if not isinstance(other, TranslateTradeTicketRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TranslateTradeTicketRequest):
            return True

        return self.to_dict() != other.to_dict()
