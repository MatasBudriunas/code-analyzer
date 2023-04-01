from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForMaskedLM

app = Flask(__name__)
tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")
model = AutoModelForMaskedLM.from_pretrained("microsoft/codebert-base")


@app.route('/analyze_code', methods=['POST'])
def analyze_code():
    content = request.form.get('content')
    inputs = tokenizer(content, return_tensors="pt")
    outputs = model(**inputs)
    response_text = tokenizer.decode(outputs.logits.argmax(-1)[0], skip_special_tokens=True)
    return jsonify(response_text)


if __name__ == '__main__':
    app.run(debug=True)
