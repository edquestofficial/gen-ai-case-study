import aws_cdk as core
import aws_cdk.assertions as assertions

from 05_cdk_poc.05_cdk_poc_stack import 05CdkPocStack

# example tests. To run these tests, uncomment this file along with the example
# resource in 05_cdk_poc/05_cdk_poc_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = 05CdkPocStack(app, "05-cdk-poc")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
