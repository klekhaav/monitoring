FROM python:3.5-onbuild

RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install psutil

RUN mkdir /usr/src/sample-server
ADD . /usr/src/sample-server
WORKDIR /usr/src/sample-server
CMD python server_script.py