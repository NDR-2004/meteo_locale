import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
from dotenv import load_dotenv

load_dotenv() # Charge les variables du fichier .env

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

API_KEY = os.getenv("API_KEY")  # Récupère la clé depuis .env

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/meteo")
def meteo():
    ville = request.args.get("ville")
    if not ville:
        return jsonify({"error": "Aucune ville spécifiée"}), 400

    url = f"http://api.openweathermap.org/data/2.5/weather?q={ville}&appid={API_KEY}"
    reponse = requests.get(url)

    if reponse.status_code != 200:
        return jsonify({"error": "Ville introuvable"}), 404

    donnees = reponse.json()
    temp = round(donnees["main"]["temp"] - 273.15, 1)
    desc = donnees["weather"][0]["description"]
    vent = donnees["wind"]["speed"]

    return jsonify({
        "ville": ville,
        "temperature": temp,
        "description": desc,
        "vent": vent
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

