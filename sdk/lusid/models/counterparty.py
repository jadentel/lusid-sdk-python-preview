# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3218
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class Counterparty(object):
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
        'counterparty_id': 'str',
        'counterparty_name': 'str',
        'country_of_risk': 'str',
        'issuer_ratings': 'list[CreditRating]',
        'industry_scheme': 'IndustryClassificationScheme',
        'scope': 'str',
        'code': 'str'
    }

    attribute_map = {
        'counterparty_id': 'counterpartyId',
        'counterparty_name': 'counterpartyName',
        'country_of_risk': 'countryOfRisk',
        'issuer_ratings': 'issuerRatings',
        'industry_scheme': 'industryScheme',
        'scope': 'scope',
        'code': 'code'
    }

    required_map = {
        'counterparty_id': 'required',
        'counterparty_name': 'required',
        'country_of_risk': 'required',
        'issuer_ratings': 'required',
        'industry_scheme': 'required',
        'scope': 'optional',
        'code': 'optional'
    }

    def __init__(self, counterparty_id=None, counterparty_name=None, country_of_risk=None, issuer_ratings=None, industry_scheme=None, scope=None, code=None):  # noqa: E501
        """
        Counterparty - a model defined in OpenAPI

        :param counterparty_id:  A unique identifier that determines the identity of the counter-party, disambiguating between related legal entities, particularly necessary in the case of multi-nationals. (required)
        :type counterparty_id: str
        :param counterparty_name:  The legal name of the entity to which this counterparty refers. (required)
        :type counterparty_name: str
        :param country_of_risk:  To which country would one naturally ascribe risk. Typically this will be synonymous with legal registration entity.  This can be used to infer funding currency and related market data in the absence of specific overrides or preference. (required)
        :type country_of_risk: str
        :param issuer_ratings:  A set of credit ratings for the counterparty fro, e.g. Standard and Poor or Moody's. (required)
        :type issuer_ratings: list[lusid.CreditRating]
        :param industry_scheme:  (required)
        :type industry_scheme: lusid.IndustryClassificationScheme
        :param scope:  The scope used when updating or inserting the convention.
        :type scope: str
        :param code:  The code of the convention.
        :type code: str

        """  # noqa: E501

        self._counterparty_id = None
        self._counterparty_name = None
        self._country_of_risk = None
        self._issuer_ratings = None
        self._industry_scheme = None
        self._scope = None
        self._code = None
        self.discriminator = None

        self.counterparty_id = counterparty_id
        self.counterparty_name = counterparty_name
        self.country_of_risk = country_of_risk
        self.issuer_ratings = issuer_ratings
        self.industry_scheme = industry_scheme
        self.scope = scope
        self.code = code

    @property
    def counterparty_id(self):
        """Gets the counterparty_id of this Counterparty.  # noqa: E501

        A unique identifier that determines the identity of the counter-party, disambiguating between related legal entities, particularly necessary in the case of multi-nationals.  # noqa: E501

        :return: The counterparty_id of this Counterparty.  # noqa: E501
        :rtype: str
        """
        return self._counterparty_id

    @counterparty_id.setter
    def counterparty_id(self, counterparty_id):
        """Sets the counterparty_id of this Counterparty.

        A unique identifier that determines the identity of the counter-party, disambiguating between related legal entities, particularly necessary in the case of multi-nationals.  # noqa: E501

        :param counterparty_id: The counterparty_id of this Counterparty.  # noqa: E501
        :type: str
        """
        if counterparty_id is None:
            raise ValueError("Invalid value for `counterparty_id`, must not be `None`")  # noqa: E501

        self._counterparty_id = counterparty_id

    @property
    def counterparty_name(self):
        """Gets the counterparty_name of this Counterparty.  # noqa: E501

        The legal name of the entity to which this counterparty refers.  # noqa: E501

        :return: The counterparty_name of this Counterparty.  # noqa: E501
        :rtype: str
        """
        return self._counterparty_name

    @counterparty_name.setter
    def counterparty_name(self, counterparty_name):
        """Sets the counterparty_name of this Counterparty.

        The legal name of the entity to which this counterparty refers.  # noqa: E501

        :param counterparty_name: The counterparty_name of this Counterparty.  # noqa: E501
        :type: str
        """
        if counterparty_name is None:
            raise ValueError("Invalid value for `counterparty_name`, must not be `None`")  # noqa: E501

        self._counterparty_name = counterparty_name

    @property
    def country_of_risk(self):
        """Gets the country_of_risk of this Counterparty.  # noqa: E501

        To which country would one naturally ascribe risk. Typically this will be synonymous with legal registration entity.  This can be used to infer funding currency and related market data in the absence of specific overrides or preference.  # noqa: E501

        :return: The country_of_risk of this Counterparty.  # noqa: E501
        :rtype: str
        """
        return self._country_of_risk

    @country_of_risk.setter
    def country_of_risk(self, country_of_risk):
        """Sets the country_of_risk of this Counterparty.

        To which country would one naturally ascribe risk. Typically this will be synonymous with legal registration entity.  This can be used to infer funding currency and related market data in the absence of specific overrides or preference.  # noqa: E501

        :param country_of_risk: The country_of_risk of this Counterparty.  # noqa: E501
        :type: str
        """
        if country_of_risk is None:
            raise ValueError("Invalid value for `country_of_risk`, must not be `None`")  # noqa: E501

        self._country_of_risk = country_of_risk

    @property
    def issuer_ratings(self):
        """Gets the issuer_ratings of this Counterparty.  # noqa: E501

        A set of credit ratings for the counterparty fro, e.g. Standard and Poor or Moody's.  # noqa: E501

        :return: The issuer_ratings of this Counterparty.  # noqa: E501
        :rtype: list[CreditRating]
        """
        return self._issuer_ratings

    @issuer_ratings.setter
    def issuer_ratings(self, issuer_ratings):
        """Sets the issuer_ratings of this Counterparty.

        A set of credit ratings for the counterparty fro, e.g. Standard and Poor or Moody's.  # noqa: E501

        :param issuer_ratings: The issuer_ratings of this Counterparty.  # noqa: E501
        :type: list[CreditRating]
        """
        if issuer_ratings is None:
            raise ValueError("Invalid value for `issuer_ratings`, must not be `None`")  # noqa: E501

        self._issuer_ratings = issuer_ratings

    @property
    def industry_scheme(self):
        """Gets the industry_scheme of this Counterparty.  # noqa: E501


        :return: The industry_scheme of this Counterparty.  # noqa: E501
        :rtype: IndustryClassificationScheme
        """
        return self._industry_scheme

    @industry_scheme.setter
    def industry_scheme(self, industry_scheme):
        """Sets the industry_scheme of this Counterparty.


        :param industry_scheme: The industry_scheme of this Counterparty.  # noqa: E501
        :type: IndustryClassificationScheme
        """
        if industry_scheme is None:
            raise ValueError("Invalid value for `industry_scheme`, must not be `None`")  # noqa: E501

        self._industry_scheme = industry_scheme

    @property
    def scope(self):
        """Gets the scope of this Counterparty.  # noqa: E501

        The scope used when updating or inserting the convention.  # noqa: E501

        :return: The scope of this Counterparty.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this Counterparty.

        The scope used when updating or inserting the convention.  # noqa: E501

        :param scope: The scope of this Counterparty.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def code(self):
        """Gets the code of this Counterparty.  # noqa: E501

        The code of the convention.  # noqa: E501

        :return: The code of this Counterparty.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Counterparty.

        The code of the convention.  # noqa: E501

        :param code: The code of this Counterparty.  # noqa: E501
        :type: str
        """

        self._code = code

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
        if not isinstance(other, Counterparty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
