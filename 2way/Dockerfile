FROM httpd:latest
COPY ./index.html /usr/local/apache2/htdocs/
RUN sed -i '/^#LoadModule.*mod_ssl.so/s/^#//' /usr/local/apache2/conf/httpd.conf
RUN sed -i '/^#LoadModule.*mod_socache_shmcb.so/s/^#//' /usr/local/apache2/conf/httpd.conf
RUN sed -i '/^#.*httpd-ssl.conf/s/^#//' /usr/local/apache2/conf/httpd.conf

COPY server.crt /usr/local/apache2/conf/
COPY server.key /usr/local/apache2/conf/
COPY httpd-ssl.conf /usr/local/apache2/conf/extra/
EXPOSE 8443
