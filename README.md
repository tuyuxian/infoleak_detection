# Infoleak Detection
## Risk Detection of Personal Info Breach（Focus on Privacy Contract）

### Website
https://infoleak-detect.com

### About
This is a application about the risk of info leak detection of privacy contracts. Using **Bert** as the main NLP model and **flask** as the frame to bulid the website.

### Model
**modelV1.joblib**  
Here I use about twelve privacy contracts from companies that provide services we often use such as, **Line**, **booking.com**, **pinterest**, and so on to train my model. First I label the sentences of privacy contracts with risk in 1, and label others with 0. Second, each of the sentences will be transformed to the matrix of 768 degrees with **Bert**, and then be put in the **SVM** model to calculate the probability of each sentence of whether being risk.

### Application
Here I use Flask as the frame, and MySQL as the database.

### How To Use
First, pick up a privacy contract that you are interested in.
![image](https://github.com/tuyuxian/infoleak_detection/blob/master/picture/step0.png)

And copy all the sentences to the area of **隱私權政策** and press **檢測**.  

See the result of the detection and can further give me some opinions and experience scores.  
