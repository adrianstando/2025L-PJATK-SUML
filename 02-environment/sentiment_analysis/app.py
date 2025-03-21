import streamlit as st
from transformers import pipeline
import matplotlib.pyplot as plt
import nltk
import time

# Załadowanie modelu analizy sentymentu
classifier = pipeline("sentiment-analysis")

# Załadowanie zasobów do tokenizacji z NLTK
nltk.download('punkt')

# Ustawienia strony w Streamlit
st.set_page_config(page_title="Analiza Sentymentu", page_icon="💬")

# Nagłówek aplikacji
st.title("🔍 Analiza Sentymentu z Hugging Face")

# Pole tekstowe do wprowadzania danych
text = st.text_area("Wpisz długi tekst do analizy:", "")

# Przyciski do uruchomienia analizy
if st.button("Analizuj sentyment"):
    if text:
        with st.spinner('Przetwarzam tekst...'):
            # Pauza, aby widać było ładowanie
            time.sleep(1)

            # Podział tekstu na listę zdań
            sentences = nltk.sent_tokenize(text)

            # Listy do przechowywania wyników
            labels = []
            scores = []

            # Analiza sentymentu dla każdego zdania
            for sentence in sentences:
                result = classifier(sentence)[0]
                label = result["label"]
                score = result["score"]
                labels.append(label)
                scores.append(score)

            # Wyświetlenie wyników
            st.write("**Wyniki analizy sentymentu dla każdego zdania:**")
            for i, sentence in enumerate(sentences):
                st.write(f"**Zdanie {i+1}:** {sentence}")
                st.write(f"🔹 **Label:** {labels[i]}")
                st.write(f"📊 **Prawdopodobieństwo:** {scores[i]:.4f}")
                st.write("---")

            # Przygotowanie wykresu
            fig, ax = plt.subplots(figsize=(10, 6))
            # Rysowanie wykresu słupkowego za pomocą pyplot.bar
            bars = plt.bar(range(len(sentences)), scores, color=['green' if label == "POSITIVE" else 'red' for label in labels])
            # Ustawienia osi X
            plt.xticks(range(len(sentences)), [f"Zdanie {i+1}" for i in range(len(sentences))])
            # Etykieta osi Y i tytuł wykresu
            plt.ylabel('Prawdopodobieństwo')
            plt.title('Analiza sentymentu dla każdego zdania')
            # Ustawienie zakresu osi Y
            plt.ylim(0, 1.05)
            # Dodanie wartości prawdopodobieństwa na słupkach
            for i, bar in enumerate(bars):
                yval = bar.get_height()
                plt.text(bar.get_x() + bar.get_width() / 2, yval, f"{yval:.2f}", ha='center', va='bottom', fontsize=10)
            # Optymalizacja rozmieszczenia elementów
            plt.tight_layout()
            # Wyświetlenie wykresu w Streamlit
            st.pyplot(fig)
    else:
        st.warning("⚠️ Wprowadź tekst do analizy!")

# Dodatkowa sekcja z informacjami o modelu
st.sidebar.header("O modelu")
st.sidebar.write(
    "Aplikacja wykorzystuje model Hugging Face do analizy sentymentu wprowadzonych tekstów. "
    "Model ten rozróżnia, czy tekst jest pozytywny, czy negatywny na podstawie analizy słów i kontekstu."
)

# Sekcja FAQ
st.sidebar.header("FAQ")
st.sidebar.write(
    "1. **Jak działa analiza sentymentu?**\n"
    "   Model analizuje wprowadzone słowa i przypisuje im etykiety, np. 'Pozytywny' lub 'Negatywny', "
    "w zależności od kontekstu emocjonalnego.\n\n"
    "2. **Czy mogę używać innych języków?**\n"
    "   Tak, możesz załadować odpowiedni model dla różnych języków."
)
