# src/app.py
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Intelligent LRU Cache")

st.title("🧠 Intelligent API Cache (LRU + ML)")

df = pd.read_csv("data/access_logs.csv")

st.subheader("Cache Access Logs")
st.dataframe(df.tail(20))

st.subheader("Cache Hit Rate")
hit_rate = df["hit"].mean() * 100
st.metric("Hit Rate", f"{hit_rate:.2f}%")
