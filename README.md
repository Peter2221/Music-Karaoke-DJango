# Projekt: Aplikacja do słuchania muzyki i karaoke (jak iSing)

Technologie: Python + Django

Funkcjonalności
- logowanie
- przeglądanie, wyszukiwanie utworów,
- słuchanie wybranego utworu,
- odtwarzanie, pauza, zatrzymywanie utworu,
- dodawanie utworu do ulubionych,
- nagrywanie swojego głosu, analiza dopasowania do oryginału (przesyłanie utworu na serwer, analiza sygnału, ekstrakcja tonu podstawowego, porównanie z nagraniem wzorcowym, zwracanie stopnia dopasowania w postaci punktów/procentu dopasowania)
- ranking użytkowników

music_karaoke:
 - templates
    base.html
    /css
    /js
    - auth
        - index.html
        - detailes.html
    - analyze
    - songs
 - auth
 - analyze
 - songs etc.

User stories:
- As a user I want to:
    - register to create account -> /register
    - login to access main part of application -> /login
    
    - see list of songs and search to pick the right record -> /songs
    - see the song details, play and record the song -> /songs/<id>
    - see ranking of user scores -> /ranking
    - go to user panel to change some settings eg. avatar, password -> /settings
    - analyze the song -> /analyze 