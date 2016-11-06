FROM python:3.5-onbuild

RUN mkdir /usr/src/static
ADD . /usr/src/api
WORKDIR /usr/src/api
CMD python manage.py runserver


