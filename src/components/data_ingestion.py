import sys,os
from src.constant import *
from src.config.configuration import *
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException


@dataclass
class DataIngestionConfig:
    train_data_path = TRAIN_FILE_PATH
    test_data_path = TEST_FILE_PATH
    raw_data_path = RAW_FILE_PATH

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()  
## so we craeted this variable and inside all three paths are stored

    def initiate_data_ingestion(self):
        try:
            logging.info('Entered the data ingestion method and process is initialized')

            df = pd.read_csv(DATA_PATH)
            logging.info('Read the dataset as a dataframe')
            
            # This will create a artifacts dir then data_ingestion dir then
            # raw_data dir in CWD then inside raw.csv raw data will stored
            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path),exist_ok=True)
            logging.info('Raw data is stored in artifacts folder')
             
            # The form in which we stored raw data
            df.to_csv(self.data_ingestion_config.raw_data_path, index=False)

            # Splitting the data
            logging.info('Train test Split initiated')
            train_set, test_set = train_test_split(df,test_size=0.20,random_state=42)
            
            # so our artifacts dir then data_ingestion dir is already created as above
            # now ingested_dir will be creates in CWD then inside train.csv train data will stored
            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path),exist_ok=True)
            train_set.to_csv(self.data_ingestion_config.train_data_path,header=True)
            logging.info('Train data successfully stored in artifacts')
            
            # similar for test data path
            os.makedirs(os.path.dirname(self.data_ingestion_config.test_data_path),exist_ok=True)
            test_set.to_csv(self.data_ingestion_config.test_data_path,header=True)
            logging.info('Test data successfully stored in artifacts')

            logging.info('Ingestion of the data is completed')

            return (
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path
            )


        except Exception as e:
            raise CustomException(e,sys)
    
