# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3085
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class A2BDataRecord(object):
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
        'holding_type': 'str',
        'instrument_uid': 'str',
        'sub_holding_keys': 'dict(str, PerpetualProperty)',
        'currency': 'str',
        'transaction_id': 'str',
        'start': 'A2BCategory',
        'flows': 'A2BCategory',
        'gains': 'A2BCategory',
        'carry': 'A2BCategory',
        'end': 'A2BCategory',
        'properties': 'dict(str, ModelProperty)'
    }

    attribute_map = {
        'holding_type': 'holdingType',
        'instrument_uid': 'instrumentUid',
        'sub_holding_keys': 'subHoldingKeys',
        'currency': 'currency',
        'transaction_id': 'transactionId',
        'start': 'start',
        'flows': 'flows',
        'gains': 'gains',
        'carry': 'carry',
        'end': 'end',
        'properties': 'properties'
    }

    required_map = {
        'holding_type': 'optional',
        'instrument_uid': 'optional',
        'sub_holding_keys': 'optional',
        'currency': 'optional',
        'transaction_id': 'optional',
        'start': 'optional',
        'flows': 'optional',
        'gains': 'optional',
        'carry': 'optional',
        'end': 'optional',
        'properties': 'optional'
    }

    def __init__(self, holding_type=None, instrument_uid=None, sub_holding_keys=None, currency=None, transaction_id=None, start=None, flows=None, gains=None, carry=None, end=None, properties=None):  # noqa: E501
        """
        A2BDataRecord - a model defined in OpenAPI

        :param holding_type:  The type of the holding e.g. Position, Balance, CashCommitment, Receivable, ForwardFX etc.
        :type holding_type: str
        :param instrument_uid:  The unique Lusid Instrument Id (LUID) of the instrument that the holding is in.
        :type instrument_uid: str
        :param sub_holding_keys:  The sub-holding properties which identify the holding. Each property will be from the 'Transaction' domain. These are configured when a transaction portfolio is created.
        :type sub_holding_keys: dict[str, lusid.PerpetualProperty]
        :param currency:  The holding currency.
        :type currency: str
        :param transaction_id:  The unique identifier for the transaction.
        :type transaction_id: str
        :param start: 
        :type start: lusid.A2BCategory
        :param flows: 
        :type flows: lusid.A2BCategory
        :param gains: 
        :type gains: lusid.A2BCategory
        :param carry: 
        :type carry: lusid.A2BCategory
        :param end: 
        :type end: lusid.A2BCategory
        :param properties:  The properties which have been requested to be decorated onto the holding. These will be from the 'Instrument' domain.
        :type properties: dict[str, lusid.ModelProperty]

        """  # noqa: E501

        self._holding_type = None
        self._instrument_uid = None
        self._sub_holding_keys = None
        self._currency = None
        self._transaction_id = None
        self._start = None
        self._flows = None
        self._gains = None
        self._carry = None
        self._end = None
        self._properties = None
        self.discriminator = None

        self.holding_type = holding_type
        self.instrument_uid = instrument_uid
        self.sub_holding_keys = sub_holding_keys
        self.currency = currency
        self.transaction_id = transaction_id
        if start is not None:
            self.start = start
        if flows is not None:
            self.flows = flows
        if gains is not None:
            self.gains = gains
        if carry is not None:
            self.carry = carry
        if end is not None:
            self.end = end
        self.properties = properties

    @property
    def holding_type(self):
        """Gets the holding_type of this A2BDataRecord.  # noqa: E501

        The type of the holding e.g. Position, Balance, CashCommitment, Receivable, ForwardFX etc.  # noqa: E501

        :return: The holding_type of this A2BDataRecord.  # noqa: E501
        :rtype: str
        """
        return self._holding_type

    @holding_type.setter
    def holding_type(self, holding_type):
        """Sets the holding_type of this A2BDataRecord.

        The type of the holding e.g. Position, Balance, CashCommitment, Receivable, ForwardFX etc.  # noqa: E501

        :param holding_type: The holding_type of this A2BDataRecord.  # noqa: E501
        :type: str
        """

        self._holding_type = holding_type

    @property
    def instrument_uid(self):
        """Gets the instrument_uid of this A2BDataRecord.  # noqa: E501

        The unique Lusid Instrument Id (LUID) of the instrument that the holding is in.  # noqa: E501

        :return: The instrument_uid of this A2BDataRecord.  # noqa: E501
        :rtype: str
        """
        return self._instrument_uid

    @instrument_uid.setter
    def instrument_uid(self, instrument_uid):
        """Sets the instrument_uid of this A2BDataRecord.

        The unique Lusid Instrument Id (LUID) of the instrument that the holding is in.  # noqa: E501

        :param instrument_uid: The instrument_uid of this A2BDataRecord.  # noqa: E501
        :type: str
        """

        self._instrument_uid = instrument_uid

    @property
    def sub_holding_keys(self):
        """Gets the sub_holding_keys of this A2BDataRecord.  # noqa: E501

        The sub-holding properties which identify the holding. Each property will be from the 'Transaction' domain. These are configured when a transaction portfolio is created.  # noqa: E501

        :return: The sub_holding_keys of this A2BDataRecord.  # noqa: E501
        :rtype: dict(str, PerpetualProperty)
        """
        return self._sub_holding_keys

    @sub_holding_keys.setter
    def sub_holding_keys(self, sub_holding_keys):
        """Sets the sub_holding_keys of this A2BDataRecord.

        The sub-holding properties which identify the holding. Each property will be from the 'Transaction' domain. These are configured when a transaction portfolio is created.  # noqa: E501

        :param sub_holding_keys: The sub_holding_keys of this A2BDataRecord.  # noqa: E501
        :type: dict(str, PerpetualProperty)
        """

        self._sub_holding_keys = sub_holding_keys

    @property
    def currency(self):
        """Gets the currency of this A2BDataRecord.  # noqa: E501

        The holding currency.  # noqa: E501

        :return: The currency of this A2BDataRecord.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this A2BDataRecord.

        The holding currency.  # noqa: E501

        :param currency: The currency of this A2BDataRecord.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def transaction_id(self):
        """Gets the transaction_id of this A2BDataRecord.  # noqa: E501

        The unique identifier for the transaction.  # noqa: E501

        :return: The transaction_id of this A2BDataRecord.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this A2BDataRecord.

        The unique identifier for the transaction.  # noqa: E501

        :param transaction_id: The transaction_id of this A2BDataRecord.  # noqa: E501
        :type: str
        """

        self._transaction_id = transaction_id

    @property
    def start(self):
        """Gets the start of this A2BDataRecord.  # noqa: E501


        :return: The start of this A2BDataRecord.  # noqa: E501
        :rtype: A2BCategory
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this A2BDataRecord.


        :param start: The start of this A2BDataRecord.  # noqa: E501
        :type: A2BCategory
        """

        self._start = start

    @property
    def flows(self):
        """Gets the flows of this A2BDataRecord.  # noqa: E501


        :return: The flows of this A2BDataRecord.  # noqa: E501
        :rtype: A2BCategory
        """
        return self._flows

    @flows.setter
    def flows(self, flows):
        """Sets the flows of this A2BDataRecord.


        :param flows: The flows of this A2BDataRecord.  # noqa: E501
        :type: A2BCategory
        """

        self._flows = flows

    @property
    def gains(self):
        """Gets the gains of this A2BDataRecord.  # noqa: E501


        :return: The gains of this A2BDataRecord.  # noqa: E501
        :rtype: A2BCategory
        """
        return self._gains

    @gains.setter
    def gains(self, gains):
        """Sets the gains of this A2BDataRecord.


        :param gains: The gains of this A2BDataRecord.  # noqa: E501
        :type: A2BCategory
        """

        self._gains = gains

    @property
    def carry(self):
        """Gets the carry of this A2BDataRecord.  # noqa: E501


        :return: The carry of this A2BDataRecord.  # noqa: E501
        :rtype: A2BCategory
        """
        return self._carry

    @carry.setter
    def carry(self, carry):
        """Sets the carry of this A2BDataRecord.


        :param carry: The carry of this A2BDataRecord.  # noqa: E501
        :type: A2BCategory
        """

        self._carry = carry

    @property
    def end(self):
        """Gets the end of this A2BDataRecord.  # noqa: E501


        :return: The end of this A2BDataRecord.  # noqa: E501
        :rtype: A2BCategory
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this A2BDataRecord.


        :param end: The end of this A2BDataRecord.  # noqa: E501
        :type: A2BCategory
        """

        self._end = end

    @property
    def properties(self):
        """Gets the properties of this A2BDataRecord.  # noqa: E501

        The properties which have been requested to be decorated onto the holding. These will be from the 'Instrument' domain.  # noqa: E501

        :return: The properties of this A2BDataRecord.  # noqa: E501
        :rtype: dict(str, ModelProperty)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this A2BDataRecord.

        The properties which have been requested to be decorated onto the holding. These will be from the 'Instrument' domain.  # noqa: E501

        :param properties: The properties of this A2BDataRecord.  # noqa: E501
        :type: dict(str, ModelProperty)
        """

        self._properties = properties

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
        if not isinstance(other, A2BDataRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
