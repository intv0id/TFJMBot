FROM python:latest

ADD . /opt

RUN pip3 install -r /opt/requirements.txt

ENTRYPOINT [ "python3", "/opt/main.py" ]
