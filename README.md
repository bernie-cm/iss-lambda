## International Space Station tracker
This small project will call the ISS Open API at regular 10 min intervals
and record location data in an Amazon RDS instance.
The containerised ingest script will run via a Lambda function, controlled
by EventBridge, and stored in AWS ECR.

> [!NOTE]
> Here's a diagram of the system:

![Link](https://github.com/bernie-cm/iss-lambda/blob/main/assets/ISS%20API%20diagram.png)

> [!IMPORTANT]
> How to run the script below

`python3 main.py -u <username> -p <password>`
