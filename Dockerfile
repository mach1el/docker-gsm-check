FROM python:3.10.5-buster

COPY requiremens.txt /
RUN pip3 install -r requiremens.txt

COPY simpleview.py /
ENTRYPOINT ['python3','simpleview.py']