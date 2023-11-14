import unittest
import os


def create_mini_batches(directory, batch_size):
    if not os.path.exists(directory):
        return None

    files = os.listdir(directory)
    batches = []

    for i in range(0, len(files), batch_size):
        batch = files[i:i + batch_size]
        batches.append(batch)

    return batches


class TestCreateMiniBatches(unittest.TestCase):
    def test_create_mini_batches_correctly(self):
        # Тестирование, что функция правильно формирует мини-пакеты для заданного каталога и размера пакета.
        directory = 'C:/Users/ivanc/PycharmProjects/Lab6/batches'
        batch_size = 2
        expected_batches = [['file1.txt', 'file2.txt'], ['file3.txt', 'file4.txt'], ['file5.txt']]
        actual_batches = create_mini_batches(directory, batch_size)
        self.assertEqual(actual_batches, expected_batches)

    def test_create_mini_batches_empty_directory(self):
        # Тестирование, что функция вернет пустой список, если каталог пуст.
        directory = 'C:/Users/ivanc/PycharmProjects/Lab6/empty'
        batch_size = 2
        expected_batches = []
        actual_batches = create_mini_batches(directory, batch_size)
        self.assertEqual(actual_batches, expected_batches)

    def test_create_mini_batches_smaller_batch_size(self):
        # Тестирование, что функция правильно формирует мини-пакеты, если размер пакета больше, чем количество файлов.
        directory = 'C:/Users/ivanc/PycharmProjects/Lab6/batches'
        batch_size = 10
        expected_batches = [['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt', 'file5.txt']]
        actual_batches = create_mini_batches(directory, batch_size)
        self.assertEqual(actual_batches, expected_batches)

    def test_create_mini_batches_nonexistent_directory(self):
        # Тестирование, что функция вернет None, если каталог не существует.
        directory = 'C:/Users/ivanc/PycharmProjects/Lab6/nonexistent_directory'
        batch_size = 2
        actual_batches = create_mini_batches(directory, batch_size)
        self.assertIsNone(actual_batches)


if __name__ == '__main__':
    unittest.main()
