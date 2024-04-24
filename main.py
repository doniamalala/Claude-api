import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def get_claude_response():
    # Remplacez 'YOUR_API_KEY' par votre propre clé API Claude AI
    api_key = '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'
    url = 'https://claudeai.com/api/v1/response'
    
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': api_key
    }
    
    data = {
        'text': 'Bonjour Claude AI, ça va ?'
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return 'Erreur: Impossible de récupérer la réponse de Claude AI'

if __name__ == '__main__':
    app.run(debug=True)
    
