# Class Design

### Node Class
#### Attributes
- Node Number
- Connection Objects Array

### Connection Class
#### Attributes
- In Node
- Out Node
- Weight
- Enabled
- Innovation Number

### Genome Class
#### Attributes
- Node Objects Array
- Connection Objects Array
#### Methods
- Get Number Of Nodes
- Get Number Of Connections

### Species Class
#### Attributes
- Genome Objects Array
#### Methods
- Compute Fitness
- Get Fit Genomes

### Mutation Class
#### Methods
- Mutate Add Nodes 
- Mutate Add Connections

### Crossover Class
#### Methods
- Produce Offspring

### Speciate Class
#### Methods
- Identify Species

### Innovation Class
#### Methods
- Generate Innovation Number

### Helper Class
#### Methods
- Align Genes

