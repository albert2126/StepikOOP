class Layer:
    def __init__(self):
        self.name = 'Layer'
        self.next_layer = None

    def __call__(self, layer):
        self.next_layer = layer
        return self.next_layer


class Input(Layer):
    def __init__(self, inputs: int):
        super().__init__()
        self.name = 'Input'
        self.inputs = inputs


class Dense(Layer):
    def __init__(self, inputs: int, outputs: int, activation: str):
        super().__init__()
        self.name = 'Dense'
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation


class NetworkIterator:
    def __init__(self, top_layer: Layer):
        self.top = top_layer

    def __iter__(self):
        lr = self.top
        while lr:
            yield lr
            lr = lr.next_layer


# Test:
network = Input(128)
layer = network(Dense(network.inputs, 1024, 'linear'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))
for x in NetworkIterator(network):
    print(x.name)

# Test 2:
nt = Input(12)
layer = nt(Dense(nt.inputs, 1024, 'relu'))
layer = layer(Dense(layer.inputs, 2048, 'relu'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))

n = 0
for x in NetworkIterator(nt):
    assert isinstance(x, Layer), "итератор должен возвращать объекты слоев с базовым классом Layer"
    n += 1

assert n == 4, "итератор перебрал неверное число слоев"
