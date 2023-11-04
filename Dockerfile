FROM public.ecr.aws/lambda/python:3.9

RUN pip install scikit-learn

COPY ["dv.bin", "model1.bin", "./"]

COPY ["lambda_function.py", "./"]

CMD ["lambda_function.lambda_handler"]
