# ImageResizer
Python script to resize images. 

It takes as input all image files from configured path, 
resizes them and saves to output path.

## Execute parameters
To change script parameters, pass correct option in command line:
````
usage: resize_images [options]
Options: 
    -h                                  display help
    -i, --input_path <arg> 	        input path of directory with images 
                                        to be processed (default = "./images_to_resize")
    -o, --output_path <arg> 		output path of directory where compressed images
                                        will be stored (default = "./resized_images")
    -s, --output_scale <arg> 		scale of output images (default = 1.0)
    -q, --output_quality <arg> 		scale of output images (default = 75)
````
## External packages
* Pillow '1.1.7'

## Windows Executable
Converting script to exe file was done by ``pyinstaller -F src/resize_images.py`` command.

Exe can be find at this [link](https://drive.google.com/open?id=1FacohH4-RKWAzrhEENNli7immRXlQySB).

## EXE file usage
* Insert photos you want to have smaller size to images_to_resize folder. 
* Run resize_images.exe
* View output files in output_images folder

