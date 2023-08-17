from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_iam as iam,
    aws_lambda as _lambda,
)
from constructs import Construct


class DanielCloudAcademyStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # my resources

        daniels_bucket = s3.Bucket(
            self,
            'daniels-bucket',
            versioned=True,
            encryption=s3.BucketEncryption.KMS,
            bucket_key_enabled=True,
        )

        daniels_bucket.add_to_resource_policy(
            iam.PolicyStatement(
                actions=['s3:*'],
                resources=[daniels_bucket.arn_for_objects('*')],
                principals=[iam.AccountRootPrincipal()],
            )
        )

        daniels_role = iam.Role(
            self,
            'daniels-role',
            assumed_by=iam.ServicePrincipal('s3.amazonaws.com'),
        )

        daniels_role.add_to_policy(
            iam.PolicyStatement(
                resources=['*'],
                actions=['lambda:*'],
            )
        )

        daniels_lambda = _lambda.Function(
            self,
            'daniels-lambda',
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset('lambda_code'),
            handler='hello.handler',
        )
