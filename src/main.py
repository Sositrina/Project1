import logging
import os

from pandas import DataFrame

from src.services import profitable_cashback_categories
from src.utils import reading_a_file

# Настройка логгера
log_path = os.path.join(os.path.dirname(__file__), "..", "logs", "example.log")
os.makedirs(os.path.dirname(log_path), exist_ok=True)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s: %(message)s",
    handlers=[
        logging.FileHandler(log_path, encoding="utf-8", delay=False),
    ],
)


def main()-> None:
    df: DataFrame = reading_a_file()
    result1 = profitable_cashback_categories(df, "2021", "03")
    return result1


if __name__ == "__main__":
    main()


def main():
    # Чтение данных
    df = reading_a_file()

    # Анализ разных периодов
    print("Анализ кешбэка за март 2021:")
    result1 = profitable_cashback_categories(df, "2021", "03")
    print(result1)


if __name__ == "__main__":
    main()
