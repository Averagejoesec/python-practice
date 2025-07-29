import streamlit as st
import plotly.express as px
import pandas
import sqlite3

connection = sqlite3.connect("data.db")

df = pandas.read_sql_query("SELECT * from temperature", connection)

figure = px.line(x=df["date"], y=df["temperature"],
                labels={"x": "Date", "y": "Temperature (C)"})

st.plotly_chart(figure)