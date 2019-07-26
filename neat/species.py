"""
Description: Genomes classes
author: syedmohsinbukhari@googlemail.com
"""


class Species:

    def __init__(self, genomes_array):
        self.genomes = genomes_array

    def get_specie_population(self):
        """
        Returns:
            Number of genomes in the species.
        """
        return len(self.genomes)
