import glob
import ntpath
import os

from PIL import Image

from src.helpers import ensure_dir


class ImageResizer:
    def __init__(self):
        self.images_input_path = "./images_to_resize"
        self.images_output_path = "./resized_images"
        self.quality = 75
        self.extensions = ("jpg", "jpeg", "png", "gif", "ico", "im", "bmp", "eps", "eps", "tiff", "psd", "msd")
        self.input_files = []
        self.scale = 1.0

    def get_images_file_names(self, path):
        """
        Method returns list of image files grabbed by specified extensions

        :param path:
        """
        files_grabbed = []
        for extension in self.extensions:
            files_grabbed.extend(glob.glob(path + os.sep + "*." + extension))
        return files_grabbed

    def compress_all_files(self):
        """
        Method compressing all files in loop
        """
        input_files = self.get_images_file_names(self.images_input_path)
        for file in input_files:
            self.compress(file)

    def compress(self, file_name):
        """
        Image compressing method

        :param file_name:
        """
        old_size = os.stat(file_name).st_size
        picture = Image.open(file_name)

        file_path = self.images_output_path + os.sep + ntpath.basename(file_name)

        ensure_dir(file_path)
        new_scale = (int(picture.size[0] * self.scale), int(picture.size[1] * self.scale))
        picture = picture.resize(new_scale, Image.ANTIALIAS)
        picture.save(file_path, optimize=True, quality=self.quality)

        new_size = os.stat(file_path).st_size
        percent = round((old_size - new_size) / float(old_size) * 100,2)
        print(f"File {file_name} size changed from {old_size} to {new_size} by {percent}%")

    def config_from_command_line(self, config):
        """
        Image resizer configuration load from command line args

        :param config:
        """
        self.images_input_path = self.images_input_path if "images_input_path" not in config else config[
            "images_input_path"]
        self.images_output_path = self.images_output_path if "images_output_path" not in config else config[
            "images_output_path"]
        self.quality = self.quality if "quality" not in config else int(config["quality"])
        self.scale = self.scale if "scale" not in config else float(config["scale"])

    def print_compression_parameters(self):
        """
        Method prints current ImageResizer object's parameters

        """
        print("ImageResizer object's parameters")
        print(f"images_input_path: {self.images_input_path}")
        print(f"images_output_path: {self.images_output_path}")
        print(f"quality: {self.quality}")
        print(f"scale: {self.scale}")
