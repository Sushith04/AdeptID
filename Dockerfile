FROM python:3.9.10

COPY ./app /app/app/
COPY ./requirements.txt /app/
COPY ./data.csv /app/
COPY ./run.py /app/
RUN pip install -r /app/requirements.txt

EXPOSE 5000 
WORKDIR /app
ENTRYPOINT gunicorn -w 4 -b 0.0.0.0:5000 run:app