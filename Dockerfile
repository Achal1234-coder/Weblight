FROM python:3.10

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /

RUN pip install -r /requirements.txt

RUN mkdir /code

WORKDIR /code

COPY . /code/

CMD ["python", "manage.py", "runserver"]