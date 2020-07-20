3. Titanic Survivor

Introduction:
On April 15, 1912, during her maiden voyage, the Titanic sank after colliding with an iceberg, killing 1502 out of 2224 passengers and crew which is around 32% Survival rate.
One of the reasons that the shipwreck led to such loss of life was that there were not enough lifeboats for the passengers and crew.


Problem Statement:
Design a model with the help of datset provided that can predict the survivors in the Titanic.


Procedure:
First of all we have downloaded the dataset.
Link for the datset is "https://www.kaggle.com/c/titanic/data"

Our datset contains details like name,age,sex,etc. of the passengers of the Titanic.So first of all we corelated different features and found the relation between them and their respective realtion with the passsenger surviving or not.

We corelated between numerical features,numerical and ordinal features,categorical features,categorical and numerical features.After that we also dropped certain features which were irrelevant in our model building such as ticket,cabin features.

We also created certain new features(from  the already existing features),like FamilySize,IsAlone,etc.We also converted certain categorical features to numerical features like Embarked feature.

After preparing the dataset in the necessary format we build our model. We build our model using Logistic regression,Support Vector Machines, K-nearest neighbour , Gaussian Naive Bayes,  Decision Tree  and Random forest.We evaluated our model and found out that Random Forest is giving us the most appropriate results among all.


Conclusion:
Thus we created our model that predicted which passenger is going to survive or which are going to die and found out that model built using Random Forest is more accurate than others.
