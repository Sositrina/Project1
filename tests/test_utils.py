from unittest.mock import patch

from src.utils import reading_a_file


# тест функции reading_a_file
def test_reading_a_file_file_not_found() -> None:
    """Тест на ошибку FileNotFound,должен возвращаться пустой DataFrame"""
    with patch("src.utils.pd.read_excel") as mock_read_excel:  # патчит чтение файла
        mock_read_excel.side_effect = FileNotFoundError  # настройка мок
        result = reading_a_file()  # вызов функции
        assert len(result) == 0
