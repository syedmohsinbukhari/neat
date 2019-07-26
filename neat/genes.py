"""
Description: Genomes classes
author: syedmohsinbukhari@googlemail.com
"""


class Connection:
    """This class models Connection Genes."""

    def __init__(self, in_node, out_node, weight, is_enabled, innovation_number):
        """Generate a connection object.

        Args:
            in_node: The node from which the connection is initiated
            out_node: The node to which the connection goes
            weight: Weight of the connection
            is_enabled: Whether the connection is enabled or not
            innovation_number: Innovation number of the connection
        """
        assert isinstance(in_node, Node)
        assert isinstance(out_node, Node)
        assert type(weight) is float
        assert type(is_enabled) is bool
        assert type(innovation_number) is int

        self.in_node = in_node
        self.out_node = out_node
        self.weight = weight
        self.enabled = is_enabled
        self.innov = innovation_number

    def enable(self):
        """Enable the connection"""
        self.enabled = True

    def disable(self):
        """Disable the connection"""
        self.enabled = False


class Node:
    """This class models Node Genes."""

    def __init__(self, node_number):
        """Generates a Node object with a given node_number.

        :param node_number: Node number to assign to the node being generated.
        """
        assert type(node_number) is int
        self.number = node_number
        self.in_connections = []
        self.out_connections = []

        """"""
    def get_num_in_conns(self):
        """Return the number of IN connections to this node.

        :return: number of IN connections to this node.
        """
        return len(self.in_connections)

    def get_num_out_conns(self):
        """Return the number of OUT connections from this node.

        :return: number of OUT connections from this node.
        """
        return len(self.out_connections)

    def get_num_total_conns(self):
        """Return the number of total connections to and from this node.

        :return: total number of connections.
        """
        return self.get_num_in_conns() + self.get_num_out_conns()

    def set_in_connections(self, in_connections):
        """Sets the incoming connections to this node.

        :param in_connections: a list containing incoming connections to this node
        """
        assert type(in_connections) is list
        assert all(isinstance(conn, Connection) for conn in in_connections)

        self.in_connections = in_connections

    def set_out_connections(self, out_connections):
        """Sets the incoming connections to this node.

        :param out_connections: a list containing outgoing connections to this node
        """
        assert type(out_connections) is list
        assert all(isinstance(conn, Connection) for conn in out_connections)

        self.out_connections = out_connections

