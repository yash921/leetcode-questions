FROM alpine

RUN apk update

# Install software
RUN apk add apache2

COPY index.html /var/www/localhost/htdocs/

RUN echo 'rm -rf /var/run/httpd/*' >> ~/.bashrc 

RUN echo '/usr/sbin/httpd' >> ~/.bashrc 

ENTRYPOINT [ "/usr/sbin/httpd","-D","FOREGROUND"]

EXPOSE 80
