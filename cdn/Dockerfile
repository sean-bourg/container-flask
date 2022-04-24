# Build a docker container that creates a nginx frontend.
FROM nginx:alpine
LABEL Maintainer="sean bourg <sean.bourg@gmail.com>"

# update environment.
RUN apk update && apk upgrade; 

# copy of nginx config files.
COPY conf.d  /etc/nginx/conf.d

# expose port 80 and start nginx.
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]