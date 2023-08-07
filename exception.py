from flask import Flask
from src.logger import logging
from src.exception import CustomException
import os,sys


app = Flask(__name__)


@app.route('/',methods=['GET','PUSH'])
def index():

    try:
        raise Exception('We are testing our exception file')
    except Exception as e:
        ML = CustomException(e,sys)
        logging.info(ML.error_message)
        
        logging.info('We are testing our logging file')

        return 'Welcome to Engineering wala bhaiya'


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)