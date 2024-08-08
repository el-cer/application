from .DataPrep import split_data
from sklearn.linear_model import LinearRegression
import numpy as np
class MachineLearning:
    def __init__(self) -> None:
        self.dict_of_models = {"Regression problem":["RL","Trees Regressor"], 'Computer Vision':['CNN','object Detection'],'Classification':['Trees Classifier','Neural Network','Clustering']}
    def RegressionLin(self, data, target):
        X_train, X_test, y_train, y_test = split_data(data, target)

        reg = LinearRegression().fit(X_train, y_train)
        score = reg.score(X_train, y_train)
        
        return np.round(score, 2)