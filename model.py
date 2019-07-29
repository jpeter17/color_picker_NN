import numpy as np

class model():
    def __init__(self):
        self.color = np.random.choice(range(256), size=3)
        self.data = []

    def recieve_data(self, data):
        entry = self.color.tolist() + data
        print(entry)
        self.data.append(entry)
        self.color = np.random.choice(range(256), size=3)
        return self.color
        
    def NN():
        return None