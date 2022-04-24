# Build a docker container that creates a postgres database image.
FROM postgres:alpine
LABEL Maintainer="sean bourg <sean.bourg@gmail.com>"

# update container.
RUN apk update && apk upgrade; 

# copy over startup folder.
COPY docker-entrypoint-initdb.d /docker-entrypoint-initdb.d

# expose ports
EXPOSE 5432