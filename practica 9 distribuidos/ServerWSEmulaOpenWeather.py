from flask import Flask, request, jsonify

app = Flask(__name__)

# Datos de ejemplo
weather_data = {
    "Mexico City": {"temperature": 22, "description": "Partly cloudy"},
    "Mazatlan": {"temperature": 28, "description": "Sunny"},
    "Guadalajara": {"temperature": 24, "description": "Thunderstorms"}
}

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if city in weather_data:
        return jsonify(weather_data[city])
    else:
        return jsonify({"error": "City not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
