"""
Description: Implementation of backpropagation algorithm in python
Author: bazarovay@github

Partial derivative of cost function with respect to weight/biases
Shows how cost changes with respect to w/b

How changing weight changes the overall behaviour
w^l(jk) : weight for k to j neuron connection. j at lth layer
b^l(j) : bias at layer l for jth neuron
a^l(j) : activation at layer l for jth neuron

activation at layer l is related to activations in l-1

alj=σ(∑kwljkal−1k+blj)

a^l=σ(w^l*a^(l−1)+b^l)

weighted output : w^l*a^(l−1)+b^
we just apply the weight matrix to the activations, then add the bias vector,
and finally apply the σ function*

The goal of backpropagation is to compute the partial derivatives


Assumptions about the cost function in order that backpropagation
can be applied
1. Cost function can be written as average

we need this assumption is because what backpropagation actually lets us do is
compute the partial derivatives ∂Cx/∂w and ∂Cx/∂b for a single training
example. We then recover ∂C/∂w and ∂C/∂b by averaging over training examples

2. C can be written as a function of the outputs from the neural network
Is a function of output activations

Hadamard/Schur product s⊙t where s and t are vectors of the same dim

4 fundamental equations behind backprop

"""
