# MLOps Monitoring Architecture

### 🔗 Key Components:
1. **SageMaker Model Monitor**: Observes data drift on inference endpoint.
2. **Prometheus + Grafana**: Monitors live model performance in Kubernetes.
3. **Airflow DAG**: Triggers retraining when drift (PSI) crosses threshold.
4. **PSI Metric**: Population Stability Index used to measure drift severity.

Each component is loosely coupled and scalable in production environments.