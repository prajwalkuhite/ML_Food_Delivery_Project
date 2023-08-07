import logging
import sys,os
from datetime import datetime


LOG_DIR = "logs"
LOG_DIR = os.path.join(os.getcwd(),LOG_DIR)
# so we join logs folder with CWD 

# now for making loges directory
os.makedirs(LOG_DIR,exist_ok=True)


# To capture the current time in log file 
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
file_name = f"log_{CURRENT_TIME_STAMP}.log"

# Now we are going to join our log DIR with file
log_file_path = os.path.join(LOG_DIR,file_name)


logging.basicConfig(filename=log_file_path,
                    filemode='w',
                    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
                    level=logging.INFO)



