# Simple Dockerfile for the Flask app
FROM python:3.10-slim

# set workdir
WORKDIR /app

# install system deps
RUN apt-get update && apt-get install -y --no-install-recommends build-essential && rm -rf /var/lib/apt/lists/*

# copy requirements and install
COPY requirements.txt /app/requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

# copy app
COPY . /app

ENV PORT=5000
EXPOSE 5000

# Use gunicorn in production
CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:5000"]
