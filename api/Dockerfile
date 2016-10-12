FROM python:3.5-onbuild

RUN mkdir /usr/src/static
ADD . /usr/src/app
WORKDIR /usr/src/app
CMD python manage.py runserver


