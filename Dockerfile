FROM python:3.10.5-buster

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY simpleview.py /
RUN chmod 775 /simpleview.py
ENTRYPOINT ["./simpleview.py"]