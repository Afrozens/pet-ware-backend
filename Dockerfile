FROM python:3.11

# set work directory
WORKDIR /app/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN useradd -rm -d /code -s /bin/bash -g root -G sudo -u 1001 ubuntu

COPY ./startup.sh /app/startup.sh

RUN chmod +x /app/startup.sh

# copy requirements file
COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

USER ubuntu

EXPOSE 8000

COPY ./app /app/app/

ENV PYTHONPATH=/app

CMD bash -c 'uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload'