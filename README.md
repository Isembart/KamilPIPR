#### Kamil Troszczyński
# Gra *Text adventure game*

## Informacje wstępne
Gra *Text adventure game* to gra przygodowa, gdzie jako główny bohater Edgar możemy poruszać się po mapie opisanej tekstem, przemieszczając się do danych lokacji, w których możemy znaleźć ciekawe postacie, ale również i wrogów. Wszystkie mapy i interakcje z postaciami są opisane tekstowo w terminalu.

## Wymagane moduły
#### pynput: Wymagany do płynnego wyświetlania teksut
- Instalacja: ```pip install pynput 

## Uruchamianie i wyłączanie gry
Aby uruchomić grę, należy przejść do folderu, gdzie znajdują się wszystkie potrzebne pliki. Następnie, należy uruchomić terminal i wpisać w nim komendę Interfejs.py aby gra się w nim uruchomiła. Inną opcją jest kliknięcie ikonki *"Run Python"*, która również powinna uruchomić menu danej gry. Jeśli chcemy zagrać w grę od początku należy wpisać *"new game"*, a jeśli chcemy załadować grę od momentu ostatniego zapisu tej gry to wtedy należy wpisać *"Load game"*, a następnie wybrać numerek ostatniego save'a. Jeżeli chcemy zakończyć grę należy wpisać komendę *"exit"* i wtedy znajdujemy się z powrotem w terminalu.

## Zasady gry
Poruszamy się postacią o imieniu Edgar. Musimy odnaleźć dwa szukane przedmioty, by zakończyć gre. Będziemy natrafiali na sojuszników, ale i na wrogów. Celem jest zabicie potworów, aby można było przechodzić do dalszych lokacji.

## Pliki z grą

#### Pliki, które są składową danej gry to:
- PlayerClass.py
- EnemyClass.py
- LocationClass.py
- GameClass.py
- Intefejs.py
- delayedPrint.py
- Constructor.json
- test_PlayerClass.py
- test_EnemyClass.py
- test_LocationClass.py


