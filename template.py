import os
from pathlib import Path
import logging # log all the information (in real time)

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:') #show the ascii time and message

project_name = "textSummarizer"

list_of_files = [
    ".github.com/workflows/.gitkeep", #This one is important for the CI/CD deployment
    f"src/{project_name}/__init__.py", # We initialize this contructor to be able to call the folder as local package
    f"src/{project_name}/components/__init__.py", #To note that this writing creates a folder with a file in it
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging//__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml", 
    "params.yaml", 
    "app.py", 
    "main.py", 
    "Dockerfile", 
    "requirements.txt", 
    "setup.py", 
    "reseach/trials.ipynb" #Create the folder that will contain all the notebooks
]

for filepath in list_of_files:
    filepath = Path(filepath) #Convert the string path to a windows paths (handle the / and \ discrepacies)
    filedir, filename = os.path.split(filepath)
    
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} with the file {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): #Create new files
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"The file {filename} already exists")
        