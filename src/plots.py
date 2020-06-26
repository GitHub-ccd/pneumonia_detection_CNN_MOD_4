#%matplotlib inline
import matplotlib.pyplot as plt
import itertools
import numpy as np 
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix
import cv2


def acc_loss_plot(model_his):
    fig, ax = plt.subplots(1, 2, figsize=(15, 5))

    ax[0].plot(model_his.history['acc'])
    ax[0].plot(model_his.history['val_acc'])
    ax[0].set(xlabel = 'Epoch', ylabel ='Accuracy' )
    ax[0].set_title('Model Accuracy', weight='bold')
    ax[0].legend(['Training set', 'Validation set'], loc='upper right')


    ax[1].plot(model_his.history['val_loss'],label='Val Loss')
    ax[1].plot(model_his.history['loss'],label='Loss')
    ax[1].set_title('Model Loss', weight='bold')
    ax[1].set(xlabel = 'Epoch', ylabel ='Loss' )
    ax[1].legend(loc='upper right')

    plt.show()


def plot_confusion_matrix(cm, classes,normalize=False,title='Confusion matrix',cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.   
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
            horizontalalignment="center",
            color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()
 
def show_eval(model, result, generator, labels):
    preds = model.predict_generator(generator)

    acc = accuracy_score(labels, np.round(preds))*100
    cm = confusion_matrix(labels, np.round(preds))
    tn, fp, fn, tp = cm.ravel()

    print('CONFUSION MATRIX ------------------')
    print(cm)

    print('\nTEST METRICS ----------------------')
    precision = (tp/(tp+fp))*100
    recall = (tp/(tp+fn))*100
    print('Accuracy: {}%'.format(acc))
    print('Precision: {}%'.format(precision))
    print('Recall: {}%'.format(recall))
    print('F1-score: {}'.format(2*precision*recall/(precision+recall)))

    print('\nTRAIN METRIC ----------------------')
    print('Train acc: {}'.format(np.round((result.history['acc'][-1])*100, 2)))

    classes=np.unique(labels) 
    normalize=False
    title='Confusion matrix'
    cmap=plt.cm.Blues


    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
            horizontalalignment="center",
            color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')    
    
    plt.show()
	
def plotImages(images_arr):
    fig, axes = plt.subplots(1, 16, figsize=(20,20))
    axes = axes.flatten() 
    for img, ax in zip( images_arr, axes):
        ax.imshow(img)
        ax.axis('off')
    plt.tight_layout()
    plt.show()