"""
Description: Genomes classes
author: syedmohsinbukhari@googlemail.com
"""
from neat.genes import Connection, Node
from neat.genomes import Genome
from neat.species import Species


class TestSpecies:

    def setup(self):
        self.in_node = Node(0)
        self.out_node = Node(1)

        self.conn = Connection(self.in_node, self.out_node, 1.0, True, 0)

        self.in_node.set_in_connections([])
        self.in_node.set_out_connections([self.conn])

        self.out_node.set_in_connections([self.conn])
        self.out_node.set_out_connections([])

        self.genome = Genome([self.in_node, self.out_node], [self.conn])

        self.species = Species([])

    def test_get_species_population(self):
        self.species = Species([])
        assert self.species.get_species_population() == 0

        self.species = Species([self.genome])
        assert self.species.get_species_population() == 1

        self.species = Species([self.genome, self.genome])
        assert self.species.get_species_population() == 2

    def test_set_genomes(self):
        self.species.set_genomes([])
        assert self.species.get_species_population() == 0

        self.species.set_genomes([self.genome])
        assert self.species.get_species_population() == 1

    def test_add_genome(self):
        self.species = Species([])
        assert self.species.get_species_population() == 0

        self.species.add_genome(self.genome)
        assert self.species.get_species_population() == 1

        self.species.add_genome(self.genome)
        assert self.species.get_species_population() == 2
