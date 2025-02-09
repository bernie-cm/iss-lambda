## International Space Station tracker
This small project will call the ISS Open API at regular 10 min intervals
and record location data in an Amazon RDS instance.
The containerised ingest script will run via a Lambda function, controlled
by EventBridge, and stored in AWS ECR.

Here's a diagram of the system:
![assets/ISS API diagram.jpeg]

