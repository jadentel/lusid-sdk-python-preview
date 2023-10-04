# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.568
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


class PortfolioGroup(object):
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
        'href': 'str',
        'id': 'ResourceId',
        'display_name': 'str',
        'description': 'str',
        'created': 'datetime',
        'portfolios': 'list[ResourceId]',
        'sub_groups': 'list[ResourceId]',
        'relationships': 'list[Relationship]',
        'version': 'Version',
        'links': 'list[Link]'
    }

    attribute_map = {
        'href': 'href',
        'id': 'id',
        'display_name': 'displayName',
        'description': 'description',
        'created': 'created',
        'portfolios': 'portfolios',
        'sub_groups': 'subGroups',
        'relationships': 'relationships',
        'version': 'version',
        'links': 'links'
    }

    required_map = {
        'href': 'optional',
        'id': 'required',
        'display_name': 'required',
        'description': 'optional',
        'created': 'optional',
        'portfolios': 'optional',
        'sub_groups': 'optional',
        'relationships': 'optional',
        'version': 'optional',
        'links': 'optional'
    }

    def __init__(self, href=None, id=None, display_name=None, description=None, created=None, portfolios=None, sub_groups=None, relationships=None, version=None, links=None, local_vars_configuration=None):  # noqa: E501
        """PortfolioGroup - a model defined in OpenAPI"
        
        :param href:  The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
        :type href: str
        :param id:  (required)
        :type id: lusid.ResourceId
        :param display_name:  The name of the portfolio group. (required)
        :type display_name: str
        :param description:  The long form description of the portfolio group.
        :type description: str
        :param created:  The effective datetime at which the portfolio group was created. No portfolios or sub groups can be added to the group before this date.
        :type created: datetime
        :param portfolios:  The collection of resource identifiers for the portfolios contained in the portfolio group.
        :type portfolios: list[lusid.ResourceId]
        :param sub_groups:  The collection of resource identifiers for the portfolio groups contained in the portfolio group as sub groups.
        :type sub_groups: list[lusid.ResourceId]
        :param relationships:  A set of relationships associated to the portfolio group.
        :type relationships: list[lusid.Relationship]
        :param version: 
        :type version: lusid.Version
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._href = None
        self._id = None
        self._display_name = None
        self._description = None
        self._created = None
        self._portfolios = None
        self._sub_groups = None
        self._relationships = None
        self._version = None
        self._links = None
        self.discriminator = None

        self.href = href
        self.id = id
        self.display_name = display_name
        self.description = description
        if created is not None:
            self.created = created
        self.portfolios = portfolios
        self.sub_groups = sub_groups
        self.relationships = relationships
        if version is not None:
            self.version = version
        self.links = links

    @property
    def href(self):
        """Gets the href of this PortfolioGroup.  # noqa: E501

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :return: The href of this PortfolioGroup.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this PortfolioGroup.

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :param href: The href of this PortfolioGroup.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def id(self):
        """Gets the id of this PortfolioGroup.  # noqa: E501


        :return: The id of this PortfolioGroup.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PortfolioGroup.


        :param id: The id of this PortfolioGroup.  # noqa: E501
        :type id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def display_name(self):
        """Gets the display_name of this PortfolioGroup.  # noqa: E501

        The name of the portfolio group.  # noqa: E501

        :return: The display_name of this PortfolioGroup.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PortfolioGroup.

        The name of the portfolio group.  # noqa: E501

        :param display_name: The display_name of this PortfolioGroup.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) < 1):
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this PortfolioGroup.  # noqa: E501

        The long form description of the portfolio group.  # noqa: E501

        :return: The description of this PortfolioGroup.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PortfolioGroup.

        The long form description of the portfolio group.  # noqa: E501

        :param description: The description of this PortfolioGroup.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def created(self):
        """Gets the created of this PortfolioGroup.  # noqa: E501

        The effective datetime at which the portfolio group was created. No portfolios or sub groups can be added to the group before this date.  # noqa: E501

        :return: The created of this PortfolioGroup.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this PortfolioGroup.

        The effective datetime at which the portfolio group was created. No portfolios or sub groups can be added to the group before this date.  # noqa: E501

        :param created: The created of this PortfolioGroup.  # noqa: E501
        :type created: datetime
        """

        self._created = created

    @property
    def portfolios(self):
        """Gets the portfolios of this PortfolioGroup.  # noqa: E501

        The collection of resource identifiers for the portfolios contained in the portfolio group.  # noqa: E501

        :return: The portfolios of this PortfolioGroup.  # noqa: E501
        :rtype: list[lusid.ResourceId]
        """
        return self._portfolios

    @portfolios.setter
    def portfolios(self, portfolios):
        """Sets the portfolios of this PortfolioGroup.

        The collection of resource identifiers for the portfolios contained in the portfolio group.  # noqa: E501

        :param portfolios: The portfolios of this PortfolioGroup.  # noqa: E501
        :type portfolios: list[lusid.ResourceId]
        """

        self._portfolios = portfolios

    @property
    def sub_groups(self):
        """Gets the sub_groups of this PortfolioGroup.  # noqa: E501

        The collection of resource identifiers for the portfolio groups contained in the portfolio group as sub groups.  # noqa: E501

        :return: The sub_groups of this PortfolioGroup.  # noqa: E501
        :rtype: list[lusid.ResourceId]
        """
        return self._sub_groups

    @sub_groups.setter
    def sub_groups(self, sub_groups):
        """Sets the sub_groups of this PortfolioGroup.

        The collection of resource identifiers for the portfolio groups contained in the portfolio group as sub groups.  # noqa: E501

        :param sub_groups: The sub_groups of this PortfolioGroup.  # noqa: E501
        :type sub_groups: list[lusid.ResourceId]
        """

        self._sub_groups = sub_groups

    @property
    def relationships(self):
        """Gets the relationships of this PortfolioGroup.  # noqa: E501

        A set of relationships associated to the portfolio group.  # noqa: E501

        :return: The relationships of this PortfolioGroup.  # noqa: E501
        :rtype: list[lusid.Relationship]
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """Sets the relationships of this PortfolioGroup.

        A set of relationships associated to the portfolio group.  # noqa: E501

        :param relationships: The relationships of this PortfolioGroup.  # noqa: E501
        :type relationships: list[lusid.Relationship]
        """

        self._relationships = relationships

    @property
    def version(self):
        """Gets the version of this PortfolioGroup.  # noqa: E501


        :return: The version of this PortfolioGroup.  # noqa: E501
        :rtype: lusid.Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PortfolioGroup.


        :param version: The version of this PortfolioGroup.  # noqa: E501
        :type version: lusid.Version
        """

        self._version = version

    @property
    def links(self):
        """Gets the links of this PortfolioGroup.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this PortfolioGroup.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PortfolioGroup.

        Collection of links.  # noqa: E501

        :param links: The links of this PortfolioGroup.  # noqa: E501
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
        if not isinstance(other, PortfolioGroup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PortfolioGroup):
            return True

        return self.to_dict() != other.to_dict()
