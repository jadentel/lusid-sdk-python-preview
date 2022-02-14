# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3960
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


class FxForwardTenorCurveData(object):
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
        'tenors': 'list[str]',
        'rates': 'list[float]',
        'market_data_type': 'str'
    }

    attribute_map = {
        'base_date': 'baseDate',
        'dom_ccy': 'domCcy',
        'fgn_ccy': 'fgnCcy',
        'tenors': 'tenors',
        'rates': 'rates',
        'market_data_type': 'marketDataType'
    }

    required_map = {
        'base_date': 'required',
        'dom_ccy': 'required',
        'fgn_ccy': 'required',
        'tenors': 'required',
        'rates': 'required',
        'market_data_type': 'required'
    }

    def __init__(self, base_date=None, dom_ccy=None, fgn_ccy=None, tenors=None, rates=None, market_data_type=None, local_vars_configuration=None):  # noqa: E501
        """FxForwardTenorCurveData - a model defined in OpenAPI"
        
        :param base_date:  EffectiveAt date of the quoted rates (required)
        :type base_date: datetime
        :param dom_ccy:  Domestic currency of the fx forward (required)
        :type dom_ccy: str
        :param fgn_ccy:  Foreign currency of the fx forward (required)
        :type fgn_ccy: str
        :param tenors:  Tenors for which the forward rates apply (required)
        :type tenors: list[str]
        :param rates:  Rates provided for the fx forward (price in FgnCcy per unit of DomCcy) (required)
        :type rates: list[float]
        :param market_data_type:  The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData (required)
        :type market_data_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._base_date = None
        self._dom_ccy = None
        self._fgn_ccy = None
        self._tenors = None
        self._rates = None
        self._market_data_type = None
        self.discriminator = None

        self.base_date = base_date
        self.dom_ccy = dom_ccy
        self.fgn_ccy = fgn_ccy
        self.tenors = tenors
        self.rates = rates
        self.market_data_type = market_data_type

    @property
    def base_date(self):
        """Gets the base_date of this FxForwardTenorCurveData.  # noqa: E501

        EffectiveAt date of the quoted rates  # noqa: E501

        :return: The base_date of this FxForwardTenorCurveData.  # noqa: E501
        :rtype: datetime
        """
        return self._base_date

    @base_date.setter
    def base_date(self, base_date):
        """Sets the base_date of this FxForwardTenorCurveData.

        EffectiveAt date of the quoted rates  # noqa: E501

        :param base_date: The base_date of this FxForwardTenorCurveData.  # noqa: E501
        :type base_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and base_date is None:  # noqa: E501
            raise ValueError("Invalid value for `base_date`, must not be `None`")  # noqa: E501

        self._base_date = base_date

    @property
    def dom_ccy(self):
        """Gets the dom_ccy of this FxForwardTenorCurveData.  # noqa: E501

        Domestic currency of the fx forward  # noqa: E501

        :return: The dom_ccy of this FxForwardTenorCurveData.  # noqa: E501
        :rtype: str
        """
        return self._dom_ccy

    @dom_ccy.setter
    def dom_ccy(self, dom_ccy):
        """Sets the dom_ccy of this FxForwardTenorCurveData.

        Domestic currency of the fx forward  # noqa: E501

        :param dom_ccy: The dom_ccy of this FxForwardTenorCurveData.  # noqa: E501
        :type dom_ccy: str
        """
        if self.local_vars_configuration.client_side_validation and dom_ccy is None:  # noqa: E501
            raise ValueError("Invalid value for `dom_ccy`, must not be `None`")  # noqa: E501

        self._dom_ccy = dom_ccy

    @property
    def fgn_ccy(self):
        """Gets the fgn_ccy of this FxForwardTenorCurveData.  # noqa: E501

        Foreign currency of the fx forward  # noqa: E501

        :return: The fgn_ccy of this FxForwardTenorCurveData.  # noqa: E501
        :rtype: str
        """
        return self._fgn_ccy

    @fgn_ccy.setter
    def fgn_ccy(self, fgn_ccy):
        """Sets the fgn_ccy of this FxForwardTenorCurveData.

        Foreign currency of the fx forward  # noqa: E501

        :param fgn_ccy: The fgn_ccy of this FxForwardTenorCurveData.  # noqa: E501
        :type fgn_ccy: str
        """
        if self.local_vars_configuration.client_side_validation and fgn_ccy is None:  # noqa: E501
            raise ValueError("Invalid value for `fgn_ccy`, must not be `None`")  # noqa: E501

        self._fgn_ccy = fgn_ccy

    @property
    def tenors(self):
        """Gets the tenors of this FxForwardTenorCurveData.  # noqa: E501

        Tenors for which the forward rates apply  # noqa: E501

        :return: The tenors of this FxForwardTenorCurveData.  # noqa: E501
        :rtype: list[str]
        """
        return self._tenors

    @tenors.setter
    def tenors(self, tenors):
        """Sets the tenors of this FxForwardTenorCurveData.

        Tenors for which the forward rates apply  # noqa: E501

        :param tenors: The tenors of this FxForwardTenorCurveData.  # noqa: E501
        :type tenors: list[str]
        """
        if self.local_vars_configuration.client_side_validation and tenors is None:  # noqa: E501
            raise ValueError("Invalid value for `tenors`, must not be `None`")  # noqa: E501

        self._tenors = tenors

    @property
    def rates(self):
        """Gets the rates of this FxForwardTenorCurveData.  # noqa: E501

        Rates provided for the fx forward (price in FgnCcy per unit of DomCcy)  # noqa: E501

        :return: The rates of this FxForwardTenorCurveData.  # noqa: E501
        :rtype: list[float]
        """
        return self._rates

    @rates.setter
    def rates(self, rates):
        """Sets the rates of this FxForwardTenorCurveData.

        Rates provided for the fx forward (price in FgnCcy per unit of DomCcy)  # noqa: E501

        :param rates: The rates of this FxForwardTenorCurveData.  # noqa: E501
        :type rates: list[float]
        """
        if self.local_vars_configuration.client_side_validation and rates is None:  # noqa: E501
            raise ValueError("Invalid value for `rates`, must not be `None`")  # noqa: E501

        self._rates = rates

    @property
    def market_data_type(self):
        """Gets the market_data_type of this FxForwardTenorCurveData.  # noqa: E501

        The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData  # noqa: E501

        :return: The market_data_type of this FxForwardTenorCurveData.  # noqa: E501
        :rtype: str
        """
        return self._market_data_type

    @market_data_type.setter
    def market_data_type(self, market_data_type):
        """Sets the market_data_type of this FxForwardTenorCurveData.

        The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData  # noqa: E501

        :param market_data_type: The market_data_type of this FxForwardTenorCurveData.  # noqa: E501
        :type market_data_type: str
        """
        if self.local_vars_configuration.client_side_validation and market_data_type is None:  # noqa: E501
            raise ValueError("Invalid value for `market_data_type`, must not be `None`")  # noqa: E501
        allowed_values = ["DiscountFactorCurveData", "EquityVolSurfaceData", "FxVolSurfaceData", "IrVolCubeData", "OpaqueMarketData", "YieldCurveData", "FxForwardCurveData", "FxForwardPipsCurveData", "FxForwardTenorCurveData", "FxForwardTenorPipsCurveData", "FxForwardCurveByQuoteReference", "CreditSpreadCurveData"]  # noqa: E501
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
        if not isinstance(other, FxForwardTenorCurveData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FxForwardTenorCurveData):
            return True

        return self.to_dict() != other.to_dict()
