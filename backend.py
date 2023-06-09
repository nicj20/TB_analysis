import re
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.downloader.download('vader_lexicon')

def get_data_lines():
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

    return {'neg': neg_scores, 'pos': pos_scores, 'flow': flow}


def get_data_pages():
    with open('haruki_murakami.txt', 'r', encoding='utf-8') as file:
        book = file.read()

    analyzer = SentimentIntensityAnalyzer()

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

    return {'neg': p_neg_scores, 'pos': p_pos_scores, 'flow': p_flow}
