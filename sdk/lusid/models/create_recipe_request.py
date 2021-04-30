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

class CreateRecipeRequest(object):
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
        'recipe_creation_market_data_scopes': 'list[str]',
        'recipe_id': 'ResourceId',
        'inline_recipe': 'ConfigurationRecipe',
        'as_at': 'datetime',
        'effective_at': 'str'
    }

    attribute_map = {
        'recipe_creation_market_data_scopes': 'recipeCreationMarketDataScopes',
        'recipe_id': 'recipeId',
        'inline_recipe': 'inlineRecipe',
        'as_at': 'asAt',
        'effective_at': 'effectiveAt'
    }

    required_map = {
        'recipe_creation_market_data_scopes': 'required',
        'recipe_id': 'optional',
        'inline_recipe': 'optional',
        'as_at': 'optional',
        'effective_at': 'required'
    }

    def __init__(self, recipe_creation_market_data_scopes=None, recipe_id=None, inline_recipe=None, as_at=None, effective_at=None):  # noqa: E501
        """
        CreateRecipeRequest - a model defined in OpenAPI

        :param recipe_creation_market_data_scopes:  The scopes in which the recipe creation would look for quotes/data. (required)
        :type recipe_creation_market_data_scopes: list[str]
        :param recipe_id: 
        :type recipe_id: lusid.ResourceId
        :param inline_recipe: 
        :type inline_recipe: lusid.ConfigurationRecipe
        :param as_at:  The asAt date to use
        :type as_at: datetime
        :param effective_at:  The market data time, i.e. the recipe generated will look for rules with this effectiveAt. (required)
        :type effective_at: str

        """  # noqa: E501

        self._recipe_creation_market_data_scopes = None
        self._recipe_id = None
        self._inline_recipe = None
        self._as_at = None
        self._effective_at = None
        self.discriminator = None

        self.recipe_creation_market_data_scopes = recipe_creation_market_data_scopes
        if recipe_id is not None:
            self.recipe_id = recipe_id
        if inline_recipe is not None:
            self.inline_recipe = inline_recipe
        self.as_at = as_at
        self.effective_at = effective_at

    @property
    def recipe_creation_market_data_scopes(self):
        """Gets the recipe_creation_market_data_scopes of this CreateRecipeRequest.  # noqa: E501

        The scopes in which the recipe creation would look for quotes/data.  # noqa: E501

        :return: The recipe_creation_market_data_scopes of this CreateRecipeRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._recipe_creation_market_data_scopes

    @recipe_creation_market_data_scopes.setter
    def recipe_creation_market_data_scopes(self, recipe_creation_market_data_scopes):
        """Sets the recipe_creation_market_data_scopes of this CreateRecipeRequest.

        The scopes in which the recipe creation would look for quotes/data.  # noqa: E501

        :param recipe_creation_market_data_scopes: The recipe_creation_market_data_scopes of this CreateRecipeRequest.  # noqa: E501
        :type: list[str]
        """
        if recipe_creation_market_data_scopes is None:
            raise ValueError("Invalid value for `recipe_creation_market_data_scopes`, must not be `None`")  # noqa: E501

        self._recipe_creation_market_data_scopes = recipe_creation_market_data_scopes

    @property
    def recipe_id(self):
        """Gets the recipe_id of this CreateRecipeRequest.  # noqa: E501


        :return: The recipe_id of this CreateRecipeRequest.  # noqa: E501
        :rtype: ResourceId
        """
        return self._recipe_id

    @recipe_id.setter
    def recipe_id(self, recipe_id):
        """Sets the recipe_id of this CreateRecipeRequest.


        :param recipe_id: The recipe_id of this CreateRecipeRequest.  # noqa: E501
        :type: ResourceId
        """

        self._recipe_id = recipe_id

    @property
    def inline_recipe(self):
        """Gets the inline_recipe of this CreateRecipeRequest.  # noqa: E501


        :return: The inline_recipe of this CreateRecipeRequest.  # noqa: E501
        :rtype: ConfigurationRecipe
        """
        return self._inline_recipe

    @inline_recipe.setter
    def inline_recipe(self, inline_recipe):
        """Sets the inline_recipe of this CreateRecipeRequest.


        :param inline_recipe: The inline_recipe of this CreateRecipeRequest.  # noqa: E501
        :type: ConfigurationRecipe
        """

        self._inline_recipe = inline_recipe

    @property
    def as_at(self):
        """Gets the as_at of this CreateRecipeRequest.  # noqa: E501

        The asAt date to use  # noqa: E501

        :return: The as_at of this CreateRecipeRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._as_at

    @as_at.setter
    def as_at(self, as_at):
        """Sets the as_at of this CreateRecipeRequest.

        The asAt date to use  # noqa: E501

        :param as_at: The as_at of this CreateRecipeRequest.  # noqa: E501
        :type: datetime
        """

        self._as_at = as_at

    @property
    def effective_at(self):
        """Gets the effective_at of this CreateRecipeRequest.  # noqa: E501

        The market data time, i.e. the recipe generated will look for rules with this effectiveAt.  # noqa: E501

        :return: The effective_at of this CreateRecipeRequest.  # noqa: E501
        :rtype: str
        """
        return self._effective_at

    @effective_at.setter
    def effective_at(self, effective_at):
        """Sets the effective_at of this CreateRecipeRequest.

        The market data time, i.e. the recipe generated will look for rules with this effectiveAt.  # noqa: E501

        :param effective_at: The effective_at of this CreateRecipeRequest.  # noqa: E501
        :type: str
        """
        if effective_at is None:
            raise ValueError("Invalid value for `effective_at`, must not be `None`")  # noqa: E501

        self._effective_at = effective_at

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
        if not isinstance(other, CreateRecipeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
