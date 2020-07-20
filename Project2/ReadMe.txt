2. Credit Card Fraud Detection


Introduction:
It is important that credit card companies are able to recognize fraudulent credit card transactions so that customers are not charged for items that they did not purchase.


Problem Statement:
Design a ML model that can distinguish between a fraudulent credit card transaction and a normal one.


Procedure:
First of all we will download the datset.
Link for our datset is "https://www.kaggle.com/mlg-ulb/creditcardfraud"

Our datset contains only numerical input variables which are the result of a PCA transformation.
We can clearly see that our datset is highly imbalanced so before creating the model we have to balance the datset.
There are 2 ways of balancing an unbalanced dataset-
1.Undersampling(removing the data from the higher class to make it comparable to the lower class) 
2.Oversampling(adding synthetic data to lower class to make it comparable to the higher class data)

We have done Undersampling approach in our project.
We have made the corelation charts and found out that some of the columns have negative corelation(columns-> V17,V14,V12,V10,etc.) with the output and some of the columns have the positive corelation (columns-> V11,V4,V2,V19,etc.)

Then next step is to find the anomaly(extreme outliers) in our dataset and remove them as they may cause overfitting in the model.

After that we are performing dimensionality reduction and also making clusters of fraud and non-fraud transactions to help us in better understanding and identifying the differences.

After that we are using 4 classifiers to create 4 models and we will see how different classifiers are giving us different accuracy,precision score,F1 score, etc.


Conclusion:
We can see after creating the models that Logistic Regression model is giving us the best results in predicting whether the credit card transaction is fradulent or not.