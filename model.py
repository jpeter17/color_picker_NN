import numpy as np

class model():
    def __init__(self):
        self.color = np.random.choice(range(256), size=3)
        self.data = []
        self.hidden_layer = 2
        self.weights = []
        self.bias = []
        for i in range(self.hidden_layer):
            self.weights.append(np.random.rand(3, 3))
            self.bias.append(np.random.rand(1, 3))
        self.weights.append(np.random.rand(3, 2))
        self.bias.append(np.random.rand(1, 2))

    def recieve_data(self, data):
        entry = self.color.tolist() + data
        print(entry)
        self.data.append(entry)
        self.color = np.random.choice(range(256), size=3)
        return self.color

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))
        
    def NN(self, value, weights, bias):
        z = (1 / 255) * value
        for i in range(self.hidden_layer + 1):
            z = z @ weights[i] + bias[i]
            z = self.sigmoid(z)
        
        print(z[0][0])
        print(z[0][1])
        return z

    def test(self):
        print(self.NN(self.color, self.weights, self.bias))