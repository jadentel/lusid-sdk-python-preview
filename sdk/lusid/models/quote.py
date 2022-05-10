# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4323
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


class Quote(object):
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
        'quote_id': 'QuoteId',
        'metric_value': 'MetricValue',
        'lineage': 'str',
        'cut_label': 'str',
        'uploaded_by': 'str',
        'as_at': 'datetime',
        'scale_factor': 'float'
    }

    attribute_map = {
        'quote_id': 'quoteId',
        'metric_value': 'metricValue',
        'lineage': 'lineage',
        'cut_label': 'cutLabel',
        'uploaded_by': 'uploadedBy',
        'as_at': 'asAt',
        'scale_factor': 'scaleFactor'
    }

    required_map = {
        'quote_id': 'required',
        'metric_value': 'optional',
        'lineage': 'optional',
        'cut_label': 'optional',
        'uploaded_by': 'required',
        'as_at': 'required',
        'scale_factor': 'optional'
    }

    def __init__(self, quote_id=None, metric_value=None, lineage=None, cut_label=None, uploaded_by=None, as_at=None, scale_factor=None, local_vars_configuration=None):  # noqa: E501
        """Quote - a model defined in OpenAPI"
        
        :param quote_id:  (required)
        :type quote_id: lusid.QuoteId
        :param metric_value: 
        :type metric_value: lusid.MetricValue
        :param lineage:  Description of the quote's lineage e.g. 'FundAccountant_GreenQuality'.
        :type lineage: str
        :param cut_label:  The cut label that this quote was updated or inserted with.
        :type cut_label: str
        :param uploaded_by:  The unique id of the user that updated or inserted the quote. (required)
        :type uploaded_by: str
        :param as_at:  The asAt datetime at which the quote was committed to LUSID. (required)
        :type as_at: datetime
        :param scale_factor:  An optional scale factor for non-standard scaling of quotes against the instrument. For example, if you wish the quote's Value to be scaled down by a factor of 100, enter 100. If not supplied, the default ScaleFactor is 1.
        :type scale_factor: float

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._quote_id = None
        self._metric_value = None
        self._lineage = None
        self._cut_label = None
        self._uploaded_by = None
        self._as_at = None
        self._scale_factor = None
        self.discriminator = None

        self.quote_id = quote_id
        if metric_value is not None:
            self.metric_value = metric_value
        self.lineage = lineage
        self.cut_label = cut_label
        self.uploaded_by = uploaded_by
        self.as_at = as_at
        self.scale_factor = scale_factor

    @property
    def quote_id(self):
        """Gets the quote_id of this Quote.  # noqa: E501


        :return: The quote_id of this Quote.  # noqa: E501
        :rtype: lusid.QuoteId
        """
        return self._quote_id

    @quote_id.setter
    def quote_id(self, quote_id):
        """Sets the quote_id of this Quote.


        :param quote_id: The quote_id of this Quote.  # noqa: E501
        :type quote_id: lusid.QuoteId
        """
        if self.local_vars_configuration.client_side_validation and quote_id is None:  # noqa: E501
            raise ValueError("Invalid value for `quote_id`, must not be `None`")  # noqa: E501

        self._quote_id = quote_id

    @property
    def metric_value(self):
        """Gets the metric_value of this Quote.  # noqa: E501


        :return: The metric_value of this Quote.  # noqa: E501
        :rtype: lusid.MetricValue
        """
        return self._metric_value

    @metric_value.setter
    def metric_value(self, metric_value):
        """Sets the metric_value of this Quote.


        :param metric_value: The metric_value of this Quote.  # noqa: E501
        :type metric_value: lusid.MetricValue
        """

        self._metric_value = metric_value

    @property
    def lineage(self):
        """Gets the lineage of this Quote.  # noqa: E501

        Description of the quote's lineage e.g. 'FundAccountant_GreenQuality'.  # noqa: E501

        :return: The lineage of this Quote.  # noqa: E501
        :rtype: str
        """
        return self._lineage

    @lineage.setter
    def lineage(self, lineage):
        """Sets the lineage of this Quote.

        Description of the quote's lineage e.g. 'FundAccountant_GreenQuality'.  # noqa: E501

        :param lineage: The lineage of this Quote.  # noqa: E501
        :type lineage: str
        """

        self._lineage = lineage

    @property
    def cut_label(self):
        """Gets the cut_label of this Quote.  # noqa: E501

        The cut label that this quote was updated or inserted with.  # noqa: E501

        :return: The cut_label of this Quote.  # noqa: E501
        :rtype: str
        """
        return self._cut_label

    @cut_label.setter
    def cut_label(self, cut_label):
        """Sets the cut_label of this Quote.

        The cut label that this quote was updated or inserted with.  # noqa: E501

        :param cut_label: The cut_label of this Quote.  # noqa: E501
        :type cut_label: str
        """

        self._cut_label = cut_label

    @property
    def uploaded_by(self):
        """Gets the uploaded_by of this Quote.  # noqa: E501

        The unique id of the user that updated or inserted the quote.  # noqa: E501

        :return: The uploaded_by of this Quote.  # noqa: E501
        :rtype: str
        """
        return self._uploaded_by

    @uploaded_by.setter
    def uploaded_by(self, uploaded_by):
        """Sets the uploaded_by of this Quote.

        The unique id of the user that updated or inserted the quote.  # noqa: E501

        :param uploaded_by: The uploaded_by of this Quote.  # noqa: E501
        :type uploaded_by: str
        """
        if self.local_vars_configuration.client_side_validation and uploaded_by is None:  # noqa: E501
            raise ValueError("Invalid value for `uploaded_by`, must not be `None`")  # noqa: E501

        self._uploaded_by = uploaded_by

    @property
    def as_at(self):
        """Gets the as_at of this Quote.  # noqa: E501

        The asAt datetime at which the quote was committed to LUSID.  # noqa: E501

        :return: The as_at of this Quote.  # noqa: E501
        :rtype: datetime
        """
        return self._as_at

    @as_at.setter
    def as_at(self, as_at):
        """Sets the as_at of this Quote.

        The asAt datetime at which the quote was committed to LUSID.  # noqa: E501

        :param as_at: The as_at of this Quote.  # noqa: E501
        :type as_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and as_at is None:  # noqa: E501
            raise ValueError("Invalid value for `as_at`, must not be `None`")  # noqa: E501

        self._as_at = as_at

    @property
    def scale_factor(self):
        """Gets the scale_factor of this Quote.  # noqa: E501

        An optional scale factor for non-standard scaling of quotes against the instrument. For example, if you wish the quote's Value to be scaled down by a factor of 100, enter 100. If not supplied, the default ScaleFactor is 1.  # noqa: E501

        :return: The scale_factor of this Quote.  # noqa: E501
        :rtype: float
        """
        return self._scale_factor

    @scale_factor.setter
    def scale_factor(self, scale_factor):
        """Sets the scale_factor of this Quote.

        An optional scale factor for non-standard scaling of quotes against the instrument. For example, if you wish the quote's Value to be scaled down by a factor of 100, enter 100. If not supplied, the default ScaleFactor is 1.  # noqa: E501

        :param scale_factor: The scale_factor of this Quote.  # noqa: E501
        :type scale_factor: float
        """

        self._scale_factor = scale_factor

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
        if not isinstance(other, Quote):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Quote):
            return True

        return self.to_dict() != other.to_dict()
