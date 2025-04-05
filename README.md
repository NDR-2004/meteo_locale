# 🌤️ Météo Locale – par Nahem Rigaldies

Bienvenue sur **Météo Locale**, une application web simple et rapide pour consulter la météo actuelle d'une ville en temps réel 🌍.  
Ce projet utilise **HTML, CSS, JavaScript et Python (Flask)** et est hébergé en ligne sur Render.

---

## 🔗 Site en ligne

👉 [Accéder au site météo](https://meteo-nahem.onrender.com/) 

---

## ⚙️ Fonctionnalités

- Entrée du nom d'une ville
- Affichage en temps réel :
  - Température (°C)
  - Description du ciel
  - Vitesse du vent
- Design simple
- Appel d’une API via back-end Flask sécurisé (clé API cachée)
- Déployé gratuitement avec Render

---

## 🛠️ Technologies utilisées

- HTML/CSS/JavaScript
- Flask (Python)
- OpenWeatherMap API
- Render.com pour l’hébergement
- Git & GitHub pour la version et le déploiement

---

## 🚀 Lancer le projet en local

```bash
git clone https://github.com/NDR-2004/meteo_locale.git
cd meteo_locale
pip install -r requirements.txt
```
## Créer un fichier .env à la racine :
API_KEY=ta_clé_openweathermap

## Puis lance le serveur :
```bash
python app.py
```
## Accéder à l'application via http://localhost:8000

### 📁 Arborescence du projet
meteo_locale/
├── app.py
├── requirements.txt
├── .env (non versionné)
├── templates/
│   └── index.html
├── static/
│   ├── CSS_API_meteo.css
│   └── JS_API_meteo.js

## 🧠 Auteur
Projet réalisé par Nahem Rigaldies — Étudiant en data, IA et technologie à l'IA School.




