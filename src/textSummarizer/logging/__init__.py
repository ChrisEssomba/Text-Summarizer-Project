import os
import sys
import logging

logging_str = '[%(asctime)s: %(levelname)s: %(module)s: %(message)s]' #it shows the time, the type of log (it can be infor, error, warnings..) the part of the code concerned and lastly the message
log_dir = 'logs'
log_filepath = os.path.join(log_dir, 'running_logs.log')
os.makedirs(log_dir, exist_ok=True) #create a folder where to store the logs


logging.basicConfig(
    level=logging.INFO, 
    format=logging_str, 
    
    handlers=[
        logging.FileHandler(log_filepath),  #save logs in a file
        logging.StreamHandler(sys.stdout)   #show logs in the terminal
    ]
)

'''
the handlers are tipically used to tell where to write the logs.
'''


logger = logging.getLogger("textSummarizerLogger")


