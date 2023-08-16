import aws_cdk as core
import aws_cdk.assertions as assertions

from daniel_cloud_academy.daniel_cloud_academy_stack import DanielCloudAcademyStack

# example tests. To run these tests, uncomment this file along with the example
# resource in daniel_cloud_academy/daniel_cloud_academy_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = DanielCloudAcademyStack(app, "daniel-cloud-academy")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
