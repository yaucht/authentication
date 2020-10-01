FROM python:3.8.6-alpine3.12

COPY requirements.txt /

RUN pip install --no-cache --quiet -r requirements.txt

RUN mkdir /features

COPY . /features/

ENTRYPOINT ["behave"]
