# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.108
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


class FxForwardsDependency(object):
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
        'domestic_currency': 'str',
        'foreign_currency': 'str',
        'curve_type': 'str',
        'date': 'datetime',
        'dependency_type': 'str'
    }

    attribute_map = {
        'domestic_currency': 'domesticCurrency',
        'foreign_currency': 'foreignCurrency',
        'curve_type': 'curveType',
        'date': 'date',
        'dependency_type': 'dependencyType'
    }

    required_map = {
        'domestic_currency': 'required',
        'foreign_currency': 'required',
        'curve_type': 'required',
        'date': 'required',
        'dependency_type': 'required'
    }

    def __init__(self, domestic_currency=None, foreign_currency=None, curve_type=None, date=None, dependency_type=None, local_vars_configuration=None):  # noqa: E501
        """FxForwardsDependency - a model defined in OpenAPI"
        
        :param domestic_currency:  DomesticCurrency is the first currency in a currency pair quote e.g. eur-gbp, eur is the domestic currency. (required)
        :type domestic_currency: str
        :param foreign_currency:  ForeignCurrency is the second currency in a currency pair quote e.g. eur-gbp, gbp is the foreign currency. (required)
        :type foreign_currency: str
        :param curve_type:  Used to describe the format in which the curve is expressed  e.g. FxFwdCurve (general term to describe any representation), TenorFxFwdCurve, PipsFxFwdCurve. (required)
        :type curve_type: str
        :param date:  The effectiveDate of the entity that this is a dependency for.  Unless there is an obvious date this should be, like for a historic reset, then this is the valuation date. (required)
        :type date: datetime
        :param dependency_type:  The available values are: Opaque, Cash, Discounting, EquityCurve, EquityVol, Fx, FxForwards, FxVol, IndexProjection, IrVol, Quote, Vendor (required)
        :type dependency_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._domestic_currency = None
        self._foreign_currency = None
        self._curve_type = None
        self._date = None
        self._dependency_type = None
        self.discriminator = None

        self.domestic_currency = domestic_currency
        self.foreign_currency = foreign_currency
        self.curve_type = curve_type
        self.date = date
        self.dependency_type = dependency_type

    @property
    def domestic_currency(self):
        """Gets the domestic_currency of this FxForwardsDependency.  # noqa: E501

        DomesticCurrency is the first currency in a currency pair quote e.g. eur-gbp, eur is the domestic currency.  # noqa: E501

        :return: The domestic_currency of this FxForwardsDependency.  # noqa: E501
        :rtype: str
        """
        return self._domestic_currency

    @domestic_currency.setter
    def domestic_currency(self, domestic_currency):
        """Sets the domestic_currency of this FxForwardsDependency.

        DomesticCurrency is the first currency in a currency pair quote e.g. eur-gbp, eur is the domestic currency.  # noqa: E501

        :param domestic_currency: The domestic_currency of this FxForwardsDependency.  # noqa: E501
        :type domestic_currency: str
        """
        if self.local_vars_configuration.client_side_validation and domestic_currency is None:  # noqa: E501
            raise ValueError("Invalid value for `domestic_currency`, must not be `None`")  # noqa: E501

        self._domestic_currency = domestic_currency

    @property
    def foreign_currency(self):
        """Gets the foreign_currency of this FxForwardsDependency.  # noqa: E501

        ForeignCurrency is the second currency in a currency pair quote e.g. eur-gbp, gbp is the foreign currency.  # noqa: E501

        :return: The foreign_currency of this FxForwardsDependency.  # noqa: E501
        :rtype: str
        """
        return self._foreign_currency

    @foreign_currency.setter
    def foreign_currency(self, foreign_currency):
        """Sets the foreign_currency of this FxForwardsDependency.

        ForeignCurrency is the second currency in a currency pair quote e.g. eur-gbp, gbp is the foreign currency.  # noqa: E501

        :param foreign_currency: The foreign_currency of this FxForwardsDependency.  # noqa: E501
        :type foreign_currency: str
        """
        if self.local_vars_configuration.client_side_validation and foreign_currency is None:  # noqa: E501
            raise ValueError("Invalid value for `foreign_currency`, must not be `None`")  # noqa: E501

        self._foreign_currency = foreign_currency

    @property
    def curve_type(self):
        """Gets the curve_type of this FxForwardsDependency.  # noqa: E501

        Used to describe the format in which the curve is expressed  e.g. FxFwdCurve (general term to describe any representation), TenorFxFwdCurve, PipsFxFwdCurve.  # noqa: E501

        :return: The curve_type of this FxForwardsDependency.  # noqa: E501
        :rtype: str
        """
        return self._curve_type

    @curve_type.setter
    def curve_type(self, curve_type):
        """Sets the curve_type of this FxForwardsDependency.

        Used to describe the format in which the curve is expressed  e.g. FxFwdCurve (general term to describe any representation), TenorFxFwdCurve, PipsFxFwdCurve.  # noqa: E501

        :param curve_type: The curve_type of this FxForwardsDependency.  # noqa: E501
        :type curve_type: str
        """
        if self.local_vars_configuration.client_side_validation and curve_type is None:  # noqa: E501
            raise ValueError("Invalid value for `curve_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                curve_type is not None and len(curve_type) > 50):
            raise ValueError("Invalid value for `curve_type`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                curve_type is not None and len(curve_type) < 0):
            raise ValueError("Invalid value for `curve_type`, length must be greater than or equal to `0`")  # noqa: E501

        self._curve_type = curve_type

    @property
    def date(self):
        """Gets the date of this FxForwardsDependency.  # noqa: E501

        The effectiveDate of the entity that this is a dependency for.  Unless there is an obvious date this should be, like for a historic reset, then this is the valuation date.  # noqa: E501

        :return: The date of this FxForwardsDependency.  # noqa: E501
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this FxForwardsDependency.

        The effectiveDate of the entity that this is a dependency for.  Unless there is an obvious date this should be, like for a historic reset, then this is the valuation date.  # noqa: E501

        :param date: The date of this FxForwardsDependency.  # noqa: E501
        :type date: datetime
        """
        if self.local_vars_configuration.client_side_validation and date is None:  # noqa: E501
            raise ValueError("Invalid value for `date`, must not be `None`")  # noqa: E501

        self._date = date

    @property
    def dependency_type(self):
        """Gets the dependency_type of this FxForwardsDependency.  # noqa: E501

        The available values are: Opaque, Cash, Discounting, EquityCurve, EquityVol, Fx, FxForwards, FxVol, IndexProjection, IrVol, Quote, Vendor  # noqa: E501

        :return: The dependency_type of this FxForwardsDependency.  # noqa: E501
        :rtype: str
        """
        return self._dependency_type

    @dependency_type.setter
    def dependency_type(self, dependency_type):
        """Sets the dependency_type of this FxForwardsDependency.

        The available values are: Opaque, Cash, Discounting, EquityCurve, EquityVol, Fx, FxForwards, FxVol, IndexProjection, IrVol, Quote, Vendor  # noqa: E501

        :param dependency_type: The dependency_type of this FxForwardsDependency.  # noqa: E501
        :type dependency_type: str
        """
        if self.local_vars_configuration.client_side_validation and dependency_type is None:  # noqa: E501
            raise ValueError("Invalid value for `dependency_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Opaque", "Cash", "Discounting", "EquityCurve", "EquityVol", "Fx", "FxForwards", "FxVol", "IndexProjection", "IrVol", "Quote", "Vendor"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and dependency_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `dependency_type` ({0}), must be one of {1}"  # noqa: E501
                .format(dependency_type, allowed_values)
            )

        self._dependency_type = dependency_type

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
        if not isinstance(other, FxForwardsDependency):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FxForwardsDependency):
            return True

        return self.to_dict() != other.to_dict()
