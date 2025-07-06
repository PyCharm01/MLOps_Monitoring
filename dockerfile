FROM python:3.10-slim

WORKDIR /app

COPY ./k8s_monitoring/flask_exporter.py .

RUN pip install flask prometheus_client

EXPOSE 5000 8000

CMD ["python", "flask_exporter.py"]