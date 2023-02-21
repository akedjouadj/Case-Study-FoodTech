from utils.utils import *
import streamlit as st
from PIL import Image
from joblib import dump, load

stars_classifier, nlp = models_loader() # take more time

"""
a solution to reduce the running time, but need more memory space :

dump(stars_classifier, 'stars_classifier.joblib')
dump(nlp, 'nlp.joblib')
stars_classifier = load('stars_classifier.joblib')
nlp = load('nlp.joblib')
"""

st.set_page_config(
    page_title="Demo",
    page_icon="👋",
)

st.title("Bienvenue sur l'outil de réponse auto aux avis des clients de LBC")
col1,col2 = st.columns(2, gap="medium")

with col1:
    image = Image.open('LBC.png')
    st.image(image, use_column_width='auto')
    

with col2:
    form1 = st.form(key = "text-zone")
    customer_review= form1.text_area("Merci de rentrer votre avis...")
    button = form1.form_submit_button("Entrer")

    if button:
        review_polarity = polarity_computer(stars_classifier, customer_review)
        nouns_review = nouns_detector(nlp, customer_review)
        response = gen_response(review_polarity, nouns_review)
        st.write(response)