# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.5200
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


class LusidTradeTicket(object):
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
        'transaction_id': 'str',
        'transaction_type': 'str',
        'source': 'str',
        'transaction_date': 'str',
        'settlement_date': 'str',
        'total_consideration': 'CurrencyAndAmount',
        'units': 'float',
        'instrument_identifiers': 'dict(str, str)',
        'instrument_scope': 'str',
        'instrument_name': 'str',
        'instrument_definition': 'LusidInstrument',
        'counterparty_agreement_id': 'ResourceId',
        'instrument_properties': 'list[ModelProperty]',
        'transaction_properties': 'list[ModelProperty]',
        'trade_ticket_type': 'str'
    }

    attribute_map = {
        'transaction_id': 'transactionId',
        'transaction_type': 'transactionType',
        'source': 'source',
        'transaction_date': 'transactionDate',
        'settlement_date': 'settlementDate',
        'total_consideration': 'totalConsideration',
        'units': 'units',
        'instrument_identifiers': 'instrumentIdentifiers',
        'instrument_scope': 'instrumentScope',
        'instrument_name': 'instrumentName',
        'instrument_definition': 'instrumentDefinition',
        'counterparty_agreement_id': 'counterpartyAgreementId',
        'instrument_properties': 'instrumentProperties',
        'transaction_properties': 'transactionProperties',
        'trade_ticket_type': 'tradeTicketType'
    }

    required_map = {
        'transaction_id': 'required',
        'transaction_type': 'required',
        'source': 'optional',
        'transaction_date': 'required',
        'settlement_date': 'required',
        'total_consideration': 'required',
        'units': 'required',
        'instrument_identifiers': 'required',
        'instrument_scope': 'optional',
        'instrument_name': 'optional',
        'instrument_definition': 'optional',
        'counterparty_agreement_id': 'optional',
        'instrument_properties': 'optional',
        'transaction_properties': 'optional',
        'trade_ticket_type': 'required'
    }

    def __init__(self, transaction_id=None, transaction_type=None, source=None, transaction_date=None, settlement_date=None, total_consideration=None, units=None, instrument_identifiers=None, instrument_scope=None, instrument_name=None, instrument_definition=None, counterparty_agreement_id=None, instrument_properties=None, transaction_properties=None, trade_ticket_type=None, local_vars_configuration=None):  # noqa: E501
        """LusidTradeTicket - a model defined in OpenAPI"
        
        :param transaction_id:  Transaction ID. Must be unique. (required)
        :type transaction_id: str
        :param transaction_type:  Type of transaction for processing. Referenced by Transaction Configuration. (required)
        :type transaction_type: str
        :param source:  Transaction Source. Referenced by Transaction Configuration.
        :type source: str
        :param transaction_date:  Transaction Date. Date at which transaction is known. (required)
        :type transaction_date: str
        :param settlement_date:  Transaction settlement. Date at which transaction is finalised and realised into the system. (required)
        :type settlement_date: str
        :param total_consideration:  (required)
        :type total_consideration: lusid.CurrencyAndAmount
        :param units:  Number of units in the transaction. For an OTC this is somewhat interchangeable with the quantity booked in the  instrument. As M x N or N x M are equivalent it is advised a client chooses one approach and sticks to it.  Arguably either the unit or holding is best unitised. (required)
        :type units: float
        :param instrument_identifiers:  Identifiers for the instrument. (required)
        :type instrument_identifiers: dict(str, str)
        :param instrument_scope:  Scope of instrument
        :type instrument_scope: str
        :param instrument_name:  Name of instrument
        :type instrument_name: str
        :param instrument_definition: 
        :type instrument_definition: lusid.LusidInstrument
        :param counterparty_agreement_id: 
        :type counterparty_agreement_id: lusid.ResourceId
        :param instrument_properties:  Set of instrument properties (as defined by client/user).
        :type instrument_properties: list[lusid.ModelProperty]
        :param transaction_properties:  Set of transaction properties (as defined by client/user).
        :type transaction_properties: list[lusid.ModelProperty]
        :param trade_ticket_type:  The available values are: LusidTradeTicket, ExternalTradeTicket (required)
        :type trade_ticket_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._transaction_id = None
        self._transaction_type = None
        self._source = None
        self._transaction_date = None
        self._settlement_date = None
        self._total_consideration = None
        self._units = None
        self._instrument_identifiers = None
        self._instrument_scope = None
        self._instrument_name = None
        self._instrument_definition = None
        self._counterparty_agreement_id = None
        self._instrument_properties = None
        self._transaction_properties = None
        self._trade_ticket_type = None
        self.discriminator = None

        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.source = source
        self.transaction_date = transaction_date
        self.settlement_date = settlement_date
        self.total_consideration = total_consideration
        self.units = units
        self.instrument_identifiers = instrument_identifiers
        self.instrument_scope = instrument_scope
        self.instrument_name = instrument_name
        if instrument_definition is not None:
            self.instrument_definition = instrument_definition
        if counterparty_agreement_id is not None:
            self.counterparty_agreement_id = counterparty_agreement_id
        self.instrument_properties = instrument_properties
        self.transaction_properties = transaction_properties
        self.trade_ticket_type = trade_ticket_type

    @property
    def transaction_id(self):
        """Gets the transaction_id of this LusidTradeTicket.  # noqa: E501

        Transaction ID. Must be unique.  # noqa: E501

        :return: The transaction_id of this LusidTradeTicket.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this LusidTradeTicket.

        Transaction ID. Must be unique.  # noqa: E501

        :param transaction_id: The transaction_id of this LusidTradeTicket.  # noqa: E501
        :type transaction_id: str
        """
        if self.local_vars_configuration.client_side_validation and transaction_id is None:  # noqa: E501
            raise ValueError("Invalid value for `transaction_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                transaction_id is not None and len(transaction_id) > 256):
            raise ValueError("Invalid value for `transaction_id`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                transaction_id is not None and len(transaction_id) < 0):
            raise ValueError("Invalid value for `transaction_id`, length must be greater than or equal to `0`")  # noqa: E501

        self._transaction_id = transaction_id

    @property
    def transaction_type(self):
        """Gets the transaction_type of this LusidTradeTicket.  # noqa: E501

        Type of transaction for processing. Referenced by Transaction Configuration.  # noqa: E501

        :return: The transaction_type of this LusidTradeTicket.  # noqa: E501
        :rtype: str
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this LusidTradeTicket.

        Type of transaction for processing. Referenced by Transaction Configuration.  # noqa: E501

        :param transaction_type: The transaction_type of this LusidTradeTicket.  # noqa: E501
        :type transaction_type: str
        """
        if self.local_vars_configuration.client_side_validation and transaction_type is None:  # noqa: E501
            raise ValueError("Invalid value for `transaction_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                transaction_type is not None and len(transaction_type) > 256):
            raise ValueError("Invalid value for `transaction_type`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                transaction_type is not None and len(transaction_type) < 0):
            raise ValueError("Invalid value for `transaction_type`, length must be greater than or equal to `0`")  # noqa: E501

        self._transaction_type = transaction_type

    @property
    def source(self):
        """Gets the source of this LusidTradeTicket.  # noqa: E501

        Transaction Source. Referenced by Transaction Configuration.  # noqa: E501

        :return: The source of this LusidTradeTicket.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this LusidTradeTicket.

        Transaction Source. Referenced by Transaction Configuration.  # noqa: E501

        :param source: The source of this LusidTradeTicket.  # noqa: E501
        :type source: str
        """
        if (self.local_vars_configuration.client_side_validation and
                source is not None and len(source) > 256):
            raise ValueError("Invalid value for `source`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                source is not None and len(source) < 0):
            raise ValueError("Invalid value for `source`, length must be greater than or equal to `0`")  # noqa: E501

        self._source = source

    @property
    def transaction_date(self):
        """Gets the transaction_date of this LusidTradeTicket.  # noqa: E501

        Transaction Date. Date at which transaction is known.  # noqa: E501

        :return: The transaction_date of this LusidTradeTicket.  # noqa: E501
        :rtype: str
        """
        return self._transaction_date

    @transaction_date.setter
    def transaction_date(self, transaction_date):
        """Sets the transaction_date of this LusidTradeTicket.

        Transaction Date. Date at which transaction is known.  # noqa: E501

        :param transaction_date: The transaction_date of this LusidTradeTicket.  # noqa: E501
        :type transaction_date: str
        """
        if self.local_vars_configuration.client_side_validation and transaction_date is None:  # noqa: E501
            raise ValueError("Invalid value for `transaction_date`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                transaction_date is not None and len(transaction_date) < 1):
            raise ValueError("Invalid value for `transaction_date`, length must be greater than or equal to `1`")  # noqa: E501

        self._transaction_date = transaction_date

    @property
    def settlement_date(self):
        """Gets the settlement_date of this LusidTradeTicket.  # noqa: E501

        Transaction settlement. Date at which transaction is finalised and realised into the system.  # noqa: E501

        :return: The settlement_date of this LusidTradeTicket.  # noqa: E501
        :rtype: str
        """
        return self._settlement_date

    @settlement_date.setter
    def settlement_date(self, settlement_date):
        """Sets the settlement_date of this LusidTradeTicket.

        Transaction settlement. Date at which transaction is finalised and realised into the system.  # noqa: E501

        :param settlement_date: The settlement_date of this LusidTradeTicket.  # noqa: E501
        :type settlement_date: str
        """
        if self.local_vars_configuration.client_side_validation and settlement_date is None:  # noqa: E501
            raise ValueError("Invalid value for `settlement_date`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                settlement_date is not None and len(settlement_date) < 1):
            raise ValueError("Invalid value for `settlement_date`, length must be greater than or equal to `1`")  # noqa: E501

        self._settlement_date = settlement_date

    @property
    def total_consideration(self):
        """Gets the total_consideration of this LusidTradeTicket.  # noqa: E501


        :return: The total_consideration of this LusidTradeTicket.  # noqa: E501
        :rtype: lusid.CurrencyAndAmount
        """
        return self._total_consideration

    @total_consideration.setter
    def total_consideration(self, total_consideration):
        """Sets the total_consideration of this LusidTradeTicket.


        :param total_consideration: The total_consideration of this LusidTradeTicket.  # noqa: E501
        :type total_consideration: lusid.CurrencyAndAmount
        """
        if self.local_vars_configuration.client_side_validation and total_consideration is None:  # noqa: E501
            raise ValueError("Invalid value for `total_consideration`, must not be `None`")  # noqa: E501

        self._total_consideration = total_consideration

    @property
    def units(self):
        """Gets the units of this LusidTradeTicket.  # noqa: E501

        Number of units in the transaction. For an OTC this is somewhat interchangeable with the quantity booked in the  instrument. As M x N or N x M are equivalent it is advised a client chooses one approach and sticks to it.  Arguably either the unit or holding is best unitised.  # noqa: E501

        :return: The units of this LusidTradeTicket.  # noqa: E501
        :rtype: float
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this LusidTradeTicket.

        Number of units in the transaction. For an OTC this is somewhat interchangeable with the quantity booked in the  instrument. As M x N or N x M are equivalent it is advised a client chooses one approach and sticks to it.  Arguably either the unit or holding is best unitised.  # noqa: E501

        :param units: The units of this LusidTradeTicket.  # noqa: E501
        :type units: float
        """
        if self.local_vars_configuration.client_side_validation and units is None:  # noqa: E501
            raise ValueError("Invalid value for `units`, must not be `None`")  # noqa: E501

        self._units = units

    @property
    def instrument_identifiers(self):
        """Gets the instrument_identifiers of this LusidTradeTicket.  # noqa: E501

        Identifiers for the instrument.  # noqa: E501

        :return: The instrument_identifiers of this LusidTradeTicket.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._instrument_identifiers

    @instrument_identifiers.setter
    def instrument_identifiers(self, instrument_identifiers):
        """Sets the instrument_identifiers of this LusidTradeTicket.

        Identifiers for the instrument.  # noqa: E501

        :param instrument_identifiers: The instrument_identifiers of this LusidTradeTicket.  # noqa: E501
        :type instrument_identifiers: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and instrument_identifiers is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_identifiers`, must not be `None`")  # noqa: E501

        self._instrument_identifiers = instrument_identifiers

    @property
    def instrument_scope(self):
        """Gets the instrument_scope of this LusidTradeTicket.  # noqa: E501

        Scope of instrument  # noqa: E501

        :return: The instrument_scope of this LusidTradeTicket.  # noqa: E501
        :rtype: str
        """
        return self._instrument_scope

    @instrument_scope.setter
    def instrument_scope(self, instrument_scope):
        """Sets the instrument_scope of this LusidTradeTicket.

        Scope of instrument  # noqa: E501

        :param instrument_scope: The instrument_scope of this LusidTradeTicket.  # noqa: E501
        :type instrument_scope: str
        """
        if (self.local_vars_configuration.client_side_validation and
                instrument_scope is not None and len(instrument_scope) > 64):
            raise ValueError("Invalid value for `instrument_scope`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instrument_scope is not None and len(instrument_scope) < 1):
            raise ValueError("Invalid value for `instrument_scope`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instrument_scope is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', instrument_scope)):  # noqa: E501
            raise ValueError(r"Invalid value for `instrument_scope`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._instrument_scope = instrument_scope

    @property
    def instrument_name(self):
        """Gets the instrument_name of this LusidTradeTicket.  # noqa: E501

        Name of instrument  # noqa: E501

        :return: The instrument_name of this LusidTradeTicket.  # noqa: E501
        :rtype: str
        """
        return self._instrument_name

    @instrument_name.setter
    def instrument_name(self, instrument_name):
        """Sets the instrument_name of this LusidTradeTicket.

        Name of instrument  # noqa: E501

        :param instrument_name: The instrument_name of this LusidTradeTicket.  # noqa: E501
        :type instrument_name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                instrument_name is not None and len(instrument_name) > 256):
            raise ValueError("Invalid value for `instrument_name`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instrument_name is not None and len(instrument_name) < 0):
            raise ValueError("Invalid value for `instrument_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._instrument_name = instrument_name

    @property
    def instrument_definition(self):
        """Gets the instrument_definition of this LusidTradeTicket.  # noqa: E501


        :return: The instrument_definition of this LusidTradeTicket.  # noqa: E501
        :rtype: lusid.LusidInstrument
        """
        return self._instrument_definition

    @instrument_definition.setter
    def instrument_definition(self, instrument_definition):
        """Sets the instrument_definition of this LusidTradeTicket.


        :param instrument_definition: The instrument_definition of this LusidTradeTicket.  # noqa: E501
        :type instrument_definition: lusid.LusidInstrument
        """

        self._instrument_definition = instrument_definition

    @property
    def counterparty_agreement_id(self):
        """Gets the counterparty_agreement_id of this LusidTradeTicket.  # noqa: E501


        :return: The counterparty_agreement_id of this LusidTradeTicket.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._counterparty_agreement_id

    @counterparty_agreement_id.setter
    def counterparty_agreement_id(self, counterparty_agreement_id):
        """Sets the counterparty_agreement_id of this LusidTradeTicket.


        :param counterparty_agreement_id: The counterparty_agreement_id of this LusidTradeTicket.  # noqa: E501
        :type counterparty_agreement_id: lusid.ResourceId
        """

        self._counterparty_agreement_id = counterparty_agreement_id

    @property
    def instrument_properties(self):
        """Gets the instrument_properties of this LusidTradeTicket.  # noqa: E501

        Set of instrument properties (as defined by client/user).  # noqa: E501

        :return: The instrument_properties of this LusidTradeTicket.  # noqa: E501
        :rtype: list[lusid.ModelProperty]
        """
        return self._instrument_properties

    @instrument_properties.setter
    def instrument_properties(self, instrument_properties):
        """Sets the instrument_properties of this LusidTradeTicket.

        Set of instrument properties (as defined by client/user).  # noqa: E501

        :param instrument_properties: The instrument_properties of this LusidTradeTicket.  # noqa: E501
        :type instrument_properties: list[lusid.ModelProperty]
        """

        self._instrument_properties = instrument_properties

    @property
    def transaction_properties(self):
        """Gets the transaction_properties of this LusidTradeTicket.  # noqa: E501

        Set of transaction properties (as defined by client/user).  # noqa: E501

        :return: The transaction_properties of this LusidTradeTicket.  # noqa: E501
        :rtype: list[lusid.ModelProperty]
        """
        return self._transaction_properties

    @transaction_properties.setter
    def transaction_properties(self, transaction_properties):
        """Sets the transaction_properties of this LusidTradeTicket.

        Set of transaction properties (as defined by client/user).  # noqa: E501

        :param transaction_properties: The transaction_properties of this LusidTradeTicket.  # noqa: E501
        :type transaction_properties: list[lusid.ModelProperty]
        """

        self._transaction_properties = transaction_properties

    @property
    def trade_ticket_type(self):
        """Gets the trade_ticket_type of this LusidTradeTicket.  # noqa: E501

        The available values are: LusidTradeTicket, ExternalTradeTicket  # noqa: E501

        :return: The trade_ticket_type of this LusidTradeTicket.  # noqa: E501
        :rtype: str
        """
        return self._trade_ticket_type

    @trade_ticket_type.setter
    def trade_ticket_type(self, trade_ticket_type):
        """Sets the trade_ticket_type of this LusidTradeTicket.

        The available values are: LusidTradeTicket, ExternalTradeTicket  # noqa: E501

        :param trade_ticket_type: The trade_ticket_type of this LusidTradeTicket.  # noqa: E501
        :type trade_ticket_type: str
        """
        if self.local_vars_configuration.client_side_validation and trade_ticket_type is None:  # noqa: E501
            raise ValueError("Invalid value for `trade_ticket_type`, must not be `None`")  # noqa: E501
        allowed_values = ["LusidTradeTicket", "ExternalTradeTicket"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and trade_ticket_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `trade_ticket_type` ({0}), must be one of {1}"  # noqa: E501
                .format(trade_ticket_type, allowed_values)
            )

        self._trade_ticket_type = trade_ticket_type

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
        if not isinstance(other, LusidTradeTicket):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LusidTradeTicket):
            return True

        return self.to_dict() != other.to_dict()
