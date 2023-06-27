# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.289
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


class UpsertIndexConventionRequest(object):
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
        'index_convention': 'IndexConvention'
    }

    attribute_map = {
        'index_convention': 'indexConvention'
    }

    required_map = {
        'index_convention': 'optional'
    }

    def __init__(self, index_convention=None, local_vars_configuration=None):  # noqa: E501
        """UpsertIndexConventionRequest - a model defined in OpenAPI"
        
        :param index_convention: 
        :type index_convention: lusid.IndexConvention

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._index_convention = None
        self.discriminator = None

        if index_convention is not None:
            self.index_convention = index_convention

    @property
    def index_convention(self):
        """Gets the index_convention of this UpsertIndexConventionRequest.  # noqa: E501


        :return: The index_convention of this UpsertIndexConventionRequest.  # noqa: E501
        :rtype: lusid.IndexConvention
        """
        return self._index_convention

    @index_convention.setter
    def index_convention(self, index_convention):
        """Sets the index_convention of this UpsertIndexConventionRequest.


        :param index_convention: The index_convention of this UpsertIndexConventionRequest.  # noqa: E501
        :type index_convention: lusid.IndexConvention
        """

        self._index_convention = index_convention

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
        if not isinstance(other, UpsertIndexConventionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpsertIndexConventionRequest):
            return True

        return self.to_dict() != other.to_dict()
