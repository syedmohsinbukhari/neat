"""
Description: A demo of genetic algorithm
author: bazarovay@github.com

- Selection
- Crossover
- Mutation
- Compute Fitness

Reference
https://towardsdatascience.com/introduction-to-genetic-algorithms-including-example-code-e396e98d8bf3
"""
import numpy as np
import copy


class Individual:
    """
    An individual is a combination of genes and has a fitness score
    """

    fitness_score = 0
    genes = []
    genes_size = 5

    def __init__(self, size=None):
        """
        Initialize individual with gene size. Default size is 5
        """
        if size:
            if size < 0:
                raise ValueError("Individual gene size can't be less than 0.\
                                Size provided was {}".format(size))
            self.genes_size = size

        self.genes = np.random.randint(2, size=self.genes_size)

    def get_fitness_score(self):
        """ Return fitness score """
        self.fitness_score = sum(self.genes)
        return self.fitness_score


class Population:
    """
    A collection of individuals
    """

    population_size = 10
    individuals = []
    fittest = 0

    def __init__(self, size=None):
        """
        Default population size 10
        """
        if size:
            self.population_size = size

        self.individuals = [Individual()
                            for _ in range(self.population_size)]

    def get_fittest_score(self):
        """
        Return score of the fittest individual
        """
        return self.get_fittest(n=1)[0].get_fitness_score()

    def get_fittest(self, n=2):
        """
        Return top n fittest individuals
        Args:
            n:

        Returns:

        """
        max_val = -1
        top_n = [max_val]*n
        top_individuals = [None]*n

        for individual in self.individuals:
            score = individual.get_fitness_score()

            top_found = False
            i = 0
            while not top_found and i < len(top_n):

                if score > top_n[i]:
                    top_n.insert(i, score)
                    top_n.pop()

                    top_individuals.insert(i, individual)
                    top_individuals.pop()
                    top_found = True
                i += 1

        return top_individuals

    def get_least_fit_index(self):
        """
        Get the least_fittest
        """
        min_val = 100  # assumes gene size 5
        min_id = None

        for idx, individual in enumerate(self.individuals):

            score = individual.get_fitness_score()
            if score < min_val:
                min_val = score
                min_id = idx

        return min_id


class Evolution:
    """
    Evolution process
    """
    population = None
    generation_count = 0
    the_best = None
    the_second_best = None

    def __init__(self):
        """
        """
        self.population = Population(size=10)

        while self.population.get_fittest_score() < 5:
            self.generation_count += 1

            self.selection()
            self.crossover()

            if np.random.randint(8)%7 == 0:
                self.mutation()

            self.generation_change()
            print('Generation#{}, fittest score {}, genes {}'.format(
                self.generation_count,
                self.population.get_fittest_score(),
                self.population.get_fittest(n=1)[0].genes
            ))

    def selection(self):
        """
        Select the best indiviiduals
        """
        parent1, parent2 = self.population.get_fittest(n=2)
        self.the_best = copy.copy(parent1)
        self.the_second_best = copy.copy(parent2)

    def crossover(self):
        """
        Crossover genes of the best two
        """
        crossover_point = np.random.randint(5)
        self.the_best.genes[crossover_point], self.the_second_best.genes[crossover_point] =\
            self.the_second_best.genes[crossover_point], self.the_best.genes[crossover_point]

    def mutation(self):
        """
        Flip a random bit
        """
        mutation_point = np.random.randint(5)
        self.the_best.genes[mutation_point] = 1 ^ self.the_best.genes[mutation_point]
        mutation_point = np.random.randint(5)
        self.the_second_best.genes[mutation_point] = 1 ^ self.the_second_best.genes[mutation_point]

    def generation_change(self):
        """
        Replace least fit with the best child
        """
        if self.the_best.get_fitness_score() >= self.the_second_best.get_fitness_score():
            best_child = self.the_best
        else:
            best_child = self.the_second_best

        self.population.individuals[self.population.get_least_fit_index()] = best_child


if __name__ == "__main__":
    Evolution()
