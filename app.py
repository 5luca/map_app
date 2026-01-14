import requests
from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/vypocet', methods=['GET'])
def vypocet():
    lat = request.args.get('lat')
    lng = request.args.get('lng')

    try:
        # Voláme skutečnou databázi výšek (Open-Topo-Data)
        api_url = f"https://api.opentopodata.org/v1/test-dataset?locations={lat},{lng}"
        response = requests.get(api_url, timeout=10)
        data = response.json()
        
        # Vytáhneme výšku v metrech
        vyska = data['results'][0]['elevation']
        
        return jsonify({
            'status': 'ok',
            'zprava': f"Analýza terénu dokončena.\nNadmořská výška: {int(vyska)} m n. m."
        })
    except Exception as e:
        return jsonify({'status': 'error', 'zprava': f"Chyba při zjišťování výšky: {str(e)}"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
