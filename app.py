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

    if not lat or not lng:
        return jsonify({'status': 'error', 'zprava': 'Chybí souřadnice!'})

    try:
        # Voláme veřejné API pro nadmořskou výšku
        # Dokumentace: https://open-elevation.com/
        api_url = f"https://api.open-elevation.com/api/v1/lookup?locations={lat},{lng}"
        
        # Server (Render) teď požádá jiný server o data
        response = requests.get(api_url, timeout=10)
        data = response.json()
        
        # Vytáhneme nadmořskou výšku z výsledků
        vyska = data['results'][0]['elevation']
        
        return jsonify({
            'status': 'ok',
            'zprava': f"Zjištěná nadmořská výška: {vyska} m n. m."
        })
        
    except Exception as e:
        return jsonify({
            'status': 'error', 
            'zprava': f"Chyba při analýze terénu: {str(e)}"
        })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
