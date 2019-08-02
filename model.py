import numpy as np

class model():
    def __init__(self):
        self.color = np.random.choice(range(256), size=3)
        self.data = [[110, 112, 102, 1, 0], [99, 82, 100, 0, 1]]
        self.z_vectors = []
        self.activation_vectors = []
        # number of nodes by layer 
        self.node_count = [3, 3, 3, 2]
        self.weights = []
        self.bias = []
        for i in range(len(self.node_count) - 1):
            self.weights.append(np.random.rand(self.node_count[i + 1], self.node_count[i]))
            self.bias.append(np.random.rand(self.node_count[i + 1], 1))

    def recieve_data(self, data):
        entry = self.color.tolist() + data
        self.data.append(entry)
        self.color = np.random.choice(range(256), size=3)
        self.train(self.weights, self.bias)
        return self.color

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def dsig(self, z):
        return self.sigmoid(z) * (1 - self.sigmoid(z))
        
    def NN(self, value, weights, bias):
        z = self.sigmoid(value)
        self.activation_vectors, self.z_vectors = [], []
        self.activation_vectors.append(z)
        for i in range(len(self.node_count) - 1):
            self.z_vectors.append(np.asarray([weights[i] @ z + bias[i]]))
            self.activation_vectors.append(self.sigmoid(self.z_vectors[i]))
        return self.activation_vectors[-1]

    def train(self, weights, bias):
        idx = np.random.choice(len(self.data))
        tdata = self.data[idx]
        rgb = self.sigmoid(np.asarray(tdata[0:3]).reshape(-1, 1))
        targets = tdata[3:5]

        self.error_signal_vectors = []
        
        predictions = self.NN(rgb, weights, bias)

        error_signal = []
        # Get error signals of last layer 
        for i in range(len(predictions)):
            dcost = 2 * (predictions[i] - targets[i])
            # Get error signal of specfic node
            err_sig = dcost * self.dsig(self.z_vectors[-1][i])
            # Add to list for this layer
            error_signal.append(err_sig)
        
        self.error_signal_vectors.append(np.asarray(error_signal).reshape(-1, 1))
        
        # Find error signals for previous layers
        for i in range(len(self.node_count) - 2):
            next_err_v = self.weights[-(i + 1)].transpose() @ self.error_signal_vectors[i]
            self.error_signal_vectors.append(next_err_v)
        
        # Build change in weight matrices
        dweights = []
        for i in range(len(self.node_count) - 1):
            matrix = self.error_signal_vectors[i] @ self.activation_vectors[-(i + 2)].reshape(1, -1)
            dweights.append(np.asarray(matrix))

        # Update weights and biases
        for i in range(len(self.node_count) - 1):
            self.weights[-(i + 1)] -= dweights[i]
            self.bias[-(i + 1)] -= self.error_signal_vectors[i]

    def test(self):
        return None