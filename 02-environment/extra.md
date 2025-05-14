Stwórz aplikację w Streamlit do tłumaczenia zdań z angielskiego na francuski.

1. Stwórz wirtualne środowisko korzystając z `venv` lub `conda`.

2. Przygotuj skrypt `app.py`. Skorzystaj z modelu `Helsinki-NLP/opus-mt-en-fr`.

    ```python
    translator = pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-en-fr")
    result = translator("Hello, how are you?")
    ```

🚨 UWAGA! 🚨

Do poprawnego działania wymagana jest instalacja biblioteki `sentencepiece`
