import place_map
import datetime
import pandas as pd
from pathlib import Path

from Service import date_service, insert_service

GMINA_ID = place_map.PLACE_MAP['Miasto Zamość']
date = datetime.datetime.now()
months = ['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII']


def run(variant):

    match variant:
        case 1:
            file_name = 'Miasto1.xlsx'

            project_root = Path(__file__).parent.parent
            excel_path = project_root / 'Data' / file_name

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

            with open(f"{project_root}/Output/Miasto{date.year}_1.txt", 'w') as f:
                for _, row in data_excel.iterrows():
                    insert = insert_service.build_insert(row, GMINA_ID)
                    if insert:
                        print(insert)
                        print(insert, file=f)

        case 2:
            file_name = 'Miasto2.xlsx'

            project_root = Path(__file__).parent.parent
            excel_path = project_root / 'Data' / file_name

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

            with open(f"{project_root}/Output/Miasto{date.year}_2.txt", 'w') as f:
                for _, row in data_excel.iterrows():
                    insert = insert_service.build_insert(row, GMINA_ID)
                    if insert:
                        print(insert)
                        print(insert, file=f)