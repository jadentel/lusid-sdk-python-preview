# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.29
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


class TranslateInstrumentDefinitionsRequest(object):
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
        'instruments': 'dict(str, LusidInstrument)',
        'dialect': 'str'
    }

    attribute_map = {
        'instruments': 'instruments',
        'dialect': 'dialect'
    }

    required_map = {
        'instruments': 'required',
        'dialect': 'required'
    }

    def __init__(self, instruments=None, dialect=None, local_vars_configuration=None):  # noqa: E501
        """TranslateInstrumentDefinitionsRequest - a model defined in OpenAPI"
        
        :param instruments:  The collection of instruments to translate.                Each instrument definition should be keyed by a unique correlation id. This id is ephemeral  and is not stored by LUSID. It serves only as a way to easily identify each instrument in the response.                Any instrument that is not already in the LUSID dialect should be given as an ExoticInstrument. (required)
        :type instruments: dict[str, lusid.LusidInstrument]
        :param dialect:  The target dialect that the given instruments should be translated to. (required)
        :type dialect: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._instruments = None
        self._dialect = None
        self.discriminator = None

        self.instruments = instruments
        self.dialect = dialect

    @property
    def instruments(self):
        """Gets the instruments of this TranslateInstrumentDefinitionsRequest.  # noqa: E501

        The collection of instruments to translate.                Each instrument definition should be keyed by a unique correlation id. This id is ephemeral  and is not stored by LUSID. It serves only as a way to easily identify each instrument in the response.                Any instrument that is not already in the LUSID dialect should be given as an ExoticInstrument.  # noqa: E501

        :return: The instruments of this TranslateInstrumentDefinitionsRequest.  # noqa: E501
        :rtype: dict[str, lusid.LusidInstrument]
        """
        return self._instruments

    @instruments.setter
    def instruments(self, instruments):
        """Sets the instruments of this TranslateInstrumentDefinitionsRequest.

        The collection of instruments to translate.                Each instrument definition should be keyed by a unique correlation id. This id is ephemeral  and is not stored by LUSID. It serves only as a way to easily identify each instrument in the response.                Any instrument that is not already in the LUSID dialect should be given as an ExoticInstrument.  # noqa: E501

        :param instruments: The instruments of this TranslateInstrumentDefinitionsRequest.  # noqa: E501
        :type instruments: dict[str, lusid.LusidInstrument]
        """
        if self.local_vars_configuration.client_side_validation and instruments is None:  # noqa: E501
            raise ValueError("Invalid value for `instruments`, must not be `None`")  # noqa: E501

        self._instruments = instruments

    @property
    def dialect(self):
        """Gets the dialect of this TranslateInstrumentDefinitionsRequest.  # noqa: E501

        The target dialect that the given instruments should be translated to.  # noqa: E501

        :return: The dialect of this TranslateInstrumentDefinitionsRequest.  # noqa: E501
        :rtype: str
        """
        return self._dialect

    @dialect.setter
    def dialect(self, dialect):
        """Sets the dialect of this TranslateInstrumentDefinitionsRequest.

        The target dialect that the given instruments should be translated to.  # noqa: E501

        :param dialect: The dialect of this TranslateInstrumentDefinitionsRequest.  # noqa: E501
        :type dialect: str
        """
        if self.local_vars_configuration.client_side_validation and dialect is None:  # noqa: E501
            raise ValueError("Invalid value for `dialect`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                dialect is not None and len(dialect) > 256):
            raise ValueError("Invalid value for `dialect`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                dialect is not None and len(dialect) < 1):
            raise ValueError("Invalid value for `dialect`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                dialect is not None and not re.search(r'^[a-zA-Z]*$', dialect)):  # noqa: E501
            raise ValueError(r"Invalid value for `dialect`, must be a follow pattern or equal to `/^[a-zA-Z]*$/`")  # noqa: E501

        self._dialect = dialect

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
        if not isinstance(other, TranslateInstrumentDefinitionsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TranslateInstrumentDefinitionsRequest):
            return True

        return self.to_dict() != other.to_dict()
