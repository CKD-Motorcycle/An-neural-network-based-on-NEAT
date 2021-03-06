import math
import random

	

class Neuron(object):
	def __init__(self, number_of_inputs):
		self.number_of_inputs = number_of_inputs + 1
		self.weights = []
		
		for i in range(self.number_of_inputs):
			self.weights.append(random.uniform(-1,1))
			
	def number_of_weights(self):
		return len(self.weights)
		

	def activation_value(self, inputs):
		result = 0;
		
		for i in range(self.number_of_inputs):
			result = result + (inputs[i] * self.weights[i])
		
		return result
			 
		
		
		
class Layer(object):
	def __init__(self, number_of_neurons, inputs_per_neuron):
		self.neurons = []
		
		for i in range(number_of_neurons):
			self.neurons.append(Neuron(inputs_per_neuron))				
		
						
class Network(object):
	def __init__(self, number_of_inputs, number_of_outputs, number_of_hidden_layers, neurons_per_hidden_layer):
		self.number_of_inputs = number_of_inputs
		self.number_of_outputs = number_of_outputs
		self.number_of_hidden_layers = number_of_hidden_layers
		self.neurons_per_hidden_layer = neurons_per_hidden_layer
		self.layers = []
		
	def create_net(self):
		if self.number_of_hidden_layers > 0:
			
			# first hidden layer
			layer = Layer(self.neurons_per_hidden_layer, self.number_of_inputs)
			self.layers.append(layer)
			
			# rest of the hidden layers
			for i in range(self.number_of_hidden_layers-1):
				layer = Layer(self.neurons_per_hidden_layer, self.neurons_per_hidden_layer)
				self.layers.append(layer)
				
			# output layer	
			self.layers.append(Layer(self.number_of_outputs, self.neurons_per_hidden_layer))
		
		else:
			self.layers.append(Layer(self.number_of_outputs, self.number_of_inputs))
		
	def get_weights(self):
		weights = []
		
		for layer in self.layers:
			for neuron in layer.neurons:
				for weight in neuron.weights:
					weights.append(weight)
		
		return weights
					
		
	def get_number_of_weights(self):
		total = 0
		
		for layer in self.layers:
			for neuron in layer.neurons:
				total = total + neuron.number_of_weights()
		
		return total
		
		
	def put_weights(self, weights):
		i = 0
		for layer in self.layers:
			for neuron in layer.neurons:
				for (j, weight) in enumerate(neuron.weights):
					neuron.weights[j] = weights[i]
					i = i + 1
			
			
								
		
	def sigmoid(self, activation):
		return (float) (1/(1 + math.exp(-activation)))
		

	def update(self, inputs):
		outputs = []
		
		if len(inputs) != self.number_of_inputs:
			return outputs
			
		#for each layer
		for layer_index, layer in enumerate(self.layers):
			if layer_index > 0:
				inputs = outputs
			
			outputs= []
			
			for neuron in layer.neurons:
				net_input = 0
				
				for (index, value) in enumerate(inputs):
					net_input = float(net_input) + (float(neuron.weights[index]) * float(value))
				
				# add bias
				net_input = net_input + (neuron.weights[-1]	* -1)
				
				output = self.sigmoid(net_input)
				outputs.append(output)
					
		
		return outputs
					

		

		

