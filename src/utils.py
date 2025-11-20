import logging

import pandas as pd
from pandas import DataFrame

logger = logging.getLogger(__name__)


def reading_a_file() -> DataFrame:
    """Читает файл xlsx и возвращает DataFrame"""
    logger.info("Начало работы функции reading_a_file")
    path_to_file = "../data/operations.xlsx"  # путь к файлу
    df = pd.DataFrame()  # на всякий случай
    try:
        logger.debug("Чтение файла...")
        df = pd.read_excel(path_to_file)
        logger.info("Файл успешно прочитан")  # чтение файла
    except FileNotFoundError:  # ошибка файл не найден
        logger.error("Ошибка! Файл не найден")
        print("Файл не найден")
    logger.info("Конец работы функции reading_a_file")
    return df  # возвращает DataFrame, если ошибка, то возвращает пустой
