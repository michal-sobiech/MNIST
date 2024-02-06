from configparser import ConfigParser
from DatasetReader import DatasetReader
from typing import Final
from os import path


def main():
    configParser = ConfigParser()
    configParser.read('config.json')
    DATASET_PATH: Final[str] = path.abspath(configParser['dataset_path'])
    TRAINING_IMAGES_FN: Final[str] = configParser['training_images_fn']
    TRAINING_LABELS_FN: Final[str] = configParser['training_labels_fn']
    TEST_IMAGES_FN: Final[str] = configParser['test_images_fn']
    TEST_LABELS_FN: Final[str] = configParser['test_labels_fn']

    datasetReader = DatasetReader(
        training_images_path=path.join(DATASET_PATH, TRAINING_IMAGES_FN),
        training_labels_path=path.join(DATASET_PATH, TRAINING_LABELS_FN),
        test_images_path=path.join(DATASET_PATH, TEST_IMAGES_FN),
        test_labels_path=path.join(DATASET_PATH, TEST_LABELS_FN)
    )


if __name__ == '__main__':
    main()
