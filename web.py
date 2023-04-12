import streamlit as st
import plotly.express as px
from backend import get_data_lines, get_data_pages

st.title("Book Sentiment Flow")
st.header("Positive lines in the book")
figure = px.line(x=get_data_lines()['flow'], y=get_data_lines()['pos'], labels={"x": "Lines", "y": "Positivity"})
st.plotly_chart(figure)

st.header("Negative lines in the book")
figure = px.line(x=get_data_lines()['flow'], y=get_data_lines()['neg'], labels={"x": "Lines", "y": "Negativity"})
st.plotly_chart(figure)

#-----------------------------------------------#


st.header("Positivity in pages")
figure = px.line(x=get_data_pages()['flow'], y=get_data_pages()['pos'], labels={"x": "Pages", "y": "Positivity"})
st.plotly_chart(figure)

st.header("Negativity in pages")
figure = px.line(x=get_data_pages()['flow'], y=get_data_pages()['neg'], labels={"x": "Pages", "y": "Negativity"})
st.plotly_chart(figure)

