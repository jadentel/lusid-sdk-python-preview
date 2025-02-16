# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.36
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


class UpsertResultValuesDataRequest(object):
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
        'document_id': 'StructuredResultDataId',
        'key': 'dict(str, str)',
        'data_address': 'str',
        'result_value': 'ResultValue'
    }

    attribute_map = {
        'document_id': 'documentId',
        'key': 'key',
        'data_address': 'dataAddress',
        'result_value': 'resultValue'
    }

    required_map = {
        'document_id': 'required',
        'key': 'optional',
        'data_address': 'optional',
        'result_value': 'optional'
    }

    def __init__(self, document_id=None, key=None, data_address=None, result_value=None, local_vars_configuration=None):  # noqa: E501
        """UpsertResultValuesDataRequest - a model defined in OpenAPI"
        
        :param document_id:  (required)
        :type document_id: lusid.StructuredResultDataId
        :param key:  The structured unit result data key.
        :type key: dict(str, str)
        :param data_address:  The address of the piece of unit result data
        :type data_address: str
        :param result_value: 
        :type result_value: lusid.ResultValue

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._document_id = None
        self._key = None
        self._data_address = None
        self._result_value = None
        self.discriminator = None

        self.document_id = document_id
        self.key = key
        self.data_address = data_address
        if result_value is not None:
            self.result_value = result_value

    @property
    def document_id(self):
        """Gets the document_id of this UpsertResultValuesDataRequest.  # noqa: E501


        :return: The document_id of this UpsertResultValuesDataRequest.  # noqa: E501
        :rtype: lusid.StructuredResultDataId
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this UpsertResultValuesDataRequest.


        :param document_id: The document_id of this UpsertResultValuesDataRequest.  # noqa: E501
        :type document_id: lusid.StructuredResultDataId
        """
        if self.local_vars_configuration.client_side_validation and document_id is None:  # noqa: E501
            raise ValueError("Invalid value for `document_id`, must not be `None`")  # noqa: E501

        self._document_id = document_id

    @property
    def key(self):
        """Gets the key of this UpsertResultValuesDataRequest.  # noqa: E501

        The structured unit result data key.  # noqa: E501

        :return: The key of this UpsertResultValuesDataRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this UpsertResultValuesDataRequest.

        The structured unit result data key.  # noqa: E501

        :param key: The key of this UpsertResultValuesDataRequest.  # noqa: E501
        :type key: dict(str, str)
        """

        self._key = key

    @property
    def data_address(self):
        """Gets the data_address of this UpsertResultValuesDataRequest.  # noqa: E501

        The address of the piece of unit result data  # noqa: E501

        :return: The data_address of this UpsertResultValuesDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._data_address

    @data_address.setter
    def data_address(self, data_address):
        """Sets the data_address of this UpsertResultValuesDataRequest.

        The address of the piece of unit result data  # noqa: E501

        :param data_address: The data_address of this UpsertResultValuesDataRequest.  # noqa: E501
        :type data_address: str
        """

        self._data_address = data_address

    @property
    def result_value(self):
        """Gets the result_value of this UpsertResultValuesDataRequest.  # noqa: E501


        :return: The result_value of this UpsertResultValuesDataRequest.  # noqa: E501
        :rtype: lusid.ResultValue
        """
        return self._result_value

    @result_value.setter
    def result_value(self, result_value):
        """Sets the result_value of this UpsertResultValuesDataRequest.


        :param result_value: The result_value of this UpsertResultValuesDataRequest.  # noqa: E501
        :type result_value: lusid.ResultValue
        """

        self._result_value = result_value

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
        if not isinstance(other, UpsertResultValuesDataRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpsertResultValuesDataRequest):
            return True

        return self.to_dict() != other.to_dict()
