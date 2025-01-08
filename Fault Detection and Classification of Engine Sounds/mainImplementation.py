#Import necessary libraries
import os
import keras
import matplotlib.pyplot as plt
from keras import callbacks

#Import all other external functions
from dataPreparation import *
from models import *
from directories import *
from recordResults import *
from experiments import *


#Functions for the three different classification experiments

#Binary classification of normal or faulty data
def binary_classification(dataset):
    #Return the directories of the data
    #Using function in Directories.ipynb
    folder_dir, normal_data, fault_data = return_dir(dataset, 'binary')

    #Initalise arrays for images and labels
    norm_images, norm_labels, fault_images, fault_labels = ([] for i in range(4))

    #Iterate through dataset folders of both normal and faulty data
    #Prep the data using transformation functions in Data_Preparation.ipynb
    for i in range(len(normal_data)):
        dir = folder_dir + normal_data[i]
        for file in os.listdir(dir):
            images, labels = data_preparation((dir + '\\' + file), 0, dataset)
            norm_images += images
            norm_labels += labels

    for i in range(len(fault_data)):
        dir = folder_dir + fault_data[i]
        for file in os.listdir(dir):
            images, labels = data_preparation((dir + '\\' + file), 1, dataset)
            fault_images += images
            fault_labels += labels

    #Create train, test and validation data from function in Data_Preparation.ipynb
    train_images, train_labels, test_images, test_labels, val_images, val_labels = return_split((norm_images+fault_images),
                                                                                                (norm_labels+fault_labels), 
                                                                                                'binary')

    return train_images, train_labels, test_images, test_labels, val_images, val_labels

#Multi-class classification of the three datasets
def dataset_classification():
    #Import all required directories 
    folder_dir, CWRU_dir, HIT_dir, XJTU_SY_dir = return_dir('all', 'dataset')

    #Initalize image and label arrays for each dataset
    CWRU_images, CWRU_labels, HIT_images, HIT_labels, XJTU_SY_images, XJTU_SY_labels = ([] for i in range(6))

    #Iterate through dataset folders
    #Prep the data using transformation functions in Data_Preparation.ipynb
    for i in range(len(CWRU_dir)):
        for file in os.listdir(folder_dir + CWRU_dir[i]):
            dir = folder_dir + CWRU_dir[i] + '\\' + file
            label = 'CWRU'
            images, labels = data_preparation(dir, label, 'CWRU')
            CWRU_images += images
            CWRU_labels += labels

    for i in range(len(HIT_dir)):
        for file in os.listdir(folder_dir + HIT_dir[i]):
            dir = folder_dir + HIT_dir[i] + '\\' + file
            label = 'HIT'
            images, labels = data_preparation(dir, label, 'HIT')
            HIT_images += images
            HIT_labels += labels

    for i in range(len(XJTU_SY_dir)):
        for file in os.listdir(folder_dir + XJTU_SY_dir[i]):
            dir = folder_dir + XJTU_SY_dir[i] + '\\' + file
            label = 'XJTU'
            images, labels = data_preparation(dir, label, 'XJTU_SY')
            XJTU_SY_images += images
            XJTU_SY_labels += labels

    #Create train, test and validation data from function in Data_Preparation.ipynb
    train_images, train_labels, test_images, test_labels, val_images, val_labels = return_split((CWRU_images+HIT_images+XJTU_SY_images), 
                                                                                                (CWRU_labels+HIT_labels+XJTU_SY_labels), 
                                                                                                'dataset')

    return train_images, train_labels, test_images, test_labels, val_images, val_labels

#Multi-class classification of types of bearings
def bearing_classification(dataset):
    #Return the directories of the data
    folder_dir, normal_data, inner_data, outer_data = return_dir(dataset, 'bearing')

    #Initalise arrays for images and labels
    norm_images, norm_labels, inner_images, inner_labels, outer_images, outer_labels = ([] for i in range(6))

    #Iterate through dataset folders of both normal and faulty data
    #Prep the data using transformation functions in Data_Preparation.ipynb
    for i in range(len(normal_data)):
        dir = folder_dir + normal_data[i]
        for file in os.listdir(dir):
            label = 'normal'
            images, labels = data_preparation((dir + '\\' + file), label, dataset)
            norm_images += images
            norm_labels += labels

    for i in range(len(inner_data)):
        dir = folder_dir + inner_data[i]
        for file in os.listdir(dir):
            label = 'inner'
            images, labels = data_preparation((dir + '\\' + file), label, dataset)
            inner_images += images
            inner_labels += labels

    for i in range(len(outer_data)):
        dir = folder_dir + outer_data[i]
        for file in os.listdir(dir):
            label = 'outer'
            images, labels = data_preparation((dir + '\\' + file), label, dataset)
            outer_images += images
            outer_labels += labels

    #Create train, test and validation data from function in Data_Preparation.ipynb
    train_images, train_labels, test_images, test_labels, val_images, val_labels = return_split((norm_images+inner_images+outer_images), 
                                                                                                           (norm_labels+inner_labels+outer_labels), 
                                                                                                           'bearing')

    return train_images, train_labels, test_images, test_labels, val_images, val_labels


#Functions for the both implementation types

