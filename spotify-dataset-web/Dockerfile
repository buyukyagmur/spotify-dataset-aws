FROM python:3-slim

RUN mkdir /app
WORKDIR /app

ADD requirements.txt .
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

ADD . .

CMD ["python", "app.py"]


