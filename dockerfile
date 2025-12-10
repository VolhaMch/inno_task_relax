FROM python:3.11-slim

WORKDIR /app
# WORKDIR /relax.by

RUN apt-get update && \
    apt-get install -y wget gnupg && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt \
    && playwright install --with-deps

# RUN mkdir -p /app/allure-results

COPY . .

CMD ["pytest", "--alluredir=/app/allure-results"]
