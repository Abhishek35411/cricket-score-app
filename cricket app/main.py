from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

API_KEY = "0f58eca1-391c-4879-9ad0-f1ae2a781cc6"
API_URL = "https://api.cricapi.com/v1/currentMatches"

def get_matches():
    """Fetch live match data from the API."""
    params = {"apikey": API_KEY}
    response = requests.get(API_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data.get("data", [])  # Return match list or empty if not found
    return []

@app.route("/")
def index():
    """Render the homepage with match listings."""
    matches = get_matches()
    return render_template("index.html", matches=matches)

@app.route("/match/<match_id>")
def match_details(match_id):
    """Render match details page."""
    matches = get_matches()
    for match in matches:
        if match.get("id") == match_id:
            return render_template("match.html", match=match)
    return render_template("match.html", error="Match not found"), 404

if __name__ == "__main__":
    app.run(debug=True)
