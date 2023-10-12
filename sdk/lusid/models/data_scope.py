# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.607
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


class DataScope(object):
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
        'client': 'Client',
        'scope': 'str'
    }

    attribute_map = {
        'client': 'client',
        'scope': 'scope'
    }

    required_map = {
        'client': 'optional',
        'scope': 'optional'
    }

    def __init__(self, client=None, scope=None, local_vars_configuration=None):  # noqa: E501
        """DataScope - a model defined in OpenAPI"
        
        :param client: 
        :type client: lusid.Client
        :param scope: 
        :type scope: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._client = None
        self._scope = None
        self.discriminator = None

        if client is not None:
            self.client = client
        self.scope = scope

    @property
    def client(self):
        """Gets the client of this DataScope.  # noqa: E501


        :return: The client of this DataScope.  # noqa: E501
        :rtype: lusid.Client
        """
        return self._client

    @client.setter
    def client(self, client):
        """Sets the client of this DataScope.


        :param client: The client of this DataScope.  # noqa: E501
        :type client: lusid.Client
        """

        self._client = client

    @property
    def scope(self):
        """Gets the scope of this DataScope.  # noqa: E501


        :return: The scope of this DataScope.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this DataScope.


        :param scope: The scope of this DataScope.  # noqa: E501
        :type scope: str
        """

        self._scope = scope

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
        if not isinstance(other, DataScope):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataScope):
            return True

        return self.to_dict() != other.to_dict()
