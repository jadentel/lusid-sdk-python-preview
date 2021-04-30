# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2938
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class ConfigurationRecipe(object):
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
        'market': 'MarketContext',
        'pricing': 'PricingContext',
        'aggregation': 'AggregationContext',
        'inherited_recipes': 'list[ResourceId]',
        'description': 'str'
    }

    attribute_map = {
        'scope': 'scope',
        'code': 'code',
        'market': 'market',
        'pricing': 'pricing',
        'aggregation': 'aggregation',
        'inherited_recipes': 'inheritedRecipes',
        'description': 'description'
    }

    required_map = {
        'scope': 'required',
        'code': 'required',
        'market': 'optional',
        'pricing': 'optional',
        'aggregation': 'optional',
        'inherited_recipes': 'optional',
        'description': 'optional'
    }

    def __init__(self, scope=None, code=None, market=None, pricing=None, aggregation=None, inherited_recipes=None, description=None):  # noqa: E501
        """
        ConfigurationRecipe - a model defined in OpenAPI

        :param scope:  The scope used when updating or inserting the Configuration Recipe. (required)
        :type scope: str
        :param code:  User given string name (code) to identify the recipe. (required)
        :type code: str
        :param market: 
        :type market: lusid.MarketContext
        :param pricing: 
        :type pricing: lusid.PricingContext
        :param aggregation: 
        :type aggregation: lusid.AggregationContext
        :param inherited_recipes:  A list of parent recipes (scope,code) that can be used to share functionality between recipes. For instance one might use common recipes to set up  pricing for individual asset classes, e.g. rates or credit, and then combine them into a single recipe to be used by an exotics desk in conjunction with  some overrides that it requires for models or other pricing options.
        :type inherited_recipes: list[lusid.ResourceId]
        :param description:  User can assign a description to understand more humanly the recipe.
        :type description: str

        """  # noqa: E501

        self._scope = None
        self._code = None
        self._market = None
        self._pricing = None
        self._aggregation = None
        self._inherited_recipes = None
        self._description = None
        self.discriminator = None

        self.scope = scope
        self.code = code
        if market is not None:
            self.market = market
        if pricing is not None:
            self.pricing = pricing
        if aggregation is not None:
            self.aggregation = aggregation
        self.inherited_recipes = inherited_recipes
        self.description = description

    @property
    def scope(self):
        """Gets the scope of this ConfigurationRecipe.  # noqa: E501

        The scope used when updating or inserting the Configuration Recipe.  # noqa: E501

        :return: The scope of this ConfigurationRecipe.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this ConfigurationRecipe.

        The scope used when updating or inserting the Configuration Recipe.  # noqa: E501

        :param scope: The scope of this ConfigurationRecipe.  # noqa: E501
        :type: str
        """
        if scope is None:
            raise ValueError("Invalid value for `scope`, must not be `None`")  # noqa: E501
        if scope is not None and len(scope) > 64:
            raise ValueError("Invalid value for `scope`, length must be less than or equal to `64`")  # noqa: E501
        if scope is not None and len(scope) < 1:
            raise ValueError("Invalid value for `scope`, length must be greater than or equal to `1`")  # noqa: E501
        if (scope is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', scope)):  # noqa: E501
            raise ValueError(r"Invalid value for `scope`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._scope = scope

    @property
    def code(self):
        """Gets the code of this ConfigurationRecipe.  # noqa: E501

        User given string name (code) to identify the recipe.  # noqa: E501

        :return: The code of this ConfigurationRecipe.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ConfigurationRecipe.

        User given string name (code) to identify the recipe.  # noqa: E501

        :param code: The code of this ConfigurationRecipe.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        if code is not None and len(code) > 64:
            raise ValueError("Invalid value for `code`, length must be less than or equal to `64`")  # noqa: E501
        if code is not None and len(code) < 1:
            raise ValueError("Invalid value for `code`, length must be greater than or equal to `1`")  # noqa: E501
        if (code is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', code)):  # noqa: E501
            raise ValueError(r"Invalid value for `code`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._code = code

    @property
    def market(self):
        """Gets the market of this ConfigurationRecipe.  # noqa: E501


        :return: The market of this ConfigurationRecipe.  # noqa: E501
        :rtype: MarketContext
        """
        return self._market

    @market.setter
    def market(self, market):
        """Sets the market of this ConfigurationRecipe.


        :param market: The market of this ConfigurationRecipe.  # noqa: E501
        :type: MarketContext
        """

        self._market = market

    @property
    def pricing(self):
        """Gets the pricing of this ConfigurationRecipe.  # noqa: E501


        :return: The pricing of this ConfigurationRecipe.  # noqa: E501
        :rtype: PricingContext
        """
        return self._pricing

    @pricing.setter
    def pricing(self, pricing):
        """Sets the pricing of this ConfigurationRecipe.


        :param pricing: The pricing of this ConfigurationRecipe.  # noqa: E501
        :type: PricingContext
        """

        self._pricing = pricing

    @property
    def aggregation(self):
        """Gets the aggregation of this ConfigurationRecipe.  # noqa: E501


        :return: The aggregation of this ConfigurationRecipe.  # noqa: E501
        :rtype: AggregationContext
        """
        return self._aggregation

    @aggregation.setter
    def aggregation(self, aggregation):
        """Sets the aggregation of this ConfigurationRecipe.


        :param aggregation: The aggregation of this ConfigurationRecipe.  # noqa: E501
        :type: AggregationContext
        """

        self._aggregation = aggregation

    @property
    def inherited_recipes(self):
        """Gets the inherited_recipes of this ConfigurationRecipe.  # noqa: E501

        A list of parent recipes (scope,code) that can be used to share functionality between recipes. For instance one might use common recipes to set up  pricing for individual asset classes, e.g. rates or credit, and then combine them into a single recipe to be used by an exotics desk in conjunction with  some overrides that it requires for models or other pricing options.  # noqa: E501

        :return: The inherited_recipes of this ConfigurationRecipe.  # noqa: E501
        :rtype: list[ResourceId]
        """
        return self._inherited_recipes

    @inherited_recipes.setter
    def inherited_recipes(self, inherited_recipes):
        """Sets the inherited_recipes of this ConfigurationRecipe.

        A list of parent recipes (scope,code) that can be used to share functionality between recipes. For instance one might use common recipes to set up  pricing for individual asset classes, e.g. rates or credit, and then combine them into a single recipe to be used by an exotics desk in conjunction with  some overrides that it requires for models or other pricing options.  # noqa: E501

        :param inherited_recipes: The inherited_recipes of this ConfigurationRecipe.  # noqa: E501
        :type: list[ResourceId]
        """

        self._inherited_recipes = inherited_recipes

    @property
    def description(self):
        """Gets the description of this ConfigurationRecipe.  # noqa: E501

        User can assign a description to understand more humanly the recipe.  # noqa: E501

        :return: The description of this ConfigurationRecipe.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConfigurationRecipe.

        User can assign a description to understand more humanly the recipe.  # noqa: E501

        :param description: The description of this ConfigurationRecipe.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 1024:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1024`")  # noqa: E501
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501
        if (description is not None and not re.search(r'(?s).*', description)):  # noqa: E501
            raise ValueError(r"Invalid value for `description`, must be a follow pattern or equal to `/(?s).*/`")  # noqa: E501

        self._description = description

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
        if not isinstance(other, ConfigurationRecipe):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
