"""
Description: Genomes classes
author: syedmohsinbukhari@googlemail.com
"""
from neat.genes import Connection, Node


class TestConnections:

    def setup(self):
        self.in_node = Node(0)
        self.out_node = Node(1)

        self.conn = Connection(self.in_node, self.out_node, 1.0, True, 0)

        self.in_node.set_in_connections([])
        self.in_node.set_out_connections([self.conn])

        self.out_node.set_in_connections([self.conn])
        self.out_node.set_out_connections([])

    def test_enable(self):
        self.conn.enable()
        assert self.conn.enabled

    def test_disable(self):
        self.conn.disable()
        assert ~self.conn.enabled


class TestNodes:

    def setup(self):
        self.in_node = Node(0)
        self.out_node = Node(1)

        self.conn = Connection(self.in_node, self.out_node, 1.0, True, 0)

        self.in_node.set_in_connections([])
        self.in_node.set_out_connections([self.conn])

        self.out_node.set_in_connections([self.conn])
        self.out_node.set_out_connections([])

    def test_get_num_in_conns(self):
        assert self.in_node.get_num_in_conns() == 0
        assert self.out_node.get_num_in_conns() == 1

    def test_get_num_out_conns(self):
        assert self.in_node.get_num_out_conns() == 1
        assert self.out_node.get_num_out_conns() == 0

    def test_get_num_total_conns(self):
        assert self.in_node.get_num_total_conns() == 1
        assert self.out_node.get_num_total_conns() == 1

    def test_set_in_connections(self):
        self.in_node.set_in_connections([])
        assert self.in_node.get_num_in_conns() == 0

        self.out_node.set_in_connections([self.conn])
        assert self.out_node.get_num_in_conns() == 1

    def test_set_out_connections(self):
        self.in_node.set_out_connections([self.conn])
        assert self.in_node.get_num_out_conns() == 1

        self.out_node.set_out_connections([])
        assert self.out_node.get_num_out_conns() == 0
