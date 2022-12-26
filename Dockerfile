FROM python:3.10-alpine
WORKDIR /app

COPY app.py .
COPY py_minIO.py
COPY requirements.txt .

RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "/app/app.py"]