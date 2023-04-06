import os
import requests
import mysql.connector

def lambda_handler(event, context):
    # Connect to the RDS MySQL database
    db = mysql.connector.connect(
        host=os.environ.get('DB_HOST'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        database=os.environ.get('DB_NAME')
    )

    # Get the list of cities to update
    cities = ['London', 'New York', 'Tokyo']

    # Loop through the list of cities and update the weather data in the database
    for city in cities:
        # Call the weather API to get the latest weather data for the city
        api_key = os.environ.get('API_KEY')
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()

        # Extract the relevant weather data from the API response
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        description = data['weather'][0]['description']

        # Update the weather data in the database
        cursor = db.cursor()
        query = "UPDATE weather_data SET temperature = %s, humidity = %s, wind_speed = %s, description = %s WHERE city_name = %s"
        values = (temperature, humidity, wind_speed, description, city)
        cursor.execute(query, values)
        db.commit()
        cursor.close()
