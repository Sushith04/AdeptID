FROM ubuntu

RUN apt-get -qq update && apt-get -qq install -y python3 python3-pip
COPY ./app /app/app/
COPY ./requirements.txt /app/
COPY ./data.csv /app/
COPY ./run.py /app/
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000 
ENTRYPOINT gunicorn -w 4 -b 0.0.0.0:5000 run:app