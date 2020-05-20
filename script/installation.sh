#!/usr/bin/env bash

sudo apt update -y

sudo apt install python3 -y

sudo apt install python3-pip -y

sudo apt install python3-venv -y

python3 -m venv venv

source /var/lib/jenkins/workspace/carhire_freestyle/venv/bin/activate

pip3 install -r requirements.txt

cd /var/lib/jenkins/workspace/carhire_freestyle

export CAR_HIRE_DB_URI=mysql+pymysql://root:helloworld@34.89.27.192/carhire_db

export SECRET_KEY=kjg345g34kjg53jk4g5kj34h535n

export CSRF_SECRET_KEY=hjkg5324gg890ddy8g98dygyds

gunicorn --bind=0.0.0.0:5000 app:app