import spacy
from transformers import pipeline
import torch
import warnings
from typing import Tuple, List

def models_loader() -> Tuple[object, object]:
    """
    This function loads the spacy model for french language 'fr_core_news_md' and the multilingual
    sentiment-analysis model 'nlptown/bert-base-multilingual-uncased-sentiment' from huggingface hub
    """

    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=UserWarning)
        stars_classifier = pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')
        nlp = spacy.load("fr_core_news_md")

    return stars_classifier, nlp

def polarity_computer(stars_classifier: object, customer_review: str) -> dict:
    """
    This function takes a polarity analysis model from the function models_loader and a customer review
    then make polarity analysis of the customer review

    Returns :
    a dictionnary with one key: 'label' which is a number of stars (between 1 and 5, 1 for very negative and
    5 for very positive). The value is a confidence score for the predicted number of stars 
    """
    return stars_classifier(customer_review)[0]

keywords = ['repas', 'rapidité', 'personnel', 'nourriture', 'menu', 'restaurant', 'attente', 'plat']

def nouns_detector(nlp: object, customer_review:str, keywords: List[str] = keywords) -> List[str]:
    """
    This function uses the spacy french model given by the function models_loader() to detect all
    nouns in the customer review which are in a given list of keywords. The function returns the 
    detected nouns in a list
    """
    doc = nlp(customer_review)
    review_key_nouns = []
    
    for token in doc:
        if token.text in keywords:
            review_key_nouns.append(token.text)

    return review_key_nouns
    
sentence_45_stars = "Merci pour votre commentaire. Nous sommes ravis d'avoir pu vous satisfaire. Au plaisir de vous revoir !"

sentence_3_stars1 = "Merci pour votre commentaire. Nous accordons une importance particulière aux retours de nos clients. Votre avis sera pris en compte pour l'amélioration de nos services"
sentence_3_stars2 = ". A très bientôt !"

sentence_12_stars1 = "Merci pour votre commentaire. Nous sommes vraiment désolés de ne pas avoir pu bien vous satisfaire comme vous l'auriez souhaité. Sachez que vos retours sur nos services" 
sentence_12_stars2 = " sera pris en compte pour une meilleure amélioration. En espérant vous revoir une prochaine fois."

def gen_response(review_polarity: dict, review_key_nouns: List[str]) -> str:
    """
    This function gives automatically a response to a customer review based on its polarity and its key nouns
    """
    response = None
    
    if len(review_key_nouns)==0:
        services = ''
    else:
        services = ' (' + ','.join(review_key_nouns)+ ', etc.'+ ')'
    
    if int(review_polarity['label'][0]) in [4, 5]:
        response = sentence_45_stars
    elif int(review_polarity['label'][0]) == 3:
        response = sentence_3_stars1+ services + sentence_3_stars2
    else:
        response = sentence_12_stars1+ services+ sentence_12_stars2 
        
    return response