FROM python:3.5-onbuild

RUN mkdir /usr/src/sample-server
ADD . /usr/src/sample-server
WORKDIR /usr/src/sample-server
RUN apt-get update && apt-get install -y \
    python-dev \
    python-pip
pip install --requirement /usr/src/sample-server/requirements.txt
CMD python server_script.py