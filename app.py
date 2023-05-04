from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Endpoint to return the version of the application
@app.route('/version')
def version():
    return jsonify({'version': '1.0'})

# Endpoint to check if a number is prime or not
@app.route('/is_prime')
def is_prime():
    num = int(request.args.get('num'))
    if num < 2:
        return jsonify({'is_prime': False})
    for i in range(2, int(num/2) + 1):
        if (num % i) == 0:
            return jsonify({'is_prime': False})
    return jsonify({'is_prime': True})

# Endpoint to get the current weather for a US zip code
@app.route('/weather')
def weather():
    zip_code = request.args.get('zip')
    if not zip_code:
        return jsonify({'error': 'Zip code parameter missing'}), 400
    # Use OpenWeatherMap API to get the weather
    api_key = '6887baf361372fd494b3841395e9f0c9'
    url = f'http://api.openweathermap.org/data/2.5/weather?zip={zip_code},us&appid={api_key}'
    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({'error': 'Unable to fetch weather information'}), 500
    data = response.json()
    return jsonify({'temperature': data['main']['temp'], 'humidity': data['main']['humidity']})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
