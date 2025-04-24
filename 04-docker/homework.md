📌 Zadanie 4 – Konteneryzacja aplikacji z modelem AI

🎯 Cel zadania:

Celem zadania jest konteneryzacja aplikacji, aby była uruchamialna w kontenerze Docker. Aplikacja powinna działać na wybranym porcie i umożliwiać interakcję z modelem AI poprzez aplikację streamlit/gradio. Aplikacja powinna działać lokalnie po uruchomieniu komendy docker run.

📝 Elementy do przygotowania:

1. Konteneryzacja aplikacji:
    * Utwórz plik Dockerfile, który będzie zawierał wszystkie zależności wymagane do uruchomienia aplikacji (np. Python, biblioteki, model AI).
    * Aplikacja powinna działać na określonym porcie.
    * Po uruchomieniu kontenera aplikacja powinna być dostępna pod adresem http://localhost:<wybrany_port>.

2. Testowanie aplikacji w Dockerze:
    * Upewnij się, że aplikacja działa płynnie, a komunikacja z modelem AI działa poprawnie.

3. Dokumentacja:
    * Zaktualizuj plik README.md w repozytorium o instrukcje dotyczące uruchamiania aplikacji w Dockerze.
    * W README.md powinna pojawić się komenda `docker run` wraz ze wskazaniem mapowanego portu.

📤 Elementy do przesłania:
* Plik Dockerfile.
* Zrzut ekranu logów Dockera pokazujący, że kontener zbudował się poprawnie i został uruchomiony.

🎙️ Elementy do pokazania na zajęciach:
* Działająca aplikacja uruchomiona w Dockerze, działająca na wybranym porcie i umożliwiająca interakcję z modelem AI.
* UWAGA! Proszę o przygotowanie się, aby pokazać uruchomiony kontener na własnym komputerze / komputerze w pracowni.
