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
        # Zavoláme bezplatnou službu pro zjištění nadmořské výšky
        url = f"https://api.open-elevation.com/api/v1/lookup?locations={lat},{lng}"
        response = requests.get(url).json()
        
        vyska = response['results'][0]['elevation']
        
        zprava = f"Analýza dokončena!\nBod se nachází v nadmořské výšce {vyska} metrů."
        
        return jsonify({
            'status': 'ok',
            'zprava': zprava
        })
    except Exception as e:
        return jsonify({'status': 'error', 'zprava': "Nepodařilo se získat data o terénu."})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
