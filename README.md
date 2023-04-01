# code-analyzer

API endpoint designed to collect input code and analyze it with pre-trained model via HuggingFace Transformers library.

## Requirements

Python 3+ : https://www.python.org/downloads/ <br/>

## Setup guide

1. Clone the repository locally
2. Run ```python -m venv venv``` to initiate library root
3. Run ```source venv/bin/activate``` or ```source venv/Scripts/activate``` if you're using GitBash to enable new library acquisition
4. Run ```pip install torch transformers flask``` to acquire flask, troch and transformers libraries.
5. Run ```server.py``` to run the webserver
6. Now you can make a postman POST request to 127.0.0.1:5000/analyze_code endpoint with value assigned to 'content' parameter.
