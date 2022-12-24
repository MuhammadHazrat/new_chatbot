import os

import tf as tf
from flask import Flask, request
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("typeform/distilbert-base-uncased-mnli")

classifier = TFAutoModelForSequenceClassification.from_pretrained("typeform/distilbert-base-uncased-mnli")

app = Flask(__name__)

# port = int(os.environ.get('PORT', 5000))


@app.route('/', methods=['POST', 'GET'])
def chat():
    sequence_to_classify = request.args.get('line')
    if sequence_to_classify == None:
        return "No inputs given"
    print("input", sequence_to_classify)

    input_ids = tokenizer.encode(sequence_to_classify, return_tensors='tf')

    candidate_labels = ['travel', 'greetings', 'help', 'health']

    attention_mask = tf.ones(input_ids.shape, dtype=tf.int32)

    pred = classifier(input_ids, attention_mask)
    print("prediction: ", pred)
    my_dict = {'health': ['I am not feeling well today', 'I am well thank you', 'Feeling Low'],
               'travel': ['I am going home', 'I am going to GYM', 'Going to University']}

    try:
        response = my_dict[pred['labels'][0]]
    except:
        response = 'I did not understand your problem'

    print(response)
    return response


if __name__ == '__main__':
    app.run(debug=True)
