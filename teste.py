import streamlit as st
import pandas as pd
import time

@st.cache_data
def load_data():
    chart_data = pd.read_csv('Arquivos/01 Spotify.csv')
    time.sleep(10)
    return chart_data

chart_data = load_data()


st.title('Spotify Dashboard', anchor=None)

chart_data = pd.read_csv('Arquivos/01 Spotify.csv')
chart_data.set_index("Track", inplace=True)

artistas = chart_data["Artist"].value_counts().index
Artista_select = st.sidebar.selectbox("Artistas", artistas)
chart_filtered = chart_data[chart_data["Artist"] == Artista_select]

Albuns = chart_filtered["Album"].value_counts().index
Album_select = st.sidebar.selectbox("Albuns", Albuns)
chart_filtered = chart_filtered[chart_filtered["Album"] == Album_select]

st.session_state['chart_filtered_save'] = chart_filtered

display = st.checkbox('display')

if display:
    st.write(chart_filtered['Stream'])
st.bar_chart(chart_filtered['Stream'])  