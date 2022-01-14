# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3891
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


class CounterpartyAgreement(object):
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
        'display_name': 'str',
        'agreement_type': 'str',
        'counterparty_signatory': 'CounterpartySignatory',
        'dated_as_of': 'datetime',
        'credit_support_annex_id': 'ResourceId',
        'id': 'ResourceId'
    }

    attribute_map = {
        'display_name': 'displayName',
        'agreement_type': 'agreementType',
        'counterparty_signatory': 'counterpartySignatory',
        'dated_as_of': 'datedAsOf',
        'credit_support_annex_id': 'creditSupportAnnexId',
        'id': 'id'
    }

    required_map = {
        'display_name': 'required',
        'agreement_type': 'required',
        'counterparty_signatory': 'required',
        'dated_as_of': 'required',
        'credit_support_annex_id': 'required',
        'id': 'required'
    }

    def __init__(self, display_name=None, agreement_type=None, counterparty_signatory=None, dated_as_of=None, credit_support_annex_id=None, id=None, local_vars_configuration=None):  # noqa: E501
        """CounterpartyAgreement - a model defined in OpenAPI"
        
        :param display_name:  A user-defined display label for the Counterparty Agreement. (required)
        :type display_name: str
        :param agreement_type:  A user-defined field to capture the type of agreement this represents. Examples might be \"ISDA 2002 Master Agreement\" or \"ISDA 1992 Master Agreement\". (required)
        :type agreement_type: str
        :param counterparty_signatory:  (required)
        :type counterparty_signatory: lusid.CounterpartySignatory
        :param dated_as_of:  The date on which the CounterpartyAgreement was signed by both parties. (required)
        :type dated_as_of: datetime
        :param credit_support_annex_id:  (required)
        :type credit_support_annex_id: lusid.ResourceId
        :param id:  (required)
        :type id: lusid.ResourceId

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._display_name = None
        self._agreement_type = None
        self._counterparty_signatory = None
        self._dated_as_of = None
        self._credit_support_annex_id = None
        self._id = None
        self.discriminator = None

        self.display_name = display_name
        self.agreement_type = agreement_type
        self.counterparty_signatory = counterparty_signatory
        self.dated_as_of = dated_as_of
        self.credit_support_annex_id = credit_support_annex_id
        self.id = id

    @property
    def display_name(self):
        """Gets the display_name of this CounterpartyAgreement.  # noqa: E501

        A user-defined display label for the Counterparty Agreement.  # noqa: E501

        :return: The display_name of this CounterpartyAgreement.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CounterpartyAgreement.

        A user-defined display label for the Counterparty Agreement.  # noqa: E501

        :param display_name: The display_name of this CounterpartyAgreement.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def agreement_type(self):
        """Gets the agreement_type of this CounterpartyAgreement.  # noqa: E501

        A user-defined field to capture the type of agreement this represents. Examples might be \"ISDA 2002 Master Agreement\" or \"ISDA 1992 Master Agreement\".  # noqa: E501

        :return: The agreement_type of this CounterpartyAgreement.  # noqa: E501
        :rtype: str
        """
        return self._agreement_type

    @agreement_type.setter
    def agreement_type(self, agreement_type):
        """Sets the agreement_type of this CounterpartyAgreement.

        A user-defined field to capture the type of agreement this represents. Examples might be \"ISDA 2002 Master Agreement\" or \"ISDA 1992 Master Agreement\".  # noqa: E501

        :param agreement_type: The agreement_type of this CounterpartyAgreement.  # noqa: E501
        :type agreement_type: str
        """
        if self.local_vars_configuration.client_side_validation and agreement_type is None:  # noqa: E501
            raise ValueError("Invalid value for `agreement_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                agreement_type is not None and len(agreement_type) > 256):
            raise ValueError("Invalid value for `agreement_type`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                agreement_type is not None and len(agreement_type) < 0):
            raise ValueError("Invalid value for `agreement_type`, length must be greater than or equal to `0`")  # noqa: E501

        self._agreement_type = agreement_type

    @property
    def counterparty_signatory(self):
        """Gets the counterparty_signatory of this CounterpartyAgreement.  # noqa: E501


        :return: The counterparty_signatory of this CounterpartyAgreement.  # noqa: E501
        :rtype: lusid.CounterpartySignatory
        """
        return self._counterparty_signatory

    @counterparty_signatory.setter
    def counterparty_signatory(self, counterparty_signatory):
        """Sets the counterparty_signatory of this CounterpartyAgreement.


        :param counterparty_signatory: The counterparty_signatory of this CounterpartyAgreement.  # noqa: E501
        :type counterparty_signatory: lusid.CounterpartySignatory
        """
        if self.local_vars_configuration.client_side_validation and counterparty_signatory is None:  # noqa: E501
            raise ValueError("Invalid value for `counterparty_signatory`, must not be `None`")  # noqa: E501

        self._counterparty_signatory = counterparty_signatory

    @property
    def dated_as_of(self):
        """Gets the dated_as_of of this CounterpartyAgreement.  # noqa: E501

        The date on which the CounterpartyAgreement was signed by both parties.  # noqa: E501

        :return: The dated_as_of of this CounterpartyAgreement.  # noqa: E501
        :rtype: datetime
        """
        return self._dated_as_of

    @dated_as_of.setter
    def dated_as_of(self, dated_as_of):
        """Sets the dated_as_of of this CounterpartyAgreement.

        The date on which the CounterpartyAgreement was signed by both parties.  # noqa: E501

        :param dated_as_of: The dated_as_of of this CounterpartyAgreement.  # noqa: E501
        :type dated_as_of: datetime
        """
        if self.local_vars_configuration.client_side_validation and dated_as_of is None:  # noqa: E501
            raise ValueError("Invalid value for `dated_as_of`, must not be `None`")  # noqa: E501

        self._dated_as_of = dated_as_of

    @property
    def credit_support_annex_id(self):
        """Gets the credit_support_annex_id of this CounterpartyAgreement.  # noqa: E501


        :return: The credit_support_annex_id of this CounterpartyAgreement.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._credit_support_annex_id

    @credit_support_annex_id.setter
    def credit_support_annex_id(self, credit_support_annex_id):
        """Sets the credit_support_annex_id of this CounterpartyAgreement.


        :param credit_support_annex_id: The credit_support_annex_id of this CounterpartyAgreement.  # noqa: E501
        :type credit_support_annex_id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and credit_support_annex_id is None:  # noqa: E501
            raise ValueError("Invalid value for `credit_support_annex_id`, must not be `None`")  # noqa: E501

        self._credit_support_annex_id = credit_support_annex_id

    @property
    def id(self):
        """Gets the id of this CounterpartyAgreement.  # noqa: E501


        :return: The id of this CounterpartyAgreement.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CounterpartyAgreement.


        :param id: The id of this CounterpartyAgreement.  # noqa: E501
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
        if not isinstance(other, CounterpartyAgreement):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CounterpartyAgreement):
            return True

        return self.to_dict() != other.to_dict()
