from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch
import pickle

app = Flask(__name__)
CORS(app)

# Load the tokenizer and model
with open('tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

model = AutoModelForQuestionAnswering.from_pretrained('bert-base-uncased')
with open('model.pkl', 'rb') as f:
    model.load_state_dict(pickle.load(f))

model.eval()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    question = data['question']
    context = data['context']
    
    inputs = tokenizer.encode_plus(question, context, add_special_tokens=True, return_tensors='pt')
    input_ids = inputs['input_ids'].tolist()[0]

    with torch.no_grad():
        output = model(**inputs)
    
    answer_start_scores = output.start_logits
    answer_end_scores = output.end_logits

    answer_start = torch.argmax(answer_start_scores)
    answer_end = torch.argmax(answer_end_scores) + 1
    
    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end]))

    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
