import pandas as pd

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


# Funkcja przyjmuje nazwe opdadu w formie kodu lub nazwy (tych z bazy)
# po czym zamienie je na ich id i zwraca
def resolve_waste_id(value:str):
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