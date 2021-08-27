# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3437
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class UpsertCdsFlowConventionsRequest(object):
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
        'cds_flow_conventions': 'CdsFlowConventions'
    }

    attribute_map = {
        'cds_flow_conventions': 'cdsFlowConventions'
    }

    required_map = {
        'cds_flow_conventions': 'optional'
    }

    def __init__(self, cds_flow_conventions=None):  # noqa: E501
        """
        UpsertCdsFlowConventionsRequest - a model defined in OpenAPI

        :param cds_flow_conventions: 
        :type cds_flow_conventions: lusid.CdsFlowConventions

        """  # noqa: E501

        self._cds_flow_conventions = None
        self.discriminator = None

        if cds_flow_conventions is not None:
            self.cds_flow_conventions = cds_flow_conventions

    @property
    def cds_flow_conventions(self):
        """Gets the cds_flow_conventions of this UpsertCdsFlowConventionsRequest.  # noqa: E501


        :return: The cds_flow_conventions of this UpsertCdsFlowConventionsRequest.  # noqa: E501
        :rtype: CdsFlowConventions
        """
        return self._cds_flow_conventions

    @cds_flow_conventions.setter
    def cds_flow_conventions(self, cds_flow_conventions):
        """Sets the cds_flow_conventions of this UpsertCdsFlowConventionsRequest.


        :param cds_flow_conventions: The cds_flow_conventions of this UpsertCdsFlowConventionsRequest.  # noqa: E501
        :type: CdsFlowConventions
        """

        self._cds_flow_conventions = cds_flow_conventions

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
        if not isinstance(other, UpsertCdsFlowConventionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
