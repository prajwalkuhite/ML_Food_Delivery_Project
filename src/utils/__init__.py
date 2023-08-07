from src.exception import CustomException
from src.logger import logging
import os,sys
import pickle

def save_obj(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as file_obj:
            pickle.dump(obj,file_obj)
            
    except Exception as e:
        raise CustomException(e,sys)

# Model evaluation
from sklearn.metrics import r2_score

def evaluate_models(X_train,y_train,X_test,y_test,models):
    try:
        report = {}      

        for i in range(len(models)):
            model = list(models.values())[i]

            model.fit(X_train,y_train)

            y_test_pred = model.predict(X_test)

            test_model_score = r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException (e,sys)
