# mlops-lambda-ecr-gateway
Deployment of a machine learning model using MLE tools from AWS:

Services:
- AWS Lambda 
- AWS ECR (Elastic Container Registry)
- AWS API Gateway

# 1. Build the docker image
The `Dockerfile` that we have basically builds a Python 3.9 from the public repository of AWS ECR, copy all the files that come with the project and runs the `lambda_handler` function that we have developed.

To build the docker image:
```
docker build -t <ADD_IMAGE_NAME> .
```

# 2. Publish your image to AWS ECR
If you still have not configured your AWS account:
```
aws configure
```
From here, let's create repo and push the docker image [documentation]([https://pages.github.com/](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html)):
