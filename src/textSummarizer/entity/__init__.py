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
