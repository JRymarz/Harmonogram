import place_map
import datetime
import pandas as pd
from pathlib import Path

import date_service
import insert_service


GMINA_ID = place_map.PLACE_MAP['Miasto Zamość']
date = datetime.datetime.now()
months = ['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII']

def run():
    project_root = Path(__file__).parent
    excel_path = project_root / 'Data' / 'Miasto.xlsx'

    data_excel = pd.read_excel(excel_path, header=3)
    data_excel[['ULICE']] = (
        data_excel[['ULICE']].ffill()
    )

    mask = data_excel['Rodzaj odpadów'].isna() & data_excel['Unnamed: 1'].notna()
    data_excel.loc[mask, 'Rodzaj odpadów'] = data_excel.loc[mask, 'Unnamed: 1']
    data_excel = data_excel.drop(columns=['Unnamed: 1'])

    print(data_excel[['Rodzaj odpadów']])

    data_excel['daty_odbioru'] = data_excel.apply(date_service.build_dates, axis=1)

    # print(data_excel[['ULICE', 'Rodzaj odpadów', 'daty_odbioru']])

    # for _, row in data_excel.iterrows():
    #     insert = insert_service.build_insert(row, GMINA_ID)
    #     if insert:
    #         print(insert)