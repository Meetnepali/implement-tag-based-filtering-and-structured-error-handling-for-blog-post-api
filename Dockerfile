FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir fastapi==0.110.0 uvicorn==0.27.1
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
