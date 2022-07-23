FROM python:3.10-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt
COPY data data
COPY scanner scanner
COPY app.py app.py

run pip3 install -r requirements.txt

CMD  [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]