# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3731
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


class ConfigurationRecipeSnippet(object):
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
        'scope': 'str',
        'code': 'str',
        'aggregation_options': 'AggregationOptions',
        'model_rules': 'list[VendorModelRule]',
        'pricing_options': 'PricingOptions',
        'market_rules': 'list[MarketDataKeyRule]',
        'market_options': 'MarketOptions',
        'recipe': 'ConfigurationRecipe'
    }

    attribute_map = {
        'scope': 'scope',
        'code': 'code',
        'aggregation_options': 'aggregationOptions',
        'model_rules': 'modelRules',
        'pricing_options': 'pricingOptions',
        'market_rules': 'marketRules',
        'market_options': 'marketOptions',
        'recipe': 'recipe'
    }

    required_map = {
        'scope': 'required',
        'code': 'required',
        'aggregation_options': 'optional',
        'model_rules': 'optional',
        'pricing_options': 'optional',
        'market_rules': 'optional',
        'market_options': 'optional',
        'recipe': 'optional'
    }

    def __init__(self, scope=None, code=None, aggregation_options=None, model_rules=None, pricing_options=None, market_rules=None, market_options=None, recipe=None, local_vars_configuration=None):  # noqa: E501
        """ConfigurationRecipeSnippet - a model defined in OpenAPI"
        
        :param scope:  The scope used when updating or inserting the Configuration Recipe snippet (required)
        :type scope: str
        :param code:  User given string name (code) to identify the recipe. (required)
        :type code: str
        :param aggregation_options: 
        :type aggregation_options: lusid.AggregationOptions
        :param model_rules:  The set of model rules that are available. There may be multiple rules for Vendors, but only one per model-instrument pair.  Which of these preference sets is used depends upon the model choice selection if specified, or failing that the global default model specification  in the options.
        :type model_rules: list[lusid.VendorModelRule]
        :param pricing_options: 
        :type pricing_options: lusid.PricingOptions
        :param market_rules:  The set of rules that define how to resolve particular use cases. These can be relatively general or specific in nature.  Nominally any number are possible and will be processed in order where applicable. However, there is evidently a potential  for increased computational cost where many rules must be applied to resolve data. Ensuring that portfolios are structured in  such a way as to reduce the number of rules required is therefore sensible.
        :type market_rules: list[lusid.MarketDataKeyRule]
        :param market_options: 
        :type market_options: lusid.MarketOptions
        :param recipe: 
        :type recipe: lusid.ConfigurationRecipe

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._scope = None
        self._code = None
        self._aggregation_options = None
        self._model_rules = None
        self._pricing_options = None
        self._market_rules = None
        self._market_options = None
        self._recipe = None
        self.discriminator = None

        self.scope = scope
        self.code = code
        if aggregation_options is not None:
            self.aggregation_options = aggregation_options
        self.model_rules = model_rules
        if pricing_options is not None:
            self.pricing_options = pricing_options
        self.market_rules = market_rules
        if market_options is not None:
            self.market_options = market_options
        if recipe is not None:
            self.recipe = recipe

    @property
    def scope(self):
        """Gets the scope of this ConfigurationRecipeSnippet.  # noqa: E501

        The scope used when updating or inserting the Configuration Recipe snippet  # noqa: E501

        :return: The scope of this ConfigurationRecipeSnippet.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this ConfigurationRecipeSnippet.

        The scope used when updating or inserting the Configuration Recipe snippet  # noqa: E501

        :param scope: The scope of this ConfigurationRecipeSnippet.  # noqa: E501
        :type scope: str
        """
        if self.local_vars_configuration.client_side_validation and scope is None:  # noqa: E501
            raise ValueError("Invalid value for `scope`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                scope is not None and len(scope) > 64):
            raise ValueError("Invalid value for `scope`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                scope is not None and len(scope) < 1):
            raise ValueError("Invalid value for `scope`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                scope is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', scope)):  # noqa: E501
            raise ValueError(r"Invalid value for `scope`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._scope = scope

    @property
    def code(self):
        """Gets the code of this ConfigurationRecipeSnippet.  # noqa: E501

        User given string name (code) to identify the recipe.  # noqa: E501

        :return: The code of this ConfigurationRecipeSnippet.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ConfigurationRecipeSnippet.

        User given string name (code) to identify the recipe.  # noqa: E501

        :param code: The code of this ConfigurationRecipeSnippet.  # noqa: E501
        :type code: str
        """
        if self.local_vars_configuration.client_side_validation and code is None:  # noqa: E501
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) > 64):
            raise ValueError("Invalid value for `code`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) < 1):
            raise ValueError("Invalid value for `code`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', code)):  # noqa: E501
            raise ValueError(r"Invalid value for `code`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._code = code

    @property
    def aggregation_options(self):
        """Gets the aggregation_options of this ConfigurationRecipeSnippet.  # noqa: E501


        :return: The aggregation_options of this ConfigurationRecipeSnippet.  # noqa: E501
        :rtype: lusid.AggregationOptions
        """
        return self._aggregation_options

    @aggregation_options.setter
    def aggregation_options(self, aggregation_options):
        """Sets the aggregation_options of this ConfigurationRecipeSnippet.


        :param aggregation_options: The aggregation_options of this ConfigurationRecipeSnippet.  # noqa: E501
        :type aggregation_options: lusid.AggregationOptions
        """

        self._aggregation_options = aggregation_options

    @property
    def model_rules(self):
        """Gets the model_rules of this ConfigurationRecipeSnippet.  # noqa: E501

        The set of model rules that are available. There may be multiple rules for Vendors, but only one per model-instrument pair.  Which of these preference sets is used depends upon the model choice selection if specified, or failing that the global default model specification  in the options.  # noqa: E501

        :return: The model_rules of this ConfigurationRecipeSnippet.  # noqa: E501
        :rtype: list[lusid.VendorModelRule]
        """
        return self._model_rules

    @model_rules.setter
    def model_rules(self, model_rules):
        """Sets the model_rules of this ConfigurationRecipeSnippet.

        The set of model rules that are available. There may be multiple rules for Vendors, but only one per model-instrument pair.  Which of these preference sets is used depends upon the model choice selection if specified, or failing that the global default model specification  in the options.  # noqa: E501

        :param model_rules: The model_rules of this ConfigurationRecipeSnippet.  # noqa: E501
        :type model_rules: list[lusid.VendorModelRule]
        """

        self._model_rules = model_rules

    @property
    def pricing_options(self):
        """Gets the pricing_options of this ConfigurationRecipeSnippet.  # noqa: E501


        :return: The pricing_options of this ConfigurationRecipeSnippet.  # noqa: E501
        :rtype: lusid.PricingOptions
        """
        return self._pricing_options

    @pricing_options.setter
    def pricing_options(self, pricing_options):
        """Sets the pricing_options of this ConfigurationRecipeSnippet.


        :param pricing_options: The pricing_options of this ConfigurationRecipeSnippet.  # noqa: E501
        :type pricing_options: lusid.PricingOptions
        """

        self._pricing_options = pricing_options

    @property
    def market_rules(self):
        """Gets the market_rules of this ConfigurationRecipeSnippet.  # noqa: E501

        The set of rules that define how to resolve particular use cases. These can be relatively general or specific in nature.  Nominally any number are possible and will be processed in order where applicable. However, there is evidently a potential  for increased computational cost where many rules must be applied to resolve data. Ensuring that portfolios are structured in  such a way as to reduce the number of rules required is therefore sensible.  # noqa: E501

        :return: The market_rules of this ConfigurationRecipeSnippet.  # noqa: E501
        :rtype: list[lusid.MarketDataKeyRule]
        """
        return self._market_rules

    @market_rules.setter
    def market_rules(self, market_rules):
        """Sets the market_rules of this ConfigurationRecipeSnippet.

        The set of rules that define how to resolve particular use cases. These can be relatively general or specific in nature.  Nominally any number are possible and will be processed in order where applicable. However, there is evidently a potential  for increased computational cost where many rules must be applied to resolve data. Ensuring that portfolios are structured in  such a way as to reduce the number of rules required is therefore sensible.  # noqa: E501

        :param market_rules: The market_rules of this ConfigurationRecipeSnippet.  # noqa: E501
        :type market_rules: list[lusid.MarketDataKeyRule]
        """

        self._market_rules = market_rules

    @property
    def market_options(self):
        """Gets the market_options of this ConfigurationRecipeSnippet.  # noqa: E501


        :return: The market_options of this ConfigurationRecipeSnippet.  # noqa: E501
        :rtype: lusid.MarketOptions
        """
        return self._market_options

    @market_options.setter
    def market_options(self, market_options):
        """Sets the market_options of this ConfigurationRecipeSnippet.


        :param market_options: The market_options of this ConfigurationRecipeSnippet.  # noqa: E501
        :type market_options: lusid.MarketOptions
        """

        self._market_options = market_options

    @property
    def recipe(self):
        """Gets the recipe of this ConfigurationRecipeSnippet.  # noqa: E501


        :return: The recipe of this ConfigurationRecipeSnippet.  # noqa: E501
        :rtype: lusid.ConfigurationRecipe
        """
        return self._recipe

    @recipe.setter
    def recipe(self, recipe):
        """Sets the recipe of this ConfigurationRecipeSnippet.


        :param recipe: The recipe of this ConfigurationRecipeSnippet.  # noqa: E501
        :type recipe: lusid.ConfigurationRecipe
        """

        self._recipe = recipe

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
        if not isinstance(other, ConfigurationRecipeSnippet):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConfigurationRecipeSnippet):
            return True

        return self.to_dict() != other.to_dict()
