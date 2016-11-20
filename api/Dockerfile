FROM python:3.5-onbuild

RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip

RUN mkdir /usr/src/static
ADD . /usr/src/api
WORKDIR /usr/src/api
CMD python manage.py runserver


