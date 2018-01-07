import os


def ensure_dir(dir_name):
    """
    Function checks if there is a directory with specified dir_name
    if not, it is not existing, dir structure is created

    :param dir_name:
    """
    directory = os.path.dirname(dir_name)
    if not os.path.exists(directory):
        os.makedirs(directory)
