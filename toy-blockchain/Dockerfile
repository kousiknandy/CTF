FROM python:3
MAINTAINER Kousik@cisco.com

RUN apt-get update && apt-get install -y vim-tiny
RUN pip install bottle
RUN mkdir -p /opt/blockchain
COPY *py /opt/blockchain/
EXPOSE 8880
WORKDIR /opt/blockchain/
ENTRYPOINT ["python3", "validate.py"]
