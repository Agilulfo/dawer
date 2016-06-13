import argparse

from dawer.image import ImagesHandler


def main():
    parser = argparse.ArgumentParser(
        description='Move images to subfolders of a collection'
    )
    parser.add_argument(
        'source_dir', metavar='path', type=str,
        help='path from where images are taken'
    )
    parser.add_argument(
        '--collection', dest='collection_path',
        metavar='path', type=str,
        help='collection path'
    )
    # parser.add_argument(
    #     '--test', dest='test', const=True,
    #     default=False, action='store_const'
    # )
    args = parser.parse_args()

    source = args.source_dir
    collection_path = args.collection_path or source
    # test = args.test

    images_handler = ImagesHandler(collection_path)
    images_handler.load_images_from_path(source)
    images_handler.move_images()


if __name__ == '__main__':
    main()
