from typing import Final, Dict, List
from io import TextIOWrapper
import numpy as np
from numpy.typing import NDArray


class DatasetReader:
    TRAINING_IMAGES_PATH: Final[str] = None
    TRAINING_LABELS_PATH: Final[str] = None
    TEST_IMAGES_PATH: Final[str] = None
    TEST_LABELS_PATH: Final[str] = None

    def __init__(self,
                 training_images_path: str,
                 training_labels_path: str,
                 test_images_path: str,
                 test_labels_path: str) -> None:
        self.TRAINING_IMAGES_PATH = training_images_path
        self.TRAINING_LABELS_PATH = training_labels_path
        self.TEST_IMAGES_PATH = test_images_path
        self.TEST_LABELS_PATH = test_labels_path

    def get_training_data(self) -> list[dict[int, NDArray]]:
        labels = self.__get_training_labels()
        images = self.__get_training_images_monochrome()

        data = []
        for label, image in zip(labels, images):
            data.append({
                'label': label,
                'image': image
            })
        return data

    def __get_images(self, image_file_path: str) -> NDArray:
        with open(image_file_path, 'rb') as handle:
            _ = self.__read_4_bytes(handle)
            image_count = self.__read_4_bytes(handle)
            row_count = self.__read_4_bytes(handle)
            column_count = self.__read_4_bytes(handle)
            pixel_data_buffer = handle.read()

            pixel_data_array = np.frombuffer(pixel_data_buffer, dtype=np.uint8)
            images = np.reshape(pixel_data_array,
                                (image_count, row_count, column_count))
            return images

    def __get_images_monochrome(self, image_file_path: str) -> NDArray:
        images = self.__get_images(image_file_path)
        return np.where(images > 127, 1, 0)

    def __get_training_images_monochrome(self) -> NDArray:
        return self.__get_images_monochrome(self.TRAINING_IMAGES_PATH)

    def __get_test_images_monochrome(self) -> NDArray:
        return self.__get_images_monochrome(self.TEST_IMAGES_PATH)

    def __get_labels(self, label_file_path: str) -> NDArray:
        with open(label_file_path, 'rb') as handle:
            _ = self.__read_4_bytes(handle)
            _ = self.__read_4_bytes(handle)
            label_data_buffer = handle.read()

            label_array = np.frombuffer(label_data_buffer, dtype=np.uint8)
            return label_array

    def __get_training_labels(self) -> NDArray:
        return self.__get_labels(self.TRAINING_LABELS_PATH)

    def __get_test_labels(self) -> NDArray:
        return self.__get_labels(self.TRAINING_LABELS_PATH)

    def __read_4_bytes(self, handle: TextIOWrapper) -> int:
        return int.from_bytes(handle.read(4), 'big')

    def test(self):
        data: List[Dict[int, NDArray]] = self.get_training_data()
        for i in range(5):
            sample = data[np.random.randint(0, 10_000)]
            print(f'Number shown: {sample["label"]}')
            print()
            print(np.where(sample['image'] == 1, '#', '.'))
            # print(sample['image'])
            print()
            print("===================")
