THis is test commit from ED-19-test branch.


https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html

create policy: 
    Open the Policies page of the IAM console.
    Choose Create Policy.
    Choose the JSON tab, and then paste the following custom policy into the JSON editor.
    Choose Next: Tags.
    Choose Next: Review.
    Under Review policy, for the policy Name, enter s3-trigger-tutorial.
    Choose Create policy.

Create an execution role
    Open the Roles page of the IAM console.
    Choose Create role.
    For the type of trusted entity, choose AWS service, then for the use case, choose Lambda.
    Choose Next.
    In the policy search box, enter s3-trigger-tutorial.
    In the search results, select the policy that you created (s3-trigger-tutorial), and then choose Next.
    Under Role details, for the Role name, enter lambda-s3-trigger-role, then choose Create role.

To create the Lambda function
    Open the Functions page of the Lambda console.
    Make sure you're working in the same AWS Region you created your Amazon S3 bucket in. You can change your Region using the drop-down list at the top of the screen.
    Choose Create function.
    Choose Author from scratch
    Under Basic information, do the following:
        For Function name, enter s3-trigger-tutorial
        For Runtime, choose Python 3.12.
        For Architecture, choose x86_64.
    In the Change default execution role tab, do the following:
        Expand the tab, then choose Use an existing role.
        Select the lambda-s3-trigger-role you created earlier.
    Choose Create function.

To create the Amazon S3 trigger
    In the Function overview pane, choose Add trigger.
    Select S3.
    Under Bucket, select the bucket you created earlier in the tutorial.
    Under Event types, be sure that All object create events is selected.
    Under Recursive invocation, select the check box to acknowledge that using the same Amazon S3 bucket for input and output is not recommended.
    Choose Add.

============================================
Test your Lambda function with a dummy event
============================================
