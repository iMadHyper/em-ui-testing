FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt && playwright install --with-deps

COPY . .

CMD ["sh", "-c", "rm -rf /app/reports/allure-reports && pytest -v --alluredir=./reports/allure-reports"]

VOLUME ["/app/reports"]