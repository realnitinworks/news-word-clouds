import feedparser
import requests
from flask import Flask, render_template
from bs4 import BeautifulSoup


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


@app.route("/")
def home():
    feed = feedparser.parse(BBC_FEED)
    articles = [
        parse_article(article['link'])
        for article in feed['entries'][:LIMIT]
    ]

    return render_template('home.html', articles=articles)
