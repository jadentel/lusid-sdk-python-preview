# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3200
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class ResourceListOfA2BDataRecord(object):
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
        'values': 'list[A2BDataRecord]',
        'href': 'str',
        'links': 'list[Link]',
        'next_page': 'str',
        'previous_page': 'str'
    }

    attribute_map = {
        'values': 'values',
        'href': 'href',
        'links': 'links',
        'next_page': 'nextPage',
        'previous_page': 'previousPage'
    }

    required_map = {
        'values': 'required',
        'href': 'optional',
        'links': 'optional',
        'next_page': 'optional',
        'previous_page': 'optional'
    }

    def __init__(self, values=None, href=None, links=None, next_page=None, previous_page=None):  # noqa: E501
        """
        ResourceListOfA2BDataRecord - a model defined in OpenAPI

        :param values:  (required)
        :type values: list[lusid.A2BDataRecord]
        :param href: 
        :type href: str
        :param links: 
        :type links: list[lusid.Link]
        :param next_page: 
        :type next_page: str
        :param previous_page: 
        :type previous_page: str

        """  # noqa: E501

        self._values = None
        self._href = None
        self._links = None
        self._next_page = None
        self._previous_page = None
        self.discriminator = None

        self.values = values
        self.href = href
        self.links = links
        self.next_page = next_page
        self.previous_page = previous_page

    @property
    def values(self):
        """Gets the values of this ResourceListOfA2BDataRecord.  # noqa: E501


        :return: The values of this ResourceListOfA2BDataRecord.  # noqa: E501
        :rtype: list[A2BDataRecord]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this ResourceListOfA2BDataRecord.


        :param values: The values of this ResourceListOfA2BDataRecord.  # noqa: E501
        :type: list[A2BDataRecord]
        """
        if values is None:
            raise ValueError("Invalid value for `values`, must not be `None`")  # noqa: E501

        self._values = values

    @property
    def href(self):
        """Gets the href of this ResourceListOfA2BDataRecord.  # noqa: E501


        :return: The href of this ResourceListOfA2BDataRecord.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this ResourceListOfA2BDataRecord.


        :param href: The href of this ResourceListOfA2BDataRecord.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def links(self):
        """Gets the links of this ResourceListOfA2BDataRecord.  # noqa: E501


        :return: The links of this ResourceListOfA2BDataRecord.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ResourceListOfA2BDataRecord.


        :param links: The links of this ResourceListOfA2BDataRecord.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def next_page(self):
        """Gets the next_page of this ResourceListOfA2BDataRecord.  # noqa: E501


        :return: The next_page of this ResourceListOfA2BDataRecord.  # noqa: E501
        :rtype: str
        """
        return self._next_page

    @next_page.setter
    def next_page(self, next_page):
        """Sets the next_page of this ResourceListOfA2BDataRecord.


        :param next_page: The next_page of this ResourceListOfA2BDataRecord.  # noqa: E501
        :type: str
        """

        self._next_page = next_page

    @property
    def previous_page(self):
        """Gets the previous_page of this ResourceListOfA2BDataRecord.  # noqa: E501


        :return: The previous_page of this ResourceListOfA2BDataRecord.  # noqa: E501
        :rtype: str
        """
        return self._previous_page

    @previous_page.setter
    def previous_page(self, previous_page):
        """Sets the previous_page of this ResourceListOfA2BDataRecord.


        :param previous_page: The previous_page of this ResourceListOfA2BDataRecord.  # noqa: E501
        :type: str
        """

        self._previous_page = previous_page

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResourceListOfA2BDataRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
