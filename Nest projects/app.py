import spacy
from flask import Flask, render_template, request

# Load the large English language model
nlp = spacy.load("en_core_web_lg")

app = Flask(__name__)

# Function to extract all named entities
def extract_entities(text):
    doc = nlp(text)
    all_entities = []
    custom_entity_labels = ["PERSON", "GPE", "ORG", "OBJECT", "ANIMALS", "FLOWERS"]
    for ent in doc.ents:
        if ent.label_ in custom_entity_labels:
            all_entities.append({
                "text": ent.text,
                "label": ent.label_,
            })
    return all_entities

@app.route('/', methods=['GET', 'POST'])
def index():
    entities = []
    if request.method == 'POST':
        text = request.form['text']
        entities = extract_entities(text)
    return render_template('index.html',entities=entities)

if __name__ == '__main__':
    app.run(debug=True)