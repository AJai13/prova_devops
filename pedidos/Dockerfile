FROM python:3.9

WORKDIR /app

COPY app.py .

RUN pip install flask redis requests mysql-connector-python

EXPOSE 3002

CMD ["python3", "app.py"]
