import os
import zipfile
from pathlib import Path

from ensure import ensure_annotations
from reytools.logger import logging


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
            if verbose:
                logging.info(f"Created directory at: {path}")
        else:
            if verbose:
                logging.info(f"Path: {path} already exists")


@ensure_annotations
def get_file_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"


@ensure_annotations
def unzip_file(src_path: Path, des_path: Path, verbose=True):
    """Unzip a file from source path to the destination path
    Args:
        src_path (Path): path of the zip file
        des_path (Path): destication path to extract to
    """
    with zipfile.ZipFile(src_path, "r") as zip_file:
        zip_file.extractall(des_path)
