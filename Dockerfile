FROM python:3.6

WORKDIR /cogs
ADD . .

RUN pip install -U pip wheel setuptools \
 && pip install -r requirements.txt

EXPOSE 8000

CMD python main.py
