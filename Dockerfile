FROM python:latest

ADD . /opt

RUN pip3 install -r /requirements.txt

ENTRYPOINT [ "python3", "/opt/IRCrobot.py" ]
