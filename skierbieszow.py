import pandas as pd
import datetime

import insert_service
import place_map
import date_service

from pathlib import Path

GMINA_ID = place_map.PLACE_MAP['Gmina Skierbieszów']
date = datetime.datetime.now()
months = ['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII']

def run():
    file_name = 'Skierbieszow.xlsx'

    project_root = Path(__file__).parent
    excel_path = project_root / 'Data' / file_name

    data_excel = pd.read_excel(excel_path, header=1)
    data_excel[['Miejscowości']] = (
        data_excel[['Miejscowości']].ffill()
    )

    data_excel = data_excel.dropna(subset=months, how='all')

    data_excel['daty_odbioru'] = data_excel.apply(date_service.build_dates, axis=1)

    for _, row in data_excel.iterrows():
        insert = insert_service.build_insert(row, GMINA_ID)
        if insert:
            print(insert)