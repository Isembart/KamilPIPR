### Kamil Troszczyński
# Gra *Text adventure game*

## Informacje wstępne
Gra *Text adventure game* to gra przygodowa, gdzie jako główny bohater Edgar możemy poruszać się po mapie opisanej tekstem, przemieszczając się do danych lokacji, w których możemy znaleźć ciekawe postacie, ale również i wrogów. Wszystkie mapy i interakcje z postaciami są opisane tekstowo w terminalu.

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
- Interfejs.py
- delayedPrint.py
- Constructor.json
- test_PlayerClass.py
- test_EnemyClass.py
- test_LocationClass.py


## Opisy klas
*PlayerClass* - jest to klasa, która posiada atrybuty naszej postaci. Mamy w niej atrybut health, armour oraz damage. Dana klasa pobiera do siebie informację z pliku "Constructor.json". Posiada ona również metody, które odpowiadają za różne komendy i sytuacje w grze. Przykładowo, jeśli zdobywamy broń to wartość naszego damage wzrasta.
*EnemyClass* - jest to klasa, która posiada atrybuty wrogów. Ta klasa posiada dwie metody: is_alive sprawdza czy dany wróg jest martwy oraz taking_damage, które ujmuje wrogowi hp w momencie gdy z nim walczymy
*LocationClass* - jest to klasa, która pobiera informacje z pliku json informacje dotyczące lokacji. Oczywiście, uwzględnia ona przedmioty, które sie tam znajdują oraz wrogów. Dodatkowo wchodząc dodanej lokacji dostaniemy jej opis. Posiada ona atrybuty, które odnoszą się do danych elementów.  Posiada ona takie metody jak "show_details" która pokazuje szczegóły lokacji takie jak wrogowie lub sojusznicy. Są również takie metody jak "get_description" i "get_enemies", które zwracają odpowiednio: opis lokacji i dialogi oraz szczegółowy opis wrogów.
*Interfejs* - jest to main. Jest to plik, który posiada funkcje do wyświetlania gry oraz menu.
