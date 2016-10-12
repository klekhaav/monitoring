FROM tutum/nginx
RUN rm /etc/nginx/sites-enabled/default
ADD sites-enabled/ /etc/nginx/sites-enabled
ADD ssl/private.key /etc/nginx/private.key
ADD ssl/server.crt /etc/nginx/server.crt
RUN rm /etc/nginx/nginx.conf
ADD nginx.conf /etc/nginx/nginx.conf
CMD service nginx restart