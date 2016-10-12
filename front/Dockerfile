FROM ubuntu
RUN apt-get update
RUN apt-get install -y nano wget dialog net-tools
RUN apt-get install -y nginx
RUN mkdir /var/log/front
ADD . /usr/src/front
WORKDIR /usr/src/front
RUN rm /etc/nginx/sites-enabled/default
ADD sites-enabled/ /etc/nginx/sites-enabled
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
EXPOSE 8080
CMD service nginx start
