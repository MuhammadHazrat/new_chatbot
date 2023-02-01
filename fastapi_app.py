from fastapi import FastAPI
from joblib import load


# Load the classifier from the binary file
classifier = load("joblib_classifier.joblib")
print(type(classifier))
app = FastAPI()
@app.get('/response')
async def get_response(sentence: str):
    if sentence == None:
        return False
    candidate_labels = ['travel', 'greetings', 'help', 'health']
    pred = classifier(sentence, candidate_labels)
    my_dict = {'health': ['I am not feeling well today', 'I am well thank you', 'Feeling Low'],
               'travel': ['I am going home', 'I am going to GYM', 'Going to University']}
    try:
        response = my_dict[pred['labels'][0]]
    except:
        response = 'I did not understand your problem'
    return response