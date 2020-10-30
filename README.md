# News Word Clouds
A web application for building Word Cloud from news artciles using Python and Flask.

## Word Cloud
Word clouds are a popular way to visualise large amounts of text. Word clouds are images showing scattered words in different sizes, where words that appear more frequently in the given text are larger, and less common words are smaller or not shown at all.

## Application

The users will see a page similar to the one shown below, but containing the latest news headlines from BBC news. The app uses web-scraping, parses RSS feeds and builds image files directly in memory to display the word cloud.

![AddMovie](/screenshots/word_cloud.png)

## Launch Application

This application could be run locally using Docker like so:

1. Clone the repo

```
# git clone https://github.com/realnitinworks/news-word-clouds.git
```

2. Build and start the application

This step starts the Flask web application in a docker container listening on port 5000
```
# cd news-word-clouds
# docker-compose up -d --build
```

3. Open browser at **127.0.0.1:5000** to see the word cloud







