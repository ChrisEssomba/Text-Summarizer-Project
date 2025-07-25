#IN THIS FILE WE WRITE THE METHODS THAT WE WANT TO PERFORM WITH THAT ENTITY, IT'S WHERE WE BUILD

import os 
from pathlib import Path
import urllib.request as request
import zipfile
from textSummarizer.entity import DataIngestionConfig
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size 

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL, 
                filename= self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
           
    
    def extract_zip_file(self):
        """
        Zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """ 
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)