# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4827
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


class InstrumentPaymentDiary(object):
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
        'instrument_id_type': 'str',
        'instrument_id': 'str',
        'instrument_scope': 'str',
        'version': 'Version',
        'legs': 'list[InstrumentPaymentDiaryLeg]',
        'href': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'instrument_id_type': 'instrumentIdType',
        'instrument_id': 'instrumentId',
        'instrument_scope': 'instrumentScope',
        'version': 'version',
        'legs': 'legs',
        'href': 'href',
        'links': 'links'
    }

    required_map = {
        'instrument_id_type': 'optional',
        'instrument_id': 'optional',
        'instrument_scope': 'optional',
        'version': 'optional',
        'legs': 'optional',
        'href': 'optional',
        'links': 'optional'
    }

    def __init__(self, instrument_id_type=None, instrument_id=None, instrument_scope=None, version=None, legs=None, href=None, links=None, local_vars_configuration=None):  # noqa: E501
        """InstrumentPaymentDiary - a model defined in OpenAPI"
        
        :param instrument_id_type:  The identifier type of the instrument.
        :type instrument_id_type: str
        :param instrument_id:  The identifier for the instrument.
        :type instrument_id: str
        :param instrument_scope:  The scope of the instrument.
        :type instrument_scope: str
        :param version: 
        :type version: lusid.Version
        :param legs:  Aggregated sets of Cashflows.
        :type legs: list[lusid.InstrumentPaymentDiaryLeg]
        :param href:  The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
        :type href: str
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._instrument_id_type = None
        self._instrument_id = None
        self._instrument_scope = None
        self._version = None
        self._legs = None
        self._href = None
        self._links = None
        self.discriminator = None

        self.instrument_id_type = instrument_id_type
        self.instrument_id = instrument_id
        self.instrument_scope = instrument_scope
        if version is not None:
            self.version = version
        self.legs = legs
        self.href = href
        self.links = links

    @property
    def instrument_id_type(self):
        """Gets the instrument_id_type of this InstrumentPaymentDiary.  # noqa: E501

        The identifier type of the instrument.  # noqa: E501

        :return: The instrument_id_type of this InstrumentPaymentDiary.  # noqa: E501
        :rtype: str
        """
        return self._instrument_id_type

    @instrument_id_type.setter
    def instrument_id_type(self, instrument_id_type):
        """Sets the instrument_id_type of this InstrumentPaymentDiary.

        The identifier type of the instrument.  # noqa: E501

        :param instrument_id_type: The instrument_id_type of this InstrumentPaymentDiary.  # noqa: E501
        :type instrument_id_type: str
        """

        self._instrument_id_type = instrument_id_type

    @property
    def instrument_id(self):
        """Gets the instrument_id of this InstrumentPaymentDiary.  # noqa: E501

        The identifier for the instrument.  # noqa: E501

        :return: The instrument_id of this InstrumentPaymentDiary.  # noqa: E501
        :rtype: str
        """
        return self._instrument_id

    @instrument_id.setter
    def instrument_id(self, instrument_id):
        """Sets the instrument_id of this InstrumentPaymentDiary.

        The identifier for the instrument.  # noqa: E501

        :param instrument_id: The instrument_id of this InstrumentPaymentDiary.  # noqa: E501
        :type instrument_id: str
        """

        self._instrument_id = instrument_id

    @property
    def instrument_scope(self):
        """Gets the instrument_scope of this InstrumentPaymentDiary.  # noqa: E501

        The scope of the instrument.  # noqa: E501

        :return: The instrument_scope of this InstrumentPaymentDiary.  # noqa: E501
        :rtype: str
        """
        return self._instrument_scope

    @instrument_scope.setter
    def instrument_scope(self, instrument_scope):
        """Sets the instrument_scope of this InstrumentPaymentDiary.

        The scope of the instrument.  # noqa: E501

        :param instrument_scope: The instrument_scope of this InstrumentPaymentDiary.  # noqa: E501
        :type instrument_scope: str
        """

        self._instrument_scope = instrument_scope

    @property
    def version(self):
        """Gets the version of this InstrumentPaymentDiary.  # noqa: E501


        :return: The version of this InstrumentPaymentDiary.  # noqa: E501
        :rtype: lusid.Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this InstrumentPaymentDiary.


        :param version: The version of this InstrumentPaymentDiary.  # noqa: E501
        :type version: lusid.Version
        """

        self._version = version

    @property
    def legs(self):
        """Gets the legs of this InstrumentPaymentDiary.  # noqa: E501

        Aggregated sets of Cashflows.  # noqa: E501

        :return: The legs of this InstrumentPaymentDiary.  # noqa: E501
        :rtype: list[lusid.InstrumentPaymentDiaryLeg]
        """
        return self._legs

    @legs.setter
    def legs(self, legs):
        """Sets the legs of this InstrumentPaymentDiary.

        Aggregated sets of Cashflows.  # noqa: E501

        :param legs: The legs of this InstrumentPaymentDiary.  # noqa: E501
        :type legs: list[lusid.InstrumentPaymentDiaryLeg]
        """

        self._legs = legs

    @property
    def href(self):
        """Gets the href of this InstrumentPaymentDiary.  # noqa: E501

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :return: The href of this InstrumentPaymentDiary.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this InstrumentPaymentDiary.

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :param href: The href of this InstrumentPaymentDiary.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def links(self):
        """Gets the links of this InstrumentPaymentDiary.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this InstrumentPaymentDiary.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this InstrumentPaymentDiary.

        Collection of links.  # noqa: E501

        :param links: The links of this InstrumentPaymentDiary.  # noqa: E501
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
        if not isinstance(other, InstrumentPaymentDiary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstrumentPaymentDiary):
            return True

        return self.to_dict() != other.to_dict()
