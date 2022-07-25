# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4636
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


class TransactionTypeAlias(object):
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
        'type': 'str',
        'description': 'str',
        'transaction_class': 'str',
        'transaction_roles': 'str',
        'is_default': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'description': 'description',
        'transaction_class': 'transactionClass',
        'transaction_roles': 'transactionRoles',
        'is_default': 'isDefault'
    }

    required_map = {
        'type': 'required',
        'description': 'required',
        'transaction_class': 'required',
        'transaction_roles': 'required',
        'is_default': 'optional'
    }

    def __init__(self, type=None, description=None, transaction_class=None, transaction_roles=None, is_default=None, local_vars_configuration=None):  # noqa: E501
        """TransactionTypeAlias - a model defined in OpenAPI"
        
        :param type:  The transaction type (required)
        :type type: str
        :param description:  Brief description of the transaction (required)
        :type description: str
        :param transaction_class:  Relates types of a similar class. E.g. Buy/Sell, StockIn/StockOut (required)
        :type transaction_class: str
        :param transaction_roles:  Transactions role within a class. E.g. Increase a long position (required)
        :type transaction_roles: str
        :param is_default:  IsDefault is a flag that denotes the default alias for a source. There can only be, at most, one per source.
        :type is_default: bool

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._description = None
        self._transaction_class = None
        self._transaction_roles = None
        self._is_default = None
        self.discriminator = None

        self.type = type
        self.description = description
        self.transaction_class = transaction_class
        self.transaction_roles = transaction_roles
        if is_default is not None:
            self.is_default = is_default

    @property
    def type(self):
        """Gets the type of this TransactionTypeAlias.  # noqa: E501

        The transaction type  # noqa: E501

        :return: The type of this TransactionTypeAlias.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TransactionTypeAlias.

        The transaction type  # noqa: E501

        :param type: The type of this TransactionTypeAlias.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and len(type) > 64):
            raise ValueError("Invalid value for `type`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and len(type) < 1):
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', type)):  # noqa: E501
            raise ValueError(r"Invalid value for `type`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._type = type

    @property
    def description(self):
        """Gets the description of this TransactionTypeAlias.  # noqa: E501

        Brief description of the transaction  # noqa: E501

        :return: The description of this TransactionTypeAlias.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TransactionTypeAlias.

        Brief description of the transaction  # noqa: E501

        :param description: The description of this TransactionTypeAlias.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 512):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `512`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 1):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and not re.search(r'^[\s\S]*$', description)):  # noqa: E501
            raise ValueError(r"Invalid value for `description`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._description = description

    @property
    def transaction_class(self):
        """Gets the transaction_class of this TransactionTypeAlias.  # noqa: E501

        Relates types of a similar class. E.g. Buy/Sell, StockIn/StockOut  # noqa: E501

        :return: The transaction_class of this TransactionTypeAlias.  # noqa: E501
        :rtype: str
        """
        return self._transaction_class

    @transaction_class.setter
    def transaction_class(self, transaction_class):
        """Sets the transaction_class of this TransactionTypeAlias.

        Relates types of a similar class. E.g. Buy/Sell, StockIn/StockOut  # noqa: E501

        :param transaction_class: The transaction_class of this TransactionTypeAlias.  # noqa: E501
        :type transaction_class: str
        """
        if self.local_vars_configuration.client_side_validation and transaction_class is None:  # noqa: E501
            raise ValueError("Invalid value for `transaction_class`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                transaction_class is not None and len(transaction_class) > 512):
            raise ValueError("Invalid value for `transaction_class`, length must be less than or equal to `512`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                transaction_class is not None and len(transaction_class) < 1):
            raise ValueError("Invalid value for `transaction_class`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                transaction_class is not None and not re.search(r'^[\s\S]*$', transaction_class)):  # noqa: E501
            raise ValueError(r"Invalid value for `transaction_class`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._transaction_class = transaction_class

    @property
    def transaction_roles(self):
        """Gets the transaction_roles of this TransactionTypeAlias.  # noqa: E501

        Transactions role within a class. E.g. Increase a long position  # noqa: E501

        :return: The transaction_roles of this TransactionTypeAlias.  # noqa: E501
        :rtype: str
        """
        return self._transaction_roles

    @transaction_roles.setter
    def transaction_roles(self, transaction_roles):
        """Sets the transaction_roles of this TransactionTypeAlias.

        Transactions role within a class. E.g. Increase a long position  # noqa: E501

        :param transaction_roles: The transaction_roles of this TransactionTypeAlias.  # noqa: E501
        :type transaction_roles: str
        """
        if self.local_vars_configuration.client_side_validation and transaction_roles is None:  # noqa: E501
            raise ValueError("Invalid value for `transaction_roles`, must not be `None`")  # noqa: E501

        self._transaction_roles = transaction_roles

    @property
    def is_default(self):
        """Gets the is_default of this TransactionTypeAlias.  # noqa: E501

        IsDefault is a flag that denotes the default alias for a source. There can only be, at most, one per source.  # noqa: E501

        :return: The is_default of this TransactionTypeAlias.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this TransactionTypeAlias.

        IsDefault is a flag that denotes the default alias for a source. There can only be, at most, one per source.  # noqa: E501

        :param is_default: The is_default of this TransactionTypeAlias.  # noqa: E501
        :type is_default: bool
        """

        self._is_default = is_default

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
        if not isinstance(other, TransactionTypeAlias):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionTypeAlias):
            return True

        return self.to_dict() != other.to_dict()
