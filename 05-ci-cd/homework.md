📌 Zadanie 5 – Stworzenie pipeline'ów CI/CD

🎯 Cel zadania:

Celem zadania jest skonfigurowanie procesu CI/CD dla aplikacji. Zadanie składa się z dwóch osobnych pipeline'ów – pierwszy odpowiada za budowanie i publikację obrazu Docker, a drugi za analizę jakości lub bezpieczeństwa kodu. Opcjonalnie, osoby bardziej zaawansowane mogą wdrożyć pipeline do tworzenia infrastruktury w chmurze za pomocą narzędzi typu Infrastructure as Code (IaC).

📝 Elementy do przygotowania:

1. Pipeline #1 – Budowanie i publikacja obrazu Docker:
    * Pipeline uruchamia się po każdej aktualizacji (merge/commit) do gałęzi main.
    * Buduje obraz Dockera z aplikacją.
    * Wysyła obraz do wybranego Docker Registry (Docker Hub, GitHub Container Registry, Azure Container Registry itp.).
    * UWAGA: Wszystkie sekrety (tokeny, loginy, hasła) muszą być trzymane wyłącznie w sekretach repozytorium. Żaden klucz API, login, hasło nie może znajdować się w kodzie ani być w obrazie Dockera.

2. Pipeline #2 – Kilka opcji do wyboru (wystarczy jedna z nich!):
    1. Jakość kodu:
        * Pipeline uruchamia się automatycznie przy otwarciu Pull Request do gałęzi main.
        * Sprawdzana jest jakość kodu przy pomocu automatycznych narzędzi.
        * Celem jest, aby kod był czysty, spójny i utrzymywalny.
        * Pipeline powinien korzystać z framework'u `pre-commit` ([https://pre-commit.com/](https://pre-commit.com/)) i wykorzystywać co najmniej 5 narzędzi, np.:
            * black – formatowanie kodu zgodnie z PEP8.
            * flake8 – analiza stylu i błędów.
            * isort – uporządkowanie importów.
            * autoflake – usuwanie nieużywanych importów i zmiennych.
            * end-of-file-fixer, trailing-whitespace – usuwanie niepotrzebnych białych znaków.
        * Pipeline musi zakończyć się sukcesem, aby móc zmergować zmiany do gałęzi main.
    2. Poprawność działania aplikacji (testy jednostkowe):
        * Pipeline uruchamia się automatycznie przy otwarciu Pull Request do gałęzi main.
        * Sprawdzana jest poprawność działania aplikacji.
        * Testy jednostkowe mogą być napisane przy pomocy narzędzia `pytest`.
        * Pipeline musi zakończyć się sukcesem, aby móc zmergować zmiany do gałęzi main.
    3. Skan bezpieczeństwa:
        * Pipeline uruchamia się automatycznie przy otwarciu Pull Request do gałęzi main.
        * Narzędzie do skanowania podatności w kodzie, zależnościach, kontenerze.
        * Cel: zapewnienie bezpieczeństwa na poziomie kodu i zależności.
        * Przykład narzędzia: `trivy` ([https://github.com/aquasecurity/trivy](https://github.com/aquasecurity/trivy)).
        * Pipeline ma się nie kończyć sukcesem, jeśli występują podatności typu HIGH lub CRITICAL – należy je rozwiązać, a nie wyciszać.
    4. Infrastructure as a Code (IaC):
        * Tworzenie infrastruktury w chmurze (Azure/AWS/GCP) przy pomocy pipeline'u i narzędzia typu Terraform.
        * Stworzenie instancji aplikacji webowej / funkcji oraz zasobu typu storage (Azure Blob Storage/S3).
        * Uwaga: Sam deployment (wdrożenie aplikacji w chmurze) będzie wymagane na kolejnym checkpointcie - teraz wymagane jest tylko stworzenie zasobów.
        * Pipeline IaC powinien wywoływać się po każdej aktualizacji (merge/commit) do gałęzi main.

📤 Elementy do przesłania:

* Link do obrazu Dockera w wybranym rejestrze obrazów.
* Zrzuty ekranu z działającymi pipeline'ami (zielone statusy!).

🎙️ Elementy do pokazania na zajęciach:

* Widok opublikowanego obrazu Dockera.
* Zielone statusy pipeline'ów.
