from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/vypocet', methods=['GET'])
def vypocet():
    # Získání souřadnic z adresy (přijdou jako text)
    lat = request.args.get('lat', '0')
    lng = request.args.get('lng', '0')
    
    # Tady můžeš udělat nějakou vědeckou analýzu
    # Pro začátek jen potvrdíme příjem dat
    odpoved = {
        "status": "ok",
        "zprava": f"Python přijal souřadnice!\nŠířka: {lat}\nDélka: {lng}\nAnalyzuji terén..."
    }
    
    return jsonify(odpoved)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)