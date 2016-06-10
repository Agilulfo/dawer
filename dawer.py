import argparse

from dawer.image import ImagesHandler


def main():
    parser = argparse.ArgumentParser(
        description='Move images to subfolders by date'
    )
    parser.add_argument(
        'source_dir', metavar='path', type=str,
        help='path from where images are taken'
    )
    parser.add_argument(
        '--dest', dest='destination_dir',
        metavar='path', type=str,
        help='destination path'
    )
    parser.add_argument(
        '--test', dest='test', const=True,
        default=False, action='store_const'
    )
    args = parser.parse_args()

    source = args.source_dir
    destination = args.destination_dir or source
    test = args.test

    images_handler = ImagesHandler(destination)
    images_handler.load_images_from_path(source)
    images_handler.move_images()


if __name__ == '__main__':
    main()
