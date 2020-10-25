import feedparser
from flask import Flask


BBC_FEED = "http://feeds.bbci.co.uk/news/world/rss.xml"


# instantiate the Flask app
app = Flask(__name__)


@app.route("/")
def home():
    feed = feedparser.parse(BBC_FEED)
    urls = [
        article['link']
        for article in feed['entries']
    ]

    return str(urls)
