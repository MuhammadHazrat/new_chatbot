import os

from flask import Flask, request
# from transformers import pipeline

# classifier = pipeline("zero-shot-classification", model="typeform/distilbert-base-uncased-mnli")

app = Flask(__name__)

port = int(os.environ.get('PORT', 5000))


@app.route('/', methods=['POST', 'GET'])
def hello():
    return "hello rathi"


# def chat():
#     sequence_to_classify = request.args.get('line')
#     print(sequence_to_classify)
#     candidate_labels = ['travel', 'greetings', 'help', 'health']
#     pred = classifier(sequence_to_classify, candidate_labels)
#     my_dict = {'health': ['I am not feeling well today', 'I am well thank you', 'Feeling Low'],
#                'travel': ['I am going home', 'I am going to GYM', 'Going to University']}
#
#     try:
#         response = my_dict[pred['labels'][0]]
#     except:
#         response = 'I did not understand your problem'
#
#     print(response)
#     return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
