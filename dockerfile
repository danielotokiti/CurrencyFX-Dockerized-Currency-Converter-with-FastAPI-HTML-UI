FROM python:3.12-slim

WORKDIR /app-ins

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app-ins/app
COPY ./Static /app-ins/Static
COPY ./Templates /app-ins/Templates


EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
