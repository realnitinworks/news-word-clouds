import feedparser
import requests
import base64
import io
from flask import Flask, render_template
from bs4 import BeautifulSoup
from wordcloud import WordCloud


BBC_FEED = "http://feeds.bbci.co.uk/news/world/rss.xml"
LIMIT = 2


# instantiate the Flask app
app = Flask(__name__)


def parse_article(article_url):
    """
    Download and parse content of the article at article_url
    """
    print(f"Downloading from {article_url}")
    r = requests.get(article_url)
    soup = BeautifulSoup(r.text, "html.parser")
    paragraphs = soup.find_all('p')
    text = "\n".join(p.get_text() for p in paragraphs)
    return text


def get_wordcloud(text):
    """
    Convert text to a word cloud
    """
    pillow_image = WordCloud().generate(text=text).to_image()
    img = io.BytesIO()
    pillow_image.save(img, "PNG")
    img.seek(0)
    # .decode -> returns base64 string instead of base64 byte string
    # .b64encode -> returns base64 byte string
    img_b64 = base64.b64encode(img.getvalue()).decode()
    return img_b64


@app.route("/")
def home():
    feed = feedparser.parse(BBC_FEED)
    articles = [
        get_wordcloud(parse_article(article['link']))
        for article in feed['entries'][:LIMIT]
    ]

    return render_template('home.html', articles=articles)
