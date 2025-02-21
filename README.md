# ISS Location Tracker
This small project consists of an ETL processor and pipeline that obtains the International Space Station's location in real-time using the ISS Open API. The processor writes historical positional data in an Amazon RDS Postgres database, and simulates a user who needs visualisation capabilities as a use case.

## Architecture Overview
- **Data ingestion**: AWS Lambda function executes a containerised Python ETL script every 5 minutes.
- **Storage**: Amazon RDS Postgres instance for historial data storage.
- **Orchestration**: Amazon EventBridge for scheduling the Lambda function calls.
- **Container registry**: AWS Elastic Container Registry (ECR).
- **Data visualisation**: *to be determined*.

## Prerequisites
- AWS account with appropriate IAM permissions
- Docker installed on local environment
- Python 3.8+
- Local Postgres client for testing and local development
- AWS CLI configured

## Setup and installation
1. **Clone the repository**
```bash
git clone https://github.com/bernie-cm/iss-lambda
cd iss-lambda
```
2. **Configure AWS Resources**
- Create an RDS Postgres instance.
- Set up an ECR repository.
- Configure appropriate KMS Key Policy.
- Create Lambda function.
- Configure EventBridge schedule.
3. **Environment variables**
```
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
POSTGRES_HOST=your_rds_endpoint
```

> [!NOTE]
> Here's a diagram of the system:

![Link](https://github.com/bernie-cm/iss-lambda/blob/main/assets/ISS%20API%20diagram.png)

