"""
Description: Genomes classes
author: syedmohsinbukhari@googlemail.com
"""
from neat.genes import Connection, Node
from neat.genomes import Genome


class TestGenomes:

    def setup(self):
        self.in_node = Node(0)
        self.out_node = Node(1)

        self.conn = Connection(self.in_node, self.out_node, 1.0, True, 0)

        self.in_node.set_in_connections([])
        self.in_node.set_out_connections([self.conn])

        self.out_node.set_in_connections([self.conn])
        self.out_node.set_out_connections([])

        self.genome = Genome([self.in_node, self.out_node], [self.conn])

    def test_get_node_count(self):
        assert self.genome.get_node_count() == 2

    def test_get_connection_count(self):
        assert self.genome.get_connection_count() == 1

    # TODO: test case for compute function of Genome class
