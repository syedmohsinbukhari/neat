import pytest
import genetic_algo_demo as g


class TestSize(object):
    """Test object initialization"""

    @pytest.mark.parametrize("size", [
        (25),
        (5),
        (1),
        (3),
        (1200)
    ])
    def test_population_size_init(self,size):
        """Test initialized population size"""
        population_size = size
        population = g.Population(size=population_size)
        assert population.population_size == population_size,\
                "population size was incorrect, should have been {}".\
                format(population_size)


    @pytest.mark.parametrize("size", [
        (25),
        (5),
        (1),
        (3),
        (1200)
    ])
    def test_individual_genes_len(self, size):
        """Test initialized individual size"""
        gene_size = size
        individual = g.Individual(size=gene_size)
        assert len(individual.genes) == gene_size# \
                # and individual.genes_size == gene_size

    def test_negative_error(self):
        """Test neagtive size custom ValueError"""
        gene_size = -5
        with pytest.raises(ValueError, match=r".* less than 0.*"):
            individual = g.Individual(size=gene_size)
            assert len(individual.genes) == gene_size# \
