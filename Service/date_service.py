import datetime
import pandas as pd
import re


date = datetime.datetime.now()


MONTH_MAP = {
    'I': '01',
    'II': '02',
    'III': '03',
    'IV': '04',
    'V': '05',
    'VI': '06',
    'VII': '07',
    'VIII': '08',
    'IX': '09',
    'X': '10',
    'XI': '11',
    'XII': '12'
}


# Funkcja pobiera dni z każdego kolejnego miesiąca w kolumnach excela i tworzy z niego format daty
def build_dates(row, year=date.year):
    dates = []

    for month_roman, month_num in MONTH_MAP.items():
        value = row[month_roman]

        if pd.isnull(value):
            continue

        days = [
            int(d) for d in re.findall(r'\d+', str(value))
            if int(d) > 0
        ]

        for day in days:
            day = int(float(day))
            dates.append(f"{year}-{month_num}-{day:02d}")

    return " ".join(dates)


# Wersja build_dates gdy w excelu są podane miesiące numerami arabskimi
def build_dates_variant(row, year=date.year):
    dates = []

    months = [f"{i:02d}" for i in range(1, 13)]

    for months_num in months:
        value = row[months_num]

        if pd.isnull(value):
            continue

        days = [int(d) for d in re.findall(r'\d+', str(value)) if int(d) > 0]

        for day in days:
            dates.append(f"{year}-{months_num}-{day:02d}")

    return " ".join(dates)