import os ,sys
from datetime import datetime

# artifacts -> pipeline folder -> timestamp -> output

def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%M-%S')}"

CURRENT_TIME_STAMP = get_current_time_stamp()

# Now we are defining our dataset root
ROOT_DIR_KEY= os.getcwd()
DATA_DIR = 'notebooks/data'
DATA_DIR_KEY = 'Zomato.csv'

# To store the output -- we saved in artifacts folder
ARTIFACT_DIR_KEY = 'artifacts'

# Data ingestion related variable
DATA_INGESTION_KEY = 'data_ingestion'
DATA_INGESTION_RAW_DATA_DIR = 'raw_data_dir'
DATA_INGESTION_INGESTED_DATA_DIR_KEY = 'ingested_dir'
RAW_DATA_DIR_KEY = 'raw.csv'
TRAIN_DATA_DIR_KEY = 'train.csv'
TEST_DATA_DIR_KEY = 'test.csv'


# Data Transformation related variables

DATA_TRANSFORMATION_ARTIFACT = 'data_transformation'

DATA_PREPROCESS_DIR = 'preprocessor'
DATA_PROCESSING_OBJ = 'preprocessor.pkl'

DATA_TRANSFORMATION_DIR = 'transformation'

TRANSFORM_TRAIN_DIR_KEY = 'train.csv'
TRANSFORM_TEST_DIR_KEY = 'test.csv'

# artifacts / data_transformation / preprocessor->preprocessor.pkl 
#                                   and transformation-> train.csv and test.csv


# Model Training variables

MODEL_TRAINER_KEY = 'model_trainer'
MODEL_OBJECT = 'model.pkl'
