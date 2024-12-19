import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff
import matplotlib.pyplot as plt

st.title("Dashboard")

data_day = pd.read_csv("dataset/day.csv")
data_hour = pd.read_csv("dataset/hour.csv")

st.dataframe(data_day.head())
# Pada hari apa rental sepada paling ramai
st.subheader("Pada hari apa rental sepada paling ramai")
day_df_weekday = data_day.groupby(by=["weekday"]).agg({"casual": "mean","registered": "mean","cnt": "mean"})
fig1 = px.bar(day_df_weekday, x=day_df_weekday.index, y=["casual", "registered", "cnt"])
st.plotly_chart(fig1)

st.subheader("Pada jam berapa rental sepada paling ramai")
hour_df = data_hour.groupby(by=["hr"]).agg({"casual": "mean","registered": "mean","cnt": "mean"})
fig2 = px.bar(hour_df, x=hour_df.index, y=["cnt"])
st.plotly_chart(fig2)


st.subheader("Trend (bulan) rental dalam seminggu")
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
              labels={"value": "Mean Value", "category": "Type", "weekday": "Weekday"})
st.plotly_chart(fig)

selected_hour = st.selectbox("Select a hour", data_hour["hr"].unique())
hour_df_weather = data_hour.groupby(by=["hr", "weathersit"]).agg({"cnt": "mean"}).reset_index()
st.dataframe(hour_df_weather[hour_df_weather["hr"] == selected_hour])
fig3 = px.bar(hour_df_weather[hour_df_weather["hr"] == selected_hour], x="weathersit", y="cnt")
st.plotly_chart(fig3)