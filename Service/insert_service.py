from Service import waste_service
import datetime

year = datetime.datetime.now().year

def build_insert(row, GMINA_ID):
    place = row['Miejscowości'] if 'Miejscowości' in row else row['ULICE']
    wastes_raw = row['Rodzaj odpadów']
    dates = row['daty_odbioru']

    if not dates:
        return None

    waste_id = waste_service.resolve_waste_id(wastes_raw)

    insert = (
        "INSERT INTO harmonogram_ogolny \n"
        "(zablokowany, rok, gmina, rodzaj_selekcji, o_rejon, daty_odbioru, "
        "created_by_user, created_date, modified_by_user, modified_date, czy_firma) \n"
        'VALUES '
        f"(0,{year},{GMINA_ID},{waste_id},"
        f"'{place}', '{dates}',"
        "'import',NOW(),'import',NOW(),0);\n"
    )

    return insert