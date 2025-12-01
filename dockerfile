FROM python:3.11-slim

WORKDIR /relax.by

RUN apt-get update && \
    apt-get install -y wget gnupg && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && playwright install --with-deps

COPY . .

CMD ["pytest", "-v", "tests/"]
