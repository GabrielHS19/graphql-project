FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /server
WORKDIR /server
COPY requirements.txt /server/
RUN pip install -r requirements.txt
COPY . /server/
