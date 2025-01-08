#Import necessary libraries
import matplotlib.pyplot as plt
import csv

#Returns line graph plots
def plot_graph(line1, line2, graph_label):
    epoch_count = len(line1)
    
    f = plt.figure()

    #For accuracy plots, scale values between 0-100 (as a percentage)
    if graph_label == 'accuracy':
        line1 = [value*100 for value in line1]
        line2 = [value*100 for value in line2]
        plt.ylim([0, 100])
    
    #Plot accuracy or loss
    plt.plot(line1, label=graph_label)
    plt.plot(line2, label="val_"+graph_label)

    #Adjust size of the x-axis
    plt.xticks(np.arange(0, epoch_count+1, step=10))

    #Configure graphs labels and key
    plt.xlabel('Epoch')
    ylabel = graph_label.capitalize()
    plt.ylabel(ylabel)
    plt.legend(loc='lower right')

    return f
    matplotlib.pyplot.close()

#Save the training history to an external .csv file
def save_to_spreadsheet(experiment_name, history, test_loss, test_acc):
    #Records the total number of epochs and accuracy and loss of the training and validation data
    epoch = len(history.history['accuracy'])
    accuracy = history.history['accuracy'][epoch-1]
    loss = history.history['loss'][epoch-1]
    val_acc = history.history['val_accuracy'][epoch-1]
    val_loss = history.history['val_loss'][epoch-1]

    input = [experiment_name, accuracy, loss, val_acc, val_loss, test_acc, test_loss]

    #Write to file
    file_dir = "D:\\Final Year Project\\Results\\Results.csv"
    with open(file_dir, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(input)

    f.close()

