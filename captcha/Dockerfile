FROM ubuntu:xenial
MAINTAINER kousik@cisco.com

RUN apt-get update && apt-get -yq install python3
RUN apt-get -yq install imagemagick
RUN mkdir -p /wecatpcha
ADD cgi-bin/captcha /wecaptcha/cgi-bin/captcha
ADD cgi-bin/catchme.py /wecaptcha/cgi-bin/catchme.py
WORKDIR /wecaptcha
EXPOSE 8000
ENTRYPOINT ["python3", "-m", "http.server", "--cgi", "8000"]
