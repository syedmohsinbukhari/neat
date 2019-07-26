"""
Description: Genomes classes
author: syedmohsinbukhari@googlemail.com
"""


class Node:

    def __init__(self, node_number, in_connections, out_connections):
        assert type(node_number) is int
        assert type(in_connections) is list
        assert type(out_connections) is list

        self.number = node_number
        self.in_connections = in_connections
        self.out_connections = out_connections

    def get_num_in_conns(self):
        """
        Returns the number of IN connections to this node
        """
        return len(self.in_connections)

    def get_num_out_conns(self):
        """
        Returns the number of OUT connections from this node
        """
        return len(self.out_connections)

    def get_num_total_conns(self):
        """
        Returns the number of total connections to and from this node
        """
        return self.get_num_in_conns() + self.get_num_out_conns()
