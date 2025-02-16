## Table of Contents
1. [Project Overview](#project-overview)
2. [Process Summary](#process-summary)
   - [1. Gathering and Prepping Data](#1-gathering-and-prepping-data)
   - [2. Diving into the Data](#2-diving-into-the-data)
   - [3. Building and Testing the Model](#3-building-and-testing-the-model)
   - [4. Bringing the Model to Life](#4-bringing-the-model-to-life)

## Project Overview

This project is all about predicting vessel fuel consumption using machine learning. The idea is to create a model that can take various factors like rpm, and cargo and give accurate fuel usage estimates.

## Process Summary

### 1. Gathering and Prepping Data

We started by getting the data we needed.  it wasn’t perfect right first. There were outliers and missing values, so we spent some time cleaning it up. This step was crucial because any garbage data could mess up our results down the line.

- **Before Cleaning**: Initially, the data was pretty messy, with lots of outliers that needed fixing.
  
    ![Before Data Cleaning](https://github.com/user-attachments/assets/a82ce0e0-c0cf-43b6-82b5-23da815fbec9)
    ![Before Data Cleaning](https://github.com/user-attachments/assets/68fbabf6-59f2-48e2-b975-f4756c5cf378)
  

- **After Cleaning**: After we rolled up our sleeves and got the data in shape, it was much more reliable and ready for analysis.
      
    ![After Data Cleaning](https://github.com/user-attachments/assets/302d5e38-347f-484b-8188-67b525d8e0d8)
    ![After Data Cleaning](https://github.com/user-attachments/assets/afd96384-0875-476e-b026-9c6a3b89c061)
### 2. Diving into the Data

With clean data at our disposal, the next step was to really get to know it. This is where exploratory data analysis (EDA) comes into play.

- **Visualizing Distributions**: We started by plotting the data to see how different variables were distributed. This helped us spot any trends or oddities right away.

  ![Visualization](https://github.com/user-attachments/assets/ea2f2e75-df1b-4736-971e-f923bce80600)
  ![Visualization](https://github.com/user-attachments/assets/d84e293b-1426-4dff-aab4-d05edf0b0061)
- **Correlation Analysis**: Next, we looked at how different variables related to each other. For instance, it became clear that speed, draft, and cargo weight were big players when it came to fuel consumption.
  
  ![Correlation Analysis](https://github.com/user-attachments/assets/4b490be4-012b-4cfc-b241-770c4e05cb8f)

#### Key Takeaways:
- **Strong Correlations**: Not surprisingly, variables like speed, steam, and RPM had a strong correlation with fuel consumption. After all, the harder a vessel works, the more fuel it burns.
- **Moderate Correlations**: Factors like wind speed and ocean currents also influenced fuel usage, though their impact was a bit more subtle.
- **Weak Correlations**: Some variables didn’t play as big a role. For example, slip (a measure of the difference between the vessel's speed through water and the engine's speed) was less impactful on fuel consumption.

### 3. Building and Testing the Model

Once we had a good grasp of the data, it was time to build the model. This is the heart of the project—transforming data into something that can make predictions.

- **Data Splitting**: We split our dataset into a training set and a test set. The training set is used to teach the model, while the test set is used to see how well it learned.

  ![Data Splitting](https://github.com/user-attachments/assets/f7df51e9-5b61-4016-977d-e39af7c2b183)

- **Choosing Models**: we tested a few different models: Random Forest, Gradient Boosting, and XGBoost. Each of these has its own strengths, so we wanted to see which would perform best in predicting fuel consumption.

- **Fine-Tuning**: After picking our model, we fine-tuned its parameters to make it as accurate as possible. This step, known as hyperparameter tuning, is all about getting the best performance out of the model without overfitting.
  
  ![Hyperparameter Tuning](https://github.com/user-attachments/assets/e5d8ba5c-2652-42e7-90c1-cb652230d30c)

- **Evaluating Performance**: Finally, we evaluated how well our model performed using several metrics, including R², MAE, and MSE. These metrics gave us a clear picture of how accurate our predictions were and whether there was room for improvement.
  
    ![Model Evaluation](https://github.com/user-attachments/assets/6037419c-69bc-4bfb-88a8-1f9990269c8c)
    ![Model Evaluation](https://github.com/user-attachments/assets/0cee805c-56e2-4c80-847a-069d67539a38)

### 4. Bringing the Model to Life

The last step was deploying our model so that it could actually be used in real-world scenarios.

- **Saving the Model**: We saved our trained model so it could be easily accessed and used whenever needed.

  ![Model Export](https://github.com/user-attachments/assets/0ad55772-23cf-4ba5-9290-9eb5b17d74c1)

- **Building a User Interface**: To make our model user-friendly, we created an interface using Streamlit. This allows users to input relevant data (like the vessel’s speed and cargo weight) and get an instant fuel consumption prediction.

  ![UI Development](https://github.com/user-attachments/assets/0ffe1d84-dce0-4a05-8cff-98fa59381505)

Check out the live demo [here](https://vessel-fuel-consumption.streamlit.app/).
