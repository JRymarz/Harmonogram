import pandas as pd

from pathlib import Path

projectRoot = Path(__file__).parent
excelPath = projectRoot / 'Data' / 'Data.xlsx'

dataExcel = pd.read_excel(excelPath, header=1)
dataExcel[['Miejscowości']] = (
    dataExcel[['Miejscowości']].ffill()
)

months = ['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII']
dataExcel = dataExcel.dropna(subset=months, how='all')

print(dataExcel)
# print(dataExcel.columns)


