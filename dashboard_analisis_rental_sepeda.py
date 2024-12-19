import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

day_df = pd.read_csv('https://raw.githubusercontent.com/rifakhaira/Analisis-Data-Rental-Sepeda/refs/heads/main/day.csv')
hour_df = pd.read_csv('https://raw.githubusercontent.com/rifakhaira/Analisis-Data-Rental-Sepeda/refs/heads/main/hour.csv')

datetime_columns = ["dteday"]

for column in datetime_columns:
  day_df[column] = pd.to_datetime(day_df[column])

datetime_columns = ["dteday"]

for column in datetime_columns:
  hour_df[column] = pd.to_datetime(hour_df[column])

day_df.weekday.replace((0,1,2,3,4,5,6), ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'), inplace=True)

st.title('Dashboard Analisis Rental Sepeda')
tab1, tab2 = st.tabs(["Pertanyaan 1", "Pertanyaan 2"])

with tab1:
    st.header("Pada hari apa rental sepeda paling ramai digunakan?")
    fig, ax = plt.subplots()
    ax.bar(x=day_df["weekday"], height=day_df["cnt"])
    ax.set_xlabel("Hari dalam seminggu")
    ax.set_xticklabels(day_df["weekday"], rotation=45)
    ax.set_ylabel("Total rental sepeda")
    ax.set_title("Hari Paling Ramai untuk Merental Sepeda")
    st.pyplot(fig)
    st.write("Rental sepeda paling ramai digunakan pada hari sabtu.")

with tab2:
    st.header("Pada pukul berapa rental sepeda paling ramai digunakan?")
    fig, ax = plt.subplots()
    ax.bar(x=hour_df["hr"], height=hour_df["cnt"])
    ax.set_xticks(range(24))
    ax.set_xticklabels(range(24))
    ax.set_xlabel("Jam dalam satu hari")
    ax.set_ylabel("Total rental sepeda")
    ax.set_title("Jam Paling Ramai untuk Merental Sepeda")
    st.pyplot(fig)
    st.write("Rental sepeda paling ramai digunakan pada pukul 17.00 dan 18.00.")

