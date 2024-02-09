## WEATHER FORECAST APP
This application shows the temperature and sky conditions for every 3 hours for up to 5 days.
Once you open the application, select your city and then choose for how many days you want the forecast
information to be shown. And then you choose whether you want the temperature to be displayed in Celsius or 
Fahrenheit, or you chose the sky conditions.

### Technologies used
- This application is built using Python and its modules.
- Streamlit was used as frontend to display the data to the user.
- Datetime was used to convert UTC times to local times.
- Zoneinfo was used to get the local time zone name to be able to convert the UTC times to local times
- Os was used to secure the API key 
- plotly was used to represent the data graphically
- requests was used to get the API data.

The API data are fetched from https://openweathermap.org/

