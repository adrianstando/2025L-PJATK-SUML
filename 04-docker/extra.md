Przygotuj system trzech kontenerów w architekturze MVC (model-view-controler) połączonych w sieci Docker i uruchamianych przy pomocy `docker compose`. Początkowa struktura systemu znajduje się w folderze [mvc-task](https://github.com/adrianstando/2025L-PJATK-SUML/tree/main/04-docker/mvc-task) w repozytorium.

System składa się z następujących elementów:

* model (baza danych) - obraz do ściągnięcia z Docker Hub; możliwość skorzystania z dowolnie wybranej bazy danych; w początkowej propozycji jest PostgreSQL (ale można ją zamienić na dowolną inną) oraz skrypt tworzący bazę danych `user_db` i jedną tabelę `people` z dostępem dla użytkownika `admin` i hasłem `password`.
* controler (kontroler) - serwer REST API z jednym endpointem do tworzenia nowych rekordów w bazie danych; początkowy schemat aplikacji jest napisany w Pythonie przy pomocy bilbioteki FastAPI; możecie użyć dowolnego języka: jedynym warunkiem jest to, że ma być co najmniej jeden endpoint do tworzenia nowych rekordów w bazie danych, która leży w oddzielnym kontenerze.
* view (widok) - prosta strona WWW wyświetlająca dane z bazy danych; poczatkowy schemat aplikacji proponuje użycie Pythona i biblioteki streamlit, ale nie jest to obowiązkowe; może to być dowolny język i dowolny pakiet.

Model działania:

1. Wstawiamy dane poprzez API (kontroler) do bazy danych, np. poprzez `curl -X 'POST' 'http://localhost:8000/people' -H 'Content-Type: application/json' -d '{"name": "Jan","surname": "Kowalski","position": "Intern","salary": 3000.00}'`
2. Dane lądują w bazie danych.
3. Tabelę z bazy danych (wszystkie dane) można zobaczyć w postaci tabeli w aplikacji webowej frontend.

UWAGA: Login i hasło do bazy danych muszą być podane jako zmienne środowiskowe (nie mogą być hard-codowane w kodzie aplikacji!).

UWAGA: W tym systemie dwa kontenery muszą być zbudowane poprzez Dockerfile: controler (api) oraz view (widok/frontend). Można je budować korzystając z sekcji `build` w pliku `docker-compose.yaml` (wtedy kontenery będą zbudowane w momencie uruchamiania `docker compose up`).

Całość ma być uruchamiana skryptem `docker-compose.yaml`.

Do przesłania:

* spakowany folder ze wszystkimi plikami i folderami (`docker-compose.yaml`, foldery `api`, `db`, `frontend`)
* screenshot frontendu, gdzie widoczne są dane w formie tabelki (Uwaga! Na zrzucie ekranu powinny być więcej niż dwa domyślne rekordy!)
