import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff
import matplotlib.pyplot as plt

st.title("Dashboard")

data_day = pd.read_csv("https://raw.githubusercontent.com/rifakhaira/Analisis-Data-Rental-Sepeda/refs/heads/main/day.csv")
data_hour = pd.read_csv("https://raw.githubusercontent.com/rifakhaira/Analisis-Data-Rental-Sepeda/refs/heads/main/hour.csv")

st.dataframe(data_day.head())
st.subheader("Pada hari apa rental sepada paling ramai ?")
st.title("Hari Paling Ramai untuk Merental Sepeda")
day_df_weekday = data_day.groupby(by=["weekday"]).agg({"casual": "mean","registered": "mean","cnt": "mean"})
fig1 = px.bar(day_df_weekday, x=day_df_weekday.index, y=["casual", "registered", "cnt"],labels={"value": "Total rental sepeda", "weekday": "Hari dalam seminggu"})
st.plotly_chart(fig1)


st.subheader("Pada jam berapa rental sepada paling ramai ?")
hour_df = data_hour.groupby(by=["hr"]).agg({"casual": "mean","registered": "mean","cnt": "mean"})
fig2 = px.bar(hour_df, x=hour_df.index, y=["cnt"],labels={"value": "Total rental sepeda", "hr": "Jam dalam satu hari"})
st.plotly_chart(fig2)


st.subheader("Pada bulan dan hari apa rental sepeda paling ramai ?")
day_df_month = data_day.groupby(by=["mnth" ,"weekday"]).agg({"casual": "mean","registered": "mean","cnt": "mean"}).reset_index()
melted_df = day_df_month.melt(
    id_vars=["mnth", "weekday"],
    value_vars=["cnt", "casual", "registered"],
    var_name="category",
    value_name="value"
)

# Pilihan bulan
selected_month = st.selectbox("Select a month", melted_df["mnth"].unique())

# Filter Dataframe
filtered_df = melted_df[melted_df["mnth"] == selected_month]

# Plot
fig = px.line(filtered_df, x="weekday", y="value", color="category", 
              title=f"Data for Month {selected_month}", 
              labels={"value": "Total rental sepeda", "category": "Type", "weekday": "Hari dalam seminggu"})
st.plotly_chart(fig)

selected_hour = st.selectbox("Select a hour", data_hour["hr"].unique())
hour_df_weather = data_hour.groupby(by=["hr", "weathersit"]).agg({"cnt": "mean"}).reset_index()
st.dataframe(hour_df_weather[hour_df_weather["hr"] == selected_hour])
fig3 = px.bar(hour_df_weather[hour_df_weather["hr"] == selected_hour], x="weathersit", y="cnt", labels={"weathersit": "Cuaca", "cnt": "Total rental sepeda"})
st.plotly_chart(fig3)
