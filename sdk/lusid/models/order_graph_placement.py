# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4182
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


class OrderGraphPlacement(object):
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
        'placement': 'Placement',
        'block_id': 'ResourceId',
        'order_ids': 'list[ResourceId]',
        'allocation_ids': 'list[ResourceId]',
        'execution_ids': 'list[ResourceId]',
        'placed': 'OrderGraphSynopsis',
        'executed': 'OrderGraphSynopsis',
        'allocated': 'OrderGraphSynopsis',
        'derived_state': 'str'
    }

    attribute_map = {
        'placement': 'placement',
        'block_id': 'blockId',
        'order_ids': 'orderIds',
        'allocation_ids': 'allocationIds',
        'execution_ids': 'executionIds',
        'placed': 'placed',
        'executed': 'executed',
        'allocated': 'allocated',
        'derived_state': 'derivedState'
    }

    required_map = {
        'placement': 'required',
        'block_id': 'required',
        'order_ids': 'required',
        'allocation_ids': 'required',
        'execution_ids': 'required',
        'placed': 'required',
        'executed': 'required',
        'allocated': 'required',
        'derived_state': 'required'
    }

    def __init__(self, placement=None, block_id=None, order_ids=None, allocation_ids=None, execution_ids=None, placed=None, executed=None, allocated=None, derived_state=None, local_vars_configuration=None):  # noqa: E501
        """OrderGraphPlacement - a model defined in OpenAPI"
        
        :param placement:  (required)
        :type placement: lusid.Placement
        :param block_id:  (required)
        :type block_id: lusid.ResourceId
        :param order_ids:  Identifiers for all orders in the block. (required)
        :type order_ids: list[lusid.ResourceId]
        :param allocation_ids:  Identifiers for all allocations relating to this placement. (required)
        :type allocation_ids: list[lusid.ResourceId]
        :param execution_ids:  Identifiers of all executions against this placement. (required)
        :type execution_ids: list[lusid.ResourceId]
        :param placed:  (required)
        :type placed: lusid.OrderGraphSynopsis
        :param executed:  (required)
        :type executed: lusid.OrderGraphSynopsis
        :param allocated:  (required)
        :type allocated: lusid.OrderGraphSynopsis
        :param derived_state:  A simple description of the overall state of a placement. (required)
        :type derived_state: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._placement = None
        self._block_id = None
        self._order_ids = None
        self._allocation_ids = None
        self._execution_ids = None
        self._placed = None
        self._executed = None
        self._allocated = None
        self._derived_state = None
        self.discriminator = None

        self.placement = placement
        self.block_id = block_id
        self.order_ids = order_ids
        self.allocation_ids = allocation_ids
        self.execution_ids = execution_ids
        self.placed = placed
        self.executed = executed
        self.allocated = allocated
        self.derived_state = derived_state

    @property
    def placement(self):
        """Gets the placement of this OrderGraphPlacement.  # noqa: E501


        :return: The placement of this OrderGraphPlacement.  # noqa: E501
        :rtype: lusid.Placement
        """
        return self._placement

    @placement.setter
    def placement(self, placement):
        """Sets the placement of this OrderGraphPlacement.


        :param placement: The placement of this OrderGraphPlacement.  # noqa: E501
        :type placement: lusid.Placement
        """
        if self.local_vars_configuration.client_side_validation and placement is None:  # noqa: E501
            raise ValueError("Invalid value for `placement`, must not be `None`")  # noqa: E501

        self._placement = placement

    @property
    def block_id(self):
        """Gets the block_id of this OrderGraphPlacement.  # noqa: E501


        :return: The block_id of this OrderGraphPlacement.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._block_id

    @block_id.setter
    def block_id(self, block_id):
        """Sets the block_id of this OrderGraphPlacement.


        :param block_id: The block_id of this OrderGraphPlacement.  # noqa: E501
        :type block_id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and block_id is None:  # noqa: E501
            raise ValueError("Invalid value for `block_id`, must not be `None`")  # noqa: E501

        self._block_id = block_id

    @property
    def order_ids(self):
        """Gets the order_ids of this OrderGraphPlacement.  # noqa: E501

        Identifiers for all orders in the block.  # noqa: E501

        :return: The order_ids of this OrderGraphPlacement.  # noqa: E501
        :rtype: list[lusid.ResourceId]
        """
        return self._order_ids

    @order_ids.setter
    def order_ids(self, order_ids):
        """Sets the order_ids of this OrderGraphPlacement.

        Identifiers for all orders in the block.  # noqa: E501

        :param order_ids: The order_ids of this OrderGraphPlacement.  # noqa: E501
        :type order_ids: list[lusid.ResourceId]
        """
        if self.local_vars_configuration.client_side_validation and order_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `order_ids`, must not be `None`")  # noqa: E501

        self._order_ids = order_ids

    @property
    def allocation_ids(self):
        """Gets the allocation_ids of this OrderGraphPlacement.  # noqa: E501

        Identifiers for all allocations relating to this placement.  # noqa: E501

        :return: The allocation_ids of this OrderGraphPlacement.  # noqa: E501
        :rtype: list[lusid.ResourceId]
        """
        return self._allocation_ids

    @allocation_ids.setter
    def allocation_ids(self, allocation_ids):
        """Sets the allocation_ids of this OrderGraphPlacement.

        Identifiers for all allocations relating to this placement.  # noqa: E501

        :param allocation_ids: The allocation_ids of this OrderGraphPlacement.  # noqa: E501
        :type allocation_ids: list[lusid.ResourceId]
        """
        if self.local_vars_configuration.client_side_validation and allocation_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `allocation_ids`, must not be `None`")  # noqa: E501

        self._allocation_ids = allocation_ids

    @property
    def execution_ids(self):
        """Gets the execution_ids of this OrderGraphPlacement.  # noqa: E501

        Identifiers of all executions against this placement.  # noqa: E501

        :return: The execution_ids of this OrderGraphPlacement.  # noqa: E501
        :rtype: list[lusid.ResourceId]
        """
        return self._execution_ids

    @execution_ids.setter
    def execution_ids(self, execution_ids):
        """Sets the execution_ids of this OrderGraphPlacement.

        Identifiers of all executions against this placement.  # noqa: E501

        :param execution_ids: The execution_ids of this OrderGraphPlacement.  # noqa: E501
        :type execution_ids: list[lusid.ResourceId]
        """
        if self.local_vars_configuration.client_side_validation and execution_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `execution_ids`, must not be `None`")  # noqa: E501

        self._execution_ids = execution_ids

    @property
    def placed(self):
        """Gets the placed of this OrderGraphPlacement.  # noqa: E501


        :return: The placed of this OrderGraphPlacement.  # noqa: E501
        :rtype: lusid.OrderGraphSynopsis
        """
        return self._placed

    @placed.setter
    def placed(self, placed):
        """Sets the placed of this OrderGraphPlacement.


        :param placed: The placed of this OrderGraphPlacement.  # noqa: E501
        :type placed: lusid.OrderGraphSynopsis
        """
        if self.local_vars_configuration.client_side_validation and placed is None:  # noqa: E501
            raise ValueError("Invalid value for `placed`, must not be `None`")  # noqa: E501

        self._placed = placed

    @property
    def executed(self):
        """Gets the executed of this OrderGraphPlacement.  # noqa: E501


        :return: The executed of this OrderGraphPlacement.  # noqa: E501
        :rtype: lusid.OrderGraphSynopsis
        """
        return self._executed

    @executed.setter
    def executed(self, executed):
        """Sets the executed of this OrderGraphPlacement.


        :param executed: The executed of this OrderGraphPlacement.  # noqa: E501
        :type executed: lusid.OrderGraphSynopsis
        """
        if self.local_vars_configuration.client_side_validation and executed is None:  # noqa: E501
            raise ValueError("Invalid value for `executed`, must not be `None`")  # noqa: E501

        self._executed = executed

    @property
    def allocated(self):
        """Gets the allocated of this OrderGraphPlacement.  # noqa: E501


        :return: The allocated of this OrderGraphPlacement.  # noqa: E501
        :rtype: lusid.OrderGraphSynopsis
        """
        return self._allocated

    @allocated.setter
    def allocated(self, allocated):
        """Sets the allocated of this OrderGraphPlacement.


        :param allocated: The allocated of this OrderGraphPlacement.  # noqa: E501
        :type allocated: lusid.OrderGraphSynopsis
        """
        if self.local_vars_configuration.client_side_validation and allocated is None:  # noqa: E501
            raise ValueError("Invalid value for `allocated`, must not be `None`")  # noqa: E501

        self._allocated = allocated

    @property
    def derived_state(self):
        """Gets the derived_state of this OrderGraphPlacement.  # noqa: E501

        A simple description of the overall state of a placement.  # noqa: E501

        :return: The derived_state of this OrderGraphPlacement.  # noqa: E501
        :rtype: str
        """
        return self._derived_state

    @derived_state.setter
    def derived_state(self, derived_state):
        """Sets the derived_state of this OrderGraphPlacement.

        A simple description of the overall state of a placement.  # noqa: E501

        :param derived_state: The derived_state of this OrderGraphPlacement.  # noqa: E501
        :type derived_state: str
        """
        if self.local_vars_configuration.client_side_validation and derived_state is None:  # noqa: E501
            raise ValueError("Invalid value for `derived_state`, must not be `None`")  # noqa: E501

        self._derived_state = derived_state

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
        if not isinstance(other, OrderGraphPlacement):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrderGraphPlacement):
            return True

        return self.to_dict() != other.to_dict()
