"""
Description: Genomes classes
author: syedmohsinbukhari@googlemail.com
"""
from .genes import Node, Connection


class Genome:
    def __init__(self, nodes, connections):
        assert type(nodes) is list
        assert type(connections) is list
        assert all(isinstance(node, Node) for node in nodes)
        assert all(isinstance(conn, Connection) for conn in connections)

        self.nodes = nodes
        self.connections = connections

    def get_node_count(self):
        """
        Returns:
            Number of nodes in the genome
        """
        return len(self.nodes)

    def get_connection_count(self):
        """
        Returns:
            Number of connections in the genome
        """
        return len(self.connections)

    def compute(self, inp):
        """
        Computes output of the Neural Network encoded by this genome

        Args:
            inp: a list of input numbers.
        """
        assert type(inp) is list

        # TODO: Correct implementation of compute
        return self.get_connection_count() + self.get_node_count()
