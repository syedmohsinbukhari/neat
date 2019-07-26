"""
Description: Genomes classes
author: syedmohsinbukhari@googlemail.com
"""


class Genome:
    def __init__(self):
        self.nodes = []
        self.connections = []

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

        # TODO
        return self.get_connection_count() + self.get_node_count()
