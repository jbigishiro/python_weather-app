import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
city = st.text_input("City")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature in Fahrenheit", "Temperature in Celsius", "Precipitation"))
if days > 1:
    d = "days"
else:
    d = "day"

if city:
    try:
        filtered_data = get_data(place=city, forecasted_days=days)

        st.subheader(f"{option} for {days} {d} in {city.title()}")

        dates = [dict["dt_txt"] for dict in filtered_data]

        if option == "Temperature in Fahrenheit":
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            temperatures_in_F = [round((k - 273.15) * 9 / 5 + 32, 2) for k in temperatures]

            figure = px.line(x=dates, y=temperatures_in_F, labels={"x": "Time", "y": "Temperature"})
            st.plotly_chart(figure)

        elif option == "Temperature in Celsius":
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            temperatures_in_F = [round(k - 273.15) for k in temperatures]

            figure = px.line(x=dates, y=temperatures_in_F, labels={"x": "Time", "y": "Temperature"})
            st.plotly_chart(figure)

        elif option == "Precipitation":
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]

            images = {'Rain': "sky_images/rain.png", 'Clouds': "sky_images/cloud.png",
                      'Clear': "sky_images/clear.png", 'Snow': "sky_images/snow.png"}
            image_paths = [images[condition] for condition in sky_conditions]

            st.image(image_paths, caption=dates, width=115)

    except KeyError:
        st.subheader("The city is not available, try again")

else:
    st.subheader("Write the name the city")
