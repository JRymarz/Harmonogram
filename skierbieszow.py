import pandas as pd

from pathlib import Path

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

# zrob year by nie bylo magic number
def buildDates(row, year=2026):
    dates = []

    for monthRoman, monthNum in MONTH_MAP.items():
        value = row[monthRoman]

        if pd.isnull(value):
            continue

        days = str(value).replace('.', ' ').split()

        for day in days:
            day = int(float(day))
            dates.append(f"{year}-{monthNum}-{day:02d}")

    return " ".join(dates)


projectRoot = Path(__file__).parent
excelPath = projectRoot / 'Data' / 'Data.xlsx'

dataExcel = pd.read_excel(excelPath, header=1)
dataExcel[['Miejscowości']] = (
    dataExcel[['Miejscowości']].ffill()
)

months = ['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII']
dataExcel = dataExcel.dropna(subset=months, how='all')

dataExcel['daty_odbioru'] = dataExcel.apply(buildDates, axis=1)

# Uwaga bo mam printy jakich dni zerowych w kazdym miesciacu
print(dataExcel[['Miejscowości', 'Rodzaj odpadów', 'daty_odbioru']])

# print(dataExcel)


