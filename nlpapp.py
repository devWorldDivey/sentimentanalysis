##############main functiom
import streamlit as st
import nltk
nltk.download('all')

# NLP Pkgs
from textblob import TextBlob
from nltk.stem.wordnet import WordNetLemmatizer
import re


def main():
    st.title("NLP")
    st.subheader("Welcome to my Application for review analysis")
    st.caption("Made by Divey Anand")
    text = st.text_area("Enter Your Text")
    #####Added Background - START
    page_bg_img = '''
    <style>
    body {
    background-image: url("https://img.freepik.com/free-vector/gradient-smooth-background_79603-1782.jpg?w=2000");
    background-size: cover;
    }
    </style>
    '''    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    #####Added Background - END
    #Text Cleaning
    #Keeping only Text and digits
    text = re.sub(r"[^A-Za-z0-9]", " ", text)
    #Removes Whitespaces
    text = re.sub(r"\'s", " ", text)
    # Removing Links if any
    text = re.sub(r"http\S+", " link ", text)
    # Removes Punctuations and Numbers
    text = re.sub(r"\b\d+(?:\.\d+)?\s+", "", text)
    # Splitting Text
    text = text.split()
    # Lemmatizer
    lemmatizer = WordNetLemmatizer()
    lemmatized_words =[lemmatizer.lemmatize(word) for word in text]
    text = " ".join(lemmatized_words)
    if st.button("Analyze"):
        blob = TextBlob(text)
        result = blob.sentiment.polarity
        if result > 0.0:
            custom_emoji = ':blush:'
            st.success('Happy : {}'.format(custom_emoji))
        elif result < 0.0:
            custom_emoji = ':disappointed:'
            st.warning('Sad : {}'.format(custom_emoji))
        else:
            custom_emoji = ':confused:'
            st.info('Confused : {}'.format(custom_emoji))
        st.success("Polarity Score is: {}".format(result))
if __name__ == '__main__':
    main()
