FROM python:3.7

RUN mkdir /opt/sfia1/

COPY . /opt/sfia1/

WORKDIR /opt/sfia1/

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "app.py"]