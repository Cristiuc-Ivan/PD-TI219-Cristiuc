import pandas as pd
from sqlalchemy import create_engine
import os


def create_mini_batches(directory, batch_size):
    """
    Создает мини-батчи из данных, сохраненных в указанной директории.

    Args:
        directory (str): Путь к директории, содержащей данные.
        batch_size (int): Размер каждого мини-батча.

    Returns:
        list: Список мини-батчей. Каждый элемент списка - список данных из файлов в мини-батче.

    Note:
        Функция перебирает файлы в указанной директории и читает их содержимое.
        Затем данные собираются в мини-батчи. Вы должны настроить чтение и обработку данных в соответствии с форматом, используемым в ваших файлах.
    """

    data_files = os.listdir(directory)
    batches = []

    for i in range(0, len(data_files), batch_size):
        batch_data = []
        for j in range(i, min(i + batch_size, len(data_files))):
            file_path = os.path.join(directory, data_files[j])

            with open(file_path, 'r') as file:
                content = file.read()

        batches.append(batch_data)

    return batches


def read_annotations(source, source_type, columns=None, filter=None):
    """
    Функция для чтения аннотаций из различных источников и преобразования их в DataFrame.

    Args:
        source (str): Путь к источнику данных (файл CSV, Excel, JSON или строка соединения с SQL базой данных).
        source_type (str): Тип источника данных ('csv', 'excel', 'json', 'sql').
        columns (list): Список столбцов для выбора. По умолчанию - все столбцы.
        filter (str): SQL-подобное условие для фильтрации данных. Например, "age > 30".

    Returns:
        pandas.DataFrame: DataFrame с аннотациями, считанными из выбранного источника данных.

    Raises:
        ValueError: Если указанный тип источника данных не поддерживается.

    Note:
        Эта функция позволяет читать аннотации из разных форматов данных (CSV, Excel, JSON, SQL).
        Вы можете задать параметры columns и filter, чтобы выбрать определенные столбцы и фильтровать данные.
    """

    if source_type == 'csv':
        df = pd.read_csv(source)

    elif source_type == 'excel':
        df = pd.read_excel(source)

    elif source_type == 'json':
        df = pd.read_json(source)

    elif source_type == 'sql':
        engine = create_engine(source)

        query = "SELECT * FROM table_name"
        if columns:
            query = f"SELECT {', '.join(columns)} FROM table_name"
        if filter:
            query += f" WHERE {filter}"

        df = pd.read_sql(query, engine)

    else:
        raise ValueError("This datatype is not supported")

    return df


# data_directory = 'C:/Users/ivanc/PycharmProjects/Lab2/dataset/rose'
# batch_size = 32
#
# mini_batches = create_mini_batches(data_directory, batch_size)
#
# for i, mini_batch in enumerate(mini_batches):
#     print(f"Mini-batch {i+1}: {mini_batch}")

data = read_annotations('data.csv', source_type='csv', columns=['Absolute Path', 'Relative Path', 'Class Label'])
print(data)
