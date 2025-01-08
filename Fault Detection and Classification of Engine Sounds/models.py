#Import necessary libraries
from tensorflow.keras.models import Model
from tensorflow.keras import layers, models
from keras.layers import *

#Return one of the three CNN model variations
def return_CNN_model(model_name, input_shape, filter_num, class_num):
    if model_name == "lenet5":
        model = lenet5(input_shape, filter_num, class_num)
    elif model_name == "three_layer_alt":
        model = three_layer_alt(input_shape, filter_num, class_num)
    elif model_name == "vgg":
        model = vgg(input_shape, class_num)

    return model

#Implementation of a LeNet5 inspired model
def lenet5(input_shape, filter_num, class_num):
    model = models.Sequential([
        Input(shape=input_shape),
        Conv2D(filter_num[0], kernel_size=(3, 3), activation='relu', padding='same'),
        BatchNormalization(),
        MaxPooling2D(pool_size=(2, 2),strides=2),
        Dropout(0.2),
        Conv2D(filter_num[1], kernel_size=(5, 5), activation='relu'),
        BatchNormalization(),
        MaxPooling2D(pool_size=(2, 2),strides=2),
        Dropout(0.2),
        GlobalAveragePooling2D(),
        Dense(16, activation="relu"),
        BatchNormalization(),
        Dropout(0.2),
        Dense(class_num, activation="softmax")
    ])

    return model

#Implementation of the TLA model
def three_layer_alt(input_shape, filter_num, class_num):
    model = models.Sequential([
        Input(shape=input_shape),
        Conv2D(filter_num[0], kernel_size=(3, 3), activation='relu'),
        BatchNormalization(),
        MaxPooling2D(pool_size=(2, 2),strides=2),
        Dropout(0.2),
        Conv2D(filter_num[1], kernel_size=(3, 3), activation='relu'),
        BatchNormalization(),
        MaxPooling2D(pool_size=(2, 2),strides=2),
        Dropout(0.2),
        Conv2D(filter_num[2], kernel_size=(3, 3), activation='relu'),
        BatchNormalization(),
        MaxPooling2D(pool_size=(2, 2),strides=2),
        Dropout(0.2),
        GlobalAveragePooling2D(),
        Dense(16, activation="relu"),
        BatchNormalization(),
        Dropout(0.2),
        Dense(class_num, activation="softmax")
    ])

    return model

#Implementation of a VGG inspired model
def vgg(input_shape, class_num):
    model = models.Sequential([
        Input(shape=input_shape),
        Conv2D(16, kernel_size=(3, 3), activation='relu', padding='same'),
        Conv2D(16, kernel_size=(3, 3), activation='relu', padding='same'),
        BatchNormalization(),
        MaxPooling2D(pool_size=(2, 2),strides=2),
        Dropout(0.2),
        Conv2D(32, kernel_size=(3, 3), activation='relu'),
        Conv2D(32, kernel_size=(3, 3), activation='relu'),
        BatchNormalization(),
        MaxPooling2D(pool_size=(2, 2),strides=2),
        Dropout(0.2),
        GlobalAveragePooling2D(),
        Dense(16, activation="relu"),
        BatchNormalization(),
        Dropout(0.2),
        Dense(class_num, activation="softmax")
    ])

    return model

#Implementation of a standard feed-forward ANN
def return_ANN_model(input_shape, filter_num, class_num):
    model = models.Sequential([
        Input(shape=input_shape),
        Dense(filter_num[0], activation="relu"),
        Dense(filter_num[1], activation="relu")
    ])

    if len(filter_num) == 3:
        model.add(layers.Dense(filter_num[2], activation="relu")),

    model.add(layers.Flatten()),
    model.add(layers.Dense(class_num, activation="softmax"))

    return model

#Source [55]
#Implementation of the SNN
def return_SNN_model(input_shape, filter_num):
    model = models.Sequential([
        Input(shape=(64,88,3)),
        Conv2D(filter_num[0], kernel_size=(2, 2), activation='relu', padding='same'),
        BatchNormalization(),
        MaxPooling2D(pool_size=(2, 2)),
        Dropout(0.2),
        Conv2D(filter_num[1], kernel_size=(2, 2), activation='relu', padding='same'),
        BatchNormalization(),
        MaxPooling2D(pool_size=(2, 2)),
        Dropout(0.2),
        GlobalAveragePooling2D(),
        Dense(filter_num[2]),
    ])
    
    return model
#End of source [55]

