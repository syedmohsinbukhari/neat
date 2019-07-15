"""
Description: Get started with TensorFlow 2.0 for experts
author: syedmohsinbukhari@googlemail.com

- Prepare dataset
- Select an optimizer
- Define the loss functions
- Train the neural net
- Test the neural net

Reference
https://www.tensorflow.org/beta/tutorials/quickstart/advanced
"""
# Import TensorFlow into your program

from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf

from tensorflow.keras.layers import Dense, Flatten, Conv2D
from tensorflow.keras import Model


# Build the tf.keras model using the Keras model subclassing API:
class MyModel(Model):
    def __init__(self):
        super(MyModel, self).__init__()
        self.conv1 = Conv2D(32, 3, activation='relu')
        self.flatten = Flatten()
        self.d1 = Dense(128, activation='relu')
        self.d2 = Dense(10, activation='softmax')

    def call(self, x):
        x = self.conv1(x)
        x = self.flatten(x)
        x = self.d1(x)
        return self.d2(x)


class MNISTExample:
    @staticmethod
    def load_and_prepare_data():
        # Load and prepare the MNIST dataset
        mnist = tf.keras.datasets.mnist

        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        x_train, x_test = x_train / 255.0, x_test / 255.0

        return (x_train, y_train), (x_test, y_test)

    @staticmethod
    def add_a_channel_dimension(x_train, x_test):
        # Add a channels dimension
        x_train = x_train[..., tf.newaxis]
        x_test = x_test[..., tf.newaxis]

        return x_train, x_test

    @staticmethod
    def batch_and_shuffle(x_train, y_train, x_test, y_test):
        # Use tf.data to batch and shuffle the dataset
        train_ds = tf.data.Dataset.from_tensor_slices(
            (x_train, y_train)).shuffle(10000).batch(32)
        test_ds = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(32)

        return train_ds, test_ds

    @staticmethod
    def make_model_object():  # better not use this function
        model = MyModel()
        return model

    @staticmethod
    def optimizer_and_loss_function():
        # Choose an optimizer and loss function for training
        loss_object = tf.keras.losses.SparseCategoricalCrossentropy()
        optimizer = tf.keras.optimizers.Adam()
        return loss_object, optimizer

    @staticmethod
    def define_metrics():
        # Select metrics to measure the loss and the accuracy of the model.
        # These metrics accumulate the values over epochs and then print the overall result.
        train_loss = tf.keras.metrics.Mean(name='train_loss')
        train_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name='train_accuracy')

        test_loss = tf.keras.metrics.Mean(name='test_loss')
        test_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name='test_accuracy')

        return train_loss, train_accuracy, test_loss, test_accuracy

    # Use tf.GradientTape to train the model
    @staticmethod
    @tf.function
    def train_step(images, labels, model, loss_object, optimizer, train_loss, train_accuracy):
        with tf.GradientTape() as tape:
            predictions = model(images)
            loss = loss_object(labels, predictions)
        gradients = tape.gradient(loss, model.trainable_variables)
        optimizer.apply_gradients(zip(gradients, model.trainable_variables))

        train_loss(loss)
        train_accuracy(labels, predictions)

    # Test the model
    @staticmethod
    @tf.function
    def test_step(images, labels, model, loss_object, test_loss, test_accuracy):
        predictions = model(images)
        t_loss = loss_object(labels, predictions)

        test_loss(t_loss)
        test_accuracy(labels, predictions)

    @staticmethod
    def process(epochs, model, train_ds, test_ds, train_loss, train_accuracy, test_loss, test_accuracy):
        # Finally run the code
        for epoch in range(epochs):
            for images, labels in train_ds:
                MNISTExample.train_step(images, labels, model, loss_object, optimizer, train_loss, train_accuracy)

            for test_images, test_labels in test_ds:
                MNISTExample.test_step(test_images, test_labels, model, loss_object, test_loss, test_accuracy)

            template = 'Epoch {}, Loss: {}, Accuracy: {}, Test Loss: {}, Test Accuracy: {}'
            print(template.format(epoch + 1,
                                  train_loss.result(),
                                  train_accuracy.result() * 100,
                                  test_loss.result(),
                                  test_accuracy.result() * 100))


if __name__ == '__main__':
    EPOCHS = 5

    (x_train, y_train), (x_test, y_test) = MNISTExample.load_and_prepare_data()

    x_train, x_test = MNISTExample.add_a_channel_dimension(x_train, x_test)

    train_ds, test_ds = MNISTExample.batch_and_shuffle(x_train, y_train, x_test, y_test)

    model = MNISTExample.make_model_object()

    loss_object, optimizer = MNISTExample.optimizer_and_loss_function()

    train_loss, train_accuracy, test_loss, test_accuracy = MNISTExample.define_metrics()

    MNISTExample.process(EPOCHS, model, train_ds, test_ds, train_loss, train_accuracy, test_loss, test_accuracy)
