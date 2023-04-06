from flask import Flask, jsonify, request
import mysql.connector
import os

app = Flask(__name__)

# Connect to the RDS MySQL database
db = mysql.connector.connect(
    host=os.environ.get('DB_HOST'),
    user=os.environ.get('DB_USER'),
    password=os.environ.get('DB_PASSWORD'),
    database=os.environ.get('DB_NAME')
)

# Route to get weather data for a specific city
@app.route('/weather_data/<city_name>', methods=['GET'])
def get_weather_data(city_name):
    cursor = db.cursor()
    query = "SELECT * FROM weather_data WHERE city_name = %s"
    cursor.execute(query, (city_name,))
    data = cursor.fetchone()
    cursor.close()

    if data:
        result = {
            "city_name": data[0],
            "temperature": data[1],
            "humidity": data[2],
            "wind_speed": data[3],
            "description": data[4]
        }
        return jsonify(result)
    else:
        return jsonify({"error": "City not found"}), 404

# Route to add weather data for a new city
@app.route('/weather_data', methods=['POST'])
def add_weather_data():
    data = request.get_json()
    city_name = data['city_name']
    temperature = data['temperature']
    humidity = data['humidity']
    wind_speed = data['wind_speed']
    description = data['description']

    cursor = db.cursor()
    query = "INSERT INTO weather_data VALUES (%s, %s, %s, %s, %s)"
    values = (city_name, temperature, humidity, wind_speed, description)
    cursor.execute(query, values)
    db.commit()
    cursor.close()

    return jsonify({"message": "Weather data added successfully"})

# Route to update weather data for an existing city
@app.route('/weather_data/<city_name>', methods=['PUT'])
def update_weather_data(city_name):
    data = request.get_json()
    temperature = data['temperature']
    humidity = data['humidity']
    wind_speed = data['wind_speed']
    description = data['description']

    cursor = db.cursor()
    query = "UPDATE weather_data SET temperature = %s, humidity = %s, wind_speed = %s, description = %s WHERE city_name = %s"
    values = (temperature, humidity, wind_speed, description, city_name)
    cursor.execute(query, values)
    db.commit()
    cursor.close()

    return jsonify({"message": "Weather data updated successfully"})

# Route to delete weather data for a city
@app.route('/weather_data/<city_name>', methods=['DELETE'])
def delete_weather_data(city_name):
    cursor = db.cursor()
    query = "DELETE FROM weather_data WHERE city_name = %s"
    cursor.execute(query, (city_name,))
    db.commit()
    cursor.close()

    return jsonify({"message": "Weather data deleted successfully"})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
