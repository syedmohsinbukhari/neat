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

class Individual():
    """
    An individual is a combination of genes and has a fitness score
    """

    fitness_score = 0
    genes = []
    genes_size = 5

    def __int__(self):
        """
        """
        self.genes = np.random.randint(2,size=genes_size)
        self.fitness_score = sum(self.genes)


    def get_fitness_score(self):
        """ Return fitness score """
        return self.fitness_score


class Population():
    """
    A collection of individuals
    """

    population_size = 10
    individuals = []
    fittest = 0

    def __init__(self,size=None):
        """
        Default population size 10
        """
        if population_size:
            self.population_size = size

        self.individuals = [Individual()
                            for i in range(self.population_size)]



    def get_fittest(self,number_of_fit=2):
        """
        Return top n fittest individuals
        """
        max_val = -1
        top_n = [max_val]*number_of_fit

        for individual in self.individuals:
            score = individual.get_fitness_score()

            top_found = False
            i = 0
            while not top_found and i < len(top_n):

                if score > top_n[i]:
                    top_n.insert(i,individual)
                    top_n.pop()
                    top_found = True
                i += 1

        return top_n





class Evolution():

    population = None
    generation_count = 0
    the_best = None
    the_second_best = None

    def __init__(self):
        """
        """
        self.population = Population(size=10)

        while (population.fittest < 5):
            self.generation_count += 1

            self.selection()
            self.crossover()

    def selection(self):
        """
        Select the best indiviiduals
        """
        self.the_best, self.the_second_best = self.population.get_fittest(n=2)

    def crossover(self):
        """
        Crossover genes of the best two
        """
    # def main():
    #     """
    #     """

if __name__ == "__main__":
    # main()
    # r = np.random.randint(2,size=5)
    # print(r)
    # print(sum(r))
    # k = [5,6,7,3,2,1]
    # max_val = -1
    # top_n = [max_val]*5
    #
    # for a in k:
    #
    #     top_found = False
    #     i = 0
    #     while not top_found and i < len(top_n):
    #
    #         if a > top_n[i]:
    #             top_n.insert(i,a)
    #             top_n.pop()
    #             top_found = True
    #         i += 1
    #
    # print(top_n)
