import streamlit as st
import pandas as pd
import time
import matplotlib as plt
import os
# zaczynamy od zaimportowania bibliotek

st.success('Gratulacje! Z powodzeniem uruchomiłeś aplikację')
# streamlit jest wykorzystywany do tworzenia aplikacji
# z tego powodu dobrą praktyką jest informowanie użytkownika o postępie, błędach, etc.

# Inne przykłady do wypróbowania:
# st.balloons() # animowane balony ;)
# st.error('Błąd!') # wyświetla informację o błędzie
# st.warning('Ostrzeżenie, działa, ale chyba tak sobie...')
# st.info('Informacja...')
# st.success('Udało się!')

# st.spinner()
# with st.spinner(text='Pracuję...'):
    # time.sleep(2)
    # st.success('Done')
# możemy dzięki temu "ukryć" późniejsze ładowanie aplikacji

st.title('Hi! Polaaaaaaa! :)')
# title, jak sama nazwa wskazuje, używamy do wyświetlenia tytułu naszej aplikacji

st.header('Welcome to wonderland!')
# header to jeden z podtytułów wykorzystywnaych w Streamlit

st.subheader('La-laaa-laaaa')
# subheader to jeden z podtytułów wykorzystywnaych w Streamlit

st.text('To Poli aplikacja z wykorzystaniem Streamlit')
# text używamy do wyświetlenia dowolnego tekstu. Można korzystać z polskich znaków.

st.image('38842_upload66d0528b150ef_1724928651-1-en1724928676.jpg', caption='Alisa')

st.write("""
### Instrukcja:
- Wybierz odpowiednią opcję z menu po lewej stronie.
- Wpisz tekst do analizy lub tłumaczenia.
- Wynik pojawi się poniżej.
""")

# st.code("st.write()", language='python')
# code może nam się czasami przydać, jeżeli chcielibyśmy pokazać np. klientowi fragment kodu, który wykorzystujemy w aplikacji

# with st.echo():
#     st.write("Echo")
# możemy też to zrobić prościej używając echo - pokazujemy kod i równocześnie go wykonujemy

# df = pd.read_csv("DSP_4.csv", sep =';')
# st.dataframe(df)
# musimy tylko pamiętać o właściwym określeniu separatora (w tym wypadku to średnik)
# masz problem z otworzeniem pliku? sprawdź w jakim katalogu pracujesz i dodaj tam plik (albo co bardziej korzystne - zmień katalog pracy)
# os.getcwd() # pokaż bieżący katalog
# os.chdir("") # zmiana katalogu

st.header('Przetwarzanie języka naturalnego')

import streamlit as st
from transformers import pipeline

translator = pipeline("translation_en_to_de", model="Helsinki-NLP/opus-mt-en-de")
print(translator("Hello world"))

option = st.selectbox(
    "Wybierz funkcję:",
    [
        "Analiza sentymentu tekstu (ENG)",
        "Tłumaczenie z angielskiego na niemiecki",
    ],
)

if option == "Wydźwięk emocjonalny tekstu (eng)":
    text = st.text_area(label="Wpisz tekst")
    if text:
        classifier = pipeline("sentiment-analysis")
        answer = classifier(text)
        st.write(answer)

elif option == "Tłumaczenie z angielskiego na niemiecki":
    text = st.text_area(label="Wprowadź tekst po angielsku do tłumaczenia:")
    if text:
        try:
            with st.spinner("Tłumaczę..."):
                time.sleep(1)  # Symulacja ładowania
                translator = pipeline("translation_en_to_de", model="Helsinki-NLP/opus-mt-en-de")
                translation = translator(text, max_length=40)
            st.success("Tłumaczenie zakończone!")
            st.write("Przetłumaczony tekst:", translation[0]['translation_text'])
        except Exception as e:
            st.error("Błąd: Nie udało się przeprowadzić tłumaczenia.")

st.subheader('s24601')
st.write('🐞 Dodaj krótką instrukcję i napisz do czego służy aplikacja')
st.write('🐞 Wpłyń na user experience, dodaj informacje o ładowaniu, sukcesie, błędzie, itd.')
st.write('🐞 Na końcu umieść swój numer indeksu')
st.write('🐞 Stwórz nowe repozytorium na GitHub, dodaj do niego swoją aplikację, plik z wymaganiami (requirements.txt)')
st.write('🐞 Udostępnij stworzoną przez siebie aplikację (https://share.streamlit.io) a link prześlij do prowadzącego')
