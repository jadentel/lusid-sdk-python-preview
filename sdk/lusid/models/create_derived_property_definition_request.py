# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4519
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


class CreateDerivedPropertyDefinitionRequest(object):
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
        'domain': 'str',
        'scope': 'str',
        'code': 'str',
        'display_name': 'str',
        'data_type_id': 'ResourceId',
        'property_description': 'str',
        'derivation_formula': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'scope': 'scope',
        'code': 'code',
        'display_name': 'displayName',
        'data_type_id': 'dataTypeId',
        'property_description': 'propertyDescription',
        'derivation_formula': 'derivationFormula'
    }

    required_map = {
        'domain': 'required',
        'scope': 'required',
        'code': 'required',
        'display_name': 'required',
        'data_type_id': 'required',
        'property_description': 'optional',
        'derivation_formula': 'required'
    }

    def __init__(self, domain=None, scope=None, code=None, display_name=None, data_type_id=None, property_description=None, derivation_formula=None, local_vars_configuration=None):  # noqa: E501
        """CreateDerivedPropertyDefinitionRequest - a model defined in OpenAPI"
        
        :param domain:  The domain that the property exists in. Not all available values are currently supported, please check the documentation: https://support.lusid.com/knowledgebase/article/KA-01719/. The available values are: NotDefined, Transaction, Portfolio, Holding, ReferenceHolding, TransactionConfiguration, Instrument, CutLabelDefinition, Analytic, PortfolioGroup, Person, AccessMetadata, Order, UnitResult, MarketData, ConfigurationRecipe, Allocation, Calendar, LegalEntity, Placement, Execution, Block, Participation, Package, OrderInstruction, NextBestAction, CustomEntity, InstrumentEvent (required)
        :type domain: str
        :param scope:  The scope that the property exists in. (required)
        :type scope: str
        :param code:  The code of the property. Together with the domain and scope this uniquely identifies the property. (required)
        :type code: str
        :param display_name:  The display name of the property. (required)
        :type display_name: str
        :param data_type_id:  (required)
        :type data_type_id: lusid.ResourceId
        :param property_description:  Describes the property
        :type property_description: str
        :param derivation_formula:  The rule that defines how data is composed for a derived property. (required)
        :type derivation_formula: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._domain = None
        self._scope = None
        self._code = None
        self._display_name = None
        self._data_type_id = None
        self._property_description = None
        self._derivation_formula = None
        self.discriminator = None

        self.domain = domain
        self.scope = scope
        self.code = code
        self.display_name = display_name
        self.data_type_id = data_type_id
        self.property_description = property_description
        self.derivation_formula = derivation_formula

    @property
    def domain(self):
        """Gets the domain of this CreateDerivedPropertyDefinitionRequest.  # noqa: E501

        The domain that the property exists in. Not all available values are currently supported, please check the documentation: https://support.lusid.com/knowledgebase/article/KA-01719/. The available values are: NotDefined, Transaction, Portfolio, Holding, ReferenceHolding, TransactionConfiguration, Instrument, CutLabelDefinition, Analytic, PortfolioGroup, Person, AccessMetadata, Order, UnitResult, MarketData, ConfigurationRecipe, Allocation, Calendar, LegalEntity, Placement, Execution, Block, Participation, Package, OrderInstruction, NextBestAction, CustomEntity, InstrumentEvent  # noqa: E501

        :return: The domain of this CreateDerivedPropertyDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this CreateDerivedPropertyDefinitionRequest.

        The domain that the property exists in. Not all available values are currently supported, please check the documentation: https://support.lusid.com/knowledgebase/article/KA-01719/. The available values are: NotDefined, Transaction, Portfolio, Holding, ReferenceHolding, TransactionConfiguration, Instrument, CutLabelDefinition, Analytic, PortfolioGroup, Person, AccessMetadata, Order, UnitResult, MarketData, ConfigurationRecipe, Allocation, Calendar, LegalEntity, Placement, Execution, Block, Participation, Package, OrderInstruction, NextBestAction, CustomEntity, InstrumentEvent  # noqa: E501

        :param domain: The domain of this CreateDerivedPropertyDefinitionRequest.  # noqa: E501
        :type domain: str
        """
        if self.local_vars_configuration.client_side_validation and domain is None:  # noqa: E501
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501
        allowed_values = ["NotDefined", "Transaction", "Portfolio", "Holding", "ReferenceHolding", "TransactionConfiguration", "Instrument", "CutLabelDefinition", "Analytic", "PortfolioGroup", "Person", "AccessMetadata", "Order", "UnitResult", "MarketData", "ConfigurationRecipe", "Allocation", "Calendar", "LegalEntity", "Placement", "Execution", "Block", "Participation", "Package", "OrderInstruction", "NextBestAction", "CustomEntity", "InstrumentEvent"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and domain not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `domain` ({0}), must be one of {1}"  # noqa: E501
                .format(domain, allowed_values)
            )

        self._domain = domain

    @property
    def scope(self):
        """Gets the scope of this CreateDerivedPropertyDefinitionRequest.  # noqa: E501

        The scope that the property exists in.  # noqa: E501

        :return: The scope of this CreateDerivedPropertyDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this CreateDerivedPropertyDefinitionRequest.

        The scope that the property exists in.  # noqa: E501

        :param scope: The scope of this CreateDerivedPropertyDefinitionRequest.  # noqa: E501
        :type scope: str
        """
        if self.local_vars_configuration.client_side_validation and scope is None:  # noqa: E501
            raise ValueError("Invalid value for `scope`, must not be `None`")  # noqa: E501

        self._scope = scope

    @property
    def code(self):
        """Gets the code of this CreateDerivedPropertyDefinitionRequest.  # noqa: E501

        The code of the property. Together with the domain and scope this uniquely identifies the property.  # noqa: E501

        :return: The code of this CreateDerivedPropertyDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CreateDerivedPropertyDefinitionRequest.

        The code of the property. Together with the domain and scope this uniquely identifies the property.  # noqa: E501

        :param code: The code of this CreateDerivedPropertyDefinitionRequest.  # noqa: E501
        :type code: str
        """
        if self.local_vars_configuration.client_side_validation and code is None:  # noqa: E501
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def display_name(self):
        """Gets the display_name of this CreateDerivedPropertyDefinitionRequest.  # noqa: E501

        The display name of the property.  # noqa: E501

        :return: The display_name of this CreateDerivedPropertyDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CreateDerivedPropertyDefinitionRequest.

        The display name of the property.  # noqa: E501

        :param display_name: The display_name of this CreateDerivedPropertyDefinitionRequest.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def data_type_id(self):
        """Gets the data_type_id of this CreateDerivedPropertyDefinitionRequest.  # noqa: E501


        :return: The data_type_id of this CreateDerivedPropertyDefinitionRequest.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._data_type_id

    @data_type_id.setter
    def data_type_id(self, data_type_id):
        """Sets the data_type_id of this CreateDerivedPropertyDefinitionRequest.


        :param data_type_id: The data_type_id of this CreateDerivedPropertyDefinitionRequest.  # noqa: E501
        :type data_type_id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and data_type_id is None:  # noqa: E501
            raise ValueError("Invalid value for `data_type_id`, must not be `None`")  # noqa: E501

        self._data_type_id = data_type_id

    @property
    def property_description(self):
        """Gets the property_description of this CreateDerivedPropertyDefinitionRequest.  # noqa: E501

        Describes the property  # noqa: E501

        :return: The property_description of this CreateDerivedPropertyDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._property_description

    @property_description.setter
    def property_description(self, property_description):
        """Sets the property_description of this CreateDerivedPropertyDefinitionRequest.

        Describes the property  # noqa: E501

        :param property_description: The property_description of this CreateDerivedPropertyDefinitionRequest.  # noqa: E501
        :type property_description: str
        """
        if (self.local_vars_configuration.client_side_validation and
                property_description is not None and len(property_description) > 512):
            raise ValueError("Invalid value for `property_description`, length must be less than or equal to `512`")  # noqa: E501

        self._property_description = property_description

    @property
    def derivation_formula(self):
        """Gets the derivation_formula of this CreateDerivedPropertyDefinitionRequest.  # noqa: E501

        The rule that defines how data is composed for a derived property.  # noqa: E501

        :return: The derivation_formula of this CreateDerivedPropertyDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._derivation_formula

    @derivation_formula.setter
    def derivation_formula(self, derivation_formula):
        """Sets the derivation_formula of this CreateDerivedPropertyDefinitionRequest.

        The rule that defines how data is composed for a derived property.  # noqa: E501

        :param derivation_formula: The derivation_formula of this CreateDerivedPropertyDefinitionRequest.  # noqa: E501
        :type derivation_formula: str
        """
        if self.local_vars_configuration.client_side_validation and derivation_formula is None:  # noqa: E501
            raise ValueError("Invalid value for `derivation_formula`, must not be `None`")  # noqa: E501

        self._derivation_formula = derivation_formula

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
        if not isinstance(other, CreateDerivedPropertyDefinitionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateDerivedPropertyDefinitionRequest):
            return True

        return self.to_dict() != other.to_dict()
