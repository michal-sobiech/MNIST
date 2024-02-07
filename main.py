from configparser import ConfigParser
from DatasetReader import DatasetReader
from typing import Final
from os import path


def main():
    WORK_DIR = path.abspath(path.dirname(__file__))
    CONFIG_FN = 'config.ini'
    ABS_CFG_PATH  = path.join(WORK_DIR, CONFIG_FN)

    # Load the config
    config = ConfigParser()
    config.read(ABS_CFG_PATH)
    settings = config['Settings']

    DATASET_PATH = path.join(WORK_DIR, settings['dataset_path'])
    TRAINING_IMAGES_FN = settings['training_images_fn']
    TRAINING_LABELS_FN = settings['training_labels_fn']
    TEST_IMAGES_FN = settings['test_images_fn']
    TEST_LABELS_FN = settings['test_labels_fn']
    BATCH_SIZE = settings['batch_size']

    # Dataset
    datasetReader = DatasetReader(
        training_images_path=path.join(DATASET_PATH, TRAINING_IMAGES_FN),
        training_labels_path=path.join(DATASET_PATH, TRAINING_LABELS_FN),
        test_images_path=path.join(DATASET_PATH, TEST_IMAGES_FN),
        test_labels_path=path.join(DATASET_PATH, TEST_LABELS_FN)
    )

    # training_data = datasetReader.get_training_data()
    # datasetReader.test()




if __name__ == '__main__':
    main()
