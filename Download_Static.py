import boto3
import os
import io



def main():
    s3_token = os.getenv("CLOUDFLARE_S3_token_id")
    s3_secret = os.getenv("cloudflare_s3_token_secret")
    account_id = os.getenv("CLOUDFLARE_ACCOUNT_ID")
    bucket_id = os.getenv("s3_bucket_id")
    s3 = boto3.resource(service_name="s3",
                        endpoint_url=f"https://{account_id}.r2.cloudflarestorage.com/",
                        aws_access_key_id=s3_token,
                        aws_secret_access_key=s3_secret
                        )
    for item in s3.Bucket(name=bucket_id).objects.all():
        if not f"{item.key}".startswith("content"):
            continue
        path = f"{item.key}"
        s3_file = item.get()["Body"]
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with io.FileIO(path, "w") as local_file:
            for i in s3_file:
                local_file.write(i)


if __name__ == "__main__":
    main()
