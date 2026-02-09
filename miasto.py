import place_map
import datetime
import pandas as pd
from pathlib import Path
import re

import date_service
import insert_service


GMINA_ID = place_map.PLACE_MAP['Miasto Zamość']
date = datetime.datetime.now()
months = ['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII']

def run(variant):

    match variant:
        case 1:
            project_root = Path(__file__).parent
            excel_path = project_root / 'Data' / 'Miasto1.xlsx'

            data_excel = pd.read_excel(excel_path, header=3)
            data_excel[['ULICE']] = (
                data_excel[['ULICE']].ffill()
            )

            # Jesli kilka ulic wpisane w jednej komorce dziele na oddzielne wiersze
            data_excel['ULICE'] = (
                data_excel['ULICE']
                    .astype(str)
                    .str.split(r'\s*,\s*')
            )
            data_excel = data_excel.explode('ULICE')

            data_excel = data_excel.dropna(subset=months, how='all')

            data_excel['daty_odbioru'] = data_excel.apply(date_service.build_dates, axis=1)

            for _, row in data_excel.iterrows():
                insert = insert_service.build_insert(row, GMINA_ID)
                if insert:
                    print(insert)

        case 2:
            project_root = Path(__file__).parent
            excel_path = project_root / 'Data' / 'Miasto2.xlsx'

            data_excel = pd.read_excel(excel_path, header=1)
            data_excel['ULICE'] = (
                data_excel['ULICE'].ffill()
            )

            # Jesli kilka ulic wpisane w jednej komorce dziele na oddzielne wiersze
            data_excel['ULICE'] = (
                data_excel['ULICE']
                .astype(str)
                .str.split(r'\s*,\s*')
            )
            data_excel = data_excel.explode('ULICE')

            data_excel = data_excel.dropna(subset=months, how='all')

            data_excel['daty_odbioru'] = data_excel.apply(date_service.build_dates, axis=1)

            for _, row in data_excel.iterrows():
                insert = insert_service.build_insert(row, GMINA_ID)
                if insert:
                    print(insert)