def single_subnetwork_implementation(train_images, train_labels, test_images, test_labels, val_images, val_labels, experiment):
    #Store the shape of the image arrays
    input_shape = train_images[0].shape

    #Set the loss function and number of classes depending on the experiment being run
    if experiment[3] == 'binary':
        loss_function = 'binary_crossentropy'
        classes = 2
    else:
        loss_function = 'categorical_crossentropy'
        classes = 3
    
    #Import chosen model from Models.ipynb
    if experiment[4][0:3] == "CNN":
        model = return_CNN_model(experiment[0], input_shape, experiment[1], classes)
    else:
        model = return_ANN_model(input_shape, experiment[1], classes)
    
    #Calculate class weights using function in Data_Preparation.ipynb
    class_weights = calculate_class_weights(train_labels)

    #Compile model
    model.compile(optimizer = keras.optimizers.Adam(), loss = loss_function, metrics = [keras.metrics.Accuracy()])
    
    #Train the model
    history = model.fit(train_images, train_labels, batch_size = 32, epochs = 100, verbose = 0,
                        validation_data = (val_images, val_labels), shuffle = False, class_weight = class_weights)

    #Evaluation of the model on the test set
    test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=0)

    plt.ioff()
    #Create and save plots for the accuracy and loss results from training
    acc_fig = plot_graph(history.history['accuracy'], history.history['val_accuracy'], 'accuracy')
    acc_fig_dir = '**File Directory**' + experiment[4]
    plt.savefig(acc_fig_dir)
    
    loss_fig = plot_graph(history.history['loss'], history.history['val_loss'], 'loss')
    loss_fig_dir = '**File Directory**' + experiment[5]
    plt.savefig(loss_fig_dir)

    #Add final accuracies and losses to a spreadsheet
    save_to_spreadsheet(experiment[2], history, test_loss, test_acc)


def multi_subnetwork_implementation(train_images, train_labels, test_images, test_labels, val_images, val_labels, experiment):
    #Removes a quarter of the data for dataset experiments
    if experiment[3] == "dataset":
        train_images, train_labels = train_images[:int(len(train_images)/4)], train_labels[:int(len(train_labels)/4)]
        test_images, test_labels = test_images[:int(len(test_images)/4)], test_labels[:int(len(test_labels)/4)]
        val_images, val_labels = val_images[:int(len(val_images)/4)], val_labels[:int(len(val_labels)/4)]

    #Source [55]
    #Create pairs for train,test and validation sets
    (pairTrain, labelTrain) = make_pairs(train_images, train_labels)
    (pairTest, labelTest) = make_pairs(test_images, test_labels)

    input_shape = train_images[0].shape
    #Create two inputs for each subnetwork
    image1 = Input(shape = input_shape)
    image2 = Input(shape = input_shape)

    #Configure the SNN
    featureExtractor = return_SNN_model(input_shape, experiment[1])
    feats1 = featureExtractor(image1)
    feats2 = featureExtractor(image2)

    #Complete the construction of the SNN
    distance = Lambda(euclidean_distance)([feats1, feats2])
    outputs = Dense(1, activation="sigmoid")(distance)
    model = Model(inputs=[image1, image2], outputs=outputs)
    #End of Source [55]

    #Calculate class weights using function in Data_Preparation.ipynb
    class_weights = calculate_class_weights(train_labels)

    #Compile model
    model.compile(optimizer = keras.optimizers.Adam(), loss = "binary_crossentropy", metrics = [keras.metrics.Accuracy()])
    
    #Train the model
    history = model.fit([pairTrain[:,0], pairTrain[:,1]], labelTrain[:], validation_data=([pairTest[:,0], pairTest[:,1]], labelTest[:]),
                         batch_size=32, epochs=100, verbose=0, shuffle=False, class_weight = class_weights)

    plt.ioff()
    #Create and save plots for the accuracy and loss results from training
    acc_fig = plot_graph(history.history['accuracy'], history.history['val_accuracy'], 'accuracy')
    acc_fig_dir = '**File Directory**' + experiment[4]
    plt.savefig(acc_fig_dir)
    
    loss_fig = plot_graph(history.history['loss'], history.history['val_loss'], 'loss')
    loss_fig_dir = '**File Directory**' + experiment[5]
    plt.savefig(loss_fig_dir)

    #Add final accuracies and losses to a spreadsheet
    save_to_spreadsheet(experiment[2], history, "N/A", "N/A")


if __name__ == "__main__":
    #Number for experiment must be changed manually
    #exp_num = integer_value
    experiment = return_experiment_array(exp_num)

    #Uses experiment list to determine which experiment and executes corresponding data preparation function
    if experiment[3] == "binary":
        train_images, train_labels, test_images, test_labels, val_images, val_labels = binary_classification(experiment[2])
    elif experiment[3] == "dataset":
        train_images, train_labels, test_images, test_labels, val_images, val_labels = dataset_classification()
    elif experiment[3] == "bearing":
        train_images, train_labels, test_images, test_labels, val_images, val_labels = bearing_classification(experiment[2])

    #Uses experiment list to determine which subnetwork implementation needs to be executed
    if experiment[4][0:3] == "CNN" or experiment[4][0:3] == "ANN":
        single_subnetwork_implementation(train_images, train_labels, test_images, test_labels, val_images, val_labels, experiment)
    elif array[4][0:3] == "SNN":
        multi_subnetwork_implementation(train_images, train_labels, test_images, test_labels, val_images, val_labels, experiment)
    
