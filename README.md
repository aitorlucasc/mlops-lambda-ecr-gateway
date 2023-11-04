# mlops-lambda-ecr-gateway
Deployment of a machine learning model using MLE tools from AWS:

Services:
- AWS Lambda 
- AWS ECR (Elastic Container Registry)
- AWS API Gateway

# Build the docker image
The `Dockerfile` that we have basically builds a Python 3.9 from the public repository of AWS ECR, copy all the files that come with the project and runs the `lambda_handler` function that we have developed.
