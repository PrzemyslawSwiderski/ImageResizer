from image_resizer import ImageResizer


def main():
    image_resizer = ImageResizer()
    image_resizer.compress_all_files()
    print("Images compression done")


if __name__ == "__main__":
    main()
