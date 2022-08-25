# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4727
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


class ComplianceRunInfo(object):
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
        'run_id': 'str',
        'instigated_at': 'datetime',
        'completed_at': 'datetime',
        'schedule': 'str',
        'all_rules_passed': 'bool',
        'has_results': 'bool',
        'as_at': 'datetime'
    }

    attribute_map = {
        'run_id': 'runId',
        'instigated_at': 'instigatedAt',
        'completed_at': 'completedAt',
        'schedule': 'schedule',
        'all_rules_passed': 'allRulesPassed',
        'has_results': 'hasResults',
        'as_at': 'asAt'
    }

    required_map = {
        'run_id': 'required',
        'instigated_at': 'required',
        'completed_at': 'required',
        'schedule': 'required',
        'all_rules_passed': 'required',
        'has_results': 'required',
        'as_at': 'required'
    }

    def __init__(self, run_id=None, instigated_at=None, completed_at=None, schedule=None, all_rules_passed=None, has_results=None, as_at=None, local_vars_configuration=None):  # noqa: E501
        """ComplianceRunInfo - a model defined in OpenAPI"
        
        :param run_id:  The unique identifier of a compliance run (required)
        :type run_id: str
        :param instigated_at:  The time the compliance run was launched (e.g. button pressed). Currently it is also both the as at and effective at time in whichthe rule set and portfolio data (including any pending trades if the run is pretrade) is taken for the caluation, although it may be possible to run compliance for historical effective at and as at dates in the future. (required)
        :type instigated_at: datetime
        :param completed_at:  The time the compliance run calculation was completed (required)
        :type completed_at: datetime
        :param schedule:  Whether the compliance run was pre or post trade (required)
        :type schedule: str
        :param all_rules_passed:  True if all rules passed, for all the portfolios they were assigned to (required)
        :type all_rules_passed: bool
        :param has_results:  False when no results have been returned eg. when no rules exist (required)
        :type has_results: bool
        :param as_at:  Legacy AsAt time for backwards compatibility (required)
        :type as_at: datetime

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._run_id = None
        self._instigated_at = None
        self._completed_at = None
        self._schedule = None
        self._all_rules_passed = None
        self._has_results = None
        self._as_at = None
        self.discriminator = None

        self.run_id = run_id
        self.instigated_at = instigated_at
        self.completed_at = completed_at
        self.schedule = schedule
        self.all_rules_passed = all_rules_passed
        self.has_results = has_results
        self.as_at = as_at

    @property
    def run_id(self):
        """Gets the run_id of this ComplianceRunInfo.  # noqa: E501

        The unique identifier of a compliance run  # noqa: E501

        :return: The run_id of this ComplianceRunInfo.  # noqa: E501
        :rtype: str
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """Sets the run_id of this ComplianceRunInfo.

        The unique identifier of a compliance run  # noqa: E501

        :param run_id: The run_id of this ComplianceRunInfo.  # noqa: E501
        :type run_id: str
        """
        if self.local_vars_configuration.client_side_validation and run_id is None:  # noqa: E501
            raise ValueError("Invalid value for `run_id`, must not be `None`")  # noqa: E501

        self._run_id = run_id

    @property
    def instigated_at(self):
        """Gets the instigated_at of this ComplianceRunInfo.  # noqa: E501

        The time the compliance run was launched (e.g. button pressed). Currently it is also both the as at and effective at time in whichthe rule set and portfolio data (including any pending trades if the run is pretrade) is taken for the caluation, although it may be possible to run compliance for historical effective at and as at dates in the future.  # noqa: E501

        :return: The instigated_at of this ComplianceRunInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._instigated_at

    @instigated_at.setter
    def instigated_at(self, instigated_at):
        """Sets the instigated_at of this ComplianceRunInfo.

        The time the compliance run was launched (e.g. button pressed). Currently it is also both the as at and effective at time in whichthe rule set and portfolio data (including any pending trades if the run is pretrade) is taken for the caluation, although it may be possible to run compliance for historical effective at and as at dates in the future.  # noqa: E501

        :param instigated_at: The instigated_at of this ComplianceRunInfo.  # noqa: E501
        :type instigated_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and instigated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `instigated_at`, must not be `None`")  # noqa: E501

        self._instigated_at = instigated_at

    @property
    def completed_at(self):
        """Gets the completed_at of this ComplianceRunInfo.  # noqa: E501

        The time the compliance run calculation was completed  # noqa: E501

        :return: The completed_at of this ComplianceRunInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._completed_at

    @completed_at.setter
    def completed_at(self, completed_at):
        """Sets the completed_at of this ComplianceRunInfo.

        The time the compliance run calculation was completed  # noqa: E501

        :param completed_at: The completed_at of this ComplianceRunInfo.  # noqa: E501
        :type completed_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and completed_at is None:  # noqa: E501
            raise ValueError("Invalid value for `completed_at`, must not be `None`")  # noqa: E501

        self._completed_at = completed_at

    @property
    def schedule(self):
        """Gets the schedule of this ComplianceRunInfo.  # noqa: E501

        Whether the compliance run was pre or post trade  # noqa: E501

        :return: The schedule of this ComplianceRunInfo.  # noqa: E501
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this ComplianceRunInfo.

        Whether the compliance run was pre or post trade  # noqa: E501

        :param schedule: The schedule of this ComplianceRunInfo.  # noqa: E501
        :type schedule: str
        """
        if self.local_vars_configuration.client_side_validation and schedule is None:  # noqa: E501
            raise ValueError("Invalid value for `schedule`, must not be `None`")  # noqa: E501

        self._schedule = schedule

    @property
    def all_rules_passed(self):
        """Gets the all_rules_passed of this ComplianceRunInfo.  # noqa: E501

        True if all rules passed, for all the portfolios they were assigned to  # noqa: E501

        :return: The all_rules_passed of this ComplianceRunInfo.  # noqa: E501
        :rtype: bool
        """
        return self._all_rules_passed

    @all_rules_passed.setter
    def all_rules_passed(self, all_rules_passed):
        """Sets the all_rules_passed of this ComplianceRunInfo.

        True if all rules passed, for all the portfolios they were assigned to  # noqa: E501

        :param all_rules_passed: The all_rules_passed of this ComplianceRunInfo.  # noqa: E501
        :type all_rules_passed: bool
        """
        if self.local_vars_configuration.client_side_validation and all_rules_passed is None:  # noqa: E501
            raise ValueError("Invalid value for `all_rules_passed`, must not be `None`")  # noqa: E501

        self._all_rules_passed = all_rules_passed

    @property
    def has_results(self):
        """Gets the has_results of this ComplianceRunInfo.  # noqa: E501

        False when no results have been returned eg. when no rules exist  # noqa: E501

        :return: The has_results of this ComplianceRunInfo.  # noqa: E501
        :rtype: bool
        """
        return self._has_results

    @has_results.setter
    def has_results(self, has_results):
        """Sets the has_results of this ComplianceRunInfo.

        False when no results have been returned eg. when no rules exist  # noqa: E501

        :param has_results: The has_results of this ComplianceRunInfo.  # noqa: E501
        :type has_results: bool
        """
        if self.local_vars_configuration.client_side_validation and has_results is None:  # noqa: E501
            raise ValueError("Invalid value for `has_results`, must not be `None`")  # noqa: E501

        self._has_results = has_results

    @property
    def as_at(self):
        """Gets the as_at of this ComplianceRunInfo.  # noqa: E501

        Legacy AsAt time for backwards compatibility  # noqa: E501

        :return: The as_at of this ComplianceRunInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._as_at

    @as_at.setter
    def as_at(self, as_at):
        """Sets the as_at of this ComplianceRunInfo.

        Legacy AsAt time for backwards compatibility  # noqa: E501

        :param as_at: The as_at of this ComplianceRunInfo.  # noqa: E501
        :type as_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and as_at is None:  # noqa: E501
            raise ValueError("Invalid value for `as_at`, must not be `None`")  # noqa: E501

        self._as_at = as_at

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
        if not isinstance(other, ComplianceRunInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComplianceRunInfo):
            return True

        return self.to_dict() != other.to_dict()
