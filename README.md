# OPIS PROJEKTU
Skrypt służy do przetwarzania plików Excel z harmonogramem odbioru odpadów i generowania plików .txt
zawierających zapytania SQL typu INSERT.

## WYMAGANIA

- Python 3.14+
- pip

## INSTALACJA

1. Sklonuj repozytorium.
2. Wejdź do katalogu projektu.
3. Utwórz środowisko wirtualne:  
	python -m venv .venv
4. Aktywuj środowisko:  
	.\.venv\Scripts\activate
5. Zainstaluj zależności:  
	pip install -r requirements.txt


## STRUKTURA KATALOGÓW
<pre>
Harmonogram/
│
├── Data/        -> tutaj wrzucamy pliki Excel
├── Output/      -> tutaj generowane są pliki .txt z INSERT-ami
├── Service/     -> logika przetwarzania
├── main.py      -> punkt startowy
└── requirements.txt	-> plik zawierający potrzebne zależności
</pre>


## JAK UŻYWAĆ

1. Wrzucić pliki Excel do folderu Data/
2. Uruchomić:
	python main.py
3. Wygenerowane pliki .txt pojawią się w folderze Output/


## UWAGI

- Pliki Excel muszą mieć zgodną strukturę kolumn.
- W przypadku zmiany layoutu może być konieczna modyfikacja serwisów przetwarzających dane.
- Akceptowane nazwy plików Excela to: Firmy.xlsx, GminaZamosc.xlsx, Labunie.xlsx, Miasto1.xlsx,
  Miasto2.xlsx, Skierbieszow.xlsx
