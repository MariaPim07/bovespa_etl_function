import json
import boto3

def lambda_handler(event, context):
    s3 = event["Records"][0]["s3"]
    bucket = s3["bucket"]["name"]
    object_key = s3["object"]["key"]

    try:
        glue = boto3.client("glue") 
        response = glue.start_job_run(
            JobName="job-bovespa",
            Arguments = {
                '--bucket': bucket,
                '--file': object_key,
            }
        )
        return {"statusCode": 200, "body": json.dumps("Job running!")}
    except Exception as err:
        print(err)
        return {"statusCode": 500, "body": json.dumps("Error")}
