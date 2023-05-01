import os
import time

import numpy as np
import tensorflow.keras as tk
import tensorflow.keras.layers as l

from matplotlib import pyplot as plt


def plot_accuracy(history):
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'valid'], loc='upper left')
    plt.show()


def plot_loss(history):
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'valid'], loc='upper left')
    plt.show()


training_time = {}


class Timer():
    def __init__(self, name, time_dict: dict = {}):
        self.start = time.time()
        self.name = name
        self.time_dict = time_dict

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.interval = self.end - self.start
        self.time_dict[self.name] = self.interval


def plot_accuracy_and_loss(history):
    def plot_accuracy(history, ax=None):
        ax.plot(history.history['accuracy'])
        ax.plot(history.history['val_accuracy'])
        ax.set_title('model accuracy')
        ax.set_ylabel('accuracy')
        ax.set_xlabel('epoch')
        ax.legend(['train', 'valid'], loc='upper left')

    def plot_loss(history, ax=None):
        ax.plot(history.history['loss'])
        ax.plot(history.history['val_loss'])
        ax.set_title('model loss')
        ax.set_ylabel('loss')
        ax.set_xlabel('epoch')
        ax.legend(['train', 'valid'], loc='upper left')

    fig, ax = plt.subplots(1, 2, figsize=(15, 5))
    plot_accuracy(history, ax[0])
    plot_loss(history, ax[1])
    plt.show()


def plot_comparison(histories, legends):
    fig, ax = plt.subplots(1, 2, figsize=(15, 5))
    for history in histories:
        ax[0].plot(history.history['val_accuracy'])

    # setting the sub-title and labels
    ax[0].set_title('models accuracy')
    ax[0].set_ylabel('Accuracy')
    ax[0].set_xlabel('epoch')
    ax[0].legend(legends, loc='upper left')

    for history in histories:
        ax[1].plot(history.history['val_loss'])

    ax[1].set_title('models loss')
    ax[1].set_ylabel('Loss')
    ax[1].set_xlabel('epoch')
    ax[1].legend(legends, loc='upper left')

    plt.show()


from keras_tuner.tuners import RandomSearch


class MyTuner(RandomSearch):
    def run_trial(self, trial, *args, **kwargs):
        kwargs['batch_size'] = trial.hyperparameters.Int('batch_size', 32, 128, step=32)
        return super(MyTuner, self).run_trial(trial, *args, **kwargs)


# turing the learning rate, dropout rate and batch size
def build_model(hp):
    model = tk.Sequential([
        l.Flatten(input_shape=[32, 32, 3]),
        l.Dense(128, activation="relu"),
        l.Dense(64, activation="relu"),
        l.Dropout(hp.Choice('dropout', values=[.2, .3, .5], )),
        l.Dense(10, activation="softmax")
    ])

    optimizer = tk.optimizers.SGD(learning_rate=hp.Float('learning_rate', 1e-4, 1e-2, sampling='log', default=1e-3))
    model.compile(loss="sparse_categorical_crossentropy", optimizer=optimizer, metrics=["accuracy"])
    return model


def get_test_accuracies(models, models_names, X_test, y_test):
    accuracies = [model.evaluate(X_test, y_test)[1] for model in models]
    test_accuracy = dict(zip(models_names, accuracies))
    return dict(sorted(test_accuracy.items(), key=lambda item: item[1]))


def plot_test_accuracies(test_accuracy):
    plt.figure(figsize=(10, 5))
    plt.barh(list(test_accuracy.keys()), test_accuracy.values())

    show_value_on_bar(test_accuracy)

    plt.xlabel("accuracy")
    plt.ylabel("model")
    plt.title("test accuracy of all models")
    plt.show()


def plot_training_time_comparations(training_times):
    training_times = dict(sorted(training_times.items(), key=lambda item: item[1], reverse=True))

    plt.barh(list(training_times.keys()), training_times.values())

    show_value_on_bar(training_times)

    plt.title("training time")
    plt.xlabel("time (s)")
    plt.ylabel("model")

    plt.title("training time of all models")
    plt.show()


def show_value_on_bar(a_dict: dict):
    for index, value in enumerate(a_dict.values()):
        plt.text(value, index, f'{value:.3f}')


def sub_percentage_of(X, y, percentage=0.1):
    sub_size = int(len(X) * percentage)
    return X[:sub_size], y[:sub_size]


def reduce_dataset_size_if_working_locally():
    global X_train, y_train, X_valid, y_valid, X_test, y_test
    # if i'm not in kaggle or colab, i'm working locally
    if not os.path.exists('/kaggle/working') and not os.path.exists('/content'):
        X_train, y_train = sub_percentage_of(X_train, y_train, 0.1)
        X_valid, y_valid = sub_percentage_of(X_valid, y_valid, 0.1)
        X_test, y_test = sub_percentage_of(X_test, y_test, 0.1)


def plot_sample_images(X, y, labels, number_of_samples=6):
    def get_label_name(i: int):
        return labels[i]

    data_iter = iter(X)
    fig = plt.figure(figsize=(7, 8))
    for x in range(number_of_samples):
        image = next(data_iter)
        label = y[x][0]
        n_row = int(np.floor(np.sqrt(number_of_samples)))
        n_col = int(np.ceil(number_of_samples / n_row))
        fig.add_subplot(n_row, n_col, x + 1)
        plt.imshow(image)
        plt.axis('off')
        plt.title(get_label_name(label))
    plt.show()
