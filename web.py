import streamlit as st
import plotly.express as px
import re
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

with open('haruki_murakami.txt', 'r', encoding='utf-8') as file:
    book = file.read()

analyzer = SentimentIntensityAnalyzer()

filter = re.compile("[^\n]+[^\n]+")
quotes = re.findall(filter, book)

neg_scores = []
pos_scores = []


for quote in quotes:
    scores = analyzer.polarity_scores(quote)
    neg_scores.append(scores['neg'])
    pos_scores.append(scores['pos'])
    ran = len(quotes)

flow = []
for n in list(range(ran)):
    flow.append(n)


st.title("Book Sentiment Flow")
st.header("Positive lines in the book")
figure = px.line(x=flow, y=neg_scores, labels={"x": "Lines", "y": "Positivity"})
st.plotly_chart(figure)

st.header("Negative lines in the book")
figure = px.line(x=flow, y=pos_scores, labels={"x": "Lines", "y": "Negativity"})
st.plotly_chart(figure)

#-----------------------------------------------#

p_neg_scores = []
p_pos_scores = []

filter2 = re.compile("\n\n\n[0-9]+")
pages = re.split(filter2, book)

for page in pages:
    p_scores = analyzer.polarity_scores(page)
    p_neg_scores.append(p_scores['neg'])
    p_pos_scores.append(p_scores['pos'])
    p_ran = len(pages)

p_flow = []
for n in list(range(p_ran)):
    p_flow.append(n)


st.header("Positivity in pages")
figure = px.line(x=p_flow, y=p_pos_scores, labels={"x": "Pages", "y": "Positivity"})
st.plotly_chart(figure)

st.header("Negativity in pages")
figure = px.line(x=p_flow, y=p_neg_scores, labels={"x": "Pages", "y": "Negativity"})
st.plotly_chart(figure)

#END