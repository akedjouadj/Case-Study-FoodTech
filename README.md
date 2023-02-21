Ce code et les librairies utilisées utilisent la version 3.8.15 de python.
Assurez-vous de disposer de la bonne version pour éviter des problèmes de dépendances lors de l'exécution.

Pour l'exécution : 
- commencer par créer un environnement virtuel dans votre dossier de fichiers à partir de python 3.8, par exemple avec la commande : python3.8 -m venv 'nom de votre venv'
- activer votre venv : commande source 'nom de votre venv'/bin/activate
- installer les packages et modules nécessaires depuis le fichier requirements.txt : commande pip3.8 install -r requirements.txt
- lancer la demo streamlit : streamlit run ./review_response_demo.py
Noter que l'application met un petit délai (environ 40sec pour importer les librairies et modèles) à se lancer.
Noter que l'appli met environ 27sec à répondre à un avis.
Une solution a été proposée dans le code pour réduire tous ces temps d'exécution, mais nécessite un compromis de stockage mémoire.

A propos de l'interface :
Il s'agit d'une petite interface de réponse automatique à des avis clients d'un restaurant codé avec le package streamlit de python.
D'une part, l'algorithme utilisé détecte les mots clés relatifs aux services de la restauration dans l'avis du client grâce à la librairie spacy de python, puis évalue la polarité de l'avis en utilisant un modèle multi-langage disponible sur le site hugging face d'autre part. 
Ces deux résultats couplés à des heuristiques hard-codées sont utilisés pour générer automatiquement une réponse à l'avis du client.
Toutes les fonctions de par l'algo sont documentées et disponibles dans le fichier utils.py.

L'indicateur de performance de l'algo dépend essentiellement de la bonne détection de la polarité de l'avis. Le modèle multi-langage utilisé est accessible via le lien https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment et est plutôt performant (voir les scores d'accuracy sur le site). De plus, l'algorithme a été robustifié de sorte qu'aucune réponse ne paraisse inadaptée à l'utilisateur, peu importe l'avis qu'il entre.
