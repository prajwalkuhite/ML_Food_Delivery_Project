from flask import Flask
from src.logger import logging

app = Flask(__name__)


@app.route('/',methods=['GET','PUSH'])
def index():
    logging.info('We are testing our logging file')

    return 'Welcome to Engineering wala bhaiya'


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)