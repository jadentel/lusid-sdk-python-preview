# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.5136
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


class ChangeHistory(object):
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
        'user_id': 'str',
        'modified_as_at': 'datetime',
        'request_id': 'str',
        'action': 'str',
        'changes': 'list[ChangeItem]',
        'links': 'list[Link]'
    }

    attribute_map = {
        'user_id': 'userId',
        'modified_as_at': 'modifiedAsAt',
        'request_id': 'requestId',
        'action': 'action',
        'changes': 'changes',
        'links': 'links'
    }

    required_map = {
        'user_id': 'required',
        'modified_as_at': 'required',
        'request_id': 'required',
        'action': 'required',
        'changes': 'required',
        'links': 'optional'
    }

    def __init__(self, user_id=None, modified_as_at=None, request_id=None, action=None, changes=None, links=None, local_vars_configuration=None):  # noqa: E501
        """ChangeHistory - a model defined in OpenAPI"
        
        :param user_id:  The unique identifier of the user that made the change. (required)
        :type user_id: str
        :param modified_as_at:  The date/time of the change. (required)
        :type modified_as_at: datetime
        :param request_id:  The unique identifier of the request that the changes were part of. (required)
        :type request_id: str
        :param action:  The action performed on the transaction, either created, updated, or deleted. The available values are: Create, Update, Delete (required)
        :type action: str
        :param changes:  The collection of changes that were made. (required)
        :type changes: list[lusid.ChangeItem]
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._user_id = None
        self._modified_as_at = None
        self._request_id = None
        self._action = None
        self._changes = None
        self._links = None
        self.discriminator = None

        self.user_id = user_id
        self.modified_as_at = modified_as_at
        self.request_id = request_id
        self.action = action
        self.changes = changes
        self.links = links

    @property
    def user_id(self):
        """Gets the user_id of this ChangeHistory.  # noqa: E501

        The unique identifier of the user that made the change.  # noqa: E501

        :return: The user_id of this ChangeHistory.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ChangeHistory.

        The unique identifier of the user that made the change.  # noqa: E501

        :param user_id: The user_id of this ChangeHistory.  # noqa: E501
        :type user_id: str
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def modified_as_at(self):
        """Gets the modified_as_at of this ChangeHistory.  # noqa: E501

        The date/time of the change.  # noqa: E501

        :return: The modified_as_at of this ChangeHistory.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_as_at

    @modified_as_at.setter
    def modified_as_at(self, modified_as_at):
        """Sets the modified_as_at of this ChangeHistory.

        The date/time of the change.  # noqa: E501

        :param modified_as_at: The modified_as_at of this ChangeHistory.  # noqa: E501
        :type modified_as_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and modified_as_at is None:  # noqa: E501
            raise ValueError("Invalid value for `modified_as_at`, must not be `None`")  # noqa: E501

        self._modified_as_at = modified_as_at

    @property
    def request_id(self):
        """Gets the request_id of this ChangeHistory.  # noqa: E501

        The unique identifier of the request that the changes were part of.  # noqa: E501

        :return: The request_id of this ChangeHistory.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ChangeHistory.

        The unique identifier of the request that the changes were part of.  # noqa: E501

        :param request_id: The request_id of this ChangeHistory.  # noqa: E501
        :type request_id: str
        """
        if self.local_vars_configuration.client_side_validation and request_id is None:  # noqa: E501
            raise ValueError("Invalid value for `request_id`, must not be `None`")  # noqa: E501

        self._request_id = request_id

    @property
    def action(self):
        """Gets the action of this ChangeHistory.  # noqa: E501

        The action performed on the transaction, either created, updated, or deleted. The available values are: Create, Update, Delete  # noqa: E501

        :return: The action of this ChangeHistory.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ChangeHistory.

        The action performed on the transaction, either created, updated, or deleted. The available values are: Create, Update, Delete  # noqa: E501

        :param action: The action of this ChangeHistory.  # noqa: E501
        :type action: str
        """
        if self.local_vars_configuration.client_side_validation and action is None:  # noqa: E501
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501
        allowed_values = ["Create", "Update", "Delete"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and action not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def changes(self):
        """Gets the changes of this ChangeHistory.  # noqa: E501

        The collection of changes that were made.  # noqa: E501

        :return: The changes of this ChangeHistory.  # noqa: E501
        :rtype: list[lusid.ChangeItem]
        """
        return self._changes

    @changes.setter
    def changes(self, changes):
        """Sets the changes of this ChangeHistory.

        The collection of changes that were made.  # noqa: E501

        :param changes: The changes of this ChangeHistory.  # noqa: E501
        :type changes: list[lusid.ChangeItem]
        """
        if self.local_vars_configuration.client_side_validation and changes is None:  # noqa: E501
            raise ValueError("Invalid value for `changes`, must not be `None`")  # noqa: E501

        self._changes = changes

    @property
    def links(self):
        """Gets the links of this ChangeHistory.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this ChangeHistory.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ChangeHistory.

        Collection of links.  # noqa: E501

        :param links: The links of this ChangeHistory.  # noqa: E501
        :type links: list[lusid.Link]
        """

        self._links = links

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
        if not isinstance(other, ChangeHistory):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChangeHistory):
            return True

        return self.to_dict() != other.to_dict()
