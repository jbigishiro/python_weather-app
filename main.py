import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
if days > 1:
    d = "days"
else:
    d = "day"

if place:
    st.subheader(f"{option} for the next {days} {d} in {place}")

    filtered_data = get_data(place=place, forecasted_days=days)
    dates = [dict["dt_txt"] for dict in filtered_data]

    if option == "Temperature":
        temperatures = [dict["main"]["temp"] for dict in filtered_data]
        temperatures_in_F = [round((k - 273.15) * 9 / 5 + 32, 2) for k in temperatures]

        figure = px.scatter(x=dates, y=temperatures_in_F, labels={"x": "Time", "y": "Temperature"})
        st.plotly_chart(figure)

    elif option == "Sky":
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]

        images = {'Rain': "sky_images/rain.png", 'Clouds': "sky_images/cloud.png",
                  'Clear': "sky_images/clear.png", 'Snow': "sky_images/snow.png"}
        image_paths = [images[condition] for condition in sky_conditions]

        # figure = px.scatter(x=dates, y=sky_conditions, labels={"x": "Time", "y": "Sky"})
        st.image(image_paths, width=115)

else:
    st.subheader("Select the place")