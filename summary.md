##### Competing Conventions Problem

    - aka Permutations Problem
    - When the same solution can be represented in different ways
    - When not the same encoding, crossover can produce damaged offspring
    - ABC can be rep in 3! 6 ways
    - When ABC | CBC crossover -> CBC. Critical information lost
    - Further complicated with _differing convention_
        - DBE, ABC | B interdependency
    - More difficult in TWEANN because
        - similar solutions totally different topolgies
        - genomes of different sizes
    - Since no constraint over topologies produced fixed topology solutions dont work
    - PDGP assumes subnet represent functional unit that can be recombined
        - but different topologies may not be based on the same network
    - Main intution behind NEAT from problem
        - **Structure representations will not always match up**
            - Genomes can have different sizes
            - Genes in the same position might express different traits
            - Genes may appear at different position for different chromosomes
        - Similar to gene alighment problem in nature
        - Genomes are not fixed len either
        - Through gene amplification, genes added to genomes
        - Genes cant just randomly insert
        - To keep crossover orderly, right genes need to be crossed
        - Nature's solution is _homology_
        - 2 genes are homologous if alleles of the same trait
        - Homology can't be determined from structure
        - Historical origin can be used to determine homology
        - NEAT performs artificial synapsis add new structures without losing track
    
##### Speciation Problem

    - Innovation through adding new structures
    - This can however reduce the performance initially
    - Need a few generations to optimize
    - GNARL adds nonfunctional structure to address this problem
    - however it might never connect to the functional units
    - Nature: niching. Different structure, different specie
    - If networks isolated into their own species, they won't have to compete with others
    - Speciation commonly applied to multi-modal functions, cooperative coevolution of modular systems
    - It requires a compatibility function to find similar species
    - Not used in neuroevolution because difficult to formulate
    - Competing Conventions make it harder since same function rep with diff network structure
    - NEAT solves that so can formulate it
    - **Explicit Fitness Sharing** is used
        - individuals with similar genomes share their fitness payoff
    - Original implicit fitness used performance similarity instead of genetic similarity
    - Result of sharing fitness is that the number of networks that can exist on single fitness peak is limited by the size of the peak
    - Population divides on different peaks without the threat of one specie taking over
    - In NEAT similarity can be measured easily so explicit fitness sharing well-suited
    - Explicit fitness sharing: http://www.cs.bham.ac.uk/~axk/lect10.pdf
        - Share the fitness score with other similar network
        - Lower overall score
        
#### Initial Population
    - Many TWEANNs have initial random population
    - Gives diversity, however sometimes can produce networks with not all connections to the output
    - Can take time to weed these out
    - Also, if we start with some random structure we are nodes which haven't proven themselves
    - As the network is only going to grow, nothing is going to remove these unnecessary nodes
    - One way is to add network size to the fitness function
    - That's adhoc, unexpected consequences
    - Different problems require different complexity
    - Start with minimal population and structure
        - If no hidden nodes and grows structure only when beneficial
        - then no need to penalize network size
    - **NEAT Design principle : start with minimal population and structure**
    - This makes sure
        - Searches in the lowest-dim weight space over all gens
        - Minimizes search space, increases performance
    - Other TWEANNs start with random pop for diversity later
        - Otherwise innovations won't survive
    - Because of speciation NEAT does not need that
   
   
#### NEAT
- _Extract requirements_

- **Genetic Encoding**
    - Genomes are linear representation of network connectivity
    - Each genome has
        - A list of connection genes
            - Each refers to 2 genes
            - In node
            - Out node
            - Weight of the connection
            - Enable bit
            - Innovation number (to find correspodning genes)
        - Node Genes provide
            - List of inputs
            - Hidden nodes
            - Outputs
    - Mutation
        - can change
            - connection weights
                - Either perturbed or not
            - network structures
                - Structural mutation in 2 ways
                    - Add connection (expand genome size)
                        - single new connection gene with random weight
                    - Add node
                        -  
