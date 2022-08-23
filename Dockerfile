FROM python:3.10.6

WORKDIR /work

COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt


WORKDIR /app

COPY ./src/ .

CMD ["python3", "./server.py"]
