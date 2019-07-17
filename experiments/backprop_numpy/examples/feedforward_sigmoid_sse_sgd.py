"""
Description: Numpy implementation of feed forward neural networks and
             and backpropagation shown through IRIS example
author: syedmohsinbukhari@googlemail.com
"""

from numpy import shape
from sklearn.utils import shuffle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from experiments.backprop_numpy.models_sequential import FeedForwardModel
from experiments.backprop_numpy.losses import SSELoss
from experiments.backprop_numpy.optimizers import SGD

EPOCHS = 20
LEARNING_RATE = 0.1
NEURON_CONFIG = [4, 2, 1]
TRAIN_TEST_SPLIT = 0.33
DATA_SAMPLE_SIZE = 100

# Load data
iris_data = load_iris()
data_features = iris_data['data'][:DATA_SAMPLE_SIZE]
data_targets = iris_data['target'][:DATA_SAMPLE_SIZE]

# Shuffle data
X, y = shuffle(data_features, data_targets)

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TRAIN_TEST_SPLIT)

# Make a feed forward model, loss and optimizer
model = FeedForwardModel(NEURON_CONFIG)
loss_obj = SSELoss()
optimizer = SGD(LEARNING_RATE, model)

# Train the model
for epoch in range(EPOCHS):
    loss_arr = []
    prediction_arr = []
    loss_test_arr = []
    prediction_test_arr = []

    # Train Loop
    for i in range(shape(X_train)[0]):
        # Reshape data for training
        X_i = X_train[i].reshape((NEURON_CONFIG[0], 1))
        y_i = y_train[i].reshape((1, 1))

        # Forward pass
        t_i = model.forward(X_i, with_grads=True)
        p_i = 1.0 if t_i > 0.5 else 0.0

        # Compute loss
        loss_val = loss_obj.forward(y_i, t_i)

        # Backward pass
        model.backward(loss_obj)

        # Apply gradients
        optimizer.apply_grads()

        # Clear gradients
        model.clear_grads()

        # Store loss and correct prediction values
        loss_arr.append(loss_val)
        prediction_arr.append(1.0 if all(p_i == y_i) else 0.0)

    # Test Loop
    for i in range(shape(X_test)[0]):
        # Reshape data for training
        X_i = X_test[i].reshape((NEURON_CONFIG[0], 1))
        y_i = y_test[i].reshape((1, 1))

        # Forward pass
        t_i = model.forward(X_i, with_grads=False)
        p_i = 1.0 if t_i > 0.5 else 0.0

        # Compute loss
        loss_val = loss_obj.forward(y_i, t_i)

        # Store loss and correct prediction values
        loss_test_arr.append(loss_val)
        prediction_test_arr.append(1.0 if all(p_i == y_i) else 0.0)

    print(f"EPOCH: {epoch}, "
          f"TRAIN_LOSS: {sum(loss_arr)/len(loss_arr)}, "
          f"TRAIN_ACCURACY: {sum(prediction_arr)/len(prediction_arr)}, "
          f"TEST_LOSS: {sum(loss_test_arr)/len(loss_test_arr)}, "
          f"TEST_ACCURACY: {sum(prediction_test_arr)/len(prediction_test_arr)}")
