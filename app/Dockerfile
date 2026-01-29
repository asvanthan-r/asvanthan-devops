FROM python:3.11-slim

# Prevents Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY app.py /app/app.py

RUN pip install flask

EXPOSE 5000

CMD ["python", "app.py"]
