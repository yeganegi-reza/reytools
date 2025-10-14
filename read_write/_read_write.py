import sys
import yaml
import json
import dill
import base64

from typing import Any
from pathlib import Path
from ensure import ensure_annotations
from box import ConfigBox

from reytools.logger import logging
from reytools.exception import CustomException


@ensure_annotations
def read_yaml(path_to_yaml: Path, verbose=True) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            if verbose:
                logging.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except Exception as e:
        raise CustomException(e, sys)


@ensure_annotations
def write_json(path: Path, data: dict, verbos=True):
    """write dic file to json

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    if verbos:
        logging.info(f"json data saved to: {path}")


def write_binary(path: Path, data, verbos=True):
    """write a data as binary file 

    Args:
        path (Path): path to save the data
        data : data to be saved in the path
    """
    with open(path, "wb") as f:
        f.write(data)
    if verbos:
        logging.info(f"Data saved as binary to: {path}")


@ensure_annotations
def read_json(path: Path, verbose=True) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)
    if verbose:
        logging.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path, verbose=True):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    dill.dump(value=data, filename=path)
    if verbose:
        logging.info(f"binary file saved at: {path}")


@ensure_annotations
def read_bin(path: Path, verbose=True) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = dill.load(path)
    if verbose:
        logging.info(f"binary file loaded from: {path}")
    return data


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, "wb") as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
