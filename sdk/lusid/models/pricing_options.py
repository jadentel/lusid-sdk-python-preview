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


class PricingOptions(object):
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
        'model_selection': 'ModelSelection',
        'use_instrument_type_to_determine_pricer': 'bool',
        'allow_any_instruments_with_sec_uid_to_price_off_lookup': 'bool',
        'allow_partially_successful_evaluation': 'bool',
        'produce_separate_result_for_linear_otc_legs': 'bool',
        'enable_use_of_cached_unit_results': 'bool',
        'window_valuation_on_instrument_start_end': 'bool',
        'remove_contingent_cashflows_in_payment_diary': 'bool',
        'use_child_sub_holding_keys_for_portfolio_expansion': 'bool',
        'validate_domestic_and_quote_currencies_are_consistent': 'bool'
    }

    attribute_map = {
        'model_selection': 'modelSelection',
        'use_instrument_type_to_determine_pricer': 'useInstrumentTypeToDeterminePricer',
        'allow_any_instruments_with_sec_uid_to_price_off_lookup': 'allowAnyInstrumentsWithSecUidToPriceOffLookup',
        'allow_partially_successful_evaluation': 'allowPartiallySuccessfulEvaluation',
        'produce_separate_result_for_linear_otc_legs': 'produceSeparateResultForLinearOtcLegs',
        'enable_use_of_cached_unit_results': 'enableUseOfCachedUnitResults',
        'window_valuation_on_instrument_start_end': 'windowValuationOnInstrumentStartEnd',
        'remove_contingent_cashflows_in_payment_diary': 'removeContingentCashflowsInPaymentDiary',
        'use_child_sub_holding_keys_for_portfolio_expansion': 'useChildSubHoldingKeysForPortfolioExpansion',
        'validate_domestic_and_quote_currencies_are_consistent': 'validateDomesticAndQuoteCurrenciesAreConsistent'
    }

    required_map = {
        'model_selection': 'optional',
        'use_instrument_type_to_determine_pricer': 'optional',
        'allow_any_instruments_with_sec_uid_to_price_off_lookup': 'optional',
        'allow_partially_successful_evaluation': 'optional',
        'produce_separate_result_for_linear_otc_legs': 'optional',
        'enable_use_of_cached_unit_results': 'optional',
        'window_valuation_on_instrument_start_end': 'optional',
        'remove_contingent_cashflows_in_payment_diary': 'optional',
        'use_child_sub_holding_keys_for_portfolio_expansion': 'optional',
        'validate_domestic_and_quote_currencies_are_consistent': 'optional'
    }

    def __init__(self, model_selection=None, use_instrument_type_to_determine_pricer=None, allow_any_instruments_with_sec_uid_to_price_off_lookup=None, allow_partially_successful_evaluation=None, produce_separate_result_for_linear_otc_legs=None, enable_use_of_cached_unit_results=None, window_valuation_on_instrument_start_end=None, remove_contingent_cashflows_in_payment_diary=None, use_child_sub_holding_keys_for_portfolio_expansion=None, validate_domestic_and_quote_currencies_are_consistent=None, local_vars_configuration=None):  # noqa: E501
        """PricingOptions - a model defined in OpenAPI"
        
        :param model_selection: 
        :type model_selection: lusid.ModelSelection
        :param use_instrument_type_to_determine_pricer:  If true then use the instrument type to set the default instrument pricer  This applies where no more specific set of overrides are provided on a per-vendor and instrument basis.
        :type use_instrument_type_to_determine_pricer: bool
        :param allow_any_instruments_with_sec_uid_to_price_off_lookup:  By default, one would not expect to price and exotic instrument, i.e. an instrument with a complicated  instrument definition simply through looking up a price as there should be a better way of evaluating it.  To override that behaviour and allow lookup for a price from the instrument identifier(s), set this to true.
        :type allow_any_instruments_with_sec_uid_to_price_off_lookup: bool
        :param allow_partially_successful_evaluation:  If true then a failure in task evaluation doesn't cause overall failure.  results will be returned where they succeeded and annotation elsewhere
        :type allow_partially_successful_evaluation: bool
        :param produce_separate_result_for_linear_otc_legs:  If true (default), when pricing an Fx-Forward or Interest Rate Swap, Future and other linearly separable products, product two results, one for each leg  rather than a single line result with the amalgamated/summed pv from both legs.
        :type produce_separate_result_for_linear_otc_legs: bool
        :param enable_use_of_cached_unit_results:  If true, when pricing using a model or for an instrument that supports use of intermediate cached-results, use them.  Default is that this caching is turned off.
        :type enable_use_of_cached_unit_results: bool
        :param window_valuation_on_instrument_start_end:  If true, when valuing an instrument outside the period where it is 'alive' (the start-maturity window) it will return a valuation of zero
        :type window_valuation_on_instrument_start_end: bool
        :param remove_contingent_cashflows_in_payment_diary:  When creating a payment diary, should contingent cash payments (e.g. from exercise of a swaption into a swap) be included or not.  i.e. Is exercise or default being assumed to happen or not.
        :type remove_contingent_cashflows_in_payment_diary: bool
        :param use_child_sub_holding_keys_for_portfolio_expansion:  Should fund constituents inherit subholding keys from the parent subholding keyb
        :type use_child_sub_holding_keys_for_portfolio_expansion: bool
        :param validate_domestic_and_quote_currencies_are_consistent:  Do we validate that the instrument domestic currency matches the quote currency (unless unknown/zzz) when using lookup pricing.
        :type validate_domestic_and_quote_currencies_are_consistent: bool

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._model_selection = None
        self._use_instrument_type_to_determine_pricer = None
        self._allow_any_instruments_with_sec_uid_to_price_off_lookup = None
        self._allow_partially_successful_evaluation = None
        self._produce_separate_result_for_linear_otc_legs = None
        self._enable_use_of_cached_unit_results = None
        self._window_valuation_on_instrument_start_end = None
        self._remove_contingent_cashflows_in_payment_diary = None
        self._use_child_sub_holding_keys_for_portfolio_expansion = None
        self._validate_domestic_and_quote_currencies_are_consistent = None
        self.discriminator = None

        if model_selection is not None:
            self.model_selection = model_selection
        if use_instrument_type_to_determine_pricer is not None:
            self.use_instrument_type_to_determine_pricer = use_instrument_type_to_determine_pricer
        if allow_any_instruments_with_sec_uid_to_price_off_lookup is not None:
            self.allow_any_instruments_with_sec_uid_to_price_off_lookup = allow_any_instruments_with_sec_uid_to_price_off_lookup
        if allow_partially_successful_evaluation is not None:
            self.allow_partially_successful_evaluation = allow_partially_successful_evaluation
        if produce_separate_result_for_linear_otc_legs is not None:
            self.produce_separate_result_for_linear_otc_legs = produce_separate_result_for_linear_otc_legs
        if enable_use_of_cached_unit_results is not None:
            self.enable_use_of_cached_unit_results = enable_use_of_cached_unit_results
        if window_valuation_on_instrument_start_end is not None:
            self.window_valuation_on_instrument_start_end = window_valuation_on_instrument_start_end
        if remove_contingent_cashflows_in_payment_diary is not None:
            self.remove_contingent_cashflows_in_payment_diary = remove_contingent_cashflows_in_payment_diary
        if use_child_sub_holding_keys_for_portfolio_expansion is not None:
            self.use_child_sub_holding_keys_for_portfolio_expansion = use_child_sub_holding_keys_for_portfolio_expansion
        if validate_domestic_and_quote_currencies_are_consistent is not None:
            self.validate_domestic_and_quote_currencies_are_consistent = validate_domestic_and_quote_currencies_are_consistent

    @property
    def model_selection(self):
        """Gets the model_selection of this PricingOptions.  # noqa: E501


        :return: The model_selection of this PricingOptions.  # noqa: E501
        :rtype: lusid.ModelSelection
        """
        return self._model_selection

    @model_selection.setter
    def model_selection(self, model_selection):
        """Sets the model_selection of this PricingOptions.


        :param model_selection: The model_selection of this PricingOptions.  # noqa: E501
        :type model_selection: lusid.ModelSelection
        """

        self._model_selection = model_selection

    @property
    def use_instrument_type_to_determine_pricer(self):
        """Gets the use_instrument_type_to_determine_pricer of this PricingOptions.  # noqa: E501

        If true then use the instrument type to set the default instrument pricer  This applies where no more specific set of overrides are provided on a per-vendor and instrument basis.  # noqa: E501

        :return: The use_instrument_type_to_determine_pricer of this PricingOptions.  # noqa: E501
        :rtype: bool
        """
        return self._use_instrument_type_to_determine_pricer

    @use_instrument_type_to_determine_pricer.setter
    def use_instrument_type_to_determine_pricer(self, use_instrument_type_to_determine_pricer):
        """Sets the use_instrument_type_to_determine_pricer of this PricingOptions.

        If true then use the instrument type to set the default instrument pricer  This applies where no more specific set of overrides are provided on a per-vendor and instrument basis.  # noqa: E501

        :param use_instrument_type_to_determine_pricer: The use_instrument_type_to_determine_pricer of this PricingOptions.  # noqa: E501
        :type use_instrument_type_to_determine_pricer: bool
        """

        self._use_instrument_type_to_determine_pricer = use_instrument_type_to_determine_pricer

    @property
    def allow_any_instruments_with_sec_uid_to_price_off_lookup(self):
        """Gets the allow_any_instruments_with_sec_uid_to_price_off_lookup of this PricingOptions.  # noqa: E501

        By default, one would not expect to price and exotic instrument, i.e. an instrument with a complicated  instrument definition simply through looking up a price as there should be a better way of evaluating it.  To override that behaviour and allow lookup for a price from the instrument identifier(s), set this to true.  # noqa: E501

        :return: The allow_any_instruments_with_sec_uid_to_price_off_lookup of this PricingOptions.  # noqa: E501
        :rtype: bool
        """
        return self._allow_any_instruments_with_sec_uid_to_price_off_lookup

    @allow_any_instruments_with_sec_uid_to_price_off_lookup.setter
    def allow_any_instruments_with_sec_uid_to_price_off_lookup(self, allow_any_instruments_with_sec_uid_to_price_off_lookup):
        """Sets the allow_any_instruments_with_sec_uid_to_price_off_lookup of this PricingOptions.

        By default, one would not expect to price and exotic instrument, i.e. an instrument with a complicated  instrument definition simply through looking up a price as there should be a better way of evaluating it.  To override that behaviour and allow lookup for a price from the instrument identifier(s), set this to true.  # noqa: E501

        :param allow_any_instruments_with_sec_uid_to_price_off_lookup: The allow_any_instruments_with_sec_uid_to_price_off_lookup of this PricingOptions.  # noqa: E501
        :type allow_any_instruments_with_sec_uid_to_price_off_lookup: bool
        """

        self._allow_any_instruments_with_sec_uid_to_price_off_lookup = allow_any_instruments_with_sec_uid_to_price_off_lookup

    @property
    def allow_partially_successful_evaluation(self):
        """Gets the allow_partially_successful_evaluation of this PricingOptions.  # noqa: E501

        If true then a failure in task evaluation doesn't cause overall failure.  results will be returned where they succeeded and annotation elsewhere  # noqa: E501

        :return: The allow_partially_successful_evaluation of this PricingOptions.  # noqa: E501
        :rtype: bool
        """
        return self._allow_partially_successful_evaluation

    @allow_partially_successful_evaluation.setter
    def allow_partially_successful_evaluation(self, allow_partially_successful_evaluation):
        """Sets the allow_partially_successful_evaluation of this PricingOptions.

        If true then a failure in task evaluation doesn't cause overall failure.  results will be returned where they succeeded and annotation elsewhere  # noqa: E501

        :param allow_partially_successful_evaluation: The allow_partially_successful_evaluation of this PricingOptions.  # noqa: E501
        :type allow_partially_successful_evaluation: bool
        """

        self._allow_partially_successful_evaluation = allow_partially_successful_evaluation

    @property
    def produce_separate_result_for_linear_otc_legs(self):
        """Gets the produce_separate_result_for_linear_otc_legs of this PricingOptions.  # noqa: E501

        If true (default), when pricing an Fx-Forward or Interest Rate Swap, Future and other linearly separable products, product two results, one for each leg  rather than a single line result with the amalgamated/summed pv from both legs.  # noqa: E501

        :return: The produce_separate_result_for_linear_otc_legs of this PricingOptions.  # noqa: E501
        :rtype: bool
        """
        return self._produce_separate_result_for_linear_otc_legs

    @produce_separate_result_for_linear_otc_legs.setter
    def produce_separate_result_for_linear_otc_legs(self, produce_separate_result_for_linear_otc_legs):
        """Sets the produce_separate_result_for_linear_otc_legs of this PricingOptions.

        If true (default), when pricing an Fx-Forward or Interest Rate Swap, Future and other linearly separable products, product two results, one for each leg  rather than a single line result with the amalgamated/summed pv from both legs.  # noqa: E501

        :param produce_separate_result_for_linear_otc_legs: The produce_separate_result_for_linear_otc_legs of this PricingOptions.  # noqa: E501
        :type produce_separate_result_for_linear_otc_legs: bool
        """

        self._produce_separate_result_for_linear_otc_legs = produce_separate_result_for_linear_otc_legs

    @property
    def enable_use_of_cached_unit_results(self):
        """Gets the enable_use_of_cached_unit_results of this PricingOptions.  # noqa: E501

        If true, when pricing using a model or for an instrument that supports use of intermediate cached-results, use them.  Default is that this caching is turned off.  # noqa: E501

        :return: The enable_use_of_cached_unit_results of this PricingOptions.  # noqa: E501
        :rtype: bool
        """
        return self._enable_use_of_cached_unit_results

    @enable_use_of_cached_unit_results.setter
    def enable_use_of_cached_unit_results(self, enable_use_of_cached_unit_results):
        """Sets the enable_use_of_cached_unit_results of this PricingOptions.

        If true, when pricing using a model or for an instrument that supports use of intermediate cached-results, use them.  Default is that this caching is turned off.  # noqa: E501

        :param enable_use_of_cached_unit_results: The enable_use_of_cached_unit_results of this PricingOptions.  # noqa: E501
        :type enable_use_of_cached_unit_results: bool
        """

        self._enable_use_of_cached_unit_results = enable_use_of_cached_unit_results

    @property
    def window_valuation_on_instrument_start_end(self):
        """Gets the window_valuation_on_instrument_start_end of this PricingOptions.  # noqa: E501

        If true, when valuing an instrument outside the period where it is 'alive' (the start-maturity window) it will return a valuation of zero  # noqa: E501

        :return: The window_valuation_on_instrument_start_end of this PricingOptions.  # noqa: E501
        :rtype: bool
        """
        return self._window_valuation_on_instrument_start_end

    @window_valuation_on_instrument_start_end.setter
    def window_valuation_on_instrument_start_end(self, window_valuation_on_instrument_start_end):
        """Sets the window_valuation_on_instrument_start_end of this PricingOptions.

        If true, when valuing an instrument outside the period where it is 'alive' (the start-maturity window) it will return a valuation of zero  # noqa: E501

        :param window_valuation_on_instrument_start_end: The window_valuation_on_instrument_start_end of this PricingOptions.  # noqa: E501
        :type window_valuation_on_instrument_start_end: bool
        """

        self._window_valuation_on_instrument_start_end = window_valuation_on_instrument_start_end

    @property
    def remove_contingent_cashflows_in_payment_diary(self):
        """Gets the remove_contingent_cashflows_in_payment_diary of this PricingOptions.  # noqa: E501

        When creating a payment diary, should contingent cash payments (e.g. from exercise of a swaption into a swap) be included or not.  i.e. Is exercise or default being assumed to happen or not.  # noqa: E501

        :return: The remove_contingent_cashflows_in_payment_diary of this PricingOptions.  # noqa: E501
        :rtype: bool
        """
        return self._remove_contingent_cashflows_in_payment_diary

    @remove_contingent_cashflows_in_payment_diary.setter
    def remove_contingent_cashflows_in_payment_diary(self, remove_contingent_cashflows_in_payment_diary):
        """Sets the remove_contingent_cashflows_in_payment_diary of this PricingOptions.

        When creating a payment diary, should contingent cash payments (e.g. from exercise of a swaption into a swap) be included or not.  i.e. Is exercise or default being assumed to happen or not.  # noqa: E501

        :param remove_contingent_cashflows_in_payment_diary: The remove_contingent_cashflows_in_payment_diary of this PricingOptions.  # noqa: E501
        :type remove_contingent_cashflows_in_payment_diary: bool
        """

        self._remove_contingent_cashflows_in_payment_diary = remove_contingent_cashflows_in_payment_diary

    @property
    def use_child_sub_holding_keys_for_portfolio_expansion(self):
        """Gets the use_child_sub_holding_keys_for_portfolio_expansion of this PricingOptions.  # noqa: E501

        Should fund constituents inherit subholding keys from the parent subholding keyb  # noqa: E501

        :return: The use_child_sub_holding_keys_for_portfolio_expansion of this PricingOptions.  # noqa: E501
        :rtype: bool
        """
        return self._use_child_sub_holding_keys_for_portfolio_expansion

    @use_child_sub_holding_keys_for_portfolio_expansion.setter
    def use_child_sub_holding_keys_for_portfolio_expansion(self, use_child_sub_holding_keys_for_portfolio_expansion):
        """Sets the use_child_sub_holding_keys_for_portfolio_expansion of this PricingOptions.

        Should fund constituents inherit subholding keys from the parent subholding keyb  # noqa: E501

        :param use_child_sub_holding_keys_for_portfolio_expansion: The use_child_sub_holding_keys_for_portfolio_expansion of this PricingOptions.  # noqa: E501
        :type use_child_sub_holding_keys_for_portfolio_expansion: bool
        """

        self._use_child_sub_holding_keys_for_portfolio_expansion = use_child_sub_holding_keys_for_portfolio_expansion

    @property
    def validate_domestic_and_quote_currencies_are_consistent(self):
        """Gets the validate_domestic_and_quote_currencies_are_consistent of this PricingOptions.  # noqa: E501

        Do we validate that the instrument domestic currency matches the quote currency (unless unknown/zzz) when using lookup pricing.  # noqa: E501

        :return: The validate_domestic_and_quote_currencies_are_consistent of this PricingOptions.  # noqa: E501
        :rtype: bool
        """
        return self._validate_domestic_and_quote_currencies_are_consistent

    @validate_domestic_and_quote_currencies_are_consistent.setter
    def validate_domestic_and_quote_currencies_are_consistent(self, validate_domestic_and_quote_currencies_are_consistent):
        """Sets the validate_domestic_and_quote_currencies_are_consistent of this PricingOptions.

        Do we validate that the instrument domestic currency matches the quote currency (unless unknown/zzz) when using lookup pricing.  # noqa: E501

        :param validate_domestic_and_quote_currencies_are_consistent: The validate_domestic_and_quote_currencies_are_consistent of this PricingOptions.  # noqa: E501
        :type validate_domestic_and_quote_currencies_are_consistent: bool
        """

        self._validate_domestic_and_quote_currencies_are_consistent = validate_domestic_and_quote_currencies_are_consistent

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
        if not isinstance(other, PricingOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PricingOptions):
            return True

        return self.to_dict() != other.to_dict()
