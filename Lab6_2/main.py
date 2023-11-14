import unittest
from pandas._testing import assert_frame_equal
import pandas as pd
from sqlalchemy import create_engine


def read_annotations(source, source_type, columns=None, filter=None):
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


class TestReadAnnotations(unittest.TestCase):
    def test_read_csv_file(self):
        # Тестирование чтения CSV-файла
        source = 'data.csv'
        source_type = 'csv'
        expected_df = pd.read_csv(source)
        actual_df = read_annotations(source, source_type)
        assert_frame_equal(actual_df, expected_df)

    def test_read_excel_file(self):
        # Тестирование чтения Excel-файла
        source = 'data.xlsx'
        source_type = 'excel'
        expected_df = pd.read_excel(source, engine='openpyxl')
        actual_df = read_annotations(source, source_type)
        assert_frame_equal(actual_df, expected_df)

    def test_read_json_file(self):
        # Тестирование чтения JSON-файла
        source = 'data.json'
        source_type = 'json'
        expected_df = pd.read_json(source)
        actual_df = read_annotations(source, source_type)
        assert_frame_equal(actual_df, expected_df)

    def test_unsupported_datatype(self):
        # Тестирование, что функция вызывает ValueError при передаче неподдерживаемого типа источника данных
        source = 'data.txt'
        source_type = 'txt'
        with self.assertRaises(ValueError):
            read_annotations(source, source_type)


if __name__ == '__main__':
    unittest.main()
