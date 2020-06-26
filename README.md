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

### Findings:

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
Our model has Accuracy: 89% and Recall: 90%.

### Recommendations:  
Incorporate our model to see how it works in hospitals so that it can assist health professionals diagnose patients with Pneumonia. Ofcourse these reports have to be validated. This is not the ultimate test. This needs to be certified by health professionals.
This model should be run under the supervision of a radiologist to enhance accuracy/recall to improve treatment outcomes which will increase hospitals' ratings and fundings.

### Future Work:
We need more data to run our validation set on so that we can be sure of the way the model is predicting.
