import boto3
from sagemaker import get_execution_role
from sagemaker.model_monitor import DefaultModelMonitor, CronExpressionGenerator

role = get_execution_role()

monitor = DefaultModelMonitor(
    role=role,
    instance_count=1,
    instance_type="ml.m5.large",
    volume_size_in_gb=20,
    max_runtime_in_seconds=3600,
)

baseline_job = monitor.suggest_baseline(
    baseline_dataset="s3://your-bucket/training-data.csv",
    dataset_format={"csv": {"header": True}},
    output_s3_uri="s3://your-bucket/baseline-output",
    wait=True,
)

monitor.schedule_monitoring_job(
    endpoint_input="your-endpoint-name",
    output_s3_uri="s3://your-bucket/monitoring-output",
    statistics=baseline_job.baseline_statistics_file_name,
    constraints=baseline_job.constraint_violations_file_name,
    schedule_cron_expression=CronExpressionGenerator.daily(),
)