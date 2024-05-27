FROM python:3.11
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app/
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt