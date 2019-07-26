"""
Description: Genomes classes
author: syedmohsinbukhari@googlemail.com
"""


class Genome:
    def __init__(self):
        self.nodes = []
        self.connections = []

    def get_node_count(self):
        return len(self.nodes)

    def get_connection_count(self):
        return len(self.connections)
