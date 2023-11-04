# mlops-lambda-ecr-gateway
Deployment of a machine learning model using MLE tools from AWS:

Services:
- AWS Lambda 
- AWS ECR (Elastic Container Registry)
- AWS API Gateway

We can use the AWS Free Tier to develop our own things. In that case, we just should take care with the amount of MB in the AWS ECR, that just accepts 500MB each month.

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
From here, let's create a ECR repo, tag our docker image and push it ([documentation](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html)):
```
# Create the repo
aws ecr get-login-password --region <REGION> | docker login --username AWS --password-stdin <XXX>.dkr.ecr.<REGION>.amazonaws.com

# Tag our image with the latest version
docker tag <IMG_NAME>:latest <XXX>.dkr.ecr.<REGION>.amazonaws.com/<ECR_REPO>

# Push the image to the AWS repo
docker push <XXX>.dkr.ecr.<REGION>.amazonaws.com/<ECR_REPO>            
```

# 3. Create the lambda function and test it
- Choose the option of creating the lambda function from a docker container.
- Give a name to the AWS Lambda function.
- Search for the image you have pushed to the repository.
- Select your architecture (if you have builded from an M1/M2 Macbook, choose `arm64` ).
- Click on create.
- Go to configuration and change the timeout, then create a json for testing, aligned with your data.
- Click on test and you will see the output of your prediction:
  - `{'get_credit_probability': 0.9019309332297606, 'get_credit': True}`

# 4. Create an endpoint using the API Gateway and test it
- Create a REST API for the AWS Lambda function.
- Create a POST request for the prediction.
- Create a test by just adding your json data to see if the endpoint works.
- Deploy it to invoke the URL.
- Go to the `test.py`, change the url variable with your URL and voilà!
