# Class Design

---
### Node Class
#### Attributes
- Node Number
- Input Connections
- Output Connections
#### Methods
- Get Number of Input Connections
- Get Number of Output Connections
- Get Number of Total Connections
---
### Connection Class
#### Attributes
- In Node
- Out Node
- Weight
- Enabled
- Innovation Number
#### Methods
- Enable
- Disable
---
### Genome Class
#### Attributes
- Node Objects Array
- Connection Objects Array
#### Methods
- Get Number Of Nodes
- Get Number Of Connections
- Compute Output From Input
---
### Species Class
#### Attributes
- Genome Objects Array
#### Methods
- Get Specie Population
---
### Mutation Class
#### Methods
- Mutate Add Nodes 
- Mutate Add Connections
---
### Crossover Class
#### Methods
- Produce Offspring
---
### Speciate Class
#### Methods
- Identify Species
---
### Innovation Class
#### Methods
- Generate Innovation Number
---
### Selection Class
#### Methods
- Compute Fitness
- Select Fit Genomes
---
### Helper Class
#### Methods
- Align Genes
---
