##############main functiom
import streamlit as st
import nltk
nltk.download('all')

# NLP Pkgs
from textblob import TextBlob
from nltk.stem.wordnet import WordNetLemmatizer
import re


def main():
    st.set_page_config(page_title='ML App', page_icon=':robot_face:')
    st.title("NLP")
    st.subheader("Welcome to my Application for review analysis")
    st.caption("Made by Divey Anand")
    text = st.text_area("Enter Your Text")
    #####Added Background - START
    def add_bg_from_url():
        st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    add_bg_from_url()
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
