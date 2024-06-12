from flask import Flask,render_template,request
from api_key import API_KEY
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET', 'POST'])
def weather():
    if request.method == "POST":
        city = request.form['city']
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
            temperature = weather_data['main']['temp']
            feels_like = weather_data['main']['feels_like']
            humidity = weather_data['main']['humidity']
            pressure = weather_data['main']['pressure']
            wind_speed = weather_data['wind']['speed']
            wind_deg = weather_data['wind']['deg']
            description = weather_data['weather'][0]['description']
            icon = weather_data['weather'][0]['icon']
            visibility = weather_data['visibility']
            sunrise = weather_data['sys']['sunrise']
            sunset = weather_data['sys']['sunset']
            return render_template('weather.html', city=city, temperature=temperature, feels_like=feels_like, humidity=humidity, pressure=pressure, wind_speed=wind_speed, wind_deg=wind_deg,description=description, icon=icon, visibility=visibility, sunrise=sunrise,sunset=sunset)
        else:
            return 'There was a problem regarding the weather data'
    return render_template('weather-form.html')

if __name__ == "__main__":
    app.run(debug=True)