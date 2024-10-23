from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    ip_info = requests.get('https://ipapi.co/json/').json()
    ip_info['ipv4'] = requests.get('https://api.ipify.org?format=json').json().get('ip')
    return render_template('index.html', ip_info=ip_info)

if __name__ == "__main__":
    app.run(debug=True)