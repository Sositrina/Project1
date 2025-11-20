import json

import pandas as pd

from src.utils import reading_a_file

# Загрузка DataFrame
df = reading_a_file()


def profitable_cashback_categories(data: pd.DataFrame, year: str, month: str) -> str :
    data["Дата платежа"] = pd.to_datetime(data["Дата платежа"], format="%d.%m.%Y")

    # фильтрация по году и месяцу
    filtered_data = data[(data["Дата платежа"].dt.year == int(year)) & (data["Дата платежа"].dt.month == int(month))]

    # группировка по категории и общая сумма кэша с округлением
    result = filtered_data.groupby("Категория")["Кэшбэк"].sum().round().astype(int)

    return json.dumps(result.to_dict(), ensure_ascii=False, indent=2)


res = profitable_cashback_categories(df, "2021", "03")
