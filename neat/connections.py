"""
Description: Genomes classes
author: syedmohsinbukhari@googlemail.com
"""
from .nodes import Node


class Connection:

    def __init__(self, in_node, out_node, weight, is_enabled, innovation_number):
        assert isinstance(in_node, Node)
        assert isinstance(out_node, Node)
        assert type(weight) is float
        assert type(is_enabled) is bool
        assert type(innovation_number) is int

        self.in_node = in_node
        self.out_node = out_node
        self.weight = weight
        self.enabled = is_enabled
        self.innov = innovation_number  # Innovation number of the connection

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False
