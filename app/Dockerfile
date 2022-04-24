# Flask docker image for serving site.
FROM python:alpine
LABEL Maintainer="sean bourg <sean.bourg@gmail.com>"

WORKDIR /app

# copy requirements file.
COPY ./requirements.txt /tmp/requirements.txt
COPY ./server.py /app/server.py

# install the dependencies and packages in the requirements file
RUN apk update && \
    apk upgrade && \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    pip install -r /tmp/requirements.txt 
    

# configure the container to liston on port 8080 and run server file.
EXPOSE 8080
CMD [ "python", "/app/server.py" ]