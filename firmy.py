import place_map
import datetime
import pandas as pd
from pathlib import Path

import date_service
import insert_service

GMINA_ID = place_map.PLACE_MAP['Miasto Zamość']
date = datetime.datetime.now()
months = [f"{i:02d}" for i in range(1, 13)]

def run():
    file_name = 'Firmy.xlsx'

    project_root = Path(__file__).parent
    excel_path = project_root / 'Data' / file_name

    data_excel = pd.read_excel(excel_path, header=1)
    data_excel[['ULICE']] = (
        data_excel[['ULICE']].ffill()
    )

    data_excel = data_excel.dropna(subset=months, how='all')

    data_excel['daty_odbioru'] = data_excel.apply(date_service.build_dates_variant, axis=1)

    for _, row in data_excel.iterrows():
        insert = insert_service.build_insert(row, GMINA_ID)
        if insert:
            print(insert)