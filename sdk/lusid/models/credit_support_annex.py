# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.388
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


class CreditSupportAnnex(object):
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
        'reference_currency': 'str',
        'collateral_currencies': 'list[str]',
        'isda_agreement_version': 'str',
        'margin_call_frequency': 'str',
        'valuation_agent': 'str',
        'threshold_amount': 'float',
        'rounding_decimal_places': 'int',
        'initial_margin_amount': 'float',
        'minimum_transfer_amount': 'float',
        'id': 'ResourceId'
    }

    attribute_map = {
        'reference_currency': 'referenceCurrency',
        'collateral_currencies': 'collateralCurrencies',
        'isda_agreement_version': 'isdaAgreementVersion',
        'margin_call_frequency': 'marginCallFrequency',
        'valuation_agent': 'valuationAgent',
        'threshold_amount': 'thresholdAmount',
        'rounding_decimal_places': 'roundingDecimalPlaces',
        'initial_margin_amount': 'initialMarginAmount',
        'minimum_transfer_amount': 'minimumTransferAmount',
        'id': 'id'
    }

    required_map = {
        'reference_currency': 'required',
        'collateral_currencies': 'required',
        'isda_agreement_version': 'required',
        'margin_call_frequency': 'required',
        'valuation_agent': 'required',
        'threshold_amount': 'required',
        'rounding_decimal_places': 'required',
        'initial_margin_amount': 'required',
        'minimum_transfer_amount': 'required',
        'id': 'required'
    }

    def __init__(self, reference_currency=None, collateral_currencies=None, isda_agreement_version=None, margin_call_frequency=None, valuation_agent=None, threshold_amount=None, rounding_decimal_places=None, initial_margin_amount=None, minimum_transfer_amount=None, id=None, local_vars_configuration=None):  # noqa: E501
        """CreditSupportAnnex - a model defined in OpenAPI"
        
        :param reference_currency:  The base, or reference, currency against which MtM value and exposure should be calculated  and in which the CSA parameters are defined if the currency is not otherwise explicitly stated. (required)
        :type reference_currency: str
        :param collateral_currencies:  The set of currencies within which it is acceptable to post cash collateral. (required)
        :type collateral_currencies: list[str]
        :param isda_agreement_version:  The transactions will take place with reference to a particular ISDA master agreement. This  will likely be either the ISDA 1992 or ISDA 2002 agremeents or ISDA close-out 2009. (required)
        :type isda_agreement_version: str
        :param margin_call_frequency:  The tenor, e.g. daily (1D) or biweekly (2W), at which frequency a margin call will be made, calculations  made and money transferred to readjust. The calculation might also require a specific time for valuation and notification. (required)
        :type margin_call_frequency: str
        :param valuation_agent:  Are the calculations performed by the institutions's counterparty or the institution trading with them. (required)
        :type valuation_agent: str
        :param threshold_amount:  At what level of exposure does collateral need to be posted. Will typically be zero for banks.  Should be stated in reference currency (required)
        :type threshold_amount: float
        :param rounding_decimal_places:  Where a calculation needs to be rounded to a specific number of decimal places,  this states the number that that requires. (required)
        :type rounding_decimal_places: int
        :param initial_margin_amount:  The initial margin that is required. In the reference currency (required)
        :type initial_margin_amount: float
        :param minimum_transfer_amount:  The minimum amount, in the reference currency, that must be transferred when required. (required)
        :type minimum_transfer_amount: float
        :param id:  (required)
        :type id: lusid.ResourceId

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._reference_currency = None
        self._collateral_currencies = None
        self._isda_agreement_version = None
        self._margin_call_frequency = None
        self._valuation_agent = None
        self._threshold_amount = None
        self._rounding_decimal_places = None
        self._initial_margin_amount = None
        self._minimum_transfer_amount = None
        self._id = None
        self.discriminator = None

        self.reference_currency = reference_currency
        self.collateral_currencies = collateral_currencies
        self.isda_agreement_version = isda_agreement_version
        self.margin_call_frequency = margin_call_frequency
        self.valuation_agent = valuation_agent
        self.threshold_amount = threshold_amount
        self.rounding_decimal_places = rounding_decimal_places
        self.initial_margin_amount = initial_margin_amount
        self.minimum_transfer_amount = minimum_transfer_amount
        self.id = id

    @property
    def reference_currency(self):
        """Gets the reference_currency of this CreditSupportAnnex.  # noqa: E501

        The base, or reference, currency against which MtM value and exposure should be calculated  and in which the CSA parameters are defined if the currency is not otherwise explicitly stated.  # noqa: E501

        :return: The reference_currency of this CreditSupportAnnex.  # noqa: E501
        :rtype: str
        """
        return self._reference_currency

    @reference_currency.setter
    def reference_currency(self, reference_currency):
        """Sets the reference_currency of this CreditSupportAnnex.

        The base, or reference, currency against which MtM value and exposure should be calculated  and in which the CSA parameters are defined if the currency is not otherwise explicitly stated.  # noqa: E501

        :param reference_currency: The reference_currency of this CreditSupportAnnex.  # noqa: E501
        :type reference_currency: str
        """
        if self.local_vars_configuration.client_side_validation and reference_currency is None:  # noqa: E501
            raise ValueError("Invalid value for `reference_currency`, must not be `None`")  # noqa: E501

        self._reference_currency = reference_currency

    @property
    def collateral_currencies(self):
        """Gets the collateral_currencies of this CreditSupportAnnex.  # noqa: E501

        The set of currencies within which it is acceptable to post cash collateral.  # noqa: E501

        :return: The collateral_currencies of this CreditSupportAnnex.  # noqa: E501
        :rtype: list[str]
        """
        return self._collateral_currencies

    @collateral_currencies.setter
    def collateral_currencies(self, collateral_currencies):
        """Sets the collateral_currencies of this CreditSupportAnnex.

        The set of currencies within which it is acceptable to post cash collateral.  # noqa: E501

        :param collateral_currencies: The collateral_currencies of this CreditSupportAnnex.  # noqa: E501
        :type collateral_currencies: list[str]
        """
        if self.local_vars_configuration.client_side_validation and collateral_currencies is None:  # noqa: E501
            raise ValueError("Invalid value for `collateral_currencies`, must not be `None`")  # noqa: E501

        self._collateral_currencies = collateral_currencies

    @property
    def isda_agreement_version(self):
        """Gets the isda_agreement_version of this CreditSupportAnnex.  # noqa: E501

        The transactions will take place with reference to a particular ISDA master agreement. This  will likely be either the ISDA 1992 or ISDA 2002 agremeents or ISDA close-out 2009.  # noqa: E501

        :return: The isda_agreement_version of this CreditSupportAnnex.  # noqa: E501
        :rtype: str
        """
        return self._isda_agreement_version

    @isda_agreement_version.setter
    def isda_agreement_version(self, isda_agreement_version):
        """Sets the isda_agreement_version of this CreditSupportAnnex.

        The transactions will take place with reference to a particular ISDA master agreement. This  will likely be either the ISDA 1992 or ISDA 2002 agremeents or ISDA close-out 2009.  # noqa: E501

        :param isda_agreement_version: The isda_agreement_version of this CreditSupportAnnex.  # noqa: E501
        :type isda_agreement_version: str
        """
        if self.local_vars_configuration.client_side_validation and isda_agreement_version is None:  # noqa: E501
            raise ValueError("Invalid value for `isda_agreement_version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                isda_agreement_version is not None and len(isda_agreement_version) > 128):
            raise ValueError("Invalid value for `isda_agreement_version`, length must be less than or equal to `128`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                isda_agreement_version is not None and len(isda_agreement_version) < 0):
            raise ValueError("Invalid value for `isda_agreement_version`, length must be greater than or equal to `0`")  # noqa: E501

        self._isda_agreement_version = isda_agreement_version

    @property
    def margin_call_frequency(self):
        """Gets the margin_call_frequency of this CreditSupportAnnex.  # noqa: E501

        The tenor, e.g. daily (1D) or biweekly (2W), at which frequency a margin call will be made, calculations  made and money transferred to readjust. The calculation might also require a specific time for valuation and notification.  # noqa: E501

        :return: The margin_call_frequency of this CreditSupportAnnex.  # noqa: E501
        :rtype: str
        """
        return self._margin_call_frequency

    @margin_call_frequency.setter
    def margin_call_frequency(self, margin_call_frequency):
        """Sets the margin_call_frequency of this CreditSupportAnnex.

        The tenor, e.g. daily (1D) or biweekly (2W), at which frequency a margin call will be made, calculations  made and money transferred to readjust. The calculation might also require a specific time for valuation and notification.  # noqa: E501

        :param margin_call_frequency: The margin_call_frequency of this CreditSupportAnnex.  # noqa: E501
        :type margin_call_frequency: str
        """
        if self.local_vars_configuration.client_side_validation and margin_call_frequency is None:  # noqa: E501
            raise ValueError("Invalid value for `margin_call_frequency`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                margin_call_frequency is not None and len(margin_call_frequency) > 32):
            raise ValueError("Invalid value for `margin_call_frequency`, length must be less than or equal to `32`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                margin_call_frequency is not None and len(margin_call_frequency) < 0):
            raise ValueError("Invalid value for `margin_call_frequency`, length must be greater than or equal to `0`")  # noqa: E501

        self._margin_call_frequency = margin_call_frequency

    @property
    def valuation_agent(self):
        """Gets the valuation_agent of this CreditSupportAnnex.  # noqa: E501

        Are the calculations performed by the institutions's counterparty or the institution trading with them.  # noqa: E501

        :return: The valuation_agent of this CreditSupportAnnex.  # noqa: E501
        :rtype: str
        """
        return self._valuation_agent

    @valuation_agent.setter
    def valuation_agent(self, valuation_agent):
        """Sets the valuation_agent of this CreditSupportAnnex.

        Are the calculations performed by the institutions's counterparty or the institution trading with them.  # noqa: E501

        :param valuation_agent: The valuation_agent of this CreditSupportAnnex.  # noqa: E501
        :type valuation_agent: str
        """
        if self.local_vars_configuration.client_side_validation and valuation_agent is None:  # noqa: E501
            raise ValueError("Invalid value for `valuation_agent`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                valuation_agent is not None and len(valuation_agent) > 256):
            raise ValueError("Invalid value for `valuation_agent`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                valuation_agent is not None and len(valuation_agent) < 0):
            raise ValueError("Invalid value for `valuation_agent`, length must be greater than or equal to `0`")  # noqa: E501

        self._valuation_agent = valuation_agent

    @property
    def threshold_amount(self):
        """Gets the threshold_amount of this CreditSupportAnnex.  # noqa: E501

        At what level of exposure does collateral need to be posted. Will typically be zero for banks.  Should be stated in reference currency  # noqa: E501

        :return: The threshold_amount of this CreditSupportAnnex.  # noqa: E501
        :rtype: float
        """
        return self._threshold_amount

    @threshold_amount.setter
    def threshold_amount(self, threshold_amount):
        """Sets the threshold_amount of this CreditSupportAnnex.

        At what level of exposure does collateral need to be posted. Will typically be zero for banks.  Should be stated in reference currency  # noqa: E501

        :param threshold_amount: The threshold_amount of this CreditSupportAnnex.  # noqa: E501
        :type threshold_amount: float
        """
        if self.local_vars_configuration.client_side_validation and threshold_amount is None:  # noqa: E501
            raise ValueError("Invalid value for `threshold_amount`, must not be `None`")  # noqa: E501

        self._threshold_amount = threshold_amount

    @property
    def rounding_decimal_places(self):
        """Gets the rounding_decimal_places of this CreditSupportAnnex.  # noqa: E501

        Where a calculation needs to be rounded to a specific number of decimal places,  this states the number that that requires.  # noqa: E501

        :return: The rounding_decimal_places of this CreditSupportAnnex.  # noqa: E501
        :rtype: int
        """
        return self._rounding_decimal_places

    @rounding_decimal_places.setter
    def rounding_decimal_places(self, rounding_decimal_places):
        """Sets the rounding_decimal_places of this CreditSupportAnnex.

        Where a calculation needs to be rounded to a specific number of decimal places,  this states the number that that requires.  # noqa: E501

        :param rounding_decimal_places: The rounding_decimal_places of this CreditSupportAnnex.  # noqa: E501
        :type rounding_decimal_places: int
        """
        if self.local_vars_configuration.client_side_validation and rounding_decimal_places is None:  # noqa: E501
            raise ValueError("Invalid value for `rounding_decimal_places`, must not be `None`")  # noqa: E501

        self._rounding_decimal_places = rounding_decimal_places

    @property
    def initial_margin_amount(self):
        """Gets the initial_margin_amount of this CreditSupportAnnex.  # noqa: E501

        The initial margin that is required. In the reference currency  # noqa: E501

        :return: The initial_margin_amount of this CreditSupportAnnex.  # noqa: E501
        :rtype: float
        """
        return self._initial_margin_amount

    @initial_margin_amount.setter
    def initial_margin_amount(self, initial_margin_amount):
        """Sets the initial_margin_amount of this CreditSupportAnnex.

        The initial margin that is required. In the reference currency  # noqa: E501

        :param initial_margin_amount: The initial_margin_amount of this CreditSupportAnnex.  # noqa: E501
        :type initial_margin_amount: float
        """
        if self.local_vars_configuration.client_side_validation and initial_margin_amount is None:  # noqa: E501
            raise ValueError("Invalid value for `initial_margin_amount`, must not be `None`")  # noqa: E501

        self._initial_margin_amount = initial_margin_amount

    @property
    def minimum_transfer_amount(self):
        """Gets the minimum_transfer_amount of this CreditSupportAnnex.  # noqa: E501

        The minimum amount, in the reference currency, that must be transferred when required.  # noqa: E501

        :return: The minimum_transfer_amount of this CreditSupportAnnex.  # noqa: E501
        :rtype: float
        """
        return self._minimum_transfer_amount

    @minimum_transfer_amount.setter
    def minimum_transfer_amount(self, minimum_transfer_amount):
        """Sets the minimum_transfer_amount of this CreditSupportAnnex.

        The minimum amount, in the reference currency, that must be transferred when required.  # noqa: E501

        :param minimum_transfer_amount: The minimum_transfer_amount of this CreditSupportAnnex.  # noqa: E501
        :type minimum_transfer_amount: float
        """
        if self.local_vars_configuration.client_side_validation and minimum_transfer_amount is None:  # noqa: E501
            raise ValueError("Invalid value for `minimum_transfer_amount`, must not be `None`")  # noqa: E501

        self._minimum_transfer_amount = minimum_transfer_amount

    @property
    def id(self):
        """Gets the id of this CreditSupportAnnex.  # noqa: E501


        :return: The id of this CreditSupportAnnex.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreditSupportAnnex.


        :param id: The id of this CreditSupportAnnex.  # noqa: E501
        :type id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

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
        if not isinstance(other, CreditSupportAnnex):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreditSupportAnnex):
            return True

        return self.to_dict() != other.to_dict()
