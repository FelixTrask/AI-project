# neuron.py
from math import exp
import random
# import numpy as np

class Neuron:
  def __init__(self, num_inputs, weights=None, bias=None):
    self.num_inputs = num_inputs
    if weights is None:
      self.weights = []
      for _ in range(num_inputs):
        self.weights.append(random.random() - 0.5)
    else:
      self.weights = weights.copy()

    if bias is None:
      self.bias = random.random() - 0.5
    else:
      self.bias = bias

  def clone(self):
    # Create a copy of this neuron with the same weights and bias
    return Neuron(self.num_inputs, weights=self.weights, bias=self.bias)

  def mutate(self, mr):
    # Mutate the weights and bias with a given mutation rate (mr)
    for i in range(self.num_inputs):
      if random.random() < mr:
        self.weights[i] += random.random() - 0.5
    if random.random() < mr:
      self.bias += random.random() - 0.5
      
  # def mutate(self, mr):
  #     self.bias += (random.random() - 0.5) * mr
  #     for i in range(len(self.weights)):
  #         if random.random() < mr:
  #             self.weights[i] += (random.random() - 0.5) * mr

  def feed_forward(self, inputs):
    # ACTIVATION FUNCTION
    # SIGMOID
    # 1 / (1 + e^(-X))
    # X = SUM(WI * XI) + BIAS
    # XI: INPUT
    # WI: WEIGHT
    # BIAS: BIAS
    x = sum([w * i for w, i in zip(self.weights, inputs)]) + self.bias
    x = max(min(x, 20), -20)
    return 1 / (1 + exp(-x))

  def crossover(self, other):
    # Create a new neuron by combining weights and bias from two parent neurons
    new_weights = []
    for i in range(self.num_inputs):
      if random.random() < 0.5:
        new_weights.append(self.weights[i])
      else:
        new_weights.append(other.weights[i])

    if random.random() < 0.5:
      new_bias = self.bias
    else:
      new_bias = other.bias

    #  Return a new neuron with the combined weights and bias
    return Neuron(self.num_inputs, weights=new_weights, bias=new_bias)