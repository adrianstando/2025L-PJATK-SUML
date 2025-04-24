📌 Zadanie 6 – Aplikacja działająca w środowisku chmurowym

🎯 Cel zadania:

Celem tego zadania jest uruchomienie aplikacji w środowisku chmurowym (Azure, AWS lub GCP), z pełnym procesem CI/CD. Aplikacja powinna działać jako kontener, być wdrażana z poziomu pipeline'u i zapisywać dane wejściowe oraz odpowiedzi modelu do zasobu typu storage (np. Blob/S3/GCP Storage).

📝 Elementy do przygotowania:

1. Wdrożenie aplikacji z pipeline'u:
    * Deployment aplikacji na chmurę ma być wykonywany wyłącznie z poziomu pipeline CI/CD.
    * Pipeline powinien pobierać obraz z registry (Docker Hub / GHCR / ACR) i wdrażać go na konkretną usługę.

2. Aplikacja w kontenerze:
    * Aplikacja powinna być wdrożona jako kontener na chmurze.
    * Publicznie dostępna pod adresem URL (autoryzacja – opcjonalna).

3. Zapis danych do storage:
    * Aplikacja ma mieć zaimplementowaną logikę do przetrzymywania danych wejściowych i wyjściowych.
    * Każde wywołanie modelu zapisuje dane do oddzielnego folderu w zasobie storage (np. 2024-01-1_12:00:03/):
        * input.txt / input.png – dane wejściowe użytkownika.
        * output.txt – wynik predykcji modelu.
        * Inne struktura plików jest również możliwa - najważniejsze, żeby pliki były tam zapisywane w sposób ustrukturyzowany.
    * Może być użyte: Azure Blob, AWS S3, Google Cloud Storage – dowolny chmurowy storage.
    * Zamiast zasobu typu storage, można wykorzystać bazę danych (jako odzielny zasób na chmurze, poza aplikacją).

4. Infrastruktura chmurowa:
    * Aplikacja webowa (usługa hostująca kontener).
    * Storage bucket (do zapisów danych).

5. CI/CD – wymagania:
    * Można rozszerzyć pipeline (z poprzedniego zadania) służący do budowania i wypychania kontenera. Można również stworzyć odzielny pipeline, ale wywoływany tylko po sukcesie wyżej wspomnianego pipeline'u.
    * Sekrety (dostępy do chmury) muszą być przechowywane w sekretach repozytorium – zero haseł w kodzie!

📤 Elementy do przesłania:
* Link do uruchomionej aplikacji (adres URL).
* Screenshot folderów input/output zapisanych w storage.
* Screenshot działajacej aplikacji w chmurze.

🎙️ Elementy do pokazania na zajęciach:
* Interakcja z uruchomioną aplikacją w chmurze.
* Pokazanie wygenerowanych danych (input/output) w storage.
