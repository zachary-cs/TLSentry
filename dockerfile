FROM python:3.11-rc-alpine

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /app

COPY src .

CMD  [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]