"""
Description: Genomes classes
author: syedmohsinbukhari@googlemail.com
"""
from .genomes import Genome


class Species:
    """This class models species."""

    def __init__(self, genomes_array):
        assert type(genomes_array) is list
        assert all(isinstance(genome, Genome) for genome in genomes_array)
        self.genomes = genomes_array

    def get_species_population(self):
        """Gets the number of genomes in the species.

        Returns:
            Number of genomes in the species.
        """
        return len(self.genomes)

    def set_genomes(self, genomes_array):
        """Sets the genomes array in the species

        Args:
            genomes_array: an array of genomes to put in this
        """
        assert type(genomes_array) is list
        assert all(isinstance(genome, Genome) for genome in genomes_array)
        self.genomes = genomes_array

    def add_genome(self, genome):
        """Adds a genome to this specie's genome array.

        Args:
            genome: The genome that is to be added to this specie
        """
        assert isinstance(genome, Genome)
        assert type(self.genomes) is list

        self.genomes.append(genome)
