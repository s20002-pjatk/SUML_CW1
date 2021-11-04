import streamlit as st
import pandas as pd
from transformers import pipeline
import time
import matplotlib as plt
import os
import json
import keyboard
# zaczynamy od zaimportowania bibliotek

st.success('Gratulacje! Z powodzeniem uruchomiłeś aplikację')

# streamlit jest wykorzystywany do tworzenia aplikacji
# z tego powodu dobrą praktyką jest informowanie użytkownika o postępie, błędach, etc.

# Inne przykłady do wypróbowania:
#st.balloons() # animowane balony ;)
# st.error('Błąd!') # wyświetla informację o błędzie
# st.warning('Ostrzeżenie, działa, ale chyba tak sobie...')
# st.info('Informacja...')
# st.success('Udało się!')

# st.spinner()
# with st.spinner(text='Pracuję...'):
    # time.sleep(2)
    # st.success('Done')
# możemy dzięki temu "ukryć" późniejsze ładowanie aplikacji

st.title('Zajęcia 1. Tłumacz angielsko-niemiecki')
st.image('https://upload.wikimedia.org/wikipedia/commons/0/0c/Flag_of_the_United_Kingdom_and_Germany.png')
# title, jak sama nazwa wskazuje, używamy do wyświetlenia tytułu naszej aplikacji

st.header('nr indeksu s20002')
# header to jeden z podtytułów wykorzystywnaych w Streamlit

st.subheader('O Aplikacji')
# subheader to jeden z podtytułów wykorzystywnaych w Streamlit

st.text('To przykładowa aplikacja z wykorzystaniem Streamlit.')
# text używamy do wyświetlenia dowolnego tekstu. Można korzystać z polskich znaków.

st.write('Streamlit jest biblioteką pozwalającą na uruchomienie modeli uczenia maszynowego.')
st.write('Aplikacja pozwala na interpretację wydźwięku emocjonalnego tekstu oraz posiada funkcję tłumacza angielsko-niemieckiego')
# write używamy również do wyświetlenia tekstu, różnica polega na formatowaniu.

st.code("st.write()", language='python')
# code może nam się czasami przydać, jeżeli chcielibyśmy pokazać np. klientowi fragment kodu, który wykorzystujemy w aplikacji

with st.echo():
    st.write("Echo")
# możemy też to zrobić prościej używając echo - pokazujemy kod i równocześnie go wykonujemy

#df = pd.read_csv("cwiczenie_1.csv", sep = ';')
#st.dataframe(df)
# musimy tylko pamiętaćo właściwym określeniu separatora (w tym wypadku to średnik)
# masz problem z otworzeniem pliku? sprawdź w jakim katalogu pracujesz i dodaj tam plik (albo co bardziej korzystne - zmień katalog pracy)
# os.getcwd() # pokaż bieżący katalog
# os.chdir("") # zmiana katalogu

st.header('Przetwarzanie języka naturalnego')

#import streamlit as st
#from transformers import pipeline

option = st.selectbox(
    "Opcje",
    [
        "Wydźwięk emocjonalny tekstu (eng)",
        "Tłumacz eng to de",
    ],
)

##
text = st.text_area(label="Wpisz tekst")

if option == "Wydźwięk emocjonalny tekstu (eng)":
    # if keyboard.is_pressed("Ctrl") and keyboard.is_pressed("Enter"):
    #      with st.spinner('Recognition in progress...'):
    #         time.sleep(5)

            classifier = pipeline("sentiment-analysis")
            answer = classifier(text)
            st.write(answer)

if option == "Tłumacz eng to de":
    # if keyboard.is_pressed("Ctrl") and keyboard.is_pressed("Enter"):
    #      with st.spinner('Translation in progress...'):
    #          time.sleep(5)
             translator = pipeline("translation_en_to_de")
             translation = translator(text, max_length=40)
             word = translation[0]['translation_text']
             if word == text:
                 st.error('Translation failed. Please, recheck the word')
             else:
                 st.success('Translation successful')
                 st.write(translation)

##print(translator("Hugging Face is a technology company based in New York and Paris", max_length=40))
##print(translator(text, max_length=40))

st.subheader('Zadanie do wykonania')
st.write('Wykorzystaj Huggin Face do stworzenia swojej własnej aplikacji tłumaczącej tekst z języka angielskiego na język niemiecki. Zmodyfikuj powyższy kod dodając do niego kolejną opcję, tj. tłumaczenie tekstu. Informacje potrzebne do zmodyfikowania kodu znajdziesz na stronie Huggin Face - https://huggingface.co/transformers/usage.html')
st.write('🐞 Dodaj właściwy tytuł do swojej aplikacji, może jakieś grafiki?')
st.write('🐞 Dodaj krótką instrukcję i napisz do czego służy aplikacja')
st.write('🐞 Wpłyń na user experience, dodaj informacje o ładowaniu, sukcesie, błędzie, itd.')
st.write('🐞 Na końcu umieść swój numer indeksu')
st.write('🐞 Stwórz nowe repozytorium na GitHub, dodaj do niego swoją aplikację, plik z wymaganiami (requirements.txt)')
st.write('🐞 Udostępnij stworzoną przez siebie aplikację (https://share.streamlit.io) a link prześlij do prowadzącego')
