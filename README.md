# Module 4 Project - Pneumonia Detection

![](/images/Pneumonia.jpg)

## Introduction  
Pneumonia is an infection that inflames air sacs in one or both lungs, which may fill with fluid.
With pneumonia, the air sacs may fill with fluid or pus. The infection can be life-threatening to anyone, but particularly to infants, children, and people over 65.
Symptoms include cough with phlegm or pus, fever, chills, and difficulty breathing.
Antibiotics can treat many forms of pneumonia. Some forms of pneumonia can be prevented by vaccines.
The WHO estimates that over 4 million premature deaths occur annually from household air pollution-related diseases including pneumonia. Over 150 million people get infected with pneumonia on an annual basis especially children under 5 years old.  

This project is about diagnosing pneumonia from XRay images of lungs of a person using Neural Networks.

__Dataset:__    
__Train folder:__  
Normal Images - 1341  
Pneumonia Images - 3875  
__Val folder:__  
Normal Images - 8  
Pneumonia Images - 8  
__Test folder:__   
Normal Images - 234  
Pneumonia Images - 390

### Methodology:  

__ROSEMED Methodology__ - This is the one of the most straightforward of the Data Science processes.   
R - Research O - Obtain S - Scrub E - Explore M - Model E - Evaluate D - Deploy  

During this process,the stages often blur together. It is completely acceptable (and often a best practice!) to float back and forth between stages as you learn new things about your problem, dataset, requirements, etc. It's quite common to get to the modeling step and realize that you need to scrub your data a bit more or engineer a different feature and jump back to the "Scrub" stage, or go all the way back to the "Obtain" stage when you realize your current data isn't sufficient to solve this problem. As with any of the frameworks, this methodology is meant to be treated more like a set of guidelines for structuring your project than set-in-stone steps that cannot be violated.  

Research - Find out about various models and see which model works best for our data.  
Obtain - This step involves understanding stakeholder requirements, gathering information on the problem, and finally, sourcing data that we think will be necessary for solving this problem.  
Scrub - During this stage, we focus on preprocessing our data. Important steps such as identifying and removing null values, dealing with outliers, normalizing data, and feature engineering/feature selection are handled around this stage.  
Explore - During this step, we create visualizations to really get a feel of the dataset. We focus on things such as understanding the distribution of different columns, checking for multicollinearity, and other tasks like that.  
Model - It consists of building and tuning models using all the tools we have in our data science toolbox. In practice, this often means defining a threshold for success, selecting machine learning algorithms to test on the project, and tuning the ones that show promise to try and increase our results.  
Evaluate - During this step, we interpret the results of models, and communicate results to stakeholders. If the results are satisfactory to all stakeholders involved, we go from this stage right into putting the model into production and automating processes necessary to support it.  
Deploy - Deploying the Model.  

### Findings:

Model|Loss|Accuracy|Val_Loss|Val_Accuracy
-----|----|--------|--------|------------
Base|Model|0.27|0.94|0.89|0.73
Improved Model|0.21|0.92|0.29|0.89


Confusion Matrix for our Test Set-

![](/images/Confusion_matrix.png)

__For our Test set :__  
TEST METRICS  
Accuracy: 88.94%  
Precision: 91.9%  
Recall: 90.25%  
F1-score: 91.07   

TRAIN METRIC  
Train acc: 91.74%  

### Conclusion:  
This study presents a deep CNN based approach for the automatic detection of Pneumonia.
We have demonstrated how to distinguish between Normal and Pneumonia Chest X-Rays with our model having an Accuracy of 89% and a Recall of 90%
We constucted a Convolutional Neural Network model from scratch to extract features from a given Chest X-Ray image and classify it to determine if a person is infected with Pneumonia.

### Recommendations:  
Incorporate our model to see how it works in hospitals so that it can assist health professionals diagnose patients with Pneumonia. Ofcourse these reports have to be validated. This is not the ultimate test. This needs to be certified by health professionals.
This model should be run under the supervision of a radiologist to enhance accuracy/recall to improve treatment outcomes which will increase hospitals' ratings and fundings.

### Future Work:
We need more data to run our validation set on so that we can be sure of the way the model is predicting.
