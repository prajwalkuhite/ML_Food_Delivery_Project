from src.constant import *
from src.config.configuration import *
from src.logger import logging
from src.exception import CustomException
import os, sys
from dataclasses import dataclass
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import pandas as pd

from src.utils import *


# models
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso,Ridge,ElasticNet
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor 
from xgboost import XGBRegressor
# Metrices
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error


# Configuration class

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = MODEL_FILE_PATH


class ModelTrainer :
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig

    
    def initiate_model_training(self,train_array,test_array):
        try:
            logging.info('Spliting train and test array into independent and dependent variable')
            X_train,y_train,X_test,y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "linear Regression": LinearRegression(),
                "Ridge":Ridge(),
                "Lasso":Lasso(),
                "Elastic Net" : ElasticNet(),
                "XGBRegressor": XGBRegressor(),
                "SVR": SVR()
            }

            model_report:dict = evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,
                                                y_test=y_test,models=models)
            print(model_report)

            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]

            print(f"Best Model Found , Model Name : {best_model_name}, R2 score {best_model_score}")

            logging.info(f"Best Model Found , Model Name : {best_model_name}, R2 score {best_model_score}")

            save_obj(file_path=self.model_trainer_config.trained_model_file_path,
                     obj = best_model)
            
    

        except Exception as e:
            raise CustomException(e,sys)
        

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
if __name__ == '__main__':
    obj = DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    train_arr,test_arr,_ = data_transformation.inititate_data_transformation(train_data_path,test_data_path)
    model_trainer = ModelTrainer()
    model_trainer.initiate_model_training(train_array=train_arr,test_array=test_arr)