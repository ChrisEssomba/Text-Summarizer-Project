#IN THIS FILE WE DEFINE THE TYPE OF THE VARIABLES HANDLED BY THE COMPONENT

from dataclasses import dataclass
from pathlib import Path

#define the entity (what are the variable return by the component)

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path              # Where to store all artifacts related to data ingestion
    source_URL: str             # Where to download the data from (a remote URL)
    local_data_file: Path       # Path to save the downloaded ZIP file
    unzip_dir: Path             # Where to extract the contents of the ZIP


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list


#define the entity
@dataclass(frozen=True)
class DataTransformationConfig: 
    root_dir: Path
    data_path: Path
    tokenizer_name: Path
    
    
#entity
@dataclass(frozen=True)
class ModelTrainerConfig: 
    root_dir: Path 
    data_path: Path
    model_ckpt: Path
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    weight_decay: float
    logging_steps: int
   # evaluation_strategy: str
    eval_steps: int
    save_steps: float
    gradient_accumulation_steps: int
    
    
@dataclass(frozen=True)
class ModelEvaluationConfig: 
    root_dir: Path
    model_path: Path
    data_path: Path
    tokenizer_path: Path
    metric_file_name: Path
    