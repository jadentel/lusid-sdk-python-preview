# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4719
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


class FxForwardPipsCurveDataAllOf(object):
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
        'base_date': 'datetime',
        'dom_ccy': 'str',
        'fgn_ccy': 'str',
        'dates': 'list[datetime]',
        'pip_rates': 'list[float]',
        'lineage': 'str',
        'market_data_type': 'str'
    }

    attribute_map = {
        'base_date': 'baseDate',
        'dom_ccy': 'domCcy',
        'fgn_ccy': 'fgnCcy',
        'dates': 'dates',
        'pip_rates': 'pipRates',
        'lineage': 'lineage',
        'market_data_type': 'marketDataType'
    }

    required_map = {
        'base_date': 'required',
        'dom_ccy': 'required',
        'fgn_ccy': 'required',
        'dates': 'required',
        'pip_rates': 'required',
        'lineage': 'optional',
        'market_data_type': 'required'
    }

    def __init__(self, base_date=None, dom_ccy=None, fgn_ccy=None, dates=None, pip_rates=None, lineage=None, market_data_type=None, local_vars_configuration=None):  # noqa: E501
        """FxForwardPipsCurveDataAllOf - a model defined in OpenAPI"
        
        :param base_date:  EffectiveAt date of the quoted pip rates (required)
        :type base_date: datetime
        :param dom_ccy:  Domestic currency of the fx forward (required)
        :type dom_ccy: str
        :param fgn_ccy:  Foreign currency of the fx forward (required)
        :type fgn_ccy: str
        :param dates:  Dates for which the forward rates apply (required)
        :type dates: list[datetime]
        :param pip_rates:  Rates provided for the fx forward (price in FgnCcy per unit of DomCcy), expressed in pips (required)
        :type pip_rates: list[float]
        :param lineage:  Description of the complex market data's lineage e.g. 'FundAccountant_GreenQuality'.
        :type lineage: str
        :param market_data_type:  The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData (required)
        :type market_data_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._base_date = None
        self._dom_ccy = None
        self._fgn_ccy = None
        self._dates = None
        self._pip_rates = None
        self._lineage = None
        self._market_data_type = None
        self.discriminator = None

        self.base_date = base_date
        self.dom_ccy = dom_ccy
        self.fgn_ccy = fgn_ccy
        self.dates = dates
        self.pip_rates = pip_rates
        self.lineage = lineage
        self.market_data_type = market_data_type

    @property
    def base_date(self):
        """Gets the base_date of this FxForwardPipsCurveDataAllOf.  # noqa: E501

        EffectiveAt date of the quoted pip rates  # noqa: E501

        :return: The base_date of this FxForwardPipsCurveDataAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._base_date

    @base_date.setter
    def base_date(self, base_date):
        """Sets the base_date of this FxForwardPipsCurveDataAllOf.

        EffectiveAt date of the quoted pip rates  # noqa: E501

        :param base_date: The base_date of this FxForwardPipsCurveDataAllOf.  # noqa: E501
        :type base_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and base_date is None:  # noqa: E501
            raise ValueError("Invalid value for `base_date`, must not be `None`")  # noqa: E501

        self._base_date = base_date

    @property
    def dom_ccy(self):
        """Gets the dom_ccy of this FxForwardPipsCurveDataAllOf.  # noqa: E501

        Domestic currency of the fx forward  # noqa: E501

        :return: The dom_ccy of this FxForwardPipsCurveDataAllOf.  # noqa: E501
        :rtype: str
        """
        return self._dom_ccy

    @dom_ccy.setter
    def dom_ccy(self, dom_ccy):
        """Sets the dom_ccy of this FxForwardPipsCurveDataAllOf.

        Domestic currency of the fx forward  # noqa: E501

        :param dom_ccy: The dom_ccy of this FxForwardPipsCurveDataAllOf.  # noqa: E501
        :type dom_ccy: str
        """
        if self.local_vars_configuration.client_side_validation and dom_ccy is None:  # noqa: E501
            raise ValueError("Invalid value for `dom_ccy`, must not be `None`")  # noqa: E501

        self._dom_ccy = dom_ccy

    @property
    def fgn_ccy(self):
        """Gets the fgn_ccy of this FxForwardPipsCurveDataAllOf.  # noqa: E501

        Foreign currency of the fx forward  # noqa: E501

        :return: The fgn_ccy of this FxForwardPipsCurveDataAllOf.  # noqa: E501
        :rtype: str
        """
        return self._fgn_ccy

    @fgn_ccy.setter
    def fgn_ccy(self, fgn_ccy):
        """Sets the fgn_ccy of this FxForwardPipsCurveDataAllOf.

        Foreign currency of the fx forward  # noqa: E501

        :param fgn_ccy: The fgn_ccy of this FxForwardPipsCurveDataAllOf.  # noqa: E501
        :type fgn_ccy: str
        """
        if self.local_vars_configuration.client_side_validation and fgn_ccy is None:  # noqa: E501
            raise ValueError("Invalid value for `fgn_ccy`, must not be `None`")  # noqa: E501

        self._fgn_ccy = fgn_ccy

    @property
    def dates(self):
        """Gets the dates of this FxForwardPipsCurveDataAllOf.  # noqa: E501

        Dates for which the forward rates apply  # noqa: E501

        :return: The dates of this FxForwardPipsCurveDataAllOf.  # noqa: E501
        :rtype: list[datetime]
        """
        return self._dates

    @dates.setter
    def dates(self, dates):
        """Sets the dates of this FxForwardPipsCurveDataAllOf.

        Dates for which the forward rates apply  # noqa: E501

        :param dates: The dates of this FxForwardPipsCurveDataAllOf.  # noqa: E501
        :type dates: list[datetime]
        """
        if self.local_vars_configuration.client_side_validation and dates is None:  # noqa: E501
            raise ValueError("Invalid value for `dates`, must not be `None`")  # noqa: E501

        self._dates = dates

    @property
    def pip_rates(self):
        """Gets the pip_rates of this FxForwardPipsCurveDataAllOf.  # noqa: E501

        Rates provided for the fx forward (price in FgnCcy per unit of DomCcy), expressed in pips  # noqa: E501

        :return: The pip_rates of this FxForwardPipsCurveDataAllOf.  # noqa: E501
        :rtype: list[float]
        """
        return self._pip_rates

    @pip_rates.setter
    def pip_rates(self, pip_rates):
        """Sets the pip_rates of this FxForwardPipsCurveDataAllOf.

        Rates provided for the fx forward (price in FgnCcy per unit of DomCcy), expressed in pips  # noqa: E501

        :param pip_rates: The pip_rates of this FxForwardPipsCurveDataAllOf.  # noqa: E501
        :type pip_rates: list[float]
        """
        if self.local_vars_configuration.client_side_validation and pip_rates is None:  # noqa: E501
            raise ValueError("Invalid value for `pip_rates`, must not be `None`")  # noqa: E501

        self._pip_rates = pip_rates

    @property
    def lineage(self):
        """Gets the lineage of this FxForwardPipsCurveDataAllOf.  # noqa: E501

        Description of the complex market data's lineage e.g. 'FundAccountant_GreenQuality'.  # noqa: E501

        :return: The lineage of this FxForwardPipsCurveDataAllOf.  # noqa: E501
        :rtype: str
        """
        return self._lineage

    @lineage.setter
    def lineage(self, lineage):
        """Sets the lineage of this FxForwardPipsCurveDataAllOf.

        Description of the complex market data's lineage e.g. 'FundAccountant_GreenQuality'.  # noqa: E501

        :param lineage: The lineage of this FxForwardPipsCurveDataAllOf.  # noqa: E501
        :type lineage: str
        """
        if (self.local_vars_configuration.client_side_validation and
                lineage is not None and len(lineage) > 1024):
            raise ValueError("Invalid value for `lineage`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                lineage is not None and len(lineage) < 0):
            raise ValueError("Invalid value for `lineage`, length must be greater than or equal to `0`")  # noqa: E501

        self._lineage = lineage

    @property
    def market_data_type(self):
        """Gets the market_data_type of this FxForwardPipsCurveDataAllOf.  # noqa: E501

        The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData  # noqa: E501

        :return: The market_data_type of this FxForwardPipsCurveDataAllOf.  # noqa: E501
        :rtype: str
        """
        return self._market_data_type

    @market_data_type.setter
    def market_data_type(self, market_data_type):
        """Sets the market_data_type of this FxForwardPipsCurveDataAllOf.

        The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData  # noqa: E501

        :param market_data_type: The market_data_type of this FxForwardPipsCurveDataAllOf.  # noqa: E501
        :type market_data_type: str
        """
        if self.local_vars_configuration.client_side_validation and market_data_type is None:  # noqa: E501
            raise ValueError("Invalid value for `market_data_type`, must not be `None`")  # noqa: E501
        allowed_values = ["DiscountFactorCurveData", "EquityVolSurfaceData", "FxVolSurfaceData", "IrVolCubeData", "OpaqueMarketData", "YieldCurveData", "FxForwardCurveData", "FxForwardPipsCurveData", "FxForwardTenorCurveData", "FxForwardTenorPipsCurveData", "FxForwardCurveByQuoteReference", "CreditSpreadCurveData", "EquityCurveByPricesData"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and market_data_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `market_data_type` ({0}), must be one of {1}"  # noqa: E501
                .format(market_data_type, allowed_values)
            )

        self._market_data_type = market_data_type

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
        if not isinstance(other, FxForwardPipsCurveDataAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FxForwardPipsCurveDataAllOf):
            return True

        return self.to_dict() != other.to_dict()
