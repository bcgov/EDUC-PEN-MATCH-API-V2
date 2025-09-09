FROM python:3.11.13
LABEL authors="JNING"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir requirements.txt

COPY . .

CMD ["python", "main.py"]