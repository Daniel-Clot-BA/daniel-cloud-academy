from aws_cdk import (
    Stack,
    aws_s3 as s3
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
        )
