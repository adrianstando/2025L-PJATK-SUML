# Środowiska uruchomieniowe AutoML - PJATK 2025L

Repozytorium zawiera materiały dotyczące realizacji przedmiotu SUML na PJATK - semestr letni 2025.

## Tematyka zajęć

Celem kursu jest zdobycie praktycznych umiejętności w zakresie budowy, wdrażania i zarządzania aplikacjami wykorzystującymi uczenie maszynowe (ML) i generatywną sztuczną inteligencję (GenAI). Studenci nauczą się konfigurować środowiska programistyczne oraz integrować modele ML w aplikacjach webowych. Kluczowe aspekty kursu obejmują:

- Pozyskiwanie i przygotowanie danych do treningu modeli ML,
- Trenowanie, ewaluację i wdrażanie modeli,
- Tworzenie interfejsów użytkownika do interakcji z modelami,
- Uruchamianie aplikacji w środowisku chmurowym,
- Automatyzację procesów wdrażania (CI/CD),
- Korzystanie z AutoML i gotowych modeli ML/GenAI (np. Hugging Face, OpenAI).

## Organizacja zajęć

Studenci pracują w zespołach dwu- lub trzyosobowych. Celem projektu jest stworzenie aplikacji działającej w środowisku chmurowym, zgodnie z dobrymi praktykami inżynierii oprogramowania. Wymagania dotyczące aplikacji:

- Powinna posiadać prosty interfejs użytkownika,
- Wykorzystywać model ML lub GenAI w praktyczny sposób.

Przykłady projektów:

1. Własny model ML wytrenowany na publicznie dostępnych danych (np. z platformy Kaggle) – aplikacja zbiera dane wejściowe i dokonuje predykcji.
2. Wykorzystanie gotowego modelu z Hugging Face – aplikacja integruje model (np. analiza sentymentu, tłumaczenie, klasyfikacja obrazów, generowanie treści) i udostępnia go użytkownikom.

W trakcie zajęć będą przedstawiane nowe technologie wraz z prostymi przykładami. W trakcie zajęć będą do rozwiązania przez studentów zadania wykorzystujące przedstawianą technologię.

## Terminy zajęć i zadania

| Termin | Numer zajęć | Ćwiczenia | Zakres zajęć | Checkpoint projektu |
|--------|-------------|-----------|--------------|---------------------|
| 08.03. | 1           | [Wprowadzenie, backlog, user stories](01-user-stories/README.md)  | - Omówienie formatu zajęć, podział na zespoły, wybór tematu projektu <br> - Wprowadzenie do backlogu i user stories (np. w Azure DevOps) | - |
| 22.03. | 2           | [Środowisko programistyczne](02-environment/README.md)| - Prioryteryzacja backlogu i sprinty <br> - Przygotowanie środowiska programistycznego w Pythonie: pyenv, conda <br> - Tworzenie pierwszej aplikacji w Streamlit bazującej na modelu z Hugging Face | [**Temat, backlog i repozytorium kodu dla projektu**](01-user-stories/homework.md) |
| 05.04. | 3           | [Interfejs użytkownika dla aplikacji ML](03-neural-networks/README.md) | - Trenowanie własnej sieci neuronowej <br> - Tworzenie aplikacji w Gradio na podstawie własnego modelu klasyfikacji obrazów | [**Działająca pierwsza wersja aplikacji (Streamlit/Gradio)**](02-environment/homework.md) |
| 26.04. | 4           | [Docker](04-docker/README.md) | - Wprowadzenie do Dockera: pisanie Dockerfile, uruchamianie aplikacji w kontenerze | [**Podłączenie modelu AI do aplikacji**](03-neural-networks/homework.md) |
| 17.05. | 5           | [CI/CD](05-ci-cd/README.md) | - Wprowadzenie do CI/CD <br> - Konfiguracja GitHub Actions | [**Konteneryzcja aplikacji (docker)**](04-docker/homework.md) |
| 31.05. | 6           | [Uruchamianie aplikacji w chmurze](06-cloud/README.md) | - Uruchamianie przykładowej aplikacji (kontenera) na Azure | [**Stworzenie pipeline'ów CI/CD**](05-ci-cd/homework.md) |
| 14.06. | 7           | [Narzędzia ML](07-ml-tools/README.md) | - Wprowadzenie do MLflow <br> - Wprowadzenie do AutoML w Pythonie <br> - Wprowadzenie do kwantyzacji sieci neuronowych <br> - Uruchamianie modeli LLM z ollama  | [**Aplikacja działająca w środowisku chmurowym**](06-cloud/homework.md) |
| 28.06. | 8           | Prezentacje i ocena | - Prezentacja projektów, ocena i feedback | [**Prezentacja**](07-ml-tools/homework.md) |


## Zasady oceniania

Ocena z przedmiotu składa się z trzech elementów: regularnej pracy w czasie semestru, końcowego rozwiązania oraz końcowej prezentacji.

W semestrze można zdobyć maksymalnie 100 pkt, w tym:

* **Checkpointy projektu (60 pkt)** – 10 pkt za każdy checkpoint.
    * Na oddaniu checkpointu powinien być obecny cały zespół.
    * Oddanie checkpointu następuje tylko w trakcie zajęć (z wyjątkiem nieobecności z powodu choroby lub jednorazowej nieobecności, jak w zasadach dodatkowych).
    * Każdy kolejny checkpoint projektu może zostać przyjęty tylko po zatwierdzeniu (oddaniu) poprzedniego.
* **Końcowe rozwiązanie (20 pkt)** – ocena spełnienia wymagań aplikacji, jakości kodu (czytelność, komentarze, struktura repozytorium, poprawność commitów, branche, itp.).
* **Końcowa prezentacja (20 pkt)** – ocena klarowności prezentacji, przedstawienia funkcjonalności oraz odpowiedzi na pytania z sali (przewidziane są dodatkowe punkty za zadawanie pytań innym zespołom). Brak końcowej prezentacji projektu skutkuje niemożliwością zaliczenia projektu.

**Zasady dodatkowe:**

- Dopuszczalna jest **jedna nieusprawiedliwiona nieobecność** – każda kolejna obniża ocenę o 10 pkt.
- Oddanie checkpointu odbywa się **podczas zajęć** (kilka minut dla każdego zespołu na koniec zajęć).
- **Opóźnienia w oddaniu checkpointu** skutkują obniżeniem punktacji o 5 pkt za każdy rozpoczęty tydzień opóźnienia (liczone do momentu przesłania rozwiązania poprzez Teamsy - punkty zostają przyznane dopiero po prezentacji checkpointu).

**Końcowe oceny są przyznawane na podstawie sumy zdobytych punktów:**

| Punkty | Ocena |
|--------|------|
| 90 - 100 | 5 |
| 80 - 89 | 4.5 |
| 70 - 79 | 4 |
| 60 - 69 | 3.5 |
| 50 - 59 | 3 |
| < 50 | 2 |
