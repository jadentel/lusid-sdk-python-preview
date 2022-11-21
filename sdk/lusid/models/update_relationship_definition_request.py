# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4992
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


class UpdateRelationshipDefinitionRequest(object):
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
        'outward_description': 'str',
        'inward_description': 'str'
    }

    attribute_map = {
        'display_name': 'displayName',
        'outward_description': 'outwardDescription',
        'inward_description': 'inwardDescription'
    }

    required_map = {
        'display_name': 'required',
        'outward_description': 'required',
        'inward_description': 'required'
    }

    def __init__(self, display_name=None, outward_description=None, inward_description=None, local_vars_configuration=None):  # noqa: E501
        """UpdateRelationshipDefinitionRequest - a model defined in OpenAPI"
        
        :param display_name:  The display name of the relation. (required)
        :type display_name: str
        :param outward_description:  The description to relate source entity object and target entity object. (required)
        :type outward_description: str
        :param inward_description:  The description to relate target entity object and source entity object. (required)
        :type inward_description: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._display_name = None
        self._outward_description = None
        self._inward_description = None
        self.discriminator = None

        self.display_name = display_name
        self.outward_description = outward_description
        self.inward_description = inward_description

    @property
    def display_name(self):
        """Gets the display_name of this UpdateRelationshipDefinitionRequest.  # noqa: E501

        The display name of the relation.  # noqa: E501

        :return: The display_name of this UpdateRelationshipDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this UpdateRelationshipDefinitionRequest.

        The display name of the relation.  # noqa: E501

        :param display_name: The display_name of this UpdateRelationshipDefinitionRequest.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) > 512):
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `512`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) < 1):
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and not re.search(r'^[\s\S]*$', display_name)):  # noqa: E501
            raise ValueError(r"Invalid value for `display_name`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._display_name = display_name

    @property
    def outward_description(self):
        """Gets the outward_description of this UpdateRelationshipDefinitionRequest.  # noqa: E501

        The description to relate source entity object and target entity object.  # noqa: E501

        :return: The outward_description of this UpdateRelationshipDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._outward_description

    @outward_description.setter
    def outward_description(self, outward_description):
        """Sets the outward_description of this UpdateRelationshipDefinitionRequest.

        The description to relate source entity object and target entity object.  # noqa: E501

        :param outward_description: The outward_description of this UpdateRelationshipDefinitionRequest.  # noqa: E501
        :type outward_description: str
        """
        if self.local_vars_configuration.client_side_validation and outward_description is None:  # noqa: E501
            raise ValueError("Invalid value for `outward_description`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                outward_description is not None and len(outward_description) > 512):
            raise ValueError("Invalid value for `outward_description`, length must be less than or equal to `512`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                outward_description is not None and len(outward_description) < 1):
            raise ValueError("Invalid value for `outward_description`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                outward_description is not None and not re.search(r'^[\s\S]*$', outward_description)):  # noqa: E501
            raise ValueError(r"Invalid value for `outward_description`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._outward_description = outward_description

    @property
    def inward_description(self):
        """Gets the inward_description of this UpdateRelationshipDefinitionRequest.  # noqa: E501

        The description to relate target entity object and source entity object.  # noqa: E501

        :return: The inward_description of this UpdateRelationshipDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._inward_description

    @inward_description.setter
    def inward_description(self, inward_description):
        """Sets the inward_description of this UpdateRelationshipDefinitionRequest.

        The description to relate target entity object and source entity object.  # noqa: E501

        :param inward_description: The inward_description of this UpdateRelationshipDefinitionRequest.  # noqa: E501
        :type inward_description: str
        """
        if self.local_vars_configuration.client_side_validation and inward_description is None:  # noqa: E501
            raise ValueError("Invalid value for `inward_description`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                inward_description is not None and len(inward_description) > 512):
            raise ValueError("Invalid value for `inward_description`, length must be less than or equal to `512`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                inward_description is not None and len(inward_description) < 1):
            raise ValueError("Invalid value for `inward_description`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                inward_description is not None and not re.search(r'^[\s\S]*$', inward_description)):  # noqa: E501
            raise ValueError(r"Invalid value for `inward_description`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._inward_description = inward_description

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
        if not isinstance(other, UpdateRelationshipDefinitionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateRelationshipDefinitionRequest):
            return True

        return self.to_dict() != other.to_dict()
