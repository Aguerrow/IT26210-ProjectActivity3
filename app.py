from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_ip_info():
    api_url = 'https://ipapi.co/json/'
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()

@app.route('/')
def index():
    ip_info = get_ip_info()
    return render_template('index.html', ip_info=ip_info)

if __name__ == "__main__":
    app.run(debug=True)
