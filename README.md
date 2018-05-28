# Evolutionary Computation


### Problem Description
The population size is 6 (i.e. m = 6). Members of this population have genotypes consisting of 3 genes. Each gene is an integer inclusively ranging from 1 to 10.

 g 1 , g 2 , g 3 ∈ [1..10]()

The fitness function for an individual is a function of the genes that comprise that individual’s genotype. For this problem, the fitness of an individual member of the population i is determined by the ith genes of that individual (i.e. g 1 is the the first gene of individual i) in the following function:
### fitnesas
fitness(i) = 0.5gi1 + 1.25gi2 + 2.0gi3

Two unique parents will be selected for reproduction. The reproducing members of the population will be chosen using Fitness-Proportional selection. You are responsible for the probability weighted selection of the parents. It is recommended that you use a random number generator that pro- duces a value in the range of [0.0, 1.0](). In this selection function, the probability of an individual i to be chosen is given by its ﬁtness divided by the total ﬁtness of all population members.
### crossover
After the 2 parents have been selected, they will reproduce to create the next generation via crossover. The ﬁrst parent chosen will be known as a and the second will be b. The ﬁrst half of the new population will take 2 genes from a and 1 gene from b. The second half will take 1 gene from a and 2 genes from b. Which genes are selected should be picked with a uniform probability distribution via your favorite random number generator. As an example, consider a to have the genotype of \< 1, 2, 3 \> and b to have a genotype of \< 4, 5, 6 \>. To create a child in the ﬁrst half of the population, pick one gene from a to replace with b’s value for that same gene. If we picked gene 2 for replacement, the resultant child c would be \< 1, 5, 3 \>.

### mutation
After the children have been generated, each has a 0.15 probability to mutate. To mutate a child, uniformly pick a gene to give a new uniformly-chosen value in the range of [1..10](). For illustration, the example child c is being considered for mutation. After receiving a value of 0.12 from a random number generator from the range of [0.0, 1.0](), c will be mutated since 0.12 is less than or equal to the mutation probability threshold of 0.15. Again, we consult the random number generator to select a gene from the range of [1..3]() which results in gene 3. We then ask the random number generator for a new value for gene 3 from the range of [1..10]() which results in 9. After replacing gene 3 with the value 9, the newly-mutated c now has the genotype of \< 1, 5, 9 \>.


