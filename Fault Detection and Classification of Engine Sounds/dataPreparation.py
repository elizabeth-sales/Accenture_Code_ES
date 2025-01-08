#Import necessary libraries
import cv2 
import imutils
import numpy as np
import random
from numpy import array
from PIL import Image
from tensorflow.keras.utils import *
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
import tensorflow.keras.backend as K

#Transforms image
#Crops and resizes to specific values
def transform_image(image):
    image = Image.fromarray(image)
    #Crops to remove white space
    image = image.crop((115, 50, 791, 582))
    #Scales the image by 0.125
    image = image.resize((84,66))
    image = np.array(image)
    
    return image

#Returns transformed variations of the input image
#Prevents overfitting in model training
def data_augmentation_for_CWRU(image):
    #Define a constant scale to account for varying image sizes
    h, w, d = image.shape
    translation_scale = h*0.25
    
    #Translates image up and down    
    up_img = imutils.translate(image, 0, -translation_scale)
    up_img[up_img == 0] = 255 #Removes black space from images after translation
    down_img = imutils.translate(image, 0, translation_scale)
    down_img[down_img == 0] = 255
    
    #Rotates image 45 degrees anticlockwise and clockwise
    left_img = imutils.rotate(image, 45)
    left_img[left_img == 0] = 255
    right_img = imutils.rotate(image, -45)
    right_img[right_img == 0] = 255

    return image, up_img, down_img, left_img, right_img

#At a set probability apply a transformation to the image
#Prevents overfitting in model training without increasing the total number of files
def data_augmentation_for_other(image, number):
    h, w, d = image.shape
    translation_scale = h*0.25
    
    if number == 1: #Keep the image the same
        trans_image = image
        return trans_image
        
    elif number == 2: #Apply a upward translation
        trans_image = imutils.translate(image, 0, -translation_scale)
        trans_image[trans_image == 0] = 255 #Removes black space from images after translation
        return trans_image
        
    elif number == 3: #Apply a downward translation
        trans_image = imutils.translate(image, 0, translation_scale)
        trans_image[trans_image == 0] = 255 #Removes black space from images after translation
        return trans_image
        
    elif number == 4: #Apply an anticlockwise rotation
        trans_image = imutils.rotate(image, 45)
        trans_image[trans_image == 0] = 255 #Removes black space from images after transition
        return trans_image
        
    elif number == 5: #Apply an clockwise rotation
        trans_image = imutils.rotate(image, -45)
        trans_image[trans_image == 0] = 255 #Removes black space from images after transition
        return trans_image


#Splits images and labels arrays into train and test sets
#Normalises images and labels arrays
def return_split(images, labels, class_type):
    #Splits images and labels into train and test sets with 80/20 split
    train_images, test_images, train_labels, test_labels = train_test_split(images, labels, 
                                                                            shuffle=True, random_state=42, 
                                                                            stratify=labels, test_size=0.2)

    #Converts images arrays to numpy arrays and normalises
    train_images = np.array(train_images)/255
    test_images = np.array(test_images)/255

    #Converts labels to a binary value
    if class_type == 'binary':
        #Converts integer values
        train_labels = to_categorical(train_labels)
        test_labels = to_categorical(test_labels)
    elif class_type != 'binary':
        #Converts string values
        encoder = LabelBinarizer()
        train_labels = encoder.fit_transform(train_labels)
        test_labels = encoder.fit_transform(test_labels)

    #Divide train set into train and validations sets with 70/10 split
    validation_split = int(0.1*len(images))
    #Validation data is taken from train data
    val_images, train_images = train_images[:validation_split], train_images[validation_split:]
    val_labels, train_labels = train_labels[:validation_split], train_labels[validation_split:]

    return train_images, train_labels, test_images, test_labels, val_images, val_labels


#Source [53]
def calculate_class_weights(labels):
    unique_classes, class_counts = np.unique(labels, return_counts=True)
    total_samples = len(labels)
    class_weights = {}

    for class_label, class_count in zip(unique_classes, class_counts):
        class_weight = total_samples / (2.0 * class_count)
        class_weights[class_label] = class_weight

    return class_weights
#End of source [53]


#Making pairs for SNN training
def make_pairs(images, labels):
    #Initalise arrays to hold (image,image) pairs and corresponding labels
    pairImages = []
    pairLabels = []
    
    #Convert string labels into integer equivalents
    labels = convert_labels(labels)

    #Source [54]
    #Calculate total number of classes present
    numClasses = len(np.unique(labels))
    #Build a list of indexes for each class
    index = [np.where(labels == i)[0] for i in range(0, numClasses)]

    #Loop over all images
    for indexA in range(len(images)):
        #Initalise current image
        currentImage = images[indexA]
        label = labels[indexA]

        #Randomly pick another image in the same class
        indexB = np.random.choice(index[label])
        posImage = images[indexB]

        #Add positive pair and label to respective arrays
        pairImages.append([currentImage, posImage])
        pairLabels.append([1])

        #Pick an image with a label not equal to the current label
        negIdx = np.where(labels != label)[0]
        negImage = images[np.random.choice(negIdx)]

        #Add negative pair and label to respective arays
        pairImages.append([currentImage, negImage])
        pairLabels.append([0])

    return (np.array(pairImages), np.array(pairLabels))

    #End of source [54]

#Converts string labels into integers for SNN pair making
def convert_labels(labels):
    for i in range (len(labels)):
        #Convert binary encoding to list
        label = labels[i].tolist()
        #Concatenate list to form binary string
        label = ''.join(map(str, a))
        #Convert binary string to integer value
        labels[i] = int(label, 2)

    return np.array(labels)

#Source [55]
#Calculating euclidean distance between two vectors
#Used in SNN training
def euclidean_distance(vectors):
	(featsA, featsB) = vectors
	
    #Compute the sum of squared distances between the vectors
	sumSquared = K.sum(K.square(featsA - featsB), axis=1, keepdims=True)
	
    #Return the euclidean distance between the vectors
	return K.sqrt(K.maximum(sumSquared, K.epsilon()))

#End of source [55]

#"Main" function
#Executes all image transformations and adds to single array
def data_preparation(img_dir, label, dataset):
    image = cv2.imread(img_dir)
    image = transform_image(image)

    images = []
    labels = []

    if dataset == "CWRU":
        #Apply data augmentation
        array = [0]*5
        array = data_augmentation_for_CWRU(image)

        #For every augmented image:
        #Convert to a numpy array and add to all image array
        #Add corresponding label to converted image
        for i in array:
            images.append(i)
            labels.append(label)

    elif dataset != "CWRU":
        #Randomly generate a number to correspond to an image transformation
        [transformation_choice] = random.choices([1, 2, 3, 4, 5], [0.4, 0.15, 0.15, 0.15, 0.15])

        #Apply data augmentation
        image = data_augmentation_for_other(image, transformation_choice)

        #Add augmneted image and corresponding label to independent arrays
        images = [image]
        labels = [label]

    return images, labels
