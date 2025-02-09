## International Space Station tracker
This small project will call the ISS API at regular intervals
and record location data in an Amazon RDS instance.
The containerised ingest script will run via a Lambda function, controlled
by EventBridge, and stored in AWS ECR.
