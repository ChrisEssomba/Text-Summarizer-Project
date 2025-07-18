#This file (Utils/common) is where you define all the functions that you will be frequently using in your code

import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads yaml file and returns

    Args:
        path_to_yaml (str): path as input
    
    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Yaml file is empty")
    except Exception as e:
        raise e
     
"""
The configbox type is prefered when dealing with yaml file.
Since these file are formed of key-value pairs, it allows to access the keys in a yaml with adding dot to the key names
ex : 
In yaml file :    --------> In config box variable
Name :                                         Content = read_yaml(path_to_yaml)
    Spanish_name: Chris                        Print(Content.Name.Spanish_name) ##Chris
"""

#to create new folders especially ingesting  data
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create list of directories

    Args:
        path_to_directories (list): list of path of directories
        verbose (bool, optional): Ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")
            

@ensure_annotations
def get_size(path) -> str:
    """Get the size of a file in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f" {size_in_kb} KB"

'''
Why do we use the decorator ensure_annotations?
To ensure that the type of the input variable entered by the user always match the one define in the function
if we have a function that return x*y, without ensure_annotion even if we precise that x and y are int, 
in case we do 2* "yo" the function will return yoyo. With that decoration, we'll have error instead #look at the research/trial file
'''