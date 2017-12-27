import json
import os


def load_config(obj):
    with open('config.json') as json_data_file:
        config = json.load(json_data_file)
        obj.images_input_path = config["images_input_path"]
        obj.images_output_path = config["images_output_path"]
        obj.quality = config["quality"]
        obj.extensions = config["extensions"]
        obj.scale = config["scale"]


def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
