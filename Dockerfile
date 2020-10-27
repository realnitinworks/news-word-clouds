# pull official base image
FROM python:3.8.1-alpine

# install numpy dependencies in alpine
RUN apk update
RUN apk add make automake gcc g++ subversion python3-dev 

# install Pillow dependencies
RUN apk add jpeg-dev zlib-dev

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
