# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.231
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


class ReconciliationRunId(object):
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
        'reconciliation': 'ReconciliationId',
        'date': 'datetime',
        'version': 'int',
        'as_string': 'str'
    }

    attribute_map = {
        'reconciliation': 'reconciliation',
        'date': 'date',
        'version': 'version',
        'as_string': 'asString'
    }

    required_map = {
        'reconciliation': 'optional',
        'date': 'optional',
        'version': 'optional',
        'as_string': 'optional'
    }

    def __init__(self, reconciliation=None, date=None, version=None, as_string=None, local_vars_configuration=None):  # noqa: E501
        """ReconciliationRunId - a model defined in OpenAPI"
        
        :param reconciliation: 
        :type reconciliation: lusid.ReconciliationId
        :param date: 
        :type date: datetime
        :param version: 
        :type version: int
        :param as_string: 
        :type as_string: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._reconciliation = None
        self._date = None
        self._version = None
        self._as_string = None
        self.discriminator = None

        if reconciliation is not None:
            self.reconciliation = reconciliation
        if date is not None:
            self.date = date
        if version is not None:
            self.version = version
        self.as_string = as_string

    @property
    def reconciliation(self):
        """Gets the reconciliation of this ReconciliationRunId.  # noqa: E501


        :return: The reconciliation of this ReconciliationRunId.  # noqa: E501
        :rtype: lusid.ReconciliationId
        """
        return self._reconciliation

    @reconciliation.setter
    def reconciliation(self, reconciliation):
        """Sets the reconciliation of this ReconciliationRunId.


        :param reconciliation: The reconciliation of this ReconciliationRunId.  # noqa: E501
        :type reconciliation: lusid.ReconciliationId
        """

        self._reconciliation = reconciliation

    @property
    def date(self):
        """Gets the date of this ReconciliationRunId.  # noqa: E501


        :return: The date of this ReconciliationRunId.  # noqa: E501
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this ReconciliationRunId.


        :param date: The date of this ReconciliationRunId.  # noqa: E501
        :type date: datetime
        """

        self._date = date

    @property
    def version(self):
        """Gets the version of this ReconciliationRunId.  # noqa: E501


        :return: The version of this ReconciliationRunId.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ReconciliationRunId.


        :param version: The version of this ReconciliationRunId.  # noqa: E501
        :type version: int
        """

        self._version = version

    @property
    def as_string(self):
        """Gets the as_string of this ReconciliationRunId.  # noqa: E501


        :return: The as_string of this ReconciliationRunId.  # noqa: E501
        :rtype: str
        """
        return self._as_string

    @as_string.setter
    def as_string(self, as_string):
        """Sets the as_string of this ReconciliationRunId.


        :param as_string: The as_string of this ReconciliationRunId.  # noqa: E501
        :type as_string: str
        """

        self._as_string = as_string

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
        if not isinstance(other, ReconciliationRunId):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReconciliationRunId):
            return True

        return self.to_dict() != other.to_dict()
