import ast

import yaml


class MongoConfig:

    def __init__(self, config):

        self.db_connection_string = config["db_connection_string"]
        self.db_name = config["db_name"]
        self.db_collection_name = config["document_collection_name"]

class InputConfig:

    def __init__(self, config):

        self.input_file_path = config["input_file_path"]
        self.pickle_file_path = config["pickle_file_path"]
        self.blob_file_download_path = config["blob_file_download_path"]

class DownloadProperties:

    def __init__(self, config):

        self.video = ast.literal_eval(config["video"])
        self.image = ast.literal_eval(config["image"])
        self.text = ast.literal_eval(config["text"])
        self.binary = ast.literal_eval(config["binary"])




class Student:

    def __init__(self, config):
        self.name = config["name"]
        self.location = config["location"]

class Config:

    def __init__(self,config_file_path):

        config = read_config(config_file_path)
        if config is not None:
            self.db = MongoConfig(config["database"])
            self.student = Student(config["student"])
            self.files = InputConfig(config["file_config"])
            self.download_properties = DownloadProperties(config["download_properties"])

def read_config(config_file_path):

    with open(config_file_path, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
        return None