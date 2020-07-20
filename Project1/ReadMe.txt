1.Recommender System 


Introduction: 
E-commerce companies like Amazon, flipkart, etc. now a days use different recommendation systems to provide their
customer suggestions for the products of their interest. Recommender system creates a similarity between the user and items 
and exploits the similarity between user/item to make recommendations.


Problem Statement: 
Design a recommender system using product reviews that provide the product recommendation to the user,
of their interest or the popular products currently in the trend.


Procedure:  
First we will download the dataset from kaggle.We will be using electronic items reviews dataset of Amazon reviews.

Our dataset contain User Id, Product Id, Rating and Time stamp.
Then we will import some necessary libraries. Then afterwards we will be analyzing the rating of different products we have, no. of unique users and products, etc.
We have dropped the Time Stamp column as it was not useful to us.

Then we have created 3 types of recommender system-
1. Popularity Based (recommends the items in trend now)
2.  Collaborative Filtering (recommendation of products for people having similar tastes)
3. Model based (training model to make them able to predict products of interest) 

In the Popularity Based System first we are creating a dataframe of users who have given ratings 50 or more.Then we are finding the average rating ,total number of rating,etc. of the products and by the help of all this, popular products are being recommneded to the user.

In the Collaborative Filtering, we are using KNNWithMeans of the Surprise library and by the help of that recommendations are shown on the basis of people having similar tastes of products.

And in the Model Based System, we are doing data mining, we are using TruncatedSVD for decomposition of matrix, we are creating corelation matrix to observe the relation among the user and the products and thus recommending top products to the user of their interest.


Conclusion:
We have created a recommender system that provides the recommendation of top products based on the user’s interest.Thus helping each specific user to find the right product of their need and interest.


