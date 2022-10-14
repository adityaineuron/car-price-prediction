# 🚗 Used Car Price Prediction

This project aims to solve the problem of predicting the price of a used car, using Sklearn's supervised machine learning techniques. It is a regression problem and predictions are carried out on dataset of used car sales in the Indian car market Cardheko website. Several regression techniques have been studied, including XGboost and Random forests of decision trees.

Their performances were compared in order to determine which one works best with out dataset and used them to predict the price of a used car from user input from Flask application.

Archt

💿 Installing
1. Environment setup.
```
conda create --prefix venv python=3.9 -y
```
```
conda activate venv/
````
2. Install Requirements and setup
```
pip install -r requirements.txt
```
5. Run Application
```
python main.py
```

Project Architecture - 

![WhatsApp Image 2022-09-22 at 15 29 04](https://user-images.githubusercontent.com/71321529/192722300-b906b222-63f7-452b-8e30-e234405031f2.jpeg)


![WhatsApp Image 2022-09-22 at 15 29 10](https://user-images.githubusercontent.com/71321529/192721926-de265f9b-f301-4943-ac7d-948bff7be9a0.jpeg)

![WhatsApp Image 2022-09-22 at 15 29 19](https://user-images.githubusercontent.com/71321529/192722336-54016f79-89ef-4c8c-9d71-a6e91ebab03f.jpeg)

In Github Secrets, give your AWS credentials and MongoDB creds

Creds - AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_DEFAULT_REGION, MONGODB_URL, ECR_REPO, HOSTNAME and AWS_PRIVATE_KEY as 


🔧 Built with
- FastAPI
- Python 3.7.6
- Machine learning
- 🏦 Industrial Use Cases

## Models Used
* Linear Regression
* Lasso Regression
* Ridge Regression
* K-Neighbors Regressor
* Decision Tree
* Random Forest Regressor
* XGBRegressor
* CatBoosting Regressor
* AdaBoost Regressor

From these above models after hyperparameter optimization we selected Top two models which were XGBRegressor and Random Forest Regressors and used the following in Pipeline.

* GridSearchCV is used for Hyperparameter Optimization in the pipeline.

## `car_price` is the main package folder which contains 


**Components** : Contains all components of Machine Learning Project
- DataIngestion
- DataValidation
- DataTransformations
- ModelTrainer

**Custom Logger and Exceptions** are used in the Project for better debugging purposes.

## Conclusion
- This Project can be used in real-life by Users or Used car dealers to predict the Estimated Price of the car based on input specifications.