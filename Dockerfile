FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN useradd --create-home --uid 10001 appuser

COPY . .

USER appuser

ENV PORT=8080
EXPOSE 8080

CMD ["python3", "-m", "app.main"]
