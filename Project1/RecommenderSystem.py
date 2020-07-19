#importing necessary libraries
import numpy as np
import pandas as pd 
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
import warnings; 
warnings.simplefilter('ignore')

#datset
electronics_data=pd.read_csv("D:/AmazonRecommenderSystem/ratings_Electronics (1).csv",names=['userId', 'productId','Rating','timestamp'])

electronics_data.head()
electronics_data.shape

#Taking subset of the dataset
electronics_data=electronics_data.iloc[:1048576,0:]

#Check the datatypes
electronics_data.dtypes
electronics_data.info()

#Five point summary 
electronics_data.describe()['Rating'].T

#Finding the minimum and maximum ratings
print('Minimum rating is: %d' %(electronics_data.Rating.min()))
print('Maximum rating is: %d' %(electronics_data.Rating.max()))

#Checking for missing values
print('Number of missing values across columns: \n',electronics_data.isnull().sum())

# Checking the distribution of the rating
sns.countplot('Rating', data=electronics_data )

#UNIQUE USERS AND PRODUCT
print("Total data ")
print("\nTotal no of ratings :",electronics_data.shape[0])
print("Total No of Users   :", len(np.unique(electronics_data.userId)))
print("Total No of products  :", len(np.unique(electronics_data.productId)))

#Dropping the Timestamp column
electronics_data.drop(['timestamp'], axis=1,inplace=True)

#Analysis of rating given by the user 
no_of_rated_products_per_user = electronics_data.groupby('userId')['Rating'].count().sort_values(ascending=False)
no_of_rated_products_per_user.head()

no_of_rated_products_per_user.describe()

quantiles = no_of_rated_products_per_user.quantile(np.arange(0, 1.01, 0.01), interpolation='higher')

plt.figure(figsize=(10,10))
plt.title("Quantiles and their Values")
quantiles.plot()
# quantiles with 0.05 difference
plt.scatter(x=quantiles.index[::5], y=quantiles.values[::5], c='yellow', label="quantiles with 0.05 intervals")
# quantiles with 0.25 difference
plt.scatter(x=quantiles.index[::25], y=quantiles.values[::25], c='red', label = "quantiles with 0.25 intervals")
plt.ylabel('No of ratings by user')
plt.xlabel('Value at the quantile')
plt.legend(loc='best')
plt.show()

print('\n No of rated product more than equal to 50 per user : {}\n'.format(sum(no_of_rated_products_per_user >= 50)) )


# =============================================================================
#                1.Popularity Based Recommendation
# Popularity based recommendation system works with the trend. It basically uses the items which are in trend right now. 
# =============================================================================

#Getting the new dataframe which contains users who has given 50 or more ratings
new_df=electronics_data.groupby("productId").filter(lambda x:x['Rating'].count() >=50)

no_of_ratings_per_product = new_df.groupby('productId')['Rating'].count().sort_values(ascending=False)

fig = plt.figure(figsize=plt.figaspect(.5))
ax = plt.gca()
plt.plot(no_of_ratings_per_product.values)
plt.title('# RATINGS per Product')
plt.xlabel('Product')
plt.ylabel('No of ratings per product')
ax.set_xticklabels([])

plt.show()

#Average rating of the product 
new_df.groupby('productId')['Rating'].mean().head()

new_df.groupby('productId')['Rating'].mean().sort_values(ascending=False).head()

#Total no of rating for product
new_df.groupby('productId')['Rating'].count().sort_values(ascending=False).head()

ratings_mean_count = pd.DataFrame(new_df.groupby('productId')['Rating'].mean())
ratings_mean_count['rating_counts'] = pd.DataFrame(new_df.groupby('productId')['Rating'].count())
ratings_mean_count.head()
ratings_mean_count['rating_counts'].max()

plt.figure(figsize=(8,6))
plt.rcParams['patch.force_edgecolor'] = True
ratings_mean_count['rating_counts'].hist(bins=50)

plt.figure(figsize=(8,6))
plt.rcParams['patch.force_edgecolor'] = True
ratings_mean_count['Rating'].hist(bins=50)

plt.figure(figsize=(8,6))
plt.rcParams['patch.force_edgecolor'] = True
sns.jointplot(x='Rating', y='rating_counts', data=ratings_mean_count, alpha=0.4)

popular_products = pd.DataFrame(new_df.groupby('productId')['Rating'].count())
most_popular = popular_products.sort_values('Rating', ascending=False)
most_popular.head(30).plot(kind = "bar")

popular_products = pd.DataFrame(new_df.groupby('productId')['Rating'].count())
most_popular = popular_products.sort_values('Rating', ascending=False)
most_popular.head(30).plot(kind = "bar")


# =============================================================================
#              2. Collaberative filtering (Item-Item recommedation)
# CF is based on the idea that the best recommendations come from people who have similar tastes. 
# =============================================================================
from surprise import KNNWithMeans
from surprise import Dataset
from surprise import accuracy
from surprise import Reader

#Reading the dataset
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(new_df,reader)

#Splitting the dataset
trainset, testset = train_test_split(data, test_size=0.3,random_state=10)

# Use user_based true/false to switch between user-based or item-based collaborative filtering
algo = KNNWithMeans(k=5, sim_options={'name': 'pearson_baseline', 'user_based': False})
algo.fit(trainset)

# running the trained model against the testset
test_pred = algo.test(testset)
test_pred

# get RMSE
print("Item-based Model : Test Set")
accuracy.rmse(test_pred, verbose=True)
# =============================================================================
#           3.Model-based collaborative filtering system¶
# These methods are based on machine learning and data mining techniques. The goal is to train models to be able to make predictions. 
# For example, we could use existing user-item interactions to train a model to predict the top-5 items that a user might like the most.  
# =============================================================================
new_df1=new_df.head(10000)
ratings_matrix = new_df1.pivot_table(values='Rating', index='userId', columns='productId', fill_value=0)
ratings_matrix.head()
ratings_matrix.shape

X = ratings_matrix.T
X.head()
X.shape

#unique products in subset  of data
X1 = X

#Decomposing the Matrix
from sklearn.decomposition import TruncatedSVD
SVD = TruncatedSVD(n_components=10)
decomposed_matrix = SVD.fit_transform(X)
decomposed_matrix.shape

#Correlation Matrix
correlation_matrix = np.corrcoef(decomposed_matrix)
correlation_matrix.shape

X.index[75]

i = "B00000K135"
product_names = list(X.index)
product_ID = product_names.index(i)
product_ID

# Correlation for all items with the item purchased by this customer based on items rated by other customers people who bought the same product
correlation_product_ID = correlation_matrix[product_ID]
correlation_product_ID.shape

#Recommending top 25 highly correlated products in sequence
Recommend = list(X.index[correlation_product_ID > 0.65])
# Removes the item already bought by the customer
Recommend.remove(i) 

Recommend[0:24]
#Here are the top 25(if any) products to be displayed by the recommendation system to the above customer based on the purchase history of other customers in the website.