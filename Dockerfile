FROM python:3.9-slim
WORKDIR /app

COPY requirements.txt .

RUN pip install pandas

CMD ["python", "app.py"]