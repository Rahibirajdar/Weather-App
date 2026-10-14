import streamlit as st
import requests
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY=os.getenv('WEATHER_API_KEY')
st.set_page_config(page_title="weather app",page_icon="⛅")
st.title("Weather App🌦️")
st.write("Enter the city name and clicK the button to fetch the weather data")
city=st.text_input("Enter City Name")
if(st.button("fetch weather")):
    response= requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric')
    if(response.status_code==200):
        st.success("WEATHER DATA FETCHED SUCCESSFULLY")
        data=response.json()

        temprature=data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data ['wind']['speed']
        weather_condition =data['weather'][0]['description']
        name=data['name']
        country =data['sys']['country']

        st.subheader(f'{name},{country}')
        #CREATE 2COL AND 2 ROWS
        col1,col2=st.columns(2)
        col3,col4=st.columns(2)

        col1.metric('Temperature🌡️',f'{temprature}℃')
        col2.metric('Humidity💧',f'{humidity}%')
        col3.metric('Windspeed🍃',f'{wind_speed}')
        col4.metric('Weather Condition🌧️',f'{weather_condition}')

    else:
        st.error("ENTER VALID CITY")