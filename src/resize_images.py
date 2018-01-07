#!/usr/bin/python
import getopt
import sys

from src.image_resizer import ImageResizer


def main(argv):
    help_message = """
usage: resize_images [options]

Options: 
    -h                                  display help
    -i, --input_path <arg> 				input path of directory with images to be processed (default = "./images_to_resize")
    -o, --output_path <arg> 			output path of directory where compressed images will be stored (default = "./resized_images")
    -s, --output_scale <arg> 			scale of output images (default = 1.0)
    -q, --output_quality <arg> 			scale of output images (default = 75)
"""
    config = {}
    try:
        opts, args = getopt.getopt(argv, "hi:o:s:q:",
                                   ["input_path=", "output_path=", "output_scale=", "output_quality="])
    except getopt.GetoptError:
        print(help_message)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(help_message)
            sys.exit()
        elif opt in ("-i", "--input_path"):
            config["input_path"] = arg
        elif opt in ("-o", "--output_path"):
            config["output_path"] = arg
        elif opt in ("-s", "--output_scale"):
            config["scale"] = arg
        elif opt in ("-q", "--output_quality"):
            config["quality"] = arg
    image_resizer = ImageResizer()
    image_resizer.config_from_command_line(config)
    image_resizer.print_compression_parameters()
    image_resizer.compress_all_files()
    print("Images compression done")


if __name__ == "__main__":
    main(sys.argv[1:])
