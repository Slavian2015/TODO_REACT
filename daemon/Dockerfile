FROM python:3.10

RUN mkdir app
WORKDIR /app

ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.

RUN pip install --upgrade pip
RUN pip install apscheduler
RUN pip install install psycopg2-binary

CMD ["python", "main.py"]