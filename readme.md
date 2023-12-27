# Sagemaker 101 | Intro to AWS Sagemaker

A simple and quick introduction to AWS SageMaker. Using SageMaker to perform modeling with XGBoost and deploying the model. Also uses Lambda and API Gateway services to deploy the model.

Detailed blog post: [Sagemaker-101 | Modelleme ve Canlıya Alma (λ ile Serverless)](https://silverstone1903.github.io/posts/2023/12/sagemaker-101/) (Turkish)

Folder structure:
```bash
|   readme.md
|
+---data
|       HR-Employee-Attrition.csv
|
+---lambda
|       lambda_function.py
|
\---notebook
        sagemaker_hr_attrition_xgb.ipynb
        test_endpoint.ipynb
```

## Resources
* [SageMaker Python SDK](https://github.com/aws/sagemaker-python-sdk)
* [Amazon SageMaker Documentation](https://docs.aws.amazon.com/sagemaker/)