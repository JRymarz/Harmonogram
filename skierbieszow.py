import pandas as pd
import datetime
import re

from pathlib import Path


PLACE_MAP = {
    'Miasto Zamość' : '1',
    'Gmina Zamość' : '2',
    'Gmina Łabunie' : '3',
    'Gmina Skierbieszów' : '4',
    'Gmina Sułów' : '5',
    'Gmina Grabowiec' : '6'
}

WASTE_MAP = {
    'SB' : '8',
    'OP' : '1',
    'MA' : '3',
    'ME' : '4',
    'S' : '11',
    'E' : '10',
    'MB' : '13',
    'GR' : '15',
    'B' : '2',
    'D' : '12',
    'SM' : '9',
    'P' : '7',
    'O' : '6',
    'G' : '5',
    'NS' : '14'
}

WASTE_MAP_KEY = {
    'Żużyte opony' : 'OP',
    'Odpady ulegające biodegradacji' : 'B',
    'Opakowania z papieru i tektury' : 'MA',
    'Opakowania z metali' : 'ME',
    'Odpady wielkogabarytowe' : 'G',
    'Niesegregowane (zmieszane) odpady komunalne' : 'O',
    'Opakowania z tworzyw sztucznych i metali' : 'P',
    'Szkło białe' : 'SB',
    'Opakowania ze szkła oraz z papieru i tektury' : 'SM',
    'Zuzyty sprzęt elektryczny i elektroniczny' : 'E',
    'Opakowania ze szkła' : 'S',
    'Inne niewymienione frakcje zbierane w sposób selektywny' : 'D',
    'Opakowania z papieru i tektury oraz odpady ulegające biodegradacji' : 'MB',
    'Zmieszane niesegregowane' : 'NS',
    'Gruz' : 'G'
}

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


date = datetime.datetime.now()

# Funkcja pobiera dni z każdego kolejnego miesiąca w kolumnach excela i tworzy z niego format daty
def buildDates(row, year=date.year):
    dates = []

    for monthRoman, monthNum in MONTH_MAP.items():
        value = row[monthRoman]

        if pd.isnull(value):
            continue

        days = [
            int(d) for d in re.findall(r'\d+', str(value))
            if int(d) > 0
        ]

        for day in days:
            day = int(float(day))
            dates.append(f"{year}-{monthNum}-{day:02d}")

    return " ".join(dates)


# Funkcja przyjmuje nazwe opdadu w formie kodu lub nazwy (tych z bazy)
# po czym zamienie je na ich id i zwraca
def resolveWasteId(value:str):
    if pd.isnull(value):
        return None

    value = value.strip()
    # Gdy jest podany kod
    if value in WASTE_MAP:
        return WASTE_MAP[value]

    #Gdy jest podana nazwa
    if value in WASTE_MAP_KEY:
        code = WASTE_MAP_KEY[value]
        return WASTE_MAP.get(code)


projectRoot = Path(__file__).parent
excelPath = projectRoot / 'Data' / 'Data.xlsx'

dataExcel = pd.read_excel(excelPath, header=1)
dataExcel[['Miejscowości']] = (
    dataExcel[['Miejscowości']].ffill()
)

months = ['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII']
dataExcel = dataExcel.dropna(subset=months, how='all')

dataExcel['daty_odbioru'] = dataExcel.apply(buildDates, axis=1)

print(dataExcel[['Miejscowości', 'Rodzaj odpadów', 'daty_odbioru']])


