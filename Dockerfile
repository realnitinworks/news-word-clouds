# pull official base image
FROM python:3.8.1-alpine

# install wordcloud dependencies
RUN apk update
RUN apk add make automake gcc g++ subversion python3-dev 
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache freetype-dev
RUN pip install pillow

# set working directory
WORKDIR /usr/src/app

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# add and install requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . .

# run server
CMD python manage.py run -h 0.0.0.0
