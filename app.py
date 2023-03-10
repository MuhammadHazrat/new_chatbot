import os

from flask import Flask, request
from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="typeform/distilbert-base-uncased-mnli")

app = Flask(__name__)

# port = int(os.environ.get('PORT', 5000))


@app.route('/', methods=['POST', 'GET'])
def chat():
    sequence_to_classify = request.args.get('line')
    if sequence_to_classify == None:
        return "no input given"
    print(sequence_to_classify)
    candidate_labels = ['travel', 'greetings', 'help', 'health']
    pred = classifier(sequence_to_classify, candidate_labels)
    my_dict = {'health': ['I am not feeling well today', 'I am well thank you', 'Feeling Low'],
               'travel': ['I am going home', 'I am going to GYM', 'Going to University']}

    try:
        response = my_dict[pred['labels'][0]]
    except:
        response = 'I did not understand your problem'

    print(response)
    return response


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app.
    app.run(host='127.0.0.1', port=8080, debug=True)